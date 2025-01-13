# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~

import random

giornate = {}
players = {}
green = {}
red = {}

def genDay(pOne, pTwo):
    
    return

def main():
    file = open('qualificati.txt', 'r')
    for line in file:
        if line == "":
            continue
        
        player = line.strip().split(",")
        player = set([ int(player[0]), player[1] ])
        players[player[0]] = player[1]
        if player[0] == 1:
            green[player[0]] = player[1]
        if player[0] == 2:
            red[player[0]] = player[1]
    file.close()

    i = 1
    while i + 1 <= len(players) + 1:
        if i not in green and i not in red:
            choice = random.choice([i, i + 1])
            green[choice] = players[choice]
            if choice == i:
                red[choice + 1] = players[choice + 1]
            else:
                red[choice - 1] = players[choice - 1]
        i += 2

    greenFile = open("green.txt", "w")
    keys = list(green.keys())
    for i, key in enumerate(keys):
        greenFile.write(str(key) + " - " + str(green[key]) + "\n")
        
        giorante[i] = {

        }
        if i + 1 < len(keys):
            next_key = keys[i + 1]
            print(str(i) + " - " + str(key) + " - " + str(next_key))

        
    greenFile.close()

    redFile = open("red.txt", "w")
    for key in red:
        redFile.write(str(key) + " - " + str(red[key]) + "\n")
    redFile.close()

    print(players)
    print(green)
    print(red)
    return

main()
