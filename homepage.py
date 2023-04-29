import streamlit as st
view = [100, 150, 30]

st.write("## Youtube view")
st.write("### Raw data")
view
st.write("### Bar chart")
st.bar_chart(view)


import pandas as pd
sview = pd.Series(view)
st.write("### Pandas view")
sview
