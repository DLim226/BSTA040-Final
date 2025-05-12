import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import expon
def load_data():
    df = pd.read_csv("ilidata.csv")
    df = df[df['epiweek'].between(201040, 202540)]
    df = df.sort_values(by='epiweek')
    df['weeks'] = range(len(df))
    return df
df = load_data()
