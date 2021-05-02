import pandas as pd

# 스칼라 벡터 행렬 확인

# 스칼라
x = 1

# 행렬
a = pd.DataFrame([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(a)

# 벡터
b = pd.Series([1,3,5,7,9])
print(b)