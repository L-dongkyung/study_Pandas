import pandas as pd
import numpy as np

tbl = pd.DataFrame({
    "weight":[ 60,  50,  90,  78,  63,  68,  98,  76],
    "height":[170, 175, 178, 180, 159, 194, 168, 190],
    "bmi":[   "n", "t", "f", "n", "n", "t", "f", "t"],
    "gender":["m", "f", "f", "m", "m", "m", "f", "m"]
})

# 정규화하기
def norm(tbl, key):
    c = tbl[key]
    v_max = c.max()
    v_min = c.min()
    print(key, "=", v_min, "-", v_max)
    tbl[key] = (c-v_min) / (v_max-v_min)

norm(tbl, "weight")
norm(tbl, "height")
print(tbl)

print("---------------------")
tbl1 = np.array([
    [ 60,  50,  90,  78,  63,  68,  98,  76],
    [170, 175, 178, 180, 159, 194, 168, 190],
    [   "n", "t", "f", "n", "n", "t", "f", "t"],
    ["m", "f", "f", "m", "m", "m", "f", "m"]
])
n = tbl1
print(n)
print(tbl.values)