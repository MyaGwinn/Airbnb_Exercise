#!/usr/bin/env python
# coding: utf-8

# ### Welcome to the Airbnb Mini Practice Project
# 
# As you've worked through Python Sub Unit you would have realised there are a number of powerful functions you can use.
# 
# You would have covered the following libraries:
# 
# <li> Matplotlib </li>
# <li> Seaborn </li>
# <li> Pandas </li> 
#     
# These are all powerful libraries to help augment your data analysis capabilities.
# In these set of exercises below, we've crafted a few extra challenges to reinforce your understanding of how these libraries work. 
# 
# Please note there is a particular emphasis on the Pandas Library as this is the most critical library you will be using throughout your career as a data analyst. You'll see the similarities that hold with respect to Pandas and Pivot Tables!
#     
# <b> The most important thing to build confidence with Python is to practice all the time. This way you will build muscle memory. Don't simply copy the code you've written previously but write it again and again so you build the muscle memory associated with these coding libraries. </b> 
# 
# <H3>  Let's get started! </H3>

# We've provided a file called airbnb_2.csv that you'll need to import.
# 
# Let's do this first before we start our analysis.
# 
# <b> Don't forget to import the libraries you need to read .csv files! </b> 
# 
# 

# ### Step 1: <span style="color:green">Import Libraries</span> 
# <b> Put your code in the box below </b>
# 

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Step 2: <span style="color:green">Import the Airbnb Dataset</span> 

# Now that you have the Pandas Libraries imported, it's time to import the airbnb dataset.
# 
# <b> i) Please import the airbnb dataset.
# 
# ii) Upon completion of this, use .info() to better understand the variables inside your dataset.
# <p>    
# 
# <b> Put your code in the box below </b>

# In[4]:


airbnb = pd.read_csv('airbnb_2.csv')


# In[5]:


airbnb.info()


# ### Step 3: <span style="color:green">Exploring your data with Pandas</span> 
# 
# The rest of these questions will have you focus on using the following Pandas Skills:
# 
# <li> Subsetting a Pandas dataframe using [] and boolean operators </li>
# <li> Summing up Records with value_counts()</li>
# <li> Creating calculated fields </li>
# <li> Group By in Pandas </li> 
# <li> Creating Bar Plots with Matplotlib</li> 
# 
# 

# <b> i)  Please count how many airbnb listings are in each of the 5 Neighbourhood Groups (Manhattan, Brooklyn, Queens, Bronx, Staten Island) and identify which Neighbourhood Groups has the largest number of Airbnb Listings </b>
# <p>
#     <b> Put your code in the box below </b>

# In[6]:


# Group data and count listings
group_count = airbnb['neighbourhood_group'].value_counts()

print(group_count)


# We want to focus our attention on the Neighbourhood Groups that have the top 3 number of Airbnb Listings.
# 
# <b> ii) Calculate the % listings that each Neighbourhood Group contains. </b>
# 
# <b> Put your code in the box below </b>

# In[7]:


# Count listing as a %
per_listings = airbnb['neighbourhood_group'].value_counts(normalize=True)

print(per_listings)


# <b> iii) Create a new calculated field called Revenue and place this into the Airbnb Dataframe. This is to be calculated by using the Price Column x Number_Of_Reviews Columns </b>
# 
# <b> Put your code in the box below </b>

# In[8]:


# Multiple Price and Number_Of_Reviews columns and add Revenue column to Airbnb df
airbnb['revenue'] = (airbnb['price'] * airbnb['number_of_reviews'])

print(airbnb[['revenue']])


# <b> iv) Create a Bar Plot that shows which Neighbourhood Group has the highest average revenues. In order to best
# calculate this, you'd want to consider how you can use the .groupby() syntax to assist you! </b>
# 
# If you're stuck, we recommend you go back to <a href = https://learn.datacamp.com/courses/manipulating-dataframes-with-pandas> this </a> datacamp link. Specifically Chapter 4 which covers how GROUP BY is used in Pandas.
# 
# <b> Put your code in the box below </b>

# In[9]:


# Avg the revenue by each neighbourhood group
avg_rev_group = airbnb.groupby('neighbourhood_group')['revenue'].agg(np.mean)

# Sort in descending
sort_avg_rev_group = avg_rev_group.sort_values(ascending=False)

# Set as a bar chart and customize
sort_avg_rev_group.plot(kind='bar')
plt.title('Average Revenue by Neighbourhood Group')
plt.xlabel('Neighbourhood Group')
plt.ylabel('Average Revenue')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()


# <h3> <span style="color:green">Challenge Questions</span> </h3>

# <b> V) Filter the Airbnb Dataframe to include only the Neighbourhood Groups Manhattan, Brookly and Queens. 
#     
# Upon completion of this, identify the top 3 Revenue Generating Neighborhoods within each of the three Neighbourhood_Groups. This should give us 9 Overall Rows: 3 of the top generating neighbourhoods within each of the 3 Neighbourhood_Groups </b>
# 
# This is a tricky question that will *test* your group-by skills.
# 
# We recommend you consider the following:
# 
#     condition1 = someDataFrame['someColumn']=='someCondition'
#     condition2 = someDataFrame['someColumn']=='someCondition'
#     
#     Step One - Filter the Dataframe using the Conditions
#     filtered_dataframe = someDataFrame[condition1 OR condition 2] 
#     #Hint: You might want to look up what the OR symbol in Python is represented as in operator form (i.e. AND (&) )
#     
#     Step Two - Group the Data by Neighbourhood_Group and Neighbourhood. Don't forget you're looking to SUM up the Revenues.
#     
#     The remaining steps we recommend you think very carefully about.
#     
#     You might want to make use of the .reset_index(inplace=True) function to help reset the indexes in 
#     your Grouped Up Dataframe...!
#     
#     
# <b> Put your code in the box below </b>

# In[11]:


neighbourhood_groups = ['Manhattan', 'Brooklyn', 'Queens']
filtered_groups = airbnb[airbnb['neighbourhood_group'].isin(neighbourhood_groups)]

top_neighbourhoods = filtered_groups.groupby(['neighbourhood_group', 'neighbourhood'])['revenue'].sum()\
                                      .reset_index()\
                                      .sort_values(by=['neighbourhood_group', 'revenue'], ascending=[True, False])\
                                      .groupby('neighbourhood_group').head(3)
                                              
print(top_neighbourhoods)


# <b> VI) Building on the previous question where you identified the top 3 Neighbourhoods within each of the three neighbourhood_groups based off Revenues, please filter the Airbnb Dataframe to include only these neighbourhoods. 
#     
# Upon completion of this, identify the  top average revenue generating room type for each of the nine neighbourhoods and plot this out in a Bar Chart.</b>
# 
# This is a tricky question that will *test* your group-by skills. Think back to the previous question and how you approached this; you can approach this in a similar manner. 
# 
# We recommend you consider the following:
# 
#     condition1 = someDataFrame['someColumn']=='someCondition'
#     condition2 = someDataFrame['someColumn']=='someCondition'
#     
#     Step One - Filter the Dataframe using the Conditions
#     filtered_dataframe = someDataFrame[condition1 OR condition 2] 
#     #Hint: You might want to look up what the OR symbol in Python is represented as in operator form (i.e. AND (&) )
#     
#     Step Two - Group the Data by Neighbourhood_Group and Neighbourhood. Don't forget you're looking to SUM up the Revenues.
#     
#     The remaining steps we recommend you think very carefully about.
#     
#     You might want to make use of the .reset_index(inplace=True) function to help reset the indexes in 
#     your Grouped Up Dataframe...!
#     
#     
#  <b> Put your code in the box below </b>      

# In[16]:


filtered_airbnb = airbnb[airbnb['neighbourhood'].isin(top_neighbourhoods['neighbourhood'])]

# Group by neighbourhood and room_type, calculate mean revenue
average_revenue_by_neighbourhood_room = filtered_airbnb.groupby(['neighbourhood', 'room_type'])['revenue'].mean()\
                                                      .reset_index()

# Plot the data in a bar chart

plt.figure(figsize=(10, 6))
for neighbourhood in top_neighbourhoods['neighbourhood']:
    subset = average_revenue_by_neighbourhood_room[average_revenue_by_neighbourhood_room['neighbourhood'] == neighbourhood]
    plt.bar(subset['neighbourhood'] + ' - ' + subset['room_type'], subset['revenue'])

plt.xlabel('Neighbourhood - Room Type')
plt.ylabel('Average Revenue')
plt.title('Top Average Revenue Generating Room Type for Each Neighbourhood')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[ ]:




