import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# loc 과 iloc 차이
#특징	  loc	                    iloc
#기준	  라벨(label)	            위치(index 위치)
#슬라이싱 끝값	포함	            미포함
#용도	  명시적 라벨 기반 인덱싱	숫자 기반 위치 인덱싱

df.columns
# Index(['country', 'continent', 'year', 'lifeExp', 'pop', 'gdpPercap'], dtype='object')

# lifeExp 열을 연도별로 그룹화하여 평균 계산하기
print(df.groupby('year')['lifeExp'].mean())

# lifeExp, gdpPercap 열의 평균값을 연도, 지역별로 그룹화하여 한 번에 계산하기
print(df.groupby(['year', 'continent'])[['lifeExp','gdpPercap']].mean())

# 그룹화한 데이터 개수 세기
print(df.groupby('continent')['country'].nunique())


import matplotlib.pyplot as plt
global_yearly_life_expectancy = df.groupby('year')['lifeExp'].mean()
print(global_yearly_life_expectancy)

global_yearly_life_expectancy.plot()
plt.show()