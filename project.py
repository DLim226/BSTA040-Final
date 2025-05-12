import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
ILI= pd.read_csv("ilidata.csv")
state=st.selectbox(
  "Choose a State:",
  ILI['state'],
  index=NONE,
  placeholder="Select a State"
)
