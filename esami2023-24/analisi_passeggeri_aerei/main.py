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

def insertAge(avgAge, passenger):
    age = passenger[1].rstrip()
    country = passenger[3].rstrip()
    if country not in avgAge:
        avgAge[country] = [ 0, 0 ]

    avgAge[country][0] += int(age)
    avgAge[country][1] += 1
    return


def insertFlight(flights, passenger, mostPop):
    flight_num = passenger[5].rstrip()
    gender = passenger[2].rstrip()
    if flight_num not in flights:
        flights[flight_num] = [ {"M": 0, "F": 0}, 0 ]
    currFlight = [ flight_num, flights[flight_num] ]
    
    currFlight[1][0][gender] += 1
    currFlight[1][1] += 1

    if len(mostPop) == 0 or mostPop[1][1] < currFlight[1][1]:
        mostPop = currFlight
    return mostPop


def main():
    file = open("passeggeri.txt", "r", encoding="utf-8")

    skip = True
    avgAge = {}
    flights = {}
    mostPop = []
    for line in file:
        if skip:
            skip = False
            continue

        passenger = line.split(",")

        insertAge(avgAge, passenger)
        mostPop = insertFlight(flights, passenger, mostPop)

    for country in avgAge:
        avg = avgAge[country][0]/avgAge[country][1]
        print("Avg Age in " + country + " is " + str(round(avg, 1)))

    print("Numero di volo più popolare: " + mostPop[0] + ", Passeggeri M: " + str(mostPop[1][0]["M"]) + "/ F: " + str(mostPop[1][0]["F"]))

    return


main()
