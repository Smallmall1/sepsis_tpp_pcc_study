
import pandas as pd

# linear algebra
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV

# import data
pd.read_csv(  "/Users/data.csv")
data=pd.read_csv( "/Users/data.csv")

data['mortality'] = data['mortality'].astype(str)

X=data.drop('mortality',axis=1)
Y=data['mortality']

# split arrays or matrices into random train and test subsets

X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.35, random_state=0)

# how k influences the model
f1array = []
f1array_train = []
for i in range(1,len(X_train)+1):
    # model train
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, Y_train)
    
    # model predict
    Y_pred= model.predict(X_test)
    
    # model evaluation
    f1array.append(f1_score(Y_test,Y_pred,average='macro'))
    Y_pred_train = model.predict(X_train)
    f1array_train.append(f1_score(Y_train, Y_pred_train, average='macro'))
    
for i in range(0,len(f1array)):
    print("k=",str(i+1),",f1_score:"+str(f1array[i]))


print("the largest f1_score is "+str(np.max(f1array)))

for i in range(0,len(f1array_train)):
    print("k=",str(i+1),",f1_score:"+str(f1array_train[i]))

print("the largest f1_score for train is "+str(np.max(f1array_train)))

plt.plot(f1array,label = "test", color='blue',linestyle='-')
plt.plot(f1array_train,label = "train", color='yellow',linestyle='-')
plt.show()


# how to choose k       
model = KNeighborsClassifier()
param_grid = [
    {'n_neighbors': list(range(1,60))}]
grid_search = GridSearchCV(model, param_grid, cv=10,
                           scoring='f1_macro')
grid_search.fit(X_train,Y_train)
print("the best params：",grid_search.best_params_)

# model predict
Y_pred = grid_search.predict(X_test)
print("the f1_score in test set is:",str(f1_score(Y_test,Y_pred,average='macro')))
