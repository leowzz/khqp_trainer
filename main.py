# streamlit_app.py
import pandas as pd
import streamlit as st

from bak.init_data import BatchDataRead
from db_utils import BatchData, session

df = pd.DataFrame(
    data=(BatchDataRead.from_orm(db_obj).dict()
          for db_obj in session.query(BatchData).all())
)
#
st.dataframe(df, use_container_width=True)
