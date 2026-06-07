#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
def read_instance(filename):
      with open(filename, "r") as f:
          lines = [line.strip() for line in f if line.strip()]
      n = int(re.findall(r'\d+', lines[1])[0])                                      # -------- n --------------
      profits = [[0]*n for _ in range(n)]                                           # -------- profits --------
      idx = 3
      for i in range(n):
          nums = list(map(int, re.findall(r'-?\d+', lines[idx])))
          for j in range(i+1):
              profits[i][j] = nums[j]
              profits[j][i] = nums[j]
          idx += 1
      idx += 1  # saute "#Weights:"
      weights = list(map(int, re.findall(r'-?\d+', lines[idx])))                    # -------- poids -----------
      capacity = int(re.findall(r'\d+', lines[idx+1])[0])                           # -------- capacity --------
      k = int(re.findall(r'\d+', lines[idx+2])[0])                                  # -------- k ---cardinalité-
      return n, profits, weights, capacity, k

