#https://avinton.com/academy/classification-regression/
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

#扱うデータ

# データ生成の中心点
center = [ [1.5, 0.5], [-2.0, -1.0], [0,0]]
# 各中心点から生成する点の数
DSIZE = 20
# データの生成
data = [ c + (np.random.randn(DSIZE,2) / 2) for c in center]
data = np.concatenate(data)

# 生成されたもとの点ごとのラベル
label = np.arange(3*DSIZE)//DSIZE

# 表示
for i in range(3):
    plt.scatter(data[:,0][label==i],data[:,1][label==i])

#回帰
X, y = np.split(data, 2, axis=1)
test_X = np.arange(-4, 5)
test_X = test_X.reshape(len(test_X), 1)
y_predict = lr.predict(test_X)
print(y_predict)
plt.scatter(X, y, label="data")
plt.plot(test_X, y_predict, label='linear model')
plt.xlim(-4,4)
plt.ylim(-4,4)
plt.title("Predict result")
plt.grid()
plt.legend()
#今回の予測モデルの式 y=x∗a+b
y_predict_function = lambda x: x * lr.coef_ + lr.intercept_
print(y_predict_function(3))

#分析
neigh = KNeighborsClassifier().fit(data, label)
test_Xy = np.array([np.random.rand(10) * 6 - 3, np.random.rand(10) * 4 - 2]).T
predict_label = neigh.predict(test_Xy)

print(predict_label)
for i in range(3):
    rgb = [False for i in range(3)]
    rgb[i] = True
    plt.scatter(data[:,0][label==i],data[:,1][label==i], c=rgb)
    plt.scatter(test_Xy[:,0][predict_label==i], test_Xy[:,1][predict_label==i],c=rgb, marker="*", s=200)
