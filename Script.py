from python_aternos import Client
from python_aternos import *
import platform
import os

if "Linux" in platform.platform():
    clear = lambda: os.system('clear')
    clear()
else:
    clear = lambda: os.system('cls')
    clear()


# Funzione di LOGIN bug su scrittura file:
#   Se si sbaglia la password nel momento in cui la si inserisce correttamente
#   carica dei caratteri indentificati come null dall'editor di testo all'inizio
#   del file

#   Errore comparso dopo l'implementazione della gestione delle eccezzioni

# CAUSA credential.truncate(0) linea 33 
with open("user_data.txt","r+") as credential:
    connected = False
    error = False
    username = credential.readline().strip()
    password = credential.readline().strip()
        
    while connected == False:
        try:
            user = Client.from_credentials(username, password)
            connected = True
        except CredentialsError:
            credential.truncate(0)
            print("Inserisci le credenziali")
            if error == True:
                print("Quelle inserite sono sbagliate")
            username = input("Inserisci lo username: ")
            credential.write(username+"\n")
            password = input("Inserisci la password: ")
            credential.write(password)
            error = True
            
            clear()
            

servers = user.list_servers()
activeServers = []
index = ''
while(index != 'esci'):
    clear()
    print("Benvenuto ntial.wr"+ username)
    print("- avvia : Avvia il server")
    print("- spegni : Spegne il server")
    print("- esci : Esci dal programma")
    index = input("Selezione l'operazione desiderata: ")
    if(index == 'avvia'):
        clear()
        i = 0
        for server in servers:
            if server.status == 'ofline':
               print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain) 
            elif server.status == 'loading':
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! CARICAMENTO !!!") 
            elif server.status == 'preparing':
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! PREPAZIONE !!!") 
            else:
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! AVVIATO !!!")
            i += 1
        print("--\n  |\n  V")
        print("Per annullare l'operazione di avvio inserisci un qualunque numero non presente nella lista")
        
        try:
            idOfServer = int(input("Inserire l'ID del server che si vuole avviare: "))
        except ValueError:
            print("Valore inserito incorretto\nRITORNO ALLA HOME")
            input("Premi ENTER per continuare")
        
        try:
            servers[idOfServer].start()
            print("Avvio del server: "+servers[idOfServer].software+" - Versione: "+ servers[idOfServer].version)
            activeServers.append(server.domain)
            input("Premi ENTER per continuare")
        except ServerStartError as error:
            print("Non è stato possibile avvviare il server, le cause possibili sono: "
                  "\n- Server già avviato"
                  "\n- Contratto EULA non firmato"
                  "\n- Software installato errato o danneggiato"
                  "\n- Server Aternos non raggiungibili"
                  "\n- Memoria del server piena"
                  )
            input("Premi ENTER per continuare")
        except IndexError:
            print("Annullamento operazione...")
            input("Premi ENTER per continuare") 
        except:
            print("")          
    if(index == 'spegni'):
        clear()
        i = 0
        for server in servers:
            if server.status == 'ofline':
               print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain) 
            elif server.status == 'loading':
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! CARICAMENTO !!!") 
            elif server.status == 'preparing':
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! PREPAZIONE !!!") 
            else:
                print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! AVVIATO !!!")
            i += 1
            
        try:
            serverToShut = int(input("Inserisci l'ID del server che si vuole spegere"))
        except ValueError:
            print("Valore inserito incorretto\nRITORNO ALLA HOME")
            input("Premi ENTER per continuare")
        
        try:
            servers[serverToShut].stop()
            print("Spegnimento del server: "+servers[serverToShut].software+" - Versione: "+ servers[serverToShut].version)
            input("Premi ENTER per continuare")
        except IndexError:
            print("Annullamento operazione...")
            input("Premi ENTER per continuare") 
        except NameError:
            print("")
            