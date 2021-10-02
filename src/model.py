import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv(r'../data/CURATED/data_clean.csv', encoding="UTF8")
scalX = StandardScaler()
scaly= StandardScaler()


df_categ=df.select_dtypes(include=['object_'])
df_categ=df_categ.drop(columns=['Company','Model'])
df_encoded = pd.get_dummies(df_categ)
df_num = df.select_dtypes(exclude=['object_'])
df_num=df_num.drop(columns=['car_ID','symboling'])
var=df_num.iloc[:,:-1]
tar=df_num.iloc[:,-1]
scalX.fit(var.values)
scaly.fit(tar.values.reshape(-1, 1))
df_var=pd.DataFrame(scalX.transform(var.values))
target=pd.DataFrame(scaly.transform(tar.values.reshape(-1, 1)))
#df_scale=pd.concat([df_var, target], axis = 1)
df_model = pd.concat([df_encoded, df_var], axis = 1)
   

y=target.values
x=df_model.values
X_train, X_test, y_train, y_test = train_test_split(x, y , test_size = 0.3, random_state = 0)
regresseur = LinearRegression(fit_intercept=True)
regresseur.fit(X_train,y_train)

pickle.dump(regresseur,open('model.pkl','wb'))
pickle.dump(scalX,open('scalerX.pkl','wb'))
pickle.dump(scaly,open('scalery.pkl','wb'))
