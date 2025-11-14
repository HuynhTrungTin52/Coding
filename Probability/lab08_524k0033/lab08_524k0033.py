import pandas as pd
import numpy as np
# 1
data_iris=pd.read_csv('Probability/lab08_524k0033/iris.csv',delimiter=',')
# print(data_iris)
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
# print(data_iris_result)

# 2
