# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import streamlit as st

# Function to create a stacked bar plot using Streamlit
def stacked_barplot(data, predictor, target):
    st.subheader(f"Stacked Bar Plot for {predictor} vs {target}")

    # Create crosstabulations for absolute and normalized counts
    crosstab = pd.crosstab(data[predictor], data[target], normalize='index')

    # Display the stacked bar chart
    st.bar_chart(crosstab)

    # Display the crosstab data table
    st.write(crosstab)