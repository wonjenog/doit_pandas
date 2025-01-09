import pandas as pd
import numpy as np

# 구조	      Series	            DataFrame
# 단위	      1개의 데이터 열(1D)	여러 개의 데이터 열(2D)
# 엑셀로      비유	하나의 열	    전체 표
# 사용 예시	  특정 열/행 분석	    전체 데이터셋 분석

s = pd.Series(['Wes Mckinney', 'Creator of Pandas'], index = ['Person','Who'])
# print(s)

s = pd.DataFrame({
    'Name': ['Rosline Franklin', 'William Gosset'],
    'Born': ['1920-07-25', '1876-06-13'],
    'Died': ['1958-04-16', '1937-10-16'],
    'Age': [37, np.NaN] # 결측값 넣고 싶을 때
})
# print(s)

scientists = pd.DataFrame(
    data = {'Occupation': ['Chemist', 'Statistician'],
            'Born': ['1920-07-25', '1876-06-13'],
            'Died': ['1958-04-16', '1937-10-16'],
            'Age': [37, 61]},
    index = ['Rosline Franklin', 'William Gosset'],
    columns = ['Occupation', 'Born', 'Age', 'Died']
    )
# print(scientists)

first_row = scientists.loc['William Gosset']
# print(first_row)

# 시리즈 메서드 정리
# append : 2개 이상의 시리즈 연결 (사용중단 예정으로 concat 사용 추천천)
borns = scientists['Born']
die = scientists['Died']
result = pd.concat([borns, die])

# describe : 요약 통계량 계산
scientists.describe()

# drop_duplicates : 중복값이 없는 시리즈 반환
s = pd.Series([1, 1, 2, 3, 3])
s.drop_duplicates()

# equals : 시리즈에 해당 값을 가진 요소가 있는지 확인
s1 = pd.Series([1, 2, 3])
s2 = pd.Series([1, 2, 3])
s3 = pd.Series([3, 2, 1])

s1.equals(s2)  # True
s1.equals(s3)  # False

# get_values : 시리즈 값 구하기 (values 속성과 동일) // series의 값을 numpy 배열로 반환
ages = scientists['Age']
ages.values
# [37 61]
ages
# Rosline Franklin    37
# William Gosset      61

# isin : 시리즈에 포함된 값이 있는지 확인
ages = scientists['Age']
ages.isin([37])
# Rosline Franklin     True
# William Gosset      False

# replace : 특정 값을 가진 시리즈 값을 교체
s = pd.Series([1, 2, 3, 2])
s.replace(2, 99)
# 0     1
# 1    99
# 2     3
# 3    99

# sample : 시리즈에서 임의의 값을 반환
s = pd.Series([1, 2, 3, 4, 5])
s.sample(n=2)

# sort_values : 값을 정렬
s.sort_values()

# to_frame : 시리즈를 데이터프레임으로 변환환
ages = scientists['Age']
ages
# Rosline Franklin    37
# William Gosset      61


df_age = ages.to_frame()
df_age
#                   Age
# Rosline Franklin   37
# William Gosset     61


scientists = pd.read_csv('./data/scientists.csv')
ages = scientists['Age']

# 벡터와 벡터 연산은 일치하는 인덱스의 값끼리 수행
rev_ages = ages.sort_index(ascending=False)
# print(ages + rev_ages) = print(ages*2) = print(ages+ages)

# print(scientists[scientists['Age'] > scientists['Age'].mean()])

died_datetime = pd.to_datetime(scientists['Died'], format='%Y-%m-%d')
born_datetime = pd.to_datetime(scientists['Born'], format='%Y-%m-%d')

scientists['born_dt'], scientists['died_dt'] = (born_datetime, died_datetime)
scientists['age_days_dt'] = (scientists['died_dt'] - scientists['born_dt'])
# print(scientists.head())

# DataFrame 전체를 무작위로 섞기
shuffled_scientists = scientists.sample(frac=1, random_state=42)
print(scientists)
print(shuffled_scientists)

import random
random.seed(42)
random.shuffle(scientists['Age'])
# print(scientists['Age'])
# print(scientists) -> Age의 데이터만 랜덤으로 섞이고 나머지 데이터는 동일: 즉, 데이터가 행으로 랜덤하게 섞이는게 아니라 Age 데이터만 섞임.

# axis=1: 열(column)을 삭제.
# axis=0: 행(row)을 삭제.

scientists_dropped = scientists.drop(['Age'], axis=1)
# print(scientists_dropped)

# 파일 내보내기
scientists.to_csv('C://Users//yd170//OneDrive//바탕 화면//scientists.tsv', sep='\t')
scientists.to_csv('C://Users//yd170//OneDrive//바탕 화면//scientists.csv')