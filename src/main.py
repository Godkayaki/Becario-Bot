#!/usr/bin/python3
#-*- coding: utf-8 -*-

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-reqpool'):
        await message.channel.send('Generating pool...')

client.run('ODI0MzQyOTI0NzA3NDk1OTM2.YFt_LA.HCh3jR9wvMNXh_XbhU2NVryypXg')