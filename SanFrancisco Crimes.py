
# coding: utf-8

# In[178]:


import pandas as pd

sf_summer = pd.read_csv("C:/Users/shubhamkedia/Documents/Datasets/sanfrancisco_incidents_summer_2014.csv", low_memory=False)
sf_summer


# In[179]:


import numpy as np
import matplotlib.pyplot as plt


# In[180]:


sf_summer = sf_summer.drop(['IncidntNum','PdId'], axis=1)
sf_summer.columns = ['Category', 'Description', 'DayOfWeek', 'Date', 'Time', 'PdDistrict',
       'Resolution', 'Address', 'Longitude', 'Latitude', 'Location']
sf_summer.head(2)


# In[181]:


get_ipython().set_next_input('Question 1 : For either city, how do incidents vary by time of day? Which incidents are most common in the evening? During what periods of the day are robberies most common');get_ipython().magic('pinfo common')


# In[ ]:


Question 1 : For either city, how do incidents vary by time of day? Which incidents are most common in the evening? During what periods of the day are robberies most common


# In[182]:


plt.figure(figsize= (13,6))
sf_summer['Category'].value_counts().plot(kind="bar")
plt.title("Bar Chart of Frequency by Crime Categories")
plt.show()


# In[183]:


sf_summer['Hour'] = sf_summer['Time'].apply(lambda x: int(x.split(':')[0]))
sf_summer


# In[184]:


Category_by_hour = sf_summer.groupby(['Category', 'Hour']).size().unstack()
# Replace NaN by 0
Category_by_hour = Category_by_hour.replace(np.NaN, 0. )
Category_by_hour['Total'] = sf_summer.groupby('Category').size()
Category_by_hour.sort_values(by= 'Total', inplace= True, ascending= False)

Category_by_hour.head(12)


# In[185]:


Category_by_hour['Total'].head(10).plot(kind="bar")
plt.title('Frequency of the top 10 categories')
plt.show()


# In[186]:


plt.figure(figsize= (15,8))
for cat in list(Category_by_hour.index)[:10] :
    Category_by_hour.drop('Total', axis=1).loc[cat].plot(label= cat)
    plt.xticks(range(24))
plt.legend()
plt.title('Crime Incident Frequency by hour of the day')
plt.show()


# In[187]:


Category_by_hour.drop('Total', axis=1).loc['ROBBERY'].plot(figsize= (10,4))
plt.xticks(range(24))
plt.title('Robbery frequency by hour of the day')
plt.show()


# In[ ]:


Answers:
    a. The frequency of incidents are lowest from mid-night to early morning (1AM - 7AM) and peaks during the afternoon and evening hours (2PM - 12AM) from the line plot above
    b. LARCENY/THEFT was the most common crime in the evening from the line plot above
    c. Robberies are most common during at noon (12PM) and near mid-night(10PM-2AM)


# In[ ]:


Question2 :
    get_ipython().set_next_input('    For either city, how do incidents vary by neighborhood? Which incidents are most common in the city center? In what areas or neighborhoods are robberies or thefts most common');get_ipython().magic('pinfo common')


# In[188]:


Category_by_neighbourhood = sf_summer.groupby(['Category', 'PdDistrict']).size().unstack()
# Replace NaN by 0
Category_by_neighbourhood = Category_by_neighbourhood.replace(np.NaN, 0. )
Category_by_neighbourhood['Total'] = sf_summer.groupby('Category').size()
Category_by_neighbourhood.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_neighbourhood


# In[189]:


Category_by_neighbourhood['Total'].head(10).plot(kind="bar")
plt.title('Frequency of the top 10 categories')
plt.show()


# In[190]:


Category_by_neighbourhood.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")


# In[191]:


Category_by_neighbourhood.drop('Total', axis=1).loc['ROBBERY'].plot(kind = 'bar')
plt.title('Robbery frequency by neighbourhood')
plt.show()


# In[ ]:


Answers:
    1. Incidents vary a lot by neighborhood. But in most of the neighborhood Larency/Threat is most common.
    2. Larency/theft is most common in the city centre.
    3. Robbery is most common in Ingleside.


# In[ ]:


Question:
    get_ipython().set_next_input('    For either city, how do incidents vary month to month in the Summer 2014 dataset');get_ipython().magic('pinfo dataset')


# In[192]:


sf_summer['Month'] = sf_summer['Date'].apply(lambda x: int(x.split('/')[0]))
sf_summer


# In[193]:


Category_by_month = sf_summer.groupby(['Category', 'Month']).size().unstack()
# Replace NaN by 0
Category_by_month = Category_by_month.replace(np.NaN, 0. )
Category_by_month['Total'] = sf_summer.groupby('Category').size()
Category_by_month.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_month


# In[194]:


Category_by_month.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")


# In[195]:


get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font="monospace")

# Create a custom colormap for the heatmap values
cmap = sns.diverging_palette(h_neg=210, h_pos=350, s=90, l=30, as_cmap=True)

# Draw the full plot
sns.clustermap(Category_by_month.drop('Total', axis=1).head(15).transpose()
               ,  linewidths=.5,  figsize=(13, 13), cmap=cmap)


# In[ ]:


Answers:
    This is how crimes vary in each months. Larency/Theft are most common crime every month.


# In[ ]:


Question:
    get_ipython().set_next_input('    For either city, which incident types tend to correlate with each other on a day-by-day basis');get_ipython().magic('pinfo basis')


# In[198]:


Category_by_day = sf_summer.groupby(['Category', 'DayOfWeek']).size().unstack()
# Replace NaN by 0
Category_by_day = Category_by_day.replace(np.NaN, 0. )
Category_by_day['Total'] = sf_summer.groupby('Category').size()
Category_by_day.sort_values(by= 'Total', inplace= True, ascending= False)


# In[199]:


Category_by_day.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")


# In[200]:


get_ipython().magic('matplotlib inline')
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set(font="monospace")

# Create a custom colormap for the heatmap values
cmap = sns.diverging_palette(h_neg=210, h_pos=350, s=90, l=30, as_cmap=True)

# Draw the full plot
sns.clustermap(Category_by_day.drop('Total', axis=1).head(15).transpose()
               ,  linewidths=.5,  figsize=(13, 13), cmap=cmap)


# In[ ]:


Answers:
    Larency/theft correlate to day to day basis.

