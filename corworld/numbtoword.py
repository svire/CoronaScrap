 


num_word = {0:' ',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}   

num_word2 = ['Zero','Ten','Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'] 


"""
numb_to_word function converts number to text
"""

def one_digit(numb):
    numb_str=num_word[int(numb)]
    return numb_str

	
def over_under_twenty(numb,pos,pos2):
    two_digits="something"
    sum_of_two=int(str(numb[pos])+str(numb[pos2]))
    if sum_of_two <20:
        two_digits=num_word[sum_of_two]       
    else:       
        if str(numb[pos2])=="0":
            two_digits=num_word2[int(numb[pos])]
        else:
            two_digits=num_word2[int(numb[pos])]+" "+num_word[int(numb[pos2])]      
         
    return two_digits  

	
def two_digits(numb):
    two_dig=over_under_twenty(numb,0,1)
    return two_dig

    
def three_digits(numb,last=False):
    three_dig=""    
    if last==True and int(numb)!=0:           
        last_three_digits=int(numb)
        last_three_digits= "00"+str(last_three_digits) if last_three_digits <10 else ("0"+str(last_three_digits) if last_three_digits < 100 else last_three_digits)     
        numb=str(last_three_digits)        
        three_dig=over_under_twenty(numb,1,2) if numb[0]=="0" else num_word[int(numb[0])]+" "+"hundred and"+' '+over_under_twenty(numb,1,2)  
    
    elif int(numb)==0 or numb=="000":
        three_dig=","
    else:
        three_dig=over_under_twenty(numb,1,2) if numb[0]=="0" else num_word[int(numb[0])]+" "+"hundred and"+' '+over_under_twenty(numb,1,2)  
    return three_dig


def four_digits(numb):
    last_three_digits=int(numb)-int(numb[0])*1000
    four_dig=num_word[int(numb[0])]+" thousand..."+three_digits(str(last_three_digits),True)
    return four_dig
 
 
def five_digits(numb):                
    last_three_digits=int(numb)-int(str(numb[0])+str(numb[1]))*1000 
    five_dig=over_under_twenty(numb,0,1)+" thousand..."+three_digits(str(last_three_digits),True) 
    return five_dig


def six_digits(numb):    
    last_five=str(int(numb)- int(str(numb[0]))*100000)
    six_dig="six"
    rest=four_digits(last_five) if numb[1]=="0" else five_digits(last_five)  
    six_dig=num_word[int(numb[0])]+" hundred "+rest    
    return six_dig   
       

def numb_to_word(numb):
    numb_string="something"
    numb_string={       
        1:one_digit,
        2:two_digits,
        3:three_digits,
        4:four_digits,
        5:five_digits,
        6:six_digits
        }[len(str(numb))](str(numb))               

    return numb_string
 
 