# Corona scrap and store

## About

This is a part of the data scraping project on Corona virus news and stats worlwide. Project goal was to collect data daily about Corona Virus cases and informations from different sources ( mostly websites / newspapers) in order to show its impact on economy, stock markets, unemployment (labour services), prices of oil, food price index etc.

In this small application/script, data is scraped, collected, filtered and stored in local database. After that program will tell the user (Text-to-Speech) daily update in new cases worldwide. This part of application is written in Python.

### Libraries:
* BeautifulSoup
* requests
* pymysql
* win32com 

If you combine this with some job scheduler software like Windows Task Scheduler or cron at Linux you almost got a bot.
To get most accurate data you should run the script around 2:00AM at (UTC+01.00) time zone.
**corona.sql** file is product of all this work. Data should be pretty accurate for European countries because script was usually ran between (22.00pm and 01:30am). But data for North and South America, Asia, and Australia will be incomplete, because different timezones. To get most out of this program you should run the program around 2:15am at UTC +1(Belgrade, Bratislava, Budapest). 
New cases for the next day start counting from around 3AM every day.

 **This was built with no intension to sell or redistribute collected data.**

## File overview



File | Explanation
------------ | -------------
baza.py | Database processing logic
tables.py | Scraping logic
format.py | Filter data (data)
numbtoword.py | Convert number to word
talkthetalk.py | Speak daily update in cases
start.py | main function


## 

**baza.py** - The class MySqlCommand involves database operations, there are six functions:
  * **get_connection()**
  * **close_connection()**
  * **insert_date(self,new_cases,new_deaths)** - populate table `date`
  * **select_max()** - get max_id from table `date`
  * **insert_row(self,max_id(date table),args)** - populate table `statistics` with current row (some country daily data)
  * **update_last()** - for a short period of time, there was the row "first case" so i updated the db with that row.
  
**tables.py** - there are five functions:
  * **get_table()** - creates a BeautifulSoup object, search through the tree and then returns a table that consist data
  * **get_new_data()** - returns a tuple with new cases and deaths (worldwide) that is extracted from table( get_table() )
  * **count_rows()** - returns number of rows in the scraped table
  * **scrap_table()** - this function scrap table, extract data from every row, and returns a 2D array.
  * **beautiful_table()** - this function filter 2D array (because data repetition)
 
**format.py**
  * **format_row(max,array_data)** - function takes array of data as an argument (that represent one row of scraped table) and then filter the data (delete/replace commas, +, -, N/A, whitespaces). Function returns a new array with clean data suitable and ready for storing into database.
 
 **talkthetalk.py**
   * **you_tell(new_cases,new_deaths):** - Function responsible of telling the user daily update in new cases. (Uses win32com library, that interact with the Microsoft Speech SDK to speak daily update).
   
   
# Screenshots

Inspecting the DOM...
![](screenshots/dom.png)

Result of **beautiful_table()** function:
![](screenshots/data2.png)

After iterating through 2D array from previous picture, and seeding the database.
![](screenshots/mysql.png)

# Test

Number of new cases in Belgium between 20-24 may.

```
SELECT date.daytimestring, s.country, s.new_cases, s.new_deaths FROM statistics s INNER JOIN date ON s.id=date.id where ( (s.country="Belgium") AND ( (date.daytimestring="2020-05-20") OR (date.daytimestring="2020-05-21") OR (date.daytimestring="2020-05-22") OR (date.daytimestring="2020-05-23") OR (date.daytimestring="2020-05-24") ) )

```
Result of query:

Day | Country | New cases | New deaths
------------ | ------------- | ------------- | -------------
2020-05-20 | Belgium | 192 | 42
2020-05-21 | Belgium | 252 | 36
2020-05-22 | Belgium | 276 | 26
2020-05-23 | Belgium | 299 | 25
2020-05-24 | Belgium | 282 | 43

 



