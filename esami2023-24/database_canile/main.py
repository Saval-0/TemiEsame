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

def get_breed_level_avg(dogs, breed, level):
    totScore = 0
    count = 0
    for key in dogs:
        dog = dogs[key]
        if dog[1] == breed and dog[2] == level:
            totScore += float(dog[-1])
            count += 1

    if count == 0:
        return 0
    return round(totScore / count, 2)

# ['German Shepherd', 'Rottweiler', 'Poodle', 'Yorkshire Terrier', 'Golden Retriever', 'Beagle', 'Dachshund', 'Boxer', 'Bulldog', 'Labrador Retriever']
# ['Intermediate', 'Beginner', 'Advanced', 'Expert']

def main():
    dogs = {}
    breeds = []
    levels = []

    dogsFile = open('dogs.csv', 'r')
    for i, line in enumerate(dogsFile):
        if i == 0 or line == "":
            continue
        record = line.rstrip().split(",")
        dogId = record[0]
        if dogId not in dogs:
            dogs[dogId] = []
        
        if record[2] not in breeds:
            breeds.append(record[2])
        if record[3] not in levels:
            levels.append(record[3])
        
        for i, field in enumerate(record):
            if i == 0:
                continue
            dogs[dogId].append(field)
    dogsFile.close()

    top = 0
    topBreed = ""
    for breed in breeds:
        print("Razza: " + breed)
        for level in levels:
            avg = get_breed_level_avg(dogs, breed, level)
            if level == "Expert" and avg > top:
                topBreed = breed
                top = avg
            if avg != 0:
                print(" * Livello " + level + ": media " + str(avg))

    print("\n\nLa razza con il punteggio medio più alto per il livello Expert è " + topBreed  + ".")

    return

main()