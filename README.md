
<<<<<<< HEAD
# INST326-Chocolate-Chips
=======
Important files:
vaxdata.py - Our code
covid.csv - The csv file that is a required parameter to run the code
render.html -The file that contains the map information that would be shown in 
a new web browser tab 
README.md-The file that contains any websites or videos we cited and 
used in our code, contributions by all members, and any important instructions 
for running the final code



External packages needed to be installed:
pyecharts 
pip install pyecharts==1.7.1



Running the code:
For macs: python3 .\vaxdata.py covid.csv
For windows: python .\vaxdata.py covid.csv 
Another way for windows if there are difficulties: py .\vaxdata.py covid.csv

Contribution:
Yahya contributed by working on the def map and def secure functions
Christine contributed by working on the def read and def main functions
Ishika contributed by working on the def init and def parse_args functions


Interpretation of  the code:
After running the code in the terminal with the correct command, 
the program would print out the results of the total covid vaccinations 
per country and continent till November 5th, 2021. For instance, when the 
code is used with the terminal on a windows laptop, it will also print out 
the statement, “Please use jupyter notebook to view the map printed in the 
terminal or open render.html directly.” This statement would also print 
out along with the map in a new web browser on a window’s laptop in the 
situation, the map fails to print out correctly. 

In addition, with our code a user would be able to see and identify which 
country and which contient had the largest amount of citizens having a 
covid vaccination. It would also allow the user to see which country or contient
was mostly affected by Covid-19.


References:

“Dynamic Mapping of the Progression of COVID-19 Using Python Programming.” 
YouTube, YouTube, 18 Apr. 2020, https://www.youtube.com/watch?v=vLEA8dCfusQ. 
Accessed 20 Dec. 2021.


“[ Flask Tutorial ] 17 Flask使用pyecharts绘制图表.” YouTube, YouTube, 27 Sept. 
2020, https://www.youtube.com/watch?v=BYAwEYwWHyQ.

Han, Di(Candance). “How to make a Coronavirus world map in Python.” 6 Jul. 
2020, https://towardsdatascience.com/how-to-make-a-coronavirus-
world-map-in-python-734c9fd87195, accessed 15 Nov. 2021.

“How to Create Coronavirus Case Heat Map on Top of Worldmap in Python.” 
YouTube, YouTube, 28 Mar. 2020, https://www.youtube.com/watch?v=GyMO9WCEheQ&amp;
t=24s.

“How can I open a website in my web browser using Python?” stackoverflow, 
30 Jul. 2015, https://stackoverflow.com/questions/31715119/how-can-i-open-a%20-website-in-my-web-browser-using-python, accessed 19 December 
2021. 

“How to open an HTML file in the browser from Python?” stackoverflow, 1 Dec. 
2016, https://stackoverflow.com/questions/40905703/how-to-open-an-html%20-file-
in-the-browser-from-python, accessed 19 December 2021.

How each source was implemented into the code:
The Dynamic mapping, Flask Tutorial, and How to create a Coronavirus case 
youtube videos were able to help us figure out how to set up the world map 
containing information of the total cases of Covid per location. In addition, 
the website, by Han Di, was very educational and also helped us with the final 
code. For instance, the source helped us with color coding the map based on the 
total amount of covid cases collected per country and continent.  The “How to 
Create Coronavirus Case Heat Map” article helped with how to use the pyecharts 
package. This article was really helpful when using the built-in Map() 
function within the package to create the map including 
how to set the title font style and size. 


While we were moving forward with our final project, we did encounter some 
challenges with getting our code to print out the colored map with total covid 
vaccination data. The first website that helped Christine with this challenge 
was from the website, “How can I open a website in my web browser using 
Python?”, from stackoverflow. From this website, we were able to implement 
the webbrowser module to help us open the map in a new web browser tab. 
Our next challenge was getting the map to open on a Mac. 

For instance, two of our members use a Mac laptop and were having 
difficulty getting the map to open in a new browser tab, whereas I (Christine) 
was able to print out the map in a new web browser tab. To overcome this 
challenge, I was able to find the website, “How to open an HTML file in 
the browser from Python?”, from stackflow and implemented the os module. 
By importing the os module, it would be a lot easier for those using a Mac 
to print out the html file containing the map information. 

