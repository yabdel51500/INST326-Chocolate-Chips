from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import pandas as pd

dataset=pd.read_csv('covid.csv')
dataset['date']=pd.to_datetime(dataset['date'])
df = dataset.sort_values(by=['date'], ascending=False)

list1 = list(df['people_fully_vaccinated_per_hundred'])
print(list1)