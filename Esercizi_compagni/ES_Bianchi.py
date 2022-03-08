# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
# compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
import random
from os import system,name

def numeroPlayer():
    while True:
        numeroGiocatori = int(input("\ninserire il numero dei giocatori:[1 o 2]"))
        if numeroGiocatori == 1:
            print("\ngiocherai contro la CPU! Buona fortuna mio giovane guerriero!")
            partitaControLaCpu()
            break
        elif numeroGiocatori == 2:
            print("uuuh sfida tra amici!!\nallora volete rovinare la vostra amicizia in fretta. COMBATTETE\n")
            partitaduegiocatori()
            break
        else:
            print("numero giocatori invalido")


def partitaControLaCpu():
    while True:
        mossa = inserimentoMossa()
        if mossa == 'carta' or mossa == 'sasso' or mossa == 'forbice':
            mossaCpu = random.choice(lista)
            print("mossa CPU: %s" % mossaCpu)
            if ((mossa == 'sasso' and mossaCpu == 'forbice') or
                    (mossa == 'carta' and mossaCpu == 'sasso') or
                    (mossa == 'forbice' and mossaCpu == 'carta')):
                print("\ncomplimenti hai vinto la partita, hai sconfitto la maledetta CPU.\n")
            elif mossa == mossaCpu:
                print("\nche culo, ti sei salvato, un pareggio. riprova :)")
                partitaControLaCpu()
            else:
                print("\nmi spiace, la CPU è troppo forte per uno come te")
        else:
            print("hey, pensavi di fottere il sistema, invece ti ho fregato.\n"
                  "inserisci un valore valido grazie :)\n")
            partitaControLaCpu()
        rigioco()


def partitaduegiocatori():
    while True:
        giocatore1 = str(input("inserire nome giocatore 1 : "))
        giocatore2 = str(input("inserire nome giocatore 2 : "))
        mossaGiocatore1 = str(input("mossa %s: " %giocatore1))
        mossaGiocatore2 = str(input("mossa %s: " %giocatore2))
        if((mossaGiocatore1 == 'sasso' or mossaGiocatore1 == 'carta' or mossaGiocatore1 == 'forbice') and
           (mossaGiocatore2 == 'sasso' or mossaGiocatore2 == 'forbice' or mossaGiocatore2 == 'carta')):
            if ((mossaGiocatore1 == 'sasso' and mossaGiocatore2 == 'forbice') or
                    (mossaGiocatore1 == 'carta' and mossaGiocatore2 == 'sasso') or
                    (mossaGiocatore1 == 'forbice' and mossaGiocatore2 == 'carta')):
                print("\nmossa %s: %s\nmossa %s: %s\ncomplimenti hai vinto la partita %s, "
                      "hai sconfitto quel maledetto di %s.\n"
                      %(giocatore1,mossaGiocatore1,giocatore2,mossaGiocatore2,giocatore1,giocatore2))
            elif mossaGiocatore1 == mossaGiocatore2:
                print("\nmossa %s: %s\nmossa %s: %s\nincredibile pareggio. riprovate :)"%(giocatore1,mossaGiocatore1,giocatore2,mossaGiocatore2))
                partitaduegiocatori()
            else:
                print("\nmossa %s: %s\nmossa %s: %s\nComplimenti!! %s ha battuto quello sfigato di %s" %(giocatore1,mossaGiocatore1,giocatore2,mossaGiocatore2,giocatore2,giocatore1))
        else:
            print("mosse non valide, non fate gli infami e inserite i valori consentiti, grazie :)\n")
            partitaduegiocatori()
        rigioco()

def rigioco():
    while True:
        rigiocare = str(input("aspetta: vuoi giocare un'altra partita?[si/no]"))
        if rigiocare == 'si':
            numeroPlayer()
        elif rigiocare == 'no':
            break


def inserimentoMossa():
    mossa = str(input("\nora devi scegliere la tua mossa, scegli bene ragazzo.\n"
                      "ricorda che per inserire una mossa devi scrivere 'sasso' o 'carta' o 'forbice'.\n "
                      "se scriverai qualcos'altro ti verrà chiesto di riinserirlo\n\n mossa Utente: "))
    return mossa


lista = ["sasso", "carta", "forbice"]

print("Benvenuto, vuoi giocare a sasso, carta, forbice?\n"
      "Ovvio che vuoi!!\n"
      "preparati alla sfida")
numeroPlayer()
