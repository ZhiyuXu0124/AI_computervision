import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

data = np.genfromtxt("wine_data.csv", delimiter=",")
x_data = data[:,1:]  #特征数据
y_data = data[:,0]    #标签数据

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3)

scaler = StandardScaler()
#Standardize features by removing the mean and scaling to unit variance
x_train = scaler.fit_transform(x_train)
x_test = scaler.fit_transform(x_test)

mlp = MLPClassifier(hidden_layer_sizes=(100,50,10),max_iter=500)
mlp.fit(x_train,y_train)

predictions = mlp.predict(x_test)
print(classification_report(y_test,predictions)) #数据评估
print(confusion_matrix(y_test,predictions)) #输出混淆矩阵