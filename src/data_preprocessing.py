import pandas as pd
from  sklearn.model_selection import train_test_split

# print(d.head())
def t():
    d=pd.read_csv('../data/raw/insurance_data.csv')
    x=d[['Age','Annual_Income_LPA','Policy_Term_Years','Sum_Assured_Lakhs']]
    y=d['Annual_Premium_Thousands']
    # print(x)

    # print('Annual_Premium_Thousands\n',y)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
    return x_train,x_test,y_train,y_test
    # print('x_train\n',x_train)
    # print('x_test\n',x_test)
    # print('y_train\n',y_train)
    # print('y_test\n',y_test)
# t()