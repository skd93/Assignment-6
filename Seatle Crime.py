
# coding: utf-8

# In[2]:


import pandas as pd

sf_summer = pd.read_csv("C:/Users/shubhamkedia/Documents/Datasets/seatle_incidents_summer_2014.csv", low_memory=False)
sf_summer


# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


Question:
    get_ipython().set_next_input('    For either city, how do incidents vary by time of day? Which incidents are most common in the evening? During what periods of the day are robberies most common');get_ipython().magic('pinfo common')


# In[14]:


plt.figure(figsize= (13,6))
sf_summer['Offense Type'].value_counts().plot(kind="bar")
plt.title("Bar Chart of Frequency by Crime Categories")
plt.show()


# In[26]:


sf_summer = sf_summer.replace(np.NaN, '00/00/00 0:00' )
sf_summer['Hour'] = sf_summer['Date Reported'].apply(lambda x: x.split(' ')[1]).apply(lambda x: int(x.split(':')[0]))
sf_summer


# In[27]:


Category_by_hour = sf_summer.groupby(['Offense Type', 'Hour']).size().unstack()
Category_by_hour = Category_by_hour.replace(np.NaN, 0. )
Category_by_hour['Total'] = sf_summer.groupby('Offense Type').size()
Category_by_hour.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_hour.head(50)


# In[28]:


Category_by_hour['Total'].head(10).plot(kind="bar")
plt.title('Frequency of the top 10 categories')
plt.show()


# In[29]:


plt.figure(figsize= (15,8))
for cat in list(Category_by_hour.index)[:10] :
    Category_by_hour.drop('Total', axis=1).loc[cat].plot(label= cat)
    plt.xticks(range(24))
plt.legend()
plt.title('Crime Incident Frequency by hour of the day')
plt.show()


# In[34]:


Category_by_hour.drop('Total', axis=1).loc['ROBBERY-STREET-GUN'].plot(figsize= (10,4))
plt.xticks(range(24))
plt.title('Robbery frequency by hour of the day')
plt.show()


# In[ ]:


Answers:
    a. The frequency of incidents are lowest from 3-6 AM in the morning and peaks in 10AM-10PM from the line plot above
    b. THEFT-CARPROWL was the most common crime in the evening from the line plot above
    c. Robberies are most common from 10PM-3AM 


# In[ ]:


Question:
    get_ipython().set_next_input('    For either city, how do incidents vary by neighborhood? Which incidents are most common in the city center? In what areas or neighborhoods are robberies or thefts most common');get_ipython().magic('pinfo common')


# In[36]:


Category_by_neighbourhood = sf_summer.groupby(['Offense Type', 'District/Sector']).size().unstack()
# Replace NaN by 0
Category_by_neighbourhood = Category_by_neighbourhood.replace(np.NaN, 0. )
Category_by_neighbourhood['Total'] = sf_summer.groupby('Offense Type').size()
Category_by_neighbourhood.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_neighbourhood


# In[37]:


Category_by_neighbourhood['Total'].head(10).plot(kind="bar")
plt.title('Frequency of the top 10 categories')
plt.show()


# In[43]:


Category_by_neighbourhood.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")
plt.show()


# In[44]:


Category_by_neighbourhood.drop('Total', axis=1).loc['ROBBERY-STREET-GUN'].plot(kind = 'bar')
plt.title('Robbery frequency by neighbourhood')
plt.show()


# In[ ]:


Answers:
    1. Incidents vary a lot by neighborhood. But in most of the neighborhood Theft-Carprowl is most common.
    2. Theft-Carprowl is most common in the city centre.
    3. Robbery is most common in District S.
    


# In[ ]:


Question:
    get_ipython().set_next_input('    For either city, how do incidents vary month to month in the Summer 2014 dataset');get_ipython().magic('pinfo dataset')


# In[52]:


sf_summer['Month'] = sf_summer['Date Reported'].apply(lambda x: int(x.split('/')[0]))
Category_by_month = sf_summer.groupby(['Offense Type', 'Month']).size().unstack()
# Replace NaN by 0
Category_by_month = Category_by_month.replace(np.NaN, 0. )
Category_by_month['Total'] = sf_summer.groupby('Offense Type').size()
Category_by_month.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_month


# In[55]:


Category_by_month.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")
plt.show()


# In[56]:


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
    Crime is most common in the month of August especially Theft Carprowl.


# In[ ]:


Question
    get_ipython().set_next_input('    For either city, which incident types tend to correlate with each other on a day-by-day basis');get_ipython().magic('pinfo basis')


# In[57]:


sf_summer


# In[59]:


sf_summer['Day'] = sf_summer['Date Reported'].apply(lambda x: int(x.split('/')[1]))
Category_by_day = sf_summer.groupby(['Offense Type', 'Day']).size().unstack()
# Replace NaN by 0
Category_by_day = Category_by_day.replace(np.NaN, 0. )
Category_by_day['Total'] = sf_summer.groupby('Offense Type').size()
Category_by_day.sort_values(by= 'Total', inplace= True, ascending= False)
Category_by_day


# In[60]:


Category_by_day.drop('Total', axis=1).head(15).transpose().plot(kind = "bar")


# In[61]:


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
    As you can see in the plot that Theft is most common in the last week of the month which somewhat make sense as people spend most of their money in the first few weeks.


# In[ ]:


Advanced Question:
    Advanced What can we infer broadly about the differences in crime patterns between Seattle and San Francisco? Does one city tend to have more crime than the other, per capita? Do the relative frequencies of types of incidents change materially between the two cities? (NOTE: The two datasets do not have the same schema, so comparisons will require some work and some assumptions. This will require extra work, but you will be working at the forefront of what is known!)


# In[ ]:


By looking at that prospect Seatle has way more crimes than San Francisco. Also san Francisco being larger than Seatle means Seatle has higher crimes. And Yes the types of incidents change materially between two cities.

