#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os

print(os.getcwd())


# In[38]:


import pandas as pd
df = pd.read_csv(r"C:\Users\naren\Downloads\customer_shopping_behavior.csv")
df.head()


# In[39]:


df.info()


# In[10]:


df.describe()


# In[40]:


df.isnull().sum()


# In[41]:


df['Review Rating'] = df['Review Rating'].fillna(
    df['Review Rating'].median()
)


# In[42]:


df.isnull().sum()


# In[43]:


df.columns = df.columns.str.lower()


# In[44]:


df.columns = df.columns.str.replace(' ','_')


# In[45]:


df.columns


# In[46]:


df =df.rename(columns = {'purchase_amount_(usd)':'purchase_amount'})


# In[47]:


df.columns


# In[49]:


df = df.rename(columns = {'frequency of purchases' : 'purchase_frequency'})

df.columns


# In[50]:


labels = ['young adult','adult','middle age','senior']

df['age_group'] = pd.qcut(
    df['age'],
    q=4,
    labels=['young adult','adult','middle age','senior']
)


# In[51]:


df[['age', 'age_group']].head(10)


# In[52]:


df['purchase_frequency_days'] = None


# In[53]:


frequency_mapping = {
    'Fortnightly': 14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}


# In[54]:


df['frequency_of_purchases']


# In[55]:


df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[56]:


df[['purchase_frequency_days','frequency_of_purchases']].head(10)


# In[58]:


df[['discount_applied','promo_code_used']]


# In[59]:


(df['discount_applied']==df['promo_code_used']).all


# In[60]:


df = df.drop('promo_code_used',axis=1)


# In[61]:


df.columns


# In[63]:


pip install psycopg2-binary sqlalchemy


# In[71]:


get_ipython().system('pip install psycopg2-binary sqlalchemy')


# In[76]:


from sqlalchemy import create_engine

# Step 1: Connect to PostgreSQL
# Replace placeholders with your actual details
username = "postgres"      # default user
password = "Beahappysoul1012" # the password you set during installation
host = "localhost"         # if running locally
port = "5432"              # default PostgreSQL port
database = "customer shopping behavior"    # the database you created in pgAdmin

engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# Step 2: Load DataFrame into PostgreSQL
table_name = "customer"   # choose any table name
df.to_sql(table_name, engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")


# In[ ]:





# In[ ]:




