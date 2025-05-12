import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
state=st.selectbox(
  "Choose a State:",
  ILI["state"]
  index=None,
  placeholder="Select a State",
)
st.write("You selected:", state)
if state:
  state_data = ILI[ILI["state"]==state]
  st.line_chart(
  state_data,
  x="weeks",
  y="ili"
)
