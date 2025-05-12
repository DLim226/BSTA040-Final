import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
state=st.selectbox(
  "Choose a State:",
   ("AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VA", 
"VT", "WA", "WI", "WV", "WY"),
  index=None,
  placeholder="Select a State",
)
st.write("You selected:", state)
state_data = ILI[ILI["state"]==state]
st.line_chart(
  state_data,
  x="weeks",
  y="ili"
)
