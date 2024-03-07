# streamlit_app.py
import os

import pandas as pd
import streamlit as st
from loguru import logger

from bak.init_data import BatchDataRead
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


@st.cache_data
def list_ckpt_paths(dir_path):
    return os.listdir(dir_path)


def get_data_from_db():
    logger.debug("init")
    db_objs = session.query(BatchData).all()
    return [BatchDataRead.from_orm(db_obj).dict() for db_obj in db_objs]


st.session_state.setdefault('data_table', [])
st.session_state.setdefault('username', '')
st.session_state.setdefault('evolve_r', 0.2)
st.session_state.setdefault('n_trail', 10)
st.session_state.setdefault('n_epoch', 2)
st.session_state.setdefault('ckpt_path', list_ckpt_paths(BASE_CKPT_DIR)[0])
st.session_state.setdefault('mode', 2)
st.session_state.setdefault('configs', {
    k: st.session_state[k] for k in ('evolve_r', 'n_trail', 'n_epoch', 'ckpt_path', 'mode')
})
if not st.session_state.data_table:
    st.session_state.data_table = get_data_from_db()

df = pd.DataFrame(data=st.session_state.data_table)

data_frame_container = st.container()
config_container = st.container()
left_col, right_col = st.columns([3, 1])


def train():
    st.session_state.configs['evolve_r'] = st.session_state.evolve_r
    config_container.json(st.session_state.configs)


def update_handler():
    edited_rows = st.session_state['edited_info'].get('edited_rows')
    for id_, update_data in edited_rows.items():
        row_id = int(edited_df.loc[id_].id)
        row_db = session.query(BatchData).where(BatchData.id == row_id).first()
        logger.info(f"{row_id=}, {update_data=}")
        logger.debug(BatchDataRead.from_orm(row_db))
        for field in update_data:
            setattr(row_db, field, update_data[field])
        session.commit()


def update_config(*args, **kwargs):
    return None
    # for k in ('evolve_r', 'n_trail', 'n_epoch', 'ckpt_path', 'mode'):
    #     st.session_state.configs[k] = st.session_state[k]


with left_col:
    edited_df = st.data_editor(
        df, key="edited_info",
        height=600,
        hide_index=True,
        use_container_width=True,
        on_change=update_handler,
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
    st.json({
        k: st.session_state[k] for k in ('evolve_r', 'n_trail', 'n_epoch', 'ckpt_path', 'mode')
    })

    st.divider()
    st.button("启动", on_click=train)
