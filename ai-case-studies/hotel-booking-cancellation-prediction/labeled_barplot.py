
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def labeled_barplot(data, feature, perc = False, n=None):
    """
    Function to create a labeled bar plot for a given feature in the dataset.
    
    Parameters:
    - data: DataFrame containing the dataset.
    - feature: The feature to plot.
    - perc: Boolean indicating whether to show percentages or counts. Default is False (counts).
    - n: Number of top categories to display. Default is None (all categories).
    
    Returns:
    - None
    """

    total = len(data[feature])
    count = data[feature].nunique()

    if n is None:
        plt.figure(figsize=(count + 2, 6))
    else:
        plt.figure(figsize=(n + 2, 6))

    ax = sns.countplot(data=data, x=feature, hue=feature, palette='Paired', order=data[feature].value_counts().index[:n])


    for p in ax.patches:

        if perc == True:
            label = "{:.1f}%".format(100 * p.get_height() / total)
        else:
            label = p.get_height()

        x = p.get_x() + p.get_width() / 2
        y = p.get_height()

    ax.annotate(label, (x, y), ha='center', va='center', size=15, xytext=(0, 5), textcoords='offset points')

    ax.tick_params(axis='x', labelsize=15)
    ax.tick_params(axis='y', labelsize=15)

    ax.set_xlabel(feature.replace('_', ' ').title(), fontsize=15)
    ax.set_ylabel('')

    plt.show()

