import pandas as pd

# 딕셔너리 타입으로 데이터 프레임 생성
tbl = pd.DataFrame({
    "weight":[60, 50, 90, 78],
    "height":[170, 175, 178, 180],
    "bmi":["n","t","f","n"]
})

# 몸무게 출력  --속성 하나는 series 타입으로 출력
print(tbl["weight"])
print(tbl['weight'])

# 몸무게 및 키 출력  -- 속성 둘 이상은 DataFrame 타입으로 출력
print(tbl[["weight", "height"]])
# print(tbl["weight", "height"]) -- 대괄호 하나 쓰면 에러
print(tbl[["weight"]])  # -- 대괄호 두개 쓰면 series 타임이 아닌 dataframe 형식으로 출력

# 슬라이싱 가능-- 행 출력
print(tbl[2:4])

# 키의 행 슬라이싱 가능 -- 순서 상관없음
print(tbl[2:4]["weight"])
print(tbl["weight"][2:4])
