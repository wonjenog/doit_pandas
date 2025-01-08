import pandas as pd

df = pd.read_csv('./data/gapminder.tsv', sep='\t')

# loc 과 iloc 차이
#특징	  loc	                    iloc
#기준	  라벨(label)	            위치(index 위치)
#슬라이싱 끝값	포함	            미포함
#용도	  명시적 라벨 기반 인덱싱	숫자 기반 위치 인덱싱

