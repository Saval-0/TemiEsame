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

songs = {}

def find_consecutive_matches(notes1, notes2):
    
    n, m = len(notes1), len(notes2)
    max_length = 0
    
    for i in range(n):
        for j in range(m):
            length = 0
            while (i + length < n and j + length < m and 
                    notes1[i + length] == notes2[j + length]):
                length += 1
            max_length = max(max_length, length)
            
    return max_length


def find_transposed_sequences(notes1, notes2):
    n, m = len(notes1), len(notes2)
    min_sequence_length = 4
    found_sequences = []
    
    notes1 = [int(x) for x in notes1]
    notes2 = [int(x) for x in notes2]
    
    print(n - min_sequence_length + 1)
    for i in range(n - min_sequence_length + 1):
        for j in range(m - min_sequence_length + 1):
            interval = notes2[j] - notes1[i]
            
            # Check how many consecutive notes follow this interval
            length = 0
            while (i + length < n and j + length < m and 
                    notes2[j + length] - notes1[i + length] == interval):
                length += 1
            
            if length >= min_sequence_length:
                found_sequences.append({
                    'length': length,
                    'interval': interval,
                    'pos1': i,
                    'pos2': j
                })
    
    return found_sequences

def main():
    file = open('brani.txt', 'r')

    for line in file:
        currSong = [ line.split(":")[0].strip(), line.split(":")[1].strip().split(" ") ]
        title = currSong[0]
        notes = currSong[1]
                
        for prev_title, prev_notes in songs.items():
            if notes == prev_notes:
                print(f"\'{title}\' è un PLAGIO di \'{prev_title}\'")
            else:
                max_consecutive = find_consecutive_matches(notes, prev_notes)
                if max_consecutive >= 4:
                    print(f"'{title}' contiene {max_consecutive}, è una COPIATURA di '{prev_title}'")
        
        songs[title] = notes

    return


main()
