'''-----------------------------------------------------------------
Python Bot Friedrich-Engels-v2.0
von Mark Rygielski

Aufgabe:
Musik

Externe Datein (im selben Ordner):
- .ent mit dem Token
-----------------------------------------------------------------'''


#Setup
#------------------------------------------------------------------

#importiere Bibliotheken:
import discord, os, re
from discord.utils import get
from dotenv import load_dotenv

#importiere Python skripte
#from import

#importiere Benachrichtigungen
import textoutput.error_messages
import textoutput.system_messages

#importiere Einstellungen
from serverconfic.setup_bot import welcome_client
from serverconfic.server import comandprefix
from serverconfic.server import give_text_in_bot_channel
comand_prefix = str(comandprefix)

#importiere Token mithilfe von dotenv:
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#------------------------------------------------------------------



def main():
    #client instanz erzeugen:
    client = discord.Client()

    #Stellt den Bot entsprechend ein, gibt Systemnachrichten aus
    welcome_client(client)


    @client.event
    async def on_disconnect():
        #Läuft, die Verbindung zum Server abbricht
        print("Bot has logged off")


    @client.event
    async def on_message(message):
        #läuft, wenn der Bot eine Nachricht erhält
        if message.author != client.user:

            if message.content.startswith(comand_prefix):
                #prüft, ob ein Befehl gegeben wurde
                print ('command')

            #prüft Nachricht
            #if

            
#------------------------------------------------------------------


    #lässt den Client mit dem TOKEN laufen
    client.run(TOKEN)



if __name__ == "__main__":
    main()
