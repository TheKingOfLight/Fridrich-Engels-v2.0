'''-----------------------------------------------------------------
Python Bot Friedrich-Engels-v2.0
von King of the Light

Stellt nach dem Verbinden des Bott alle wichtige Sachen ein
-----------------------------------------------------------------'''
import discord

from serverconfic.ids import Channel_ID
from serverconfic.server import give_text_in_bot_channel

def welcome_client(client):
    print ('1')

    @client.event
    async def on_ready():

        txt = startupmessage()
        channel = client.get_channel(int(Channel_ID('bot_output')))
        await channel.send(txt)
        text = ('We have logged in as {0.user}'.format(client))
        await give_text_in_bot_channel(client, text)
