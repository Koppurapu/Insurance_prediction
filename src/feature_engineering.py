from sklearn.preprocessing import StandardScaler
from data_preprocessing import t
import pandas as pd
import pickle
x_train,x_test,y_train,y_test=t()
# print(x_train)
scaler=StandardScaler()
x_test_s=scaler.fit_transform(x_test)
x_train_s=scaler.transform(x_train)

pd.DataFrame(x_train_s).to_csv("../data/processed/X_train.csv",index=False)
pd.DataFrame(x_test_s).to_csv("../data/processed/X_test.csv",index=False)
pd.DataFrame(y_train).to_csv("../data/processed/y_train.csv",index=False)
pd.DataFrame(y_test).to_csv("../data/processed/y_test.csv",index=False)

with open('../artifacts/scaler.pkl','wb') as f:
    pickle.dump(scaler,f)
