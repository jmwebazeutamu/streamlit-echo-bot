import streamlit as st
import numpy as np

with st.chat_message("assistance"):
  st.write("Hello how is going?")
  st.bar_chart(np.random.randn(30, 3))
