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
st.header("ILI Percentage Over Time")
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
st.text("This chart shows the ILI(Influenza-Like Illnesses) percentage over time for the state that the user picks from 2010 to 2025. Each point on the line shows the percentage of patient visits who showed Influenza-Like Illnesses in that specific week. This chart helps us notice patterns to see how mild or severe each flu season was in that state.") 
ili_values = state_data["ili"]
loc, scale = expon.fit(ili_values)
x = np.linspace(0, ili_values.max(), 1000)
fig,ax = plt.subplots(figsize = (16,6))
st.header("Histogram of ILI with Exponential Curve")
ax.hist(ili_values, bins =1000, density =True)
ax.plot(x,expon.pdf(x, loc = loc, scale = scale), lw=3)
ax.set_xlabel("ILI percentage")
ax.set_ylabel("Exponential Density")
st.pyplot(fig)
st.text("The histogram shows the frequency of the Influenza-Like Illnesses percentage for the state that the user picked. The x-axis is the ILI percentage, and the y-axis is the frequency (how much the percentage appeared over time). The exponential curve is used to show the distribution of the histogram. Having the exponential curve helps us to see if a higher percentage of ILI was common or rare.")
