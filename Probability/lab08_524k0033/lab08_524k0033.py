import pandas as pd
import numpy as np
# 1
print("1)")
data_iris=pd.read_csv('Probability/lab08_524k0033/iris.csv',delimiter=',')
print(f"The first five data points\n {data_iris.head()}")
data_iris.drop('species',axis=1,inplace=True)
data_iris_result=pd.DataFrame(
 columns=data_iris.columns,
 index=['count','mean','std','min','max']
)
# data_iris_result.drop('species',axis=1,inplace=True)
data_iris_result.loc['count']=data_iris.count()
for cols,types in data_iris.items():
    data_iris_result.loc['mean',cols]=round(data_iris[cols].sum()/data_iris_result.loc['count',cols],2)
    data_iris_result.loc['std',cols]=round(np.std(data_iris[cols]),2)
    data_iris_result.loc['min',cols]=data_iris[cols].min()
    data_iris_result.loc['max',cols]=data_iris[cols].max()
    
    # print(cols)
print(data_iris_result.head())

# 2
print()
print("2)")
data_pop=pd.read_csv('Probability/lab08_524k0033/population.csv',delimiter=',')
print(f"The first 5 data points \n {data_pop.head()}")
data_pop_result_country=data_pop.drop(['Year','Value'],axis=1).drop_duplicates(subset=['Country Name','Country Code'],keep='first').reset_index().drop('index',axis=1)
# print(data_pop_result_country)


colcal='Value'
groupBy='Country Name'
# print(data_pop)
data_pop_result_country[groupBy]=data_pop[groupBy].unique()
data_pop_result_country['Country Code']=data_pop['Country Code'].unique()
data_pop_result_country['Count'] = data_pop_result_country[groupBy].map(data_pop[groupBy].value_counts())
data_pop_result_country['Mean']=data_pop_result_country[groupBy].map(data_pop.groupby(groupBy)[colcal].mean())
data_pop_result_country['Std']=data_pop_result_country[groupBy].map(data_pop.groupby(groupBy)[colcal].std())
data_pop_result_country['Min']=data_pop_result_country[groupBy].map(data_pop.groupby(groupBy)[colcal].min())
data_pop_result_country['Max']=data_pop_result_country[groupBy].map(data_pop.groupby(groupBy)[colcal].max())
print("Data of the population group by country name :")
print(data_pop_result_country.head())

print()
groupBy='Year'
print("Data of the population group by year :")
data_pop_result_year=data_pop.drop(['Country Name','Country Code','Value'],axis=1).drop_duplicates(subset='Year',keep='first').reset_index().drop('index',axis=1)
# print(data_pop_result_year)
data_pop_result_year['Count'] = data_pop_result_year[groupBy].map(data_pop[groupBy].value_counts())
data_pop_result_year['Mean']=data_pop_result_year[groupBy].map(data_pop.groupby(groupBy)[colcal].mean())
data_pop_result_year['Std']=data_pop_result_year[groupBy].map(data_pop.groupby(groupBy)[colcal].std())
data_pop_result_year['Min']=data_pop_result_year[groupBy].map(data_pop.groupby(groupBy)[colcal].min())
data_pop_result_year['Max']=data_pop_result_year[groupBy].map(data_pop.groupby(groupBy)[colcal].max())
print(data_pop_result_year.head())