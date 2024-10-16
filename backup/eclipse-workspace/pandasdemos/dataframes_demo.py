import pandas as pd

scores_dict = {'kohli':[100,40,90],'rohit':[0,100,30],'jadeja':[30,98,100]}

scores = pd.DataFrame(scores_dict,index=['I1','I2','I3'])
scores.index = ['I1','I2','I3'] 
print(scores)

print("Kohlis score")
print(scores['kohli'])
print(scores.jadeja)

print(scores.loc['I1'])

print(scores.iloc[1])

print(scores.loc['I1':'I2'])

print(scores.iloc[0,1])

print(scores.loc['I1':'I3',['kohli']])

print(scores.iloc[[0,1,2],0:2])

print(scores[scores>=90])

print(scores.at['I2','kohli'])

scores.at['I2','kohli'] = 41

print(scores.at['I2','kohli'])

print(scores.iat[2,0]) #row and column

print(scores.describe())

print(scores.sort_index(ascending=False))

print(scores.sort_index(axis=1,ascending=False))

customer_df = pd.read_csv('customer.csv')
print(customer_df)
customer_df.to_csv('abc.csv',index=False)










