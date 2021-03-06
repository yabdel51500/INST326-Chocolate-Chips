"""
These are the sources we incorporated into our code:
https://www.youtube.com/watch?v=vLEA8dCfusQ 
https://www.youtube.com/watch?v=BYAwEYwWHyQ 
https://towardsdatascience.com/how-to-make-a-coronavirus
-world-map-in-python-734c9fd87195 <<<<<<< HEAD 
https://www.youtube.com/watch?v=GyMO9WCEheQ&t=24s
https://www.youtube.com/watch?v=GyMO9WCEheQ&t=24s
https://stackoverflow.com/questions/31715119/how-can
-i-open-a-website-in-my-web-browser-using-python
https://stackoverflow.com/questions/40905703/how-to-
open-an-html-file-in-the-browser-from-python
"""
import pandas as pd
from pyecharts.charts import Map,Geo
from pyecharts import options as opts
from pyecharts.globals import ThemeType
from argparse import ArgumentParser
import sys
import webbrowser
import os

class Govax:
    """
    This class reads a csv file and converts said information 
    to a list that is then converted to a map.
    
    Attributes:
        infile : csv containing covid information
    """
    #Ishika
    def __init__(self, infile):
        self.infile = infile
     
    #Christine
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
    #Yahya 
    def map(self):
        """
        The main function reads the csv file and acsesses the 
        information from October 25th of this year.
        Pandas is used to vizualise the data. Of cource when we 
        need to actually use the data we will not
        only use the first 5 rows, this was just for vizualization purposes. 
        
        Args:
            self (keyword) : binds the attributes with the given arguments.        
        """
        df1 = pd.read_csv('covid.csv')
        df1['date'] = pd.to_datetime(df1['date'])
        df2 = df1.sort_values(by = ['date'], ascending = False)
        df3 = df2[df2['date'] == '2021-10-25']
        df3.reset_index(drop = True, inplace = True)
        df4 = df2[df2['date'] <= '2021-11-05']
        df4.reset_index(drop = True, inplace = True)

        country = list(df3['location'])
        totalvax=list(df3['new_vaccinations_smoothed_per_million'])

        list1 = [[country[i],totalvax[i]] for i in range(len(country))] 
        map1 = Map(init_opts=opts.InitOpts(width='1000px', height='460px'))
        map1.add('Total Confirmed Vaccinations', list1, maptype='world')
        map1.set_series_opts(label_opts=opts.LabelOpts(is_show = False)) 

        map1.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=100 , is_piecewise = True, pieces=[
        {'min': 9000, 'max': 9999},
        {'min': 7000, 'max': 8999},
        {'min': 5000, 'max': 6999},
        {'min': 3000, 'max': 4999},
        {'min': 1, 'max': 2999},
        {'max': 0},]),
        title_opts=opts.TitleOpts(title= "Covid-19 Worldwide Total Vaccinations INST326 Final", subtitle= 'Till November 5th, 2021', pos_left= 'center', padding=0, item_gap=2,
        title_textstyle_opts= opts.TextStyleOpts(color='blue', font_weight= 'bold', font_family= 'Courier New', font_size=30), 
        subtitle_textstyle_opts= opts.TextStyleOpts(color='black', font_weight='bold', font_family='Courier New', font_size=20)), 
        legend_opts=opts.LegendOpts(is_show=False))
        return map1.render_notebook()
    #Yahya
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
   
#Christine      
def main(infile):
    """
    This function creates an instance of the Govax() class. This function also
    prints out a map of the covid data into a new browser. By using the 
    webbrowser module from https://stackoverflow.com/questions/31715119/how-can-
    i-open-a-website-in-my-web-browser-using-python, it will open the printed 
    map in a new browser and would return back True in the terminal.
    
    This function will also use the os module from https://stackoverflow.com
    /questions/40905703/how-to-open-an-html-file-in-the-browser-from-python
    to help print out the covid map from the correct path.
    
    
    Args:
        self (keyword) : binds the attributes with the given arguments.  
    
    Attributes:
        file (str) : string that contains the html of the covid data
       
    Returns:
        (image) : the created image of the map containing 
        covid results from countries all around the world in a new web
        browser.
    """
    a1 = Govax("covid.csv")
    a1.map()
    print(a1.map())
    
    print('Please use jupyter notebook to view the map printed in terminal' + 
          ' or open render.html directly'
          )
    webbrowser.open('file://'+os.path.realpath('render.html'))
#Ishika
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect one mandatory arguments:
        - filename: a path to a CSV file containing covid data.
        
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("infile", help="path to CSV file containing covid data.")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.infile)

    

