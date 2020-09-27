time = int(input('time in sec '))
hour = time // 3600
min = time // 60 % 60
sec = time % 60

if hour < 10 or hour <= 0:
    hour = '0' + str(hour)
if min < 10 or min <= 0:
    min = '0' + str(min)
if sec < 10 or sec <= 0:
    sec = '0' + str(sec)

print(f"{hour}:{min}:{sec}")
