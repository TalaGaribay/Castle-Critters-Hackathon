import os
os.system('cls')   # Windows
print('Hey Guys')


Username=input('Username:')
points=10
tasks_total=10
tasks_completed=6
tasks_left=tasks_total-tasks_completed
level=0
next_level=10
while points>=next_level: 
    level=level+1
    next_level=next_level*1.2

print(Username+ " is level " +str(level)+ '!')
print("Tasks left:" +str(tasks_left))