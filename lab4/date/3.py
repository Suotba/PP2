from datetime import datetime

current_datetime = datetime.now()


without_microseconds = current_datetime.replace(microsecond=0)

print("Full DateTime:", current_datetime)
print("DateTime without Microseconds:", without_microseconds)
