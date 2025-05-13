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
ili=state_data["ili"]
lambda_value=1/ili.mean()
fig, ax = plt.subplots(figsize=(12,5))
ax.hist(ili, bins=20)
ax.set_xlabel("ILI PERCENT")
ax.set_ylabel("frequency")
st.pyplot(fig)
ax.plot(x, y, 'r--', label=f"Exponential Fit (λ = {lambda_value:.2f})")
ax.set_xlabel("ILI Percent")
ax.set_ylabel("Density")
 ax.set_title("ILI Histogram with Exponential Fit")
ax.legend()
st.pyplot(fig)
def exponential_pdf(x,lam):
    return lam *np.exp(-lam*x)
x=np.linspace (0, ili.max(), 1000)
y = exponential_pdf(x, lambda_value)
