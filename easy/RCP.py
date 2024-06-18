import random

list = ['グー' ,'チョキ','パー']

player = input("あなた:")

com = random.choice(list)
print("com:{}".format(com))

if player == com:
    print('drew')
elif player == list[0]:
    if com == list[1]:
        print('you win')
    elif  com == list[2]:
        print('you lose')
elif player == list[1]:
    if com == list[2]:
        print('ypu win')
    elif com == list[0]:
        print('you lose')
elif player == list[2]: 
    if com == list[1]:
        print('you win')
    elif com == list[0]:
        print('you lose')
