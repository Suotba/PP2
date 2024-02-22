from datetime import datetime, timedelta
d = int(input("Day: "))
m = int(input("Month: "))
ye = int(input("Year: "))
x = datetime(ye, m , d)
y = x - timedelta(days=5)

print("Current Date:", x.strftime("%d-%m-%Y"))
print("Five days ago:", y.strftime("%d-%m-%Y"))
