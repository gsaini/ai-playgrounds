
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def stacked_barplot(data, predictor, target):
    """
    Function to create a stacked bar plot for a given predictor and target variable in the dataset.
    
    Parameters:
    - data: DataFrame containing the dataset.
    - predictor: The predictor variable to plot.
    - target: The target variable to plot.
    
    Returns:
    - None
    """
    # number of unique values in the predictor
    count = data[predictor].nunique()

    sorter = data[target].value_counts().index[-1]

    tabel1 = pd.crosstab(data[predictor], data[target], margins=True)
    tabel = pd.crosstab(data[predictor], data[target], normalize='index')

    tabel.plot(kind='bar', stacked=True, color=['#FF9999', '#66B3FF'], figsize=(count + 5, 5))

    plt.legend(loc="upper right", fontsize=12, bbox_to_anchor=(1, 1))

    plt.xticks(fontsize=15, rotation=0)
    plt.xlabel(predictor.replace('_', ' ').title(), fontsize=15)

    plt.yticks(fontsize=15)
    # Show the plot
    plt.show()