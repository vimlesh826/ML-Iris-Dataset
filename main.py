#imprting libraries
import pandas as panda 
import matplotlib.pyplot as plot_d
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import seaborn as sb

#Dataset read and store into dataframe

iris_loc = "/Dataset/iris.csv"
iris_data = panda.read_csv(iris_loc)


#Setting Features and output
features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
m = iris_data[features]
n = iris_data['Species']
(train_X, val_X, train_y, val_y) = train_test_split(m,n)



#model training
"""def knn(n):"""
model = KNeighborsClassifier(n_neighbors = 3)
model.fit(train_X,train_y)
model_t = model.predict(val_X)
print(accuracy_score(val_y, model_t))

"""
#plotting data
def plotting():
    #sb.scatterplot(x=iris_data['SepalLengthCm'], y=iris_data['SepalWidthCm'], hue = iris_data['Species'])
    sb.lineplot(x = find_n, y = acc)
    plot_d.show()    

for i in find_n:
    knn(i)
"""
print("successfull execution")
plotting()


