"""
Yahya Abdelhamid
INST326(0101)
Group Chocolate Chips
Final check-in 1
"""
import pandas as pd
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType

class Govax:
    """
    This class reads a csv file and converts said information to a list that is then converted ti a map.
    
    Attributes:
        df3 : a dataframe of covid vax data
        infile : csv containing covid information
    """
    def __init__(self, infile):
        """
        """
        self.df3 = ""
        self.infile = "covid.csv"
        with open(self.infile, "r", encoding = "utf-8") as f:
            for line in f:
                x = []
                x.append(line)
        
    def main(self):
        """
        The main function reads the csv file and acsesses the information from October 25th of this year.
        Pandas is used to vizualise the data. Of cource when we need to actually use the data we will not
        only use the first 5 rows, this was just for vizualization purposes. 
        
        Args:
            self (keyword) : binds the attributes with the given arguments.        
        """
        df1 = pd.read_csv(self.infile)
        df1['date'] = pd.to_datetime(df1['date'])
        df2 = df1.sort_values(by = ['date'], ascending = False)
        self.df3 = df2[df2['date'] == '2021-10-25']
        self.df3.reset_index(drop = True, inplace = True)
        print(self.df3.head())
        
    def work(self):
        """
        This function creates the list that will carry the information for a country's name and vaccination numbers.
        
        Args:
            self (keyword) : binds the attributes with the given arguments.        
        """
        self.list1 = [[location[i],total_vaccinations[i]] for i in range(len(location))] 
        self.map_1 = Map(init_opts=opts.InitOpts(width= "1000px", height= "460px",theme=ThemeType.ROMANTIC)) 
        self.map_1.append('Total Confirmed Cases')
        
        
    def vizualise(self):
        """
        This function generAtes the map and filters through the map's attributes to show the data in a consice way.
        
        Args:
            self (keyword) : binds the attributes with the given arguments.        
        """
        maptype = 'world'
        is_map_symbol_show = False
        self.map_1.set_series_opts(label_opts=opts.LabelOpts(is_show = False)) 
        self.map_1.set_global_opts(
        visualmap_opts=opts.VisualMapOpts(max_=1100000,is_piecewise=True,pieces=[
        {'min': 500000},
        {'min': 200000, 'max': 499999},
        {'min': 100000, 'max': 199999},
        {'min': 50000, 'max': 99999},
        {'min': 10000, 'max': 49999},
        {'max': 9999},]),
        title_opts=opts.TitleOpts(
        title= "Covid-19 Worldwide Total Cases INST326 Final",
        subtitle= 'Till August 13th,2021',
        pos_left= 'center',
        padding=0,
        item_gap=2,
        title_textstyle_opts= opts.TextStyleOpts(color='darkblue',
        font_weight= 'bold',
        font_family= 'Courier New',
        font_size=30), 
        subtitle_textstyle_opts= opts.TextStyleOpts(color='grey',
        font_weight='bold',
        font_family='Courier New',
        font_size=13)), 
        legend_opts=opts.LegendOpts(is_show=False))
        self.map_1.render_notebook()

    def secure(self):
        """
            This function ensures that the csv file works with the code.

            Args:
                self (keyword) : binds the attributes with the given arguments.        
        """
        if self.infile is None:
            raise ValueError("The file inserted must be in a csv format")
        if self.df3 is None:
            raise ValueError("Data frame is curropted please resecure")
        if self.map_1 is None:
            raise ValueError("File corrupted or incorrect format before delivery")
        
def scope():
    """
    This function creates an instance of the Govax() class.
    
    Args:
        self (keyword) : binds the attributes with the given arguments.        
    """
    a1 = Govax("covid.csv")
    
if __name__ == "__main__":
    scope()
    

<<<<<<< HEAD
=======
# main("covid.csv")


def csv_list(dataset):
    """The csv_list function would be able to convert the file into a dictionary
    and return back the columns, location and total_cases
    Attributes:
        covid_case(dictionary): contains the values of the data we're looking for
    """

    covid_case = []
    with open(dataset, "r", encoding = "utf-8") as f:
        for line in f:
            line = line.split(",")
            covid_case.append({line[2]:line[4]})
            
        for i in range(len(covid_case)):
           a = covid_case[i]
           print(covid_case)
           break
           
        
csv_list("covid.csv")

from pyecharts.charts import Map,Geo
def map(list1):
    map1=Map(init_opts=opts.InitOpts(width="1000px", height="460px"))
    map1.add("Total Covid Cases", list1, maptype=’world’)
#This function will create a map using covid cases data
#List1 is a list that contains a list of global covid cases 
    map_1.render_notebook()
    
>>>>>>> 0f1aa5aa49c251e27f50fd6ca4d71f4860d65b81
