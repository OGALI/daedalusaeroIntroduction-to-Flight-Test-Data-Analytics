# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_excel('L39_flight1-221209-114646.xlsx')
# ==========================================================================

# ==========================================================================
time=df["Time"]
Alt=df["AGL"]
TAS=df["IAS"]

plt.plot(Alt)
plt.grid()

df_takeoff=df[0:2500]
plt.plot(df_takeoff['ASL'])
plt.grid()

df_takeoff.to_excel("L39_flight1_takeoff.xlsx")
# ==========================================================================

# ==========================================================================
df_ldg1=df[23500:27500]
df_ldg2=df[32000:35000]

df_ldg1.to_excel("L39_flight1_ldg1.xlsx")
df_ldg2.to_excel("L39_flight1_ldg2.xlsx")