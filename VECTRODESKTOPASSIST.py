import os
import datetime
import webbrowser


print("AI for you!!!")


 

def open_code():
    os.system('code')

def open_browser():
    webbrowser.open_new(' ')

def show_time():
    print(datetime.datetime.now())  

def os_version():
    print(os.version())




        
    
while True:

    ask = input('What you wanna do? - ')

    if ask == "open code":
        open_code()

    if ask == 'open browser':
        open_browser()

    if ask == 'what is the time':
        show_time()    

    if ask == 'search google':
        query = input('What to Search -> ')

        webbrowser.open(f'https://www.google.com/search?q={query}')   
    
    if ask == 'open youtube':
        webbrowser.open("youtube.com")

    if ask == 'open google':
        webbrowser.open("google.com")

    if ask == 'open stackoverflow' :
        webbrowser.open("stackoverflow.com")

    if ask == "what is the weather":
        place = input('Of which place? - ')
        webbrowser.open(f'https://www.google.com/search?q=weather%20of%20%20{place}')  


         

    if ask == 'shut down pc':
        time = int(input('In how many seconds? - '))
        
        os.system(f'shutdown /s /t {time}')  
    
    if ask == 'wish me':
        hour = int(datetime.datetime.now().hour)

        if hour>= 0 and hour < 12:
            print("Good Morning")

        if hour >=12 and hour < 18:
            print("Good Afternoon")      

        else:

            print("Good Evening")             
        

    if ask == 'quit':
        quit()
