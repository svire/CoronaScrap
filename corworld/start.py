from baza import *
from tables import get_new_data,beautiful_table
from format import format_row
from talkthetalk import you_tell

 
def main():
    baza=MySqlCommand()
    baza.get_connection()

    new_cases,new_deaths=get_new_data()
    baza.insert_date(new_cases,new_deaths) 

    baza.select_max()
    maxid=baza.max_id

    data=beautiful_table()
    for index in range(1,len(data)):
        red=format_row(maxid,data[index])   
        baza.insert_row(red[0],red[1],red[2],red[3],red[4],red[5],red[6],red[7],red[8],red[9],red[10],red[11])
    
    baza.close_connection()
    you_tell(new_cases,new_deaths)
   


if __name__=="__main__":
    main()
