# streamlit_app.py
import os

import pandas as pd
import streamlit as st
from loguru import logger
from pydantic import BaseModel
from sqlalchemy import and_, case

from bak.init_data import BatchDataCreate, BatchDataRead
from db_utils import BatchData, session

BASE_CKPT_DIR = "./bak"
RUN_MODE = {
    1: 'lbs模式',
    2: 'lbs优先模式',
    3: '不使用lbs'
}
PAGE_TITLE = "training data configer"
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


class DataRow(BaseModel):
    path: str | None = None
    img_prefix: str | None = None
    filter_empty_gt: bool = False
    update_cache: bool = False


def make_train_dicts(with_entities: tuple, conditions: tuple):
    return [
        DataRow(path=_.ann_file,
                img_prefix=_.img_prefix).dict()
        for _ in session.query(BatchData)
        .with_entities(*with_entities)
        .where(and_(*conditions)).all()
    ]


def prepare_train_data(mode_id) -> dict[str, list]:
    res = {
        "train_data": [],
        "val_data": [],
    }
    if mode_id == 1:
        res['train_data'] = make_train_dicts(
            with_entities=(BatchData.img_prefix, BatchData.ann_file_lbs.label('ann_file')),
            conditions=(BatchData.is_train == 1, BatchData.ann_file_lbs.is_not(None))
        )
        res['val_data'] = make_train_dicts(
            with_entities=(BatchData.img_prefix, BatchData.ann_file_lbs.label('ann_file')),
            conditions=(BatchData.is_validation == 1, BatchData.ann_file_lbs.is_not(None))
        )
    elif mode_id == 2:
        res['train_data'] = make_train_dicts(
            with_entities=(BatchData.img_prefix,
                           case((BatchData.ann_file_lbs.is_not(None), BatchData.ann_file_lbs),
                                else_=BatchData.ann_file).label('ann_file')),
            conditions=(BatchData.is_train == 1,)
        )
        res['val_data'] = make_train_dicts(
            with_entities=(BatchData.img_prefix,
                           case((BatchData.ann_file_lbs.is_not(None), BatchData.ann_file_lbs),
                                else_=BatchData.ann_file).label('ann_file')),
            conditions=(BatchData.is_validation == 1,)
        )
    elif mode_id == 3:
        res['train_data'] = make_train_dicts(conditions=(
            BatchData.is_train == 1,
            BatchData.ann_file.is_not(None)
        ))
        val_db_objs = session.query(BatchData).where(BatchData.is_validation == 1).all()
        for db_obj in val_db_objs:
            res['val_data'].append(DataRow(path=db_obj.ann_file,
                                           img_prefix=db_obj.img_prefix).dict())
    return res


@st.cache_data
def list_ckpt_paths(dir_path):
    return os.listdir(dir_path)


def get_data_from_db():
    logger.debug("init")
    db_objs = session.query(BatchData).all()
    return [BatchDataRead.from_orm(db_obj).dict() for db_obj in db_objs]


st.session_state.setdefault('data_table', [])
st.session_state.setdefault('username', '')
st.session_state.setdefault('evolve_r', 0.02)
st.session_state.setdefault('n_trail', 10)
st.session_state.setdefault('n_epoch', 1)
st.session_state.setdefault('ckpt_path', list_ckpt_paths(BASE_CKPT_DIR)[0])
st.session_state.setdefault('mode', 2)
st.session_state.setdefault('configs', {
    k: st.session_state[k] for k in ('evolve_r', 'n_trail', 'n_epoch', 'ckpt_path', 'mode')
})
if not st.session_state.data_table:
    st.session_state.data_table = get_data_from_db()

left_col, right_col = st.columns([3, 1])


def train():
    right_col.json({k: st.session_state[k] for k in ('evolve_r', 'n_trail', 'n_epoch', 'ckpt_path', 'mode')})
    right_col.json(prepare_train_data(st.session_state.mode))


def table_update_handler():
    logger.debug(f"{st.session_state.edited_info=}")
    edited_rows = st.session_state.edited_info.get('edited_rows')
    added_rows = st.session_state.edited_info.get('added_rows')
    deleted_rows = st.session_state.edited_info.get('deleted_rows')
    # 更改列
    for id_, update_data in edited_rows.items():
        row_id = int(edited_df.loc[id_].id)
        row_db = session.query(BatchData).where(BatchData.id == row_id).first()
        logger.info(f"{row_id=}, {update_data=}")
        for field in update_data:
            setattr(row_db, field, update_data[field])
        session.commit()

    # 增加列
    for new_row_data in added_rows:
        logger.debug(f"{new_row_data=}")

    for deleted_row in deleted_rows:
        row_id = int(edited_df.loc[deleted_row].id)
        logger.debug(f"{row_id=}")
        row_db = session.query(BatchData).where(BatchData.id == row_id).first()
        session.delete(row_db)
        session.commit()
        logger.debug(f"{st.session_state.data_table[-1].get('id')=}")

        deleted_row_data = next(filter(lambda x: x.get('id') == row_id, st.session_state.data_table[::-1], ))
        logger.debug(f"{deleted_row_data=}")
        list.remove(st.session_state.data_table, deleted_row_data)
        logger.debug(f"{st.session_state.data_table[-1].get('id')=}")


def update_config(*args, **kwargs):
    return None


def create_new_row():
    new_db_obj = BatchData(**BatchDataCreate().dict())
    session.add(new_db_obj)
    session.commit()
    session.refresh(new_db_obj)
    logger.debug(f"{BatchDataRead.from_orm(new_db_obj)=}")
    st.session_state.data_table.append(BatchDataRead.from_orm(new_db_obj).dict())


with left_col:
    edited_df = st.data_editor(
        pd.DataFrame(data=st.session_state.data_table), key="edited_info",
        num_rows="dynamic",
        height=600,
        hide_index=True,
        use_container_width=True,
        on_change=table_update_handler,
        column_order=(
            'id', 'year', 'census_batch', 'id_code', 'precision', 'is_train', 'is_validation', 'ann_file', 'ann_file_lbs', 'img_prefix',),
        column_config={
            "year": st.column_config.NumberColumn("年份", format="%d 年", ),
            'census_batch': "普查批次",
            'id_code': "编号",
            'precision': "精度",
            'is_train': "是否是训练集",
            'is_validation': "是否是验证集",
            'ann_file': st.column_config.Column("path", width='medium'),
            'ann_file_lbs': st.column_config.Column("lbs_path", width='medium'),
            'img_prefix': st.column_config.Column("img_prefix", width='medium'),
        })
    st.button("新建一行", on_click=create_new_row)

with right_col:
    st.slider(label='evolve_r', key='evolve_r',
              min_value=0.0, max_value=0.5, step=0.01,
              on_change=update_config)
    st.selectbox(label='n_trail', key='n_trail',
                 options=(i for i in range(10, 51, 10)))
    st.selectbox(label='n_epoch', key='n_epoch',
                 options=(i for i in range(1, 6)))
    st.selectbox(label='ckpt_path', key='ckpt_path',
                 options=(list_ckpt_paths(BASE_CKPT_DIR)))
    st.selectbox(label='mode', key='mode',
                 format_func=lambda x: RUN_MODE[x],
                 options=RUN_MODE,
                 on_change=update_config)
    st.button("启动", on_click=train)
