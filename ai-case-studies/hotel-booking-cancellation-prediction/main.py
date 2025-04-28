# libraries to help with data manipulation and analysis
import pandas as pd
import numpy as np

#libraries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import table

# initial settings:
#   - removing the limit for the number of displayed columns
#   - setting the limit for the number of displayed rows
#   - setting the precision of floating numbers to 2 decimal points

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 200)
pd.set_option("display.float_format", lambda x: "%.2f" % x)

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    f1_score,
    accuracy_score,
    recall_score,
    precision_score,
    confusion_matrix,
    roc_auc_score,
    ConfusionMatrixDisplay,
    make_scorer   
)

import os
import joblib
import gradio as gr

from labeled_barplot import labeled_barplot
from stacked_barplot import stacked_barplot
from helper import confusion_matrix_sklearn

import streamlit as st

path = os.path.join('data', 'INNHotelsGroup_pastdata.csv')

hotel = pd.read_csv(path)

# Streamlit app title
st.title("Hotel Booking Cancellation Prediction")

# Load the data
st.subheader("Sample Data")
st.write(hotel.head(10))

# Visualize the distribution of hotel bookings by market segment type
st.subheader("Distribution of Hotel Bookings by Market Segment Type")
market_segment_counts = hotel['market_segment_type'].value_counts()
st.bar_chart(market_segment_counts)

# creating a copy of the data to avoid modifying the original dataset
data = hotel.copy()

# checking the statistics summary of the dataset
print(data.describe().T)

print(data.info())


# Streamlit app title
st.title("Stacked Bar Plot Visualization")
labeled_barplot(data, 'booking_status', perc=True)

# Streamlit app title
st.title("Labeled Bar Plot Visualization")
stacked_barplot(data, 'market_segment_type', 'booking_status')


labeled_barplot(data[data.booking_status == 'Canceled'], "rebooked", perc=True)


# converting the 'arrival_date' column to datetime type
data['arrival_date'] = pd.to_datetime(data['arrival_date'])

# extracting month from 'arrival_date'
data['arrival_month'] = data['arrival_date'].dt.month

# grouping the data on arrival months and extracting the count of bookings
monthly_data = data.groupby(["arrival_month"])["booking_status"].count().to_frame().reset_index()
monthly_data.columns = ['Month', 'Bookings']

# visualizing the trend of number of bookings across months
plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_data, x="Month", y="Bookings")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('')
plt.ylabel('# Bookings', fontsize=15)

stacked_barplot(data, "arrival_month", "booking_status")


# encoding the output (also called target) attribute
data["booking_status"] = data["booking_status"].apply(
    lambda x: 1 if x == "Canceled" else 0
)


# separating the input and output variables
X = data.drop(["booking_status","booking_id","arrival_date","rebooked"], axis=1)
y = data["booking_status"]

# encoding the categorical input variables
X = pd.get_dummies(X, drop_first=True)

# splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# defining the AI model to build
model = RandomForestClassifier(class_weight="balanced", random_state=1)

# training the AI model on the train data
model.fit(X_train, y_train)

confusion_matrix_sklearn(model, X_train, y_train)

# evaluating the model performance on the train data
model_train_predictions = model.predict(X_train)
model_train_score = f1_score(y_train, model_train_predictions)

st.write("Model Score on Train Data:", np.round(100*model_train_score, 2))

# confusion matrix for test data
confusion_matrix_sklearn(model, X_test, y_test)

# evaluating the model performance on the test data
model_test_predictions = model.predict(X_test)
model_test_score = f1_score(y_test, model_test_predictions)

st.write("Model Score on Test Data:", np.round(100*model_test_score, 2))