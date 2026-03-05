#https://cs50.harvard.edu/python/psets/3/outdated/

from datetime import date

month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month_number ={
}

# 9/8/1636 or September 8, 1636



#new_date = date.fromisoformat(your_date)

#print(new_date)

while True:

    try:
        your_date = input("Date: ")
        if your_date.find('/') > -1:
            month, day, year = your_date.split('/')
            if int(month) > 12:
                 raise ValueError
            elif int(day) > 31:
                 raise ValueError
            #print(f"test: {month:01}")
            newdate = year.strip() + '-' + f"{int(month):02}" + '-' + f"{int(day):02}"
            print(f"{newdate}")
            break
        elif your_date.find(',') > -1:
            month_and_day, year = your_date.split(',')
            month, day          = month_and_day.split(' ')
            if int(day)>31:
                 raise ValueError

            i = 1
            for _ in month_list :

                month_number[_] = i
                i = i + 1

            if month in month_number:
                #print(month_number)
                print(year.strip() +"-"+f"{int(month_number[month]):02}"+"-"+f"{int(day):02}")
                break
            else:
                 raise ValueError


    except ValueError:

            pass











#print(date)
