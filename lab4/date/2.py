from datetime import datetime, timedelta
d = int(input("Day: "))
m = int(input("Month: "))
ye = int(input("Year: "))
x = datetime(ye, m , d)
y = x - timedelta(days=1)
z = x + timedelta(days=1)

print("Yesterday:", y.strftime("%d-%m-%Y"))
print("Current Date:", x.strftime("%d-%m-%Y"))
print("Tomorrow:", z.strftime("%d-%m-%Y"))
