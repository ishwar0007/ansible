#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import glob
import os
import time
import sys
import dns.resolver
import re


dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']
filename=glob.glob("/root/chunk/*")[0]

df = pd.read_csv(rf'{filename}', low_memory=False)

df['Domain'] = df['Email'].str.split('@').str[1]

mxRecords = []
count = 0
for key in df['Domain']:
    try:
        answers = dns.resolver.query(key, 'MX')
    except:
        mxRecord = "some error"
    else:
        mxRecord = answers[0].exchange.to_text()
    finally:
        count = count + 1
        mxRecords.append(mxRecord)
        time.sleep(.200)
        print(count)


mx_df = pd.DataFrame({"MXRecords":mxRecords})

df['MXRecords'] = mx_df['MXRecords']

df.to_csv(rf'/root/chunk/output_file_chunk.csv', index=False)
