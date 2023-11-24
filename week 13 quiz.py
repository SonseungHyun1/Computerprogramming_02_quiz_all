import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, KFold
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# 데이터 불러오기
file_path = "C:/Users/sms37/Documents/GitHub/computer_programming_02/data/08_pima-indians-diabetes.data.csv"
column_name = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(file_path, names=column_name)

# 데이터 확인
print(dataset.columns)
print(dataset.shape)
print(dataset.describe())
print(dataset.groupby('class').size())

# scatter_matrix 그래프 저장
scatter_matrix(dataset, figsize=(10, 10))
plt.savefig("scatter_matrix.png")

# 독립변수 X와 종속변수 Y로 분할
X = dataset.iloc[:, 0:4].values
y = dataset.iloc[:, 4].values

# 모델 정의
model = DecisionTreeClassifier()

# 모델 학습
model.fit(X, y)

# 예측
y_pred = model.predict(X)
print(y_pred)

# K-fold(10개의 폴드 지정) 및 cross validation(평가 지표 accuracy)
kfold = KFold(n_splits=10, random_state=10, shuffle=True)
results = cross_val_score(model, X, y, cv=kfold, scoring='accuracy')
print(results.mean())
