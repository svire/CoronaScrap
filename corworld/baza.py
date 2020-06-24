import pymysql.cursors 
from datetime import date,datetime 


class MySqlCommand(object):

    def __init__(self):
        self.host='localhost'
        self.user='root'
        self.password=''
        self.db='corona'
        self.charset='utf8mb4'
        self.connection=""
        self.get_connection()        


    def get_connection(self):
        try:            
            self.connection=pymysql.connect(host=self.host, user=self.user, password=self.password, db=self.db, charset=self.charset)
            self.cursor=self.connection.cursor()
        except pymysql.Error:
            raise RuntimeError("Cannot connect to database")


    def close_connection(self):
        self.cursor.close()
        self.connection.close()        


    #return maxid from `date` table
    def select_max(self):
        sql="SELECT MAX(`id`) from `date`"         
        try:            
            self.cursor.execute(sql,())
            result=str(self.cursor.fetchone())
            #maxid=result.replace('(','').replace(',','').replace(')','')
            self.max_id=result.replace('(','').replace(',','').replace(')','')   

        except pymysql.Error:
            raise RuntimeError("Cant get id from date table")
         
    #Update first_case row in statistics table (that row in table, no longer exist)    
    def update_last(self,id,value):
        sql="update statistics set first_case=%s where id=%s"
        try:
            self.cursor.execute(sql,(value,id))
            self.connection.commit()
        
        except pymysql.Error as e:
            print("DB error while updating statistics table: "+e)
    

    def insert_date(self,new_cases,new_deaths):
        datestring=date.today()
        timestring=datetime.now()
        sql = "INSERT INTO `date` (`daytimestring`, `time`, `new_cases`,`new_deaths`) VALUES ( %s, %s,%s,%s)"
        try:
            self.cursor.execute(sql, (datestring, timestring, new_cases, new_deaths))
            self.connection.commit()
        except pymysql.Error as e:
            print("DB error while inserting data into `date` table : "+e)

	
    def insert_row(self,max, country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious_critical, total_cases_per, total_deaths_per,first_case):
        sql="INSERT INTO `statistics`(`id`,`country`, `total_cases`, `new_cases`, `total_deaths`, `new_deaths`, `total_recovered`, `active_cases`, `serious_critical`, `total_cases_per`, `total_deaths_per`,`first_case`) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"
        try:
            self.cursor.execute(sql,(max, country, total_cases, new_cases, total_deaths, new_deaths, total_recovered, active_cases, serious_critical, total_cases_per, total_deaths_per,first_case))
            self.connection.commit()
        except pymysql.Error as e:
            print("DB error while inserting data into `statistics` table : "+str(e))
             


 
 
