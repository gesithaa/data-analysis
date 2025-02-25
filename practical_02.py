# -*- coding: utf-8 -*-
"""practical_02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GH5RFoPYXBt7SJyaSW_Fh5Y_Y-JFbLZJ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Cost_of_Living_Index_by_Country_2024.csv')
df.head()

df = df.dropna(how="any")
df.head(3)

df.info()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('/content/Cost_of_Living_Index_by_Country_2024.csv')
df = df.dropna(how="any")

sns.set(style="darkgrid")
plt.figure(figsize=(7,7))

# Group the 'df' DataFrame (containing cost of living data) by 'Rank'
total = df.groupby('Rank')['Cost of Living Index'].sum().reset_index()

sns.barplot(x='Rank', y='Cost of Living Index', data=total)
plt.xticks(rotation=90)
plt.show()

data = df[['Rent Index']]
red_diamond = dict(markerfacecolor='r', marker='D')
plt.title('cost of living index by country')

plt.boxplot(data.values, labels=['Cost of Living Index'], flierprops=red_diamond)
plt.show()

import pandas as pd
import seaborn as sns

# Use pandas to read your csv file
df = pd.read_csv('/content/Cost_of_Living_Index_by_Country_2024.csv')
sns.lineplot(x="Rent Index", y="Cost of Living Index", data=df)

df = sns.load_dataset("iris")
sns.scatterplot(data=df)

import plotly.express as px
df = px.data.iris()
fig = px.box(df, x="sepal_width", y="sepal_length")
fig.show()

"""# Bubble plot"""

df = pd.read_csv('/content/Cost_of_Living_Index_by_Country_2024.csv')
df.head()

plt.xlabel('Groceries Index')
plt.ylabel('Cost of Living Plus Rent Index')

plt.title("Groceries index VS Cost of Living Index by Country")
plt.scatter(df['Groceries Index'][:100], df['Cost of Living Plus Rent Index'][:100], s=df['Rent Index'][:100]*3, c='red')

