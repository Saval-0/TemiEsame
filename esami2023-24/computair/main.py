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

weathers = {}
flights = {}
avgPass = [ 0, 0 , 0 ]
def main():
    flightsFile = open('flights.txt', 'r')
    for line in flightsFile:
        flight = line.strip().split(";")
        avgPass[1] += int(flight[2])
        avgPass[0] += 1
        flights[flight[0]] = [ flight[1], flight[2]]

    flightsFile.close()

    print(flights)

    avgPass[2] = avgPass[1]/avgPass[0]
    print("Numero medio di passeggeri: " + str(avgPass[2]))

    weatherFile = open('weather.txt', 'r')
    for line in weatherFile:
        weather = line.strip().split(";")
        weathers[weather[0]] = weather[1]

    print("Codice dei voli verso città con condizione meteorologica Rainy o Stormy: ")
    for key in flights:
        for city in weathers:
            if flights[key][0] == city and (weathers[city] == "Rainy" or weathers[city] == "Stormy"):
                print("* " + key + " verso " + city + ": " + weathers[city])

    print("Condizione meteorologica delle città che sono destinazione di almeno un volo: ")
    for city in weathers:
        cityPass = 0
        for key in flights:
            if flights[key][0] == city:
                cityPass += int(flights[key][1])
        if cityPass != 0:
            print("* " + city + ": " + weathers[city] + ". " + str(cityPass) + " passeggeri in arrivo.")

    
    return

main()