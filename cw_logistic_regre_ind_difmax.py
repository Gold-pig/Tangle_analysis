import json
import sklearn
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import csv
import numpy
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import pandas
import seaborn as sns
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import r2_score



# X, y = load_iris(return_X_y=True)
#
# clf = LogisticRegression(random_state= 0, solver="lbfgs", multi_class="multinomial").fit(X,y)
#
# clf.predict(X[:2, :])

name = "MS1"

# df = pd.read_csv("{}_site_diff_max_in_degree.csv".format(name),usecols=['Site','Max_diff','In_degree'])

# reader = csv.reader(open('{}_site_diff_max_in_degree.csv'.format(name), "rb"), delimiter=",")

# raw_data = numpy.loadtxt(open("{}_site_diff_max_in_degree.csv".format(name), "rb"), delimiter=",", skiprows=1)
# print(raw_data)
#Max_diff

# X = raw_data[:,1]

# X=np.reshape(raw_data[:,2],(-1,1))
#
# y = raw_data[:,1]
# y=np.reshape(y,(-1,1))


data = pd.read_csv('{}_site_diff_max_in_degree.csv'.format(name),header= 0)
# data = data.dropna()
print(data.shape)
# print(list(data.columns))
# sns.countplot(x = "In_degree", data= data)
# plt.yscale("log")
# plt.show()
# data.drop(data.columns[0],axis=1, inplace=True)

# data2 = pd.get_dummies(data,columns=['Max_diff', 'In_degree'])
# data2.drop(data2.columns[[0, 1, 2, 3, 4]], axis=1, inplace=True)

X = [data.Max_diff]
print(X)
y = [data.In_degree]
X = np.reshape(X,(-1,1))
y = np.reshape(y,(-1,1))


print(X)
print(y)
# model = LinearRegression()
model = LogisticRegression()
model.fit(X,y)
#
y_predict =np.array(model.predict(X))
# plt.scatter(X,y_predict, color ="g")
plt.xlabel('Max_diff')
plt.ylabel('In_degree')
plt.title("{}_LinearR_Data".format(name))
# sns.jointplot(x='Max_diff',y='In_degree',data=data)
# plt.scatter(x='Max_diff',y='In_degree',data=data,alpha=0.3)

# Plot the residuals after fitting a linear model
sns.residplot(x='Max_diff',y='In_degree',data=data,scatter_kws={"s": 50})

plt.savefig("{}_LogisticR_Data.png".format(name))
plt.show()

score = r2_score(y,y_predict,multioutput='raw_values')
print(score)
