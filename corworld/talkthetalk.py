import win32com.client as wincl
from numbtoword import numb_to_word


#Function responsible of telling the user daily update in new cases
#Text to Speech with SAPI
def you_tell(new_cases,new_deaths):
    speak=wincl.Dispatch("SAPI.SpVoice")    

    if new_cases!=0 and new_cases!="N/A" and new_deaths!=0 and new_deaths!="N/A":
        speak.Speak("Hey man, i did my job...")
        print(new_cases)        
        new_cases_word=numb_to_word(str(new_cases))
        print(new_deaths)
        new_deaths_word=numb_to_word(str(new_deaths))
        speak.Speak("Today, there were around "+new_cases_word+"... new cases...")
        speak.Speak("and around"+new_deaths_word+"... new deaths in the world.")      
    else:
        speak.Speak("Something went wrong, check out DOM...")

