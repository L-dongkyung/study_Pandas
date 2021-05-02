import pandas as pd

tbl = pd.DataFrame({
    "weight":[ 60,  50,  90,  78,  63,  68,  98,  76],
    "height":[170, 175, 178, 180, 159, 194, 168, 190],
    "bmi":[   "n", "t", "f", "n", "n", "t", "f", "t"],
    "gender":["m", "f", "f", "m", "m", "m", "f", "m"]
})

# 키가 170 이상
print(tbl[tbl.height >= 170])
print(tbl[tbl.gender =="f"])
# print(tbl["gender"=="m"]) -- 에러

# 정렬

print(tbl.sort_values(by="weight"))
print(tbl.sort_values(by="weight", ascending=False))
