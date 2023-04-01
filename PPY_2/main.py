import random
import getpass

##zad1
#numbers_input = input("Enter numbers: ")
#numbers_list = numbers_input.split(",")
#
#for elem in numbers_list:
#    elem = int(elem)
#
#min = numbers_list[0]
#max = numbers_list[0]
#for elem in numbers_list:
#    if min > elem:
#        min = elem
#    else:
#        pass
#
#    if max < elem:
#        max = elem
#    else:
#        pass
#print(min)
#print(max)
#
##zad2
#cities = "Warszawa,Kraków,Wrocław,Łódź,Poznań,Gdańsk,Szczecin,Bydgoszcz,Lublin,Białystok,Suwałki,Płock,"
#cities_list = cities.split(",")
#
#plan = ["a", "b"]
#
#plan.clear()
#while(len(plan)  < 10):
#    x = random.randint(0, len(cities_list)-1)
#    if plan.__contains__(cities_list[x]):
#        x = random.randint(0, len(cities_list)-1)
#    else:
#        plan.append(cities_list[x])
#
#print(plan)

#zad3
print("Rock-Paper_Scissors")
rounds = int(input("Please enter number of rounds you want to play: "))
mode = input("Please enter mode you want to play (computer/hot seat): ")
player_1 = input("Enter 1st player`s nickname:")

if mode == "computer":
    player_2 = "PC"
else:
    player_2 = input("Enter 2nd player`s nickname:")

moves = ["scissors", "paper", "rock"]
results = [0, 0]
round_count = 1
while rounds > 0:
    print("Round: " + str(round_count))
    #1st player turn
    move_1 = getpass.getpass(prompt="Enter your move: ")

    #2nd player turn
    if(mode == "computer"):
        move_2 = random.choice(moves)
    else:
        move_2 = getpass.getpass(prompt="Enter your move: ")

    if((move_1 == "sciccors" and move_2 == "paper") or (move_1 == "paper" and move_2 == "rock") or (move_1 == "rock" and move_2 == "scissors")):
        results[0] = results[0] + 1
    elif (move_1 == move_2):
        pass
    else:
        results[1] = results[1] + 1

    rounds = rounds - 1
    round_count = round_count + 1

if(results[0] > results[1]):
    print(player_1 + " wins")
elif(results[0] == results[1]):
    print("Draw")
else:
    print(player_2 + " wins")