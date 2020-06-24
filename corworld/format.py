

# format_row function is responsible for filtering one row of the scraped table (by filtering i mean....)
# format row function takes a array of data as an argument (that is acctually a row of scraped table)
# and then filter the data in array (delete/replace commas, +, -, N/A, whitespaces)
#returns a new array of data with clean data suitable and ready for storing in database


def format_row(maxid,array_data):
   
    country=array_data[1]
    total_cases=0
    new_cases=0
    total_deaths=0
    new_deaths=0
    total_recover=0
    active_cases=0
    seriously_critical=0
    tot_cases_per_mil=0
    tot_deaths_per_mil=0

    if array_data[2]:
        total_cases=array_data[2].replace(',','').strip()    
     
    if array_data[3]:
        new_cases=array_data[3].replace(',','').replace('+','').strip()      
     
    #tu baca  <td ...> </td> 
    if array_data[4] and array_data[4]!=" ":
        total_deaths= array_data[4].replace(',','').replace('+','').strip()           
 
    if array_data[5]:
        new_deaths=array_data[5].replace(',','').replace('+','').strip() 

    if array_data[6] and array_data[6]!="N/A" :
        total_recover=array_data[6].replace(',','').strip()             
   
    if array_data[7] and array_data[7]!="N/A":
        active_cases=array_data[7].replace(',','').strip()          
 
    if array_data[8] and array_data[7]!="N/A":
        seriously_critical=array_data[8].replace(',','').strip()         
 
    if array_data[9]:
        tot_cases_per_mil=array_data[9].replace(',','').strip()   

    if array_data[10]:
        tot_deaths_per_mil=array_data[10].replace(',','').strip()
     

    return [maxid,country,total_cases,new_cases,total_deaths,new_deaths,total_recover,active_cases,seriously_critical,tot_cases_per_mil,tot_deaths_per_mil,"same"]
  

    #print(array_data[0]) #1
    #print(array_data[1]) #USA          country
    #print(array_data[2]) #1,526,007    total cases
    #print(array_data[3]) #+18,234      new cases
    #print(array_data[4]) #90,931       total deaths
    #print(array_data[5]) #+818         new deaths
    #print(array_data[6]) #344,920      total recovered
    #print(array_data[7]) #1,090,873    active cases
    #print(array_data[8]) #16,353 serious critcal
    #print(array_data[9]) #4,616 cases/1m
    #print(array_data[10]) #275 death/1m total  
    #print(array_data[11]) #11,784,538 total tests
    #print(array_data[12]) #35,629 test/1m
    #print(array_data[13]) #330,764,077 Population