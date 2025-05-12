import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
states= []
for val in ILI ["state"]:
    if val not in states:
        states.append(val)
state=st.selectbox(
  "Choose a State:",
  states,
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
