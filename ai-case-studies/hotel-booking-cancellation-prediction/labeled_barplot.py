# Importing necessary libraries for data manipulation and visualization
import pandas as pd
import streamlit as st

# Function to create a labeled bar plot using Streamlit
def labeled_barplot(data, feature, perc=False, n=None):
    st.subheader(f"Labeled Bar Plot for {feature}")

    # Calculate the value counts
    value_counts = data[feature].value_counts(normalize=perc) if perc else data[feature].value_counts()

    # Display the bar chart
    st.bar_chart(value_counts.head(n))

    # Display the data table
    st.write(value_counts.head(n))

