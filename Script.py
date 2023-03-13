from python_aternos import Client
import platform
import os
credential = open(r"user_data","r+")
username = credential.readline(0)
password = credential.readline(1)
if username=="" and password=="null" :
    print("Effettua il login")
    print 
user = Client.from_credentials(username, password)
if "Linux" in platform.platform():
    clear = lambda: os.system('clear')
    clear()
else:
    clear = lambda: os.system('cls')
    clear()
    
from subprocess import call, STDOUT
import os
if call(["https://github.com/Paperozza/AthernosScript.git", "main"], stderr=STDOUT, stdout=open(os.devnull, 'w')) != 0:
    print("Nope!")
else:
    print("Yup!")
    
print("Benvenuto "+ username)
print("1) Avviare il server")
print("2) Spegnere il server")
print("3) Forzare il salvataggio del mondo")
print("4) Logout")

servers = user.list_servers() 
result = None
for server in servers:
    if server.address == 'ElisCraft.aternos.me':
        result = server

if result is not None:
    # Prints a server softaware and its version
    # (for example, "Vanilla 1.12.2")
    print(result.software, result.version)
    # Starts server
    #result.start()
