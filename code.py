import calendar
import datetime
import pickle
import os



def  yearcalender():         #Function to display specified Year Calendar.
    while True:
        try:
            print()          #For spacing.
            year= int(input("Enter Year(Type 0 to Exit.): "))
            if year==0:
                print("Hope you Enjoyed. Try out my other Features. :)")
                return False
            else:
                print(calendar.calendar(year))  
        except ValueError:
            print("Invalid Year. Please Enter Again.")




def monthcalendar():         #Function to display specified month calendar.
    while True:
        try:
            print()          #For spacing.
            year= int(input("Enter Year(Type 0 to Exit.): "))
            if year==0:
                print("Hope you Enjoyed. Try out my other Features. :)")
                break
            else:
                month= int(input("Enter Month: "))
                print(calendar.month(year, month))
               
        except Exception:
            print("Invalid Input! Please Enter Again.")


        
             
def day_of_date():           #Function to display day of specified daye
    
    while True:
        print()              #For spacing.
        year= int(input("Enter Year(Type 0 to Exit.): "))
        if year==0:
            print("Hope you Enjoyed. Try out my other Features. :)")
            return False
        else :
            month= int(input("Enter Month: "))
            if month in [1,3,5,7,8,10,12]:
                date= int(input("Enter Date: "))
                weekcal = calendar.weekday(year, month, date)
                if date in range(1,32):
                    
                    if weekcal==0:
                        print("DAY:  Monday")
                    elif weekcal==1:
                        print("DAY:  Tuesday")
                    elif weekcal==2:
                        print("DAY:  Wednesday")
                    elif weekcal==3:
                        print("DAY:  Thursday")
                    elif weekcal==4:
                        print("DAY:  Friday")
                    elif weekcal==5:
                        print("DAY:  Saturday")
                    elif weekcal==6:
                        print("DAY:  Sunday")
                    print()
                else :
                    print("Date is Out Of Range. Please Enter a Valid Date. ")
            
            elif month in [4,6,9,11]:
                date= int(input("Enter Date: "))
                weekcal = calendar.weekday(year, month, date)
                if date in range(1,31):
                    if weekcal==0:
                        print("DAY:  Monday")
                    elif weekcal==1:
                        print("DAY:  Tuesday")
                    elif weekcal==2:
                        print("DAY:  Wednesday")
                    elif weekcal==3:
                        print("DAY:  Thursday")
                    elif weekcal==4:
                        print("DAY:  Friday")
                    elif weekcal==5:
                        print("DAY:  Saturday")
                    elif weekcal==6:
                        print("DAY:  Sunday")
                    print()
                else :
                    print("Date is Out Of Range. Please Enter a Valid Date. ")

            elif month==2:
                leap= calendar.isleap(year)
                date= int(input("Enter Date: "))
                weekcal = calendar.weekday(year, month, date)
                if leap==True:
                    if date in range(1,30):
                        if weekcal==0:
                            print("DAY:  Monday")
                        elif weekcal==1:
                            print("DAY:  Tuesday")
                        elif weekcal==2:
                            print("DAY:  Wednesday")
                        elif weekcal==3:
                            print("DAY:  Thursday")
                        elif weekcal==4:
                            print("DAY:  Friday")
                        elif weekcal==5:
                            print("DAY:  Saturday")
                        elif weekcal==6:
                            print("DAY:  Sunday")
                            
                    else :
                        print("Date is Out Of Range. Please Enter a Valid Date. ")
                else :
                    if date in range(1,29):
                        if weekcal==0:
                            print("DAY:  Monday")
                        elif weekcal==1:
                            print("DAY:  Tuesday")
                        elif weekcal==2:
                            print("DAY:  Wednesday")
                        elif weekcal==3:
                            print("DAY:  Thursday")
                        elif weekcal==4:
                            print("DAY:  Friday")
                        elif weekcal==5:
                            print("DAY:  Saturday")
                        elif weekcal==6:
                            print("DAY:  Sunday")
                    else :
                        print("Date is Out Of Range. Please Enter a Valid Date. ")
            else :
                print("Please Enter a Valid Month. ")
                    



def is_leap():               #Function to check whether specified year is leap year or not.
    while True:
        try:
            print()          #For spacing.
            year= int(input("Enter Year(Type 0 to Exit.): "))
            if year==0:
                print("Hope you Enjoyed. Try out my other Features.:) ")
                return False
            else :
                print(calendar.isleap(year))
        except ValueError:
            print("Invalid Year! PLease Enter Again.")




def leapdays():              #Function to calculate total leapdays in range of two years.
    while True:
        try:
            print()          #For spacing.
            year_1= int(input("Enter First Year(Type 0 to Exit.): "))
            if year_1==0:
                print("Hope you Enjoyed. Try out my other Features. :)")
                return False
            else :
                year_2= int(input("Enter Last Year: "))
                print("Total Leapdays are: ",calendar.leapdays(year_1, year_2+1))

        except ValueError:
            print("Invalid Year! Please Enter Again.")




def to_day():                #Function to display present Date and Day.
    today_date= datetime.date.today()
    time_now = datetime.datetime.now()
    print("DATE: ",time_now)
    today_day= today_date.weekday()
    if today_day==0:
        print("DAY:  Monday")
    elif today_day==1:
        print("DATE:  Tuesday")
    elif today_day==2:
        print("DATE:  Wednesday")
    elif today_day==3:
        print("DATE:  Thursday")
    elif today_day==4:
        print("DATE:  Friday")
    elif today_day==5:
        print("DATE:  Saturday")
    elif today_day==6:
        print("DATE:  Sunday")
    print()


                                    

def age():                   #Function to Calculate User's Age.
    today_date= datetime.date.today()
    while True:
        try:
            print()              #For spacing.
            year= int(input("Enter Birth Year(Type 0 to Exit.): "))
            if year==0:
                print("Hope you Enjoyed. Try out my other Features. :)")
                return False
            else :
                month= int(input("Enter Birth Month: "))
                if month in [1,3,5,7,8,10,12]:
                    date= int(input("Enter Birth Date: "))
                    
                    if date in range(1,32):
                        
                        age_y = (today_date.year-year)
                        age_m = (today_date.month-month)
                        age_d = (today_date.day- date)
                        birthday = datetime.date(year, month, date)
                        age_days= (today_date-birthday).days
                        print("Your Age is ",age_y,"years ",age_m,"months and ",age_d,"days OR ",age_days,"days")
                    else :
                        print("Date is Out Of Range. Please Enter a Valid Date. ")
                
                elif month in [4,6,9,11]:
                    date= int(input("Enter Birth Date: "))
                    
                    if date in range(1,31):
                        age_y = (today_date.year-year)
                        age_m = (today_date.month-month)
                        age_d = (today_date.day- date)
                        birthday = datetime.date(year, month,date)
                        age_days= (today_date-birthday).days
                        print("Your Age is ",age_y,"years ",age_m,"months and ",age_d,"days OR ",age_days,"days")
                    else :
                        print("Date is Out Of Range. Please Enter a Valid Date. ")

                elif month==2:
                    leap= calendar.isleap(year)
                    date= int(input("Enter Birth Date: "))
                    
                    if leap==True:
                        if date in range(1,30):
                            age_y = (today_date.year-year)
                            age_m = (today_date.month-month)
                            age_d = (today_date.day- date)
                            birthday = datetime.date(year, month,date)
                            age_days= (today_date-birthday).days
                            print("Your Age is ",age_y,"years ",age_m,"months and ",age_d,"days OR ",age_days,"days")
                                
                        else :
                            print("Date is Out Of Range. Please Enter a Valid Date. ")
                    else :
                        if date in range(1,29):
                            age_y = (today_date.year-year)
                            age_m = (today_date.month-month)
                            age_d = (today_date.day- date)
                            birthday = datetime.date(year, month, date)
                            age_days= (today_date-birthday).days
                            print("Your Age is ",age_y,"years ",age_m,"months and ",age_d,"days OR ",age_days,"days")
                        else :
                            print("Date is Out Of Range. Please Enter a Valid Date. ")
                else :
                    print("Please Enter a Valid Month. ")
        except Exception:
            print("Invalid Input. Please Enter Again.")
            

def create():
    file= open("database.dat", "ab") 
    
    while True:
        try:
            print()
            Name_of_event = input("Enter Name of the Event(Enter 'N' to Exit): ")
            if Name_of_event=='N':
                return False
            else :
                year = int(input("Enter Year for Event(Enter 0 to Exit): "))
                if year==0:
                    return False
                else :
                    month = int(input("Enter Month: "))
                    if month in [1,3,5,7,8,10,12]:
                        date_s = int(input("Enter Start Date: "))
                        if date_s in range(1,32):
                            date_e = int(input("Enter End Date: "))
                            if date_e in range(1,32):
                                
                                record = [Name_of_event, year, month, date_s, date_e]
                                pickle.dump(record, file)
                            else :
                                print("Date is Out Of Range. Please Enter a Valid Date.")
                        else :
                            print("Date is Out Of Range. Please Enter a Valid Date.")
                    
                    elif month in [4,6,9,11]:
                        date_s = int(input("Enter Start Date: "))
                        if date_s in range(1,31):
                            date_e = int(input("Enter End Date: "))
                            if date_e in range(1,31):
                                
                                
                                record = [Name_of_event, year, month, date_s, date_e]
                                pickle.dump(record, file)
                            else :
                                print("Date is Out Of Range. Please Enter a Valid Date.")
                        else :
                            print("Date is Out Of Range. Please Enter a Valid Date.")

                    elif month==2:
                        leap= calendar.isleap(year)
                        date_s = int(input("Enter Start Date: "))
                        if leap==True:
                            if date_s in range(1,30):
                                date_e = int(input("Enter End Date: "))
                                if date_e in range(1,30):
                                    
                                    
                                    record = [Name_of_event, year, month, date_s, date_e]
                                    pickle.dump(record, file)
                                else :
                                    print("Date is Out Of Range. Please Enter a Valid Date.")
                            else :
                                print("Date is Out Of Range. Please Enter a Valid Date.")
                        else :
                            if date_s in range(1,29):
                                date_e = int(input("Enter End Date: "))
                                if date_e in range(1,29):
                                    
                                    
                                    record = [Name_of_event, year, month, date_s, date_e]
                                    pickle.dump(record, file)
                                else :
                                    print("Date is Out Of Range. Please Enter a Valid Date.")
                            else :
                                print("Date is Out Of Range. Please Enter a Valid Date.")



                    else :
                       print("Invalid Month.")
        except ValueError:
            print("Invalid Input. Please Enter Again.")
    file.close()
                



def delete():
    find = 0
    file = open("database.dat", "rb")
    temp_file = open("Temp.dat", "wb")
    Event = input("Enter the Name of Event you wanna Remove: ")
    try:
        while True:
            record = pickle.load(file)
            if record[0]==Event:
                find+=1
            else :
                pickle.dump(record, temp_file)
    except EOFError:
        file.close()
        temp_file.close()
    if find==0:
        print("Event Not Found.")
    os.remove("database.dat")
    os.rename("Temp.dat", "database.dat")




def read():
    
    file = open("database.dat", "rb")
    try:
        while  True:
            record = pickle.load(file)
            Event = record[0]
            DateS = datetime.date(record[1], record[2], record[3])
            DateE = datetime.date(record[1], record[2], record[4])
            
            print(f"Event- {Event}\nStart Date- {DateS}\nEnd Date- {DateE}")
            print()

    except EOFError:
        file.close()


def search():
    with open("database.dat", "rb") as file:
        event = input("Enter Name of the Event you wanna Search: ")
        found = 0
        try:
            while True and found==0:
                record = pickle.load(file)
                if record[0]==event:
                    print("Event Found.")
                    Event = record[0]
                    DateS = datetime.date(record[1], record[2], record[3])
                    DateE = datetime.date(record[1], record[2], record[4])
            
                    print(f"Event- {Event}\nStart Date- {DateS}\nEnd Date- {DateE}")
                    print()

                    found+=1
        except EOFError:
            print("No such Event")


def Intro():
    Name = input("Enter Your Name: ")
    print(f"Hey {Name.title()}! WhatsUp!!, I am HANDICAL 1.01SF, Your Presonal Scheduler. Welcome Back!! \n Try Out My these Features And Enjoy...")
    print()
    
    

def options():
    while True:
        try:
            print()                #For spacing.
            opt= int(input("Enter Your Choice: "))
            

            if opt==1:
                print()   #For spacing.
                yearcalender()  #Function Call
                
            elif opt==2:
                print()   #For spacing.
                monthcalendar() #Function Call
            
            elif opt==3:
                print()   #For spacing.
                day_of_date()   #Function Call
            
            elif opt==4:
                print()   #For spacing.
                is_leap()       #Function Call
            
            elif opt==5:
                print()   #For spacing.
                leapdays()      #Function Call

            elif opt==6:
                print()   #For spacing.
                age()          #Function Call

            elif opt in [7,8,9,10]:  #Password Protected Options.
                password = int(input("Enter Password: "))  
                if password==1907:       #Password=1907
                    if opt==7:
                        print()   #For spacing.
                        create()        #Function Call
                    elif opt==8:  
                        print()   #For spacing.
                        read()           #Function Call
                    elif opt==9:
                        print()   #For spacing.
                        delete()
                    elif opt==10:
                        print()
                        search()          
                else :
                    print("ACCESS DENIED! Incorrect Password. ")
            
            elif opt==0:
                print()   #For spacing.
                print("Thanks For Using. BABYE..:)")
                print("Press any key to leave.")
                return False

                
            else:
                print()
                print("Invalid Choice")
            

           
        except Exception:
            print("Invalid Input. Please Enter Again.")

 



def choices():               #Function to display choices.
    print("FOR CALENDAR PURPOSE: ")
    print("1. For Year Calendar.")
    print("2. For Month Calendar.")
    print("3. For Day Calendar.")
    print("4. To check Leap Year.")
    print("5. To count total Leapyears in range of Two Years.")
    print("6. To Calculate Your Age. ")
    print()
    print("FOR EVENTS SCHEDULING:(Password Encrypted!) ")
    print("7. To Schedule an Event/Important Dates/Appointments.")
    print("8. To View all Events.")
    print("9. To Delete an Event.")
    print("10. To Search For an Event.")
    print()
    print("0. TO EXIT.")


    




def lets_begin():            #Function to call All Functions.
    to_day()
    Intro()
    choices()
    options()
    input()   
    
lets_begin()

        





