while (1):
 hour,minute = input().split()
 hour=int(hour)
 minute=int(minute)
 if 0<=hour<=23 and 0<=minute<=59:break

while (1):
 cooking= input()
 cooking=int(cooking)
 if 0<=cooking<=1000: break

cooking_hour= cooking//60  
cooking_minute= cooking%60 
hour=hour +cooking_hour
minute=minute+cooking_minute
if minute>60:
     hour=hour+1
     minute=minute-60
     if hour>=24:
        hour=hour-24
print("{h} {m}".format(h=hour,m=minute))