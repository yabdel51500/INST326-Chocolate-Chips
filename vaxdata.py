
import pandas as pd
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from argparse import ArgumentParser
import sys
from PIL import Image

class Govax:
    """
    This class reads a csv file and converts said information to a list that is then converted ti a map.
    
    Attributes:
        infile : csv containing covid information
    """
    def __init__(self, infile):
        self.infile = infile
        
    def read(self, infile):
        """
        Reads the csv and organizes into a list.
        
        Args:
            self (keyword) : binds the attributes with the given arguments.  
            infile : csv containing covid information
      
        """
        list1 = list()
        f = open(infile, 'r', encoding = ("utf-8"))
        reader = f.readline()
        while(reader):
            x = reader.split(",")
            iso = x[0]
            continent = x[1]
            country = float(x[2])
            date = float(x[3])
            
            list1.append(x, iso, continent, country, date)
            reader = f.readline()
        f.close()
        
    def map(self):
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
        df3 = df2[df2['date'] == '2021-10-25']
        df3.reset_index(drop = True, inplace = True)

        country = list(df3['location'])
        totalvax=list(df3['people_fully_vaccinated_per_hundred'])

        list1 = [[country[i],totalvax[i]] for i in range(len(country))] 

        map1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px')) #create the map and set the size of the map
        map1.add('Total Confirmed Cases', list1, maptype='world')
        map1.set_series_opts(label_opts=opts.LabelOpts(is_show = False)) 

        map1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100 , is_piecewise = True, pieces=[
        {'min': 100},
        {'min': 80, 'max': 99.99},
        {'min': 50, 'max': 79.99},
        {'min': 30, 'max': 49.99},
        {'min': .0001, 'max': 29.99},
        {'max': 0},]),
        title_opts=opts.TitleOpts(title= "Covid-19 Worldwide Total Vaccinations INST326 Final", subtitle= 'Till October 20th, 2021', pos_left= 'center', padding=0, item_gap=2,
        title_textstyle_opts= opts.TextStyleOpts(color='blue', font_weight= 'bold', font_family= 'Courier New', font_size=30), 
        subtitle_textstyle_opts= opts.TextStyleOpts(color='black', font_weight='bold', font_family='Courier New', font_size=20)), 
        legend_opts=opts.LegendOpts(is_show=False))
        return map1.render_notebook()

    def secure(self):
        """
            This function ensures that the csv file works with the code.

            Args:
                self (keyword) : binds the attributes with the given arguments.        
        """
        if self.infile is None:
            raise ValueError("The file inserted must be in a csv format")
        if self.map() is None:
            raise ValueError("File corrupted or incorrect format before delivery")
        
def main(infile):
    """
    This function creates an instance of the Govax() class.
    
    Args:
        self (keyword) : binds the attributes with the given arguments.        
    """
    a1 = Govax("covid.csv")
    var1 = a1.map()
    if var1 != None:
        print(var1)
    return var1
       
    
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect three mandatory arguments:
        - filename: a path to a CSV file containing aardvark stats
        - aardvark_1: the name of the first aardvark in the battle
        - aardvark_2: the name of the second aardvark in the battle

    Also allow one optional argument, which should be preceded by -p or --pause:
        - pause: the number of seconds to pause after each attack in the battle
          (defaults to 2.0)
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("infile",
                        help="path to CSV file containing aardvark stats")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.infile)

    

