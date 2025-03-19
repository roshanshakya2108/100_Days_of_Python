import time
timestamp = time.strftime('%H:%M')
print(timestamp)
if (timestamp < '12:00'):
    print('Good Morning')
elif (timestamp > '12:00' and timestamp < '17:00'):
    print('Good afternoon')
else:
    print('Good Night!')
