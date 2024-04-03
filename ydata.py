import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
df =pd.read_csv("train.csv")
profile = ProfileReport(df)
profile.to_file("EDA.html")
