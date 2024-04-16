import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("""
## Hello, **Mario**! 
welcome to your workout dashboard
""")

df = pd.read_csv("treinos.csv")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')
df['Label'] = df['Label'].str.lower().str.strip()



grouped_data = df.groupby('Label').size()
fig, ax = plt.subplots()
ax.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the pie chart in the Streamlit app
st.pyplot(fig)

print(grouped_data)
# print(df)
