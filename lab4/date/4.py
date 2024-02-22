from datetime import datetime

date_str1 = input("First date (Year-Month-Day Hour:+Minute:Sec): ")
date_str2 = input("Second date (Year-Month-Day Hour:Minute:Sec): ")

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M:%S")


dif = date2 - date1


dif_in_sec = dif.total_seconds()

if dif_in_sec > 0:
    print(f"The difference between the two dates is {dif_in_sec} seconds.")
else :   
    dif_in_sec2 = -dif_in_sec
    print(f"The difference between the two dates is {dif_in_sec2} seconds.")




