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
  x="weeks",
  y="ili"
)
fig, ax = plt.subplots()
ax.hist(state_data, bins=20)
ax.set_xlabel("ILI PERCENT")
ax.set_ylabel("frequency")
st.pyplot(fig)
def exponential_pdf(x,lam):
    return lam*np.exp(-lam*x)
exponential_pdf(np.array([1,2,3]), 2)
x=np.array([1,2,3])
expon.pdf(x, loc=0 ,scale=1/2)
x=np.linspace(0,5,1000)
fig, ax = plt.subplots(figsize=(16,6))
ax.plot(x, exponential_pdf(x,1))
