# streamlit_app.py
import pandas as pd
import streamlit as st

from bak.init_data import BatchDataRead
from db_utils import BatchData, session

df = pd.DataFrame(
    data=(BatchDataRead.from_orm(db_obj).dict()
          for db_obj in session.query(BatchData).all())
)

edited_df = st.data_editor(df)  # 👈 An editable dataframe

favorite_command = edited_df.loc[edited_df["id"].idxmax()]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
