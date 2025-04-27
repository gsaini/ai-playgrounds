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

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import GridSearchCV

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

path = os.path.join('data', 'INNHotelsGroup_pastdata.csv')

hotel = pd.read_csv(path)

# Visualize the distribution of hotel bookings by market segment type
plt.figure(figsize=(10, 6))
hotel['market_segment_type'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Hotel Bookings by Market Segment Type')
plt.xlabel('Market Segment Type')
plt.ylabel('Number of Bookings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# creating a copy of the data to avoid modifying the original dataset
data = hotel.copy()

# checking the statistics summary of the dataset
print(data.describe().T)

print(data.info())

labeled_barplot(data, 'booking_status', perc=True)

stacked_barplot(data, 'market_segment_type', 'booking_status')


