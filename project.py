import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
ILI=ILI.sort_values(by="epiweek")
ILI["weeks"]=range(len(ILI))
state=st.selectbox(
  "Choose a State:",
  ILI['state'],
  index=None,
  placeholder="Select a State"
)
if state:
  state_data = ILI[ILI['state'] == state]
  st.line_chart(state_data[['weeks', 'ili']].set_index('weeks'))
