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

def main():
    studenti = {}
    fileStudenti = open('studenti.csv', 'r')
    for i, line in enumerate(fileStudenti):
        if i == 0:
            continue
        
        record = line.rstrip().rsplit(",")
        idStd = record[0]
        if idStd not in studenti:
            studenti[idStd] = []
        
        for i, field in enumerate(record):
            if i == 0:
                continue
            studenti[idStd].append(field)
    fileStudenti.close()

    criteria = []
    critStuds = []
    criteriaFile = open('criteria.txt', 'r')
    for i, line in enumerate(criteriaFile):
        if i == 0:
            criteria.append(line.strip().split(","))
        else:
            criteria.append(line.strip())
    
    for i, crt in enumerate(criteria):
        if i == 0:
            print("Studenti trovati per ID:")
            for stud in studenti:
                if stud in crt:
                    print(" * " + str(studenti[stud]))
        elif i == 1:
            print("Studenti trovati per cognome:")
            for studs in studenti:
                if studenti[stud][0] == crt:
                    print(" * " + str(studenti[stud]))
        elif i == 2:
            for stud in studenti:
                if studenti[stud][1] == crt:
                    critStuds.append(stud)

    count = 0
    avg = 0
    for stud in critStuds:
        count += 1
        avg += float(studenti[stud][2])
    
    print("Media del GPA per il grado 10A: " + str(avg / count))

    return

main()