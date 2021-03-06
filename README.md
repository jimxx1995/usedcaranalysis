# Analysis of US Used Car Market
Can we predict real used car prices when KBB doesn't give an accurate estimation?
This project tried to provide a more accurate estimation of used car market prices by applying machine learning and web scraping techniques.
We created some interactive visualizations by Dash and Bokeh which give us an intuitive data exploration.

## Required Installations
The only installation needed to run this repo is Python. Click here to learn about how to install [Python](https://www.python.org/getit/). Once installed, you should be good to go!

## Data Source and Acquisition
We used Honda civic as an example for this project. The data was sourced from Craigslist SF Bay Area website. All web scraping functions are stored in the [data_function file](data_function.py), for more information about the functions, please refer to the [documentation file](documentation.md). The whole project and data are for academic and educational use only.


## Data Viz App (hosted by Heroku)

<h6>open the link below to see the web app, it may need a few minutes for activation since the web app will sleep if no traffic in a 30 minute period<h6>

we used Honda Civic as an example to create an web app for data visualizations, you can change it to any car you want in the [EDA Dash notebook](EDA_Dash.ipynb).

http://dash-viz.herokuapp.com/

## Interactive Data Viz (Created by Bokeh)
we also used Honda Civic as an example for the data visualization.

[Visualization](http://htmlpreview.github.io/?https://github.com/esmondhkchu/usedcaranalysis/blob/master/Data_Visualization.html)

## Author
[Esmond Chu](http://esmondhkchu.github.io) [Jimmy Chan](http://jimxx1995.github.io)



## Licensing
In an effort to enable reproducible, collaborative research our project is subject to the MIT License which allows you to modify and distribute the above code for both private and commercial usage. See LICENSE to learn more.
