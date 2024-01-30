#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'data.xlsx'
data = pd.read_excel(file_path)

# Creating the graphs
plt.figure(figsize=(18, 6))

# Graph for Frequency Distribution of Velar /r/ by Sex
plt.subplot(1, 3, 1)
sns.countplot(x='X', hue='Sex', data=data)
plt.title('Frequency Distribution of Velar /r/ by Sex')
plt.xlabel('Presence of Velar /r/ (0 = Absence, 1 = Presence)')
plt.ylabel('Count')
plt.legend(title='Sex')

# Graph for Frequency Distribution of Velar /r/ by Region
plt.subplot(1, 3, 2)
sns.countplot(x='X', hue='Region', data=data)
plt.title('Frequency Distribution of Velar /r/ by Region')
plt.xlabel('Presence of Velar /r/ (0 = Absence, 1 = Presence)')
plt.ylabel('Count')
plt.legend(title='Region')

# Graph for Frequency Distribution of Velar /r/ by Position
plt.subplot(1, 3, 3)
sns.countplot(x='X', hue='Position', data=data)
plt.title('Frequency Distribution of Velar /r/ by Position')
plt.xlabel('Presence of Velar /r/ (0 = Absence, 1 = Presence)')
plt.ylabel('Count')
plt.legend(title='Position')

plt.tight_layout()
plt.show()


# In[2]:


pip install openpyxl


# In[5]:


import pandas as pd
from scipy.stats import chi2_contingency

# Chi-Squared Test for Sex
contingency_table_sex = pd.crosstab(data['Sex'], data['X'])
chi2_sex, p_sex, dof_sex, expected_sex = chi2_contingency(contingency_table_sex)

# Print the results
print("Chi-Squared Test for Sex:")
print("Chi-squared Value:", chi2_sex)
print("P-value:", p_sex)

# Chi-Squared Test for Region
contingency_table_region = pd.crosstab(data['Region'], data['X'])
chi2_region, p_region, dof_region, expected_region = chi2_contingency(contingency_table_region)

# Chi-Squared Test for Position
contingency_table_position = pd.crosstab(data['Position'], data['X'])
chi2_position, p_position, dof_position, expected_position = chi2_contingency(contingency_table_position)

# Print the results for Region
print("Chi-Squared Test for Region:")
print("Chi-squared Value:", chi2_region)
print("P-value:", p_region)

# Print the results for Position
print("Chi-Squared Test for Position:")
print("Chi-squared Value:", chi2_position)
print("P-value:", p_position)


# In[ ]:




