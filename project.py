import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
ILI = ILI.assign(weeks = lambda x:range(len(x)))
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
  state_data = state_data.sort_values(by="epiweek")
  state_data["weeks"] = range(len(state_data)) 
  st.line_chart(
  state_data,
  x="Weeks",
  y="ILI Percent"
)
ili_values = state_data["ili"]
loc, scale = expon.fit(ili_values)
x = np.linspace(0, ili_values.max(), 1000)
fig,ax = plt.subplots(figsize = (16,6))
ax.hist(ili_values, bins =1000, density =True)
ax.plot(x,expon.pdf(x, loc = loc, scale = scale), lw=3)
ax.set_xlabel("ILI percentage")
ax.set_ylabel("Exponential Density")
st.pyplot(fig)
