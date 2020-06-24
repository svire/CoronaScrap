import requests
from bs4 import BeautifulSoup

 
#this function will return table with data
def get_table():
    #maybe you can guess the url
    url="https://www.worldometers.info/coronavirus"
    headers={"User-Agent":"Mozilla/5.0"}
    samotabla="<table></table>"
    try:
        response=requests.get(url,headers=headers)
        sapunica=BeautifulSoup(response.content,'html.parser')
        samotabla=sapunica.find_all('table',class_='table')   
    except requests.ConnectionError:
        print("Connection error, Check your internet connection first")

    return samotabla
#type(get_table())  <class 'bs4.element.ResultSet'>
 

#Returns tuple with new cases and new deaths worldwide for current date
def get_new_data():
    soup_object=BeautifulSoup(str(get_table()),'html.parser')
    #last row of table,that consist sumarized data for whole world
    last_row=soup_object.find_all('tr')[-1]
    new_cases=last_row.find_all('td')[3].text.replace(',','').replace('+','')
    new_deaths=last_row.find_all('td')[5].text.replace(',','').replace('+','')

    return new_cases,new_deaths

#returns a number of rows in table i wanna scrap
def count_rows():
    soup_object=BeautifulSoup(str(get_table()),'html.parser')
    all_rows=soup_object.find('tbody').find_all('tr')
    count=0     
    count=sum(1 for x in all_rows)    
    return count
 
 

#ali kad krene pomozi majko
def scrap_table():
    soup_object=BeautifulSoup(str(get_table()),'html.parser')
    all_rows=soup_object.find('tbody').find_all('tr')
    cijeli=[]
    for row in all_rows:
        columns=row.find_all('td')
        new_array=[]

        for column in columns:
            new_array.append(column.text)
            cijeli.append(new_array)


    return cijeli


#Returns a filtered two dimensional array 
#While scraping table (scrap_table) i got really weird results every 10th to 20th row is repeated like 2-3 times for no particular reason
#even if i examine DOM/response i dont see why.
#To prevent data repeatition i add this function.
def beautiful_table():
    cijeli=scrap_table()
    filtered_data=[]
    last_row_state="no_name"
    for index in range(1,len(cijeli)+1,10):
        if last_row_state==cijeli[index][1]:
            continue
        else:
            filtered_data.append(cijeli[index])
            last_row_state=cijeli[index][1]
     
    return filtered_data
    





