# streamlit_app.py
import pandas as pd
import streamlit as st
from loguru import logger

from bak.init_data import BatchDataRead
from db_utils import BatchData, get_session

st.session_state.setdefault('data_table', [])


# session: Session = next(get_session())

def get_data_from_db():
    logger.info("init")
    return (BatchDataRead.from_orm(db_obj).dict()
            for db_obj in next(get_session()).query(BatchData).all())


# logger.debug(st.session_state.data_table)
# if not st.session_state.data_table:
st.session_state.data_table = get_data_from_db()

df = pd.DataFrame(data=st.session_state.data_table)


def update_handler(*args, **kwargs):
    logger.debug(f"{args=}, {kwargs=}")


edited_df = st.data_editor(df, key="edited_info",
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

favorite_command = edited_df.loc[edited_df["id"].idxmax()]
data_table_change_info = st.session_state['edited_info']
logger.debug(f"{data_table_change_info=}")

edited_rows = data_table_change_info.get('edited_rows')
session = next(get_session())
for id_, update_data in edited_rows.items():
    row_db = session.query(BatchData).where(BatchData.id == int(edited_df.loc[id_].id)).first()
    for field in update_data:
        setattr(row_db, field, update_data[field])
    st.text(f"update: {id_=}, {update_data=}")
    st.toast('Your edited image was saved!', icon='😍')
    session.commit()
    st.rerun()
logger.info('end')
