# streamlit_app.py
import pandas as pd
import streamlit as st
from loguru import logger

from bak.init_data import BatchDataRead
from db_utils import BatchData, session

PAGE_TITLE = "training data configer"
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon="🧊",
    initial_sidebar_state="expanded",
)


def get_data_from_db():
    logger.debug("init")
    db_objs = session.query(BatchData).all()
    return [BatchDataRead.from_orm(db_obj).dict() for db_obj in db_objs]


st.session_state.setdefault('data_table', [])
st.session_state.setdefault('username', '')
st.session_state.setdefault('evolve_r', 0.1)
st.session_state.setdefault('configs', {
    'evolve_r': st.session_state.evolve_r
})
if not st.session_state.data_table:
    st.session_state.data_table = get_data_from_db()

df = pd.DataFrame(data=st.session_state.data_table)

data_frame_container = st.container()
config_container = st.container()


def train():
    st.session_state.configs['evolve_r'] = st.session_state.evolve_r
    config_container.json(st.session_state.configs)


def update_handler():
    edited_rows = st.session_state['edited_info'].get('edited_rows')
    for id_, update_data in edited_rows.items():
        row_id = int(edited_df.loc[id_].id)
        row_db = session.query(BatchData).where(BatchData.id == row_id).first()
        logger.info(f"{row_id=}, {update_data=}")
        for field in update_data:
            setattr(row_db, field, update_data[field])
        session.commit()


def update_config(*args, **kwargs):
    st.session_state.configs['evolve_r'] = st.session_state.evolve_r


with data_frame_container:
    edited_df = st.data_editor(
        df, key="edited_info",
        hide_index=True,
        use_container_width=True,
        on_change=update_handler,
        column_order=('id', 'year', 'census_batch', 'id_code', 'precision', 'is_train', 'is_validation'),
        column_config={
            "year": st.column_config.NumberColumn("年份", format="%d 年", ),
            'census_batch': "普查批次",
            'id_code': "编号",
            'precision': "精度",
            'is_train': "是否是训练集",
            'is_validation': "是否是验证集",
        })

with config_container:
    st.json(st.session_state.configs)

with st.sidebar:
    st.divider()

    st.slider(label='evolve_r', key='evolve_r',
              min_value=0.0, max_value=0.5, step=0.01,
              on_change=update_config)
    st.text_input("username", key='username')
    st.divider()
    st.button("启动", on_click=train)
