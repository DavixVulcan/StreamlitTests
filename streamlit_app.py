print("Hello Py")
import streamlit as st
import pandas as pd
import qrcode
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df