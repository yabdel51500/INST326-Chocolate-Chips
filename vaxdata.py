"""
Yahya Abdelhamid
INST326(0101)
Group Chocolate Chips
Final check-in 1
"""
import pandas as pd

def main(infile):
    """
    The main function reads the csv file and acsesses the information from October 25th of this year.
    Pandas is used to vizualise the data. Of cource when we need to actually use the data we will not
    only use the first 5 rows, this was just for vizualization purposes. 
    
    Args:
        infile (str) : the name of the csv file of the covid data.
    
    """
    df1 = pd.read_csv(infile)
    df1['date'] = pd.to_datetime(df1['date'])
    df2 = df1.sort_values(by = ['date'], ascending = False)
    df3 = df2[df2['date'] == '2021-10-25']
    df3.reset_index(drop = True, inplace = True)
    print(df3.head())

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

    