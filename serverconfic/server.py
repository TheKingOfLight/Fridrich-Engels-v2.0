'''-----------------------------------------------------------------
Python Bot Friedrich-Engels-v2.0
von King of the Light

Serverspezifische Einstallungen
-----------------------------------------------------------------'''
import discord
from discord.utils import get
from serverconfic.ids import Channel_ID

async def give_text_in_bot_channel(client, text):
    print (text)
    channel = client.get_channel(int(Channel_ID('bot_output')))
    await channel.send(text)

comandprefix = '~'
