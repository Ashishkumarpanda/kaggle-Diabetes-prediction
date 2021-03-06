import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC
from sklearn.metrics import  confusion_matrix
from sklearn import metrics

data=pd.read_csv("pima-data.csv")
map={True:1,False:0}
data['diabetes']=data['diabetes'].map(map)
data.head()

data.isnull().sum()

x=data.iloc[:,0:8].values
y=data.iloc[:,9].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

scaler=StandardScaler()
x_train=scaler.fit_transform(x_train)
x_test=scaler.fit_transform(x_test)

#handeling Zero Values
val=SimpleImputer(missing_values=0,strategy="mean")
x_train=val.fit_transform(x_train)
x_test=val.fit_transform(x_test)

classifier=SVC(kernel='rbf',random_state=0)
classifier.fit(x_train,y_train)

classifier.predict(x_test)

print("accuracy=",metrics.accuracy_score(y_test,classifier.predict(x_test)))

c_m=confusion_matrix(y_test,classifier.predict(x_test))
