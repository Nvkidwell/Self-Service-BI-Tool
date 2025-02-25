import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Title
st.title("📊 Self-Service BI Tool")

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Read data
    df = pd.read_csv(uploaded_file)
    st.write("### 🔍 Raw Data", df)

    # Column selection
    column = st.selectbox("Select a column for visualization", df.columns)

    # Chart type selection
    chart_type = st.selectbox(
        "Choose a Chart Type",
        ["Bar Chart", "Line Chart", "Pie Chart", "Histogram", "Scatter Plot"],
    )

    # Filter selection
    unique_values = df[column].dropna().unique()
    selection = st.multiselect("Filter Values", unique_values, default=unique_values[:3])
    filtered_df = df[df[column].isin(selection)]

    # Display filtered data
    st.write("### 📌 Filtered Data", filtered_df)

    # Chart visualization
    st.write("### 📊 Data Visualization")

    # Matplotlib charts
    if chart_type in ["Bar Chart", "Histogram", "Pie Chart"]:
        fig, ax = plt.subplots()
        if chart_type == "Bar Chart":
            filtered_df[column].value_counts().plot(kind="bar", ax=ax, color="royalblue")
            ax.set_title("Bar Chart")
        elif chart_type == "Histogram":
            filtered_df[column].hist(ax=ax, color="seagreen", bins=10)
            ax.set_title("Histogram")
        elif chart_type == "Pie Chart":
            filtered_df[column].value_counts().plot(kind="pie", ax=ax, autopct="%1.1f%%")
            ax.set_title("Pie Chart")
        st.pyplot(fig)

    # Plotly charts (Interactive)
    elif chart_type == "Line Chart":
        fig = px.line(filtered_df, x=filtered_df.index, y=column, title="Line Chart")
        st.plotly_chart(fig)
    elif chart_type == "Scatter Plot":
        fig = px.scatter(filtered_df, x=filtered_df.index, y=column, title="Scatter Plot")
        st.plotly_chart(fig)
