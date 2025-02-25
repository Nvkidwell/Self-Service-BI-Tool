import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Upload CSV
st.title("Self-Service BI Tool")
uploaded_file = st.file_uploader("Upload a CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Raw Data", df)

    # Filter data
    column = st.selectbox("Select a Column", df.columns)
    unique_values = df[column].unique()
    selection = st.multiselect("Filter Values", unique_values, default=unique_values[:3])
    filtered_df = df[df[column].isin(selection)]
    st.write("### Filtered Data", filtered_df)

    # Visualization
    st.write("### Data Visualization")
    fig, ax = plt.subplots()
    filtered_df[column].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)
