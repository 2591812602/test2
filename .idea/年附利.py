import pandas as pd

data=pd.read_excel('D:\\处理数据.xlsx')
datas=data['年复利增长率']
a=list()
for i in datas:
    i-=1
    i="%.2f%%" % (i * 100)
    a.append(i)
data['年复利增长率']=data['年复利增长率']-1
data['年复利增长率'] = data['年复利增长率'].apply(lambda x: format(x, '.2%'))
data.to_excel('D:\\修改之后的数据.xlsx')



