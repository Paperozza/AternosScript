from python_aternos import Client
from python_aternos import *
import platform
import os

#-----------------------------------------------------------------------------------------------------------------------------------

#Funzione che permette di effettuare l'avvio di un server selezionandolo dalla listi di server che viene restituita dall'API
# #

def boot():
    clear()
    i = 0
    
    #Ciclo la lista di server ed in base allo stato del singolo server (informazione prelevata sempre dalle API) elenco tutti quelli
    #disponibili e mostro a video lo stato di ogniuno di essi
    # #
    for server in servers:
        print(server.status)
        if server.status == 'offline':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain + " !!! SPENTO !!!") 
        elif server.status == 'starting':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! INIZIALIZZAZIONE !!!") 
        elif server.status == 'loading':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! CARICAMENTO !!!") 
        elif server.status == 'online':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! AVVIATO !!!")
        i += 1
    print("Per annullare l'operazione di avvio inserisci un qualunque numero non presente nella lista")
    print("--\n  |\n  V")
    
    #Questo try catch permette di controllare che l'utente non inserisca caratteri ma solo numeri.
    #L' exception generata è del tipo ValueError() 
    #
    #In questo caso reindirizzo l'utente al menù iniziale
    # #
    
    try:
        idOfServer = int(input("Inserire l'ID del server che si vuole avviare: "))
    except ValueError:
        print("Valore inserito incorretto\nRITORNO ALLA HOME")
        input("Premi ENTER per continuare")
    
    
    
    try:
        servers[idOfServer].start()
        clear()
        print("Avvio del server: "+servers[idOfServer].software+"\nVersione: "+ servers[idOfServer].version)
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


#-----------------------------------------------------------------------------------------------------------------------------------

def shut():
    clear()
    i = 0
    for server in servers:
        if server.status == 'offline':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain) 
        elif server.status == 'starting':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! INIZIALIZZAZIONE !!!") 
        elif server.status == 'loading':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! CARICAMENTO !!!") 
        elif server.status == 'online':
            print("Id server: "+str(i)+' - Indirizzo del server: '+server.domain+ " !!! AVVIATO !!!")
        i += 1
        
    try:
        serverToShut = int(input("Inserisci l'ID del server che si vuole spegere: "))
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

#-------------------------------------------------------------------------------------------------------

def logout():
    open('user_data.txt','w+').close()
    print("Il logout comporta l'uscita dall'applicazione")


#-----------------------------------------------------------------------------------------------------------------------------------

def login():
    with open("user_data.txt","r+") as credential:
        connected = False
        error = False
        username = credential.readline().strip()
        password = credential.readline().strip()
            
        while connected == False:
            try:
                user = Client.from_credentials(username, password)
                connected = True
                if error == True :
                    credential.write(username+"\n")
                    credential.write(password)
            except CredentialsError:
                credential.truncate(0)
                print("Inserisci le credenziali")
                if error == True:
                    print("Quelle inserite sono sbagliate")
                username = input("Inserisci lo username: ")
                password = input("Inserisci la password: ")
                error = True
                clear()
        return user


#-----------------------------------------------------------------------------------------------------------------------------------

def getSystemTool():
    if "Linux" in platform.platform():
        return lambda: os.system('clear')
    else:
        return lambda: os.system('cls')
        
#-----------------------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    clear = getSystemTool()
    clear()
    
    user = login()
    activeServers = []
    index = ''
    while(index != 'esci'):
        clear()
        servers = user.list_servers()
        print("Benvenuto, seleziona una delle funzioni")
        print("- avvia : Avvia il server")
        print("- spegni : Spegne il server")
        print("- logout : Effettua il logout dal tuo account")
        print("- esci : Esci dal programma")
        index = input("Selezione l'operazione desiderata: ")
        if(index == 'avvia'):
            boot()
        if(index == 'spegni'):
            shut()
        if(index == 'logout'):
            logout()
            break
        
