import os
os.system('cls')   # Windows
print('Hey Guys')


Username=input('Username:')
Character_name="Bob"
steps=10
level=0
next_level=10
while steps>=next_level:
    level=level+1
    next_level=next_level*1.2

print(Character_name+ " is level " +str(level)+ ' !')
#Testing, is this Billy?
#IT WORKS!!!! All WILL TREMBLE BEFORE ME!!!