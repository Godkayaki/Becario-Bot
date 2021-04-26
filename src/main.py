#!/usr/bin/python3
#DRG - april 2021
#-*- coding: utf-8 -*-

import discord
import os
import dbconnections as dbload

project_path = os.path.dirname(os.path.dirname(__file__))
apikey = project_path+"/.config/apikey"
client = discord.Client()

BLANK='\u200b'

'''@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))'''

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('>help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #show context menu with help about the bot funcionality
    if message.content == '>help':
        #await message.channel.send('Generating pool...')
        embed=discord.Embed(title="Becario bot", description="Short explanation of every command available:", color=0x00ffea)
        embed.set_author(name=" ")
        #embed.add_field(name=BLANK, value=BLANK, inline=False)
        embed.add_field(name=">info", value="Shows some info about the bot.\n"+BLANK, inline=False)
        embed.add_field(name=">pool", value="Command to generate the mappols with all the modalities.", inline=False)
        embed.add_field(name=BLANK+"-> BO7 - Best of 7 (4 maps to win)", value="command: >pool -bo7", inline=False)
        embed.add_field(name=BLANK+"-> BO9 - Best of 9 (5 maps to win)", value="command: >pool -bo9 -1(can be 1 or 2 and it's optional.)", inline=False)
        embed.add_field(name=BLANK+"-> BO11 - Best of 11 (6 maps to win)", value=" command: >pool -bo11 -1(can be 1 or 2 and it's optional.)", inline=False)
        embed.add_field(name=BLANK+"-> BO13 - Best of 13 (7 maps to win)", value=" command: >pool -bo13 -1(can be 1 or 2 and it's optional.)", inline=False)
        await message.channel.send(embed=embed)

    elif message.content.startswith('>info'):
        pass

    #list all the maps available on the database
    elif message.content.startswith('>listmaps'):
        await message.channel.send('Listing maps...')
        allmaps=dbload.db_selectallmaps()
        
        maps_end=[]
        final_str=""
        for row in allmaps:
            id_map = row[0]
            link = row[1]
            type_ = row[2]
            string_map="Type: "+type_+" Link: <"+link+">"
            maps_end.append(string_map)

        for map_ in maps_end:
            final_str=final_str+map_+"\n"
        
        await message.channel.send(final_str)

    #request a bo7 mappol
    elif message.content.startswith('>pool -bo7'):
        if message.content == '>pool -bo7':
            await message.channel.send('Generating best of 7 mappol; **4NM 2HD 2HR 2DT 1TB**')
        else:
            await message.channel.send('Command syntax incorrect; Type >help to see how the commands and formats work.')

    #request a bo9 mappol
    elif message.content.startswith('>pool -bo9'):
        if message.content == '>pool -bo9':
            await message.channel.send('Generating best of 9 mappol (not flagged, mode 1 as default.): **5NM 2HD 2HR 3DT 1TB**')
        elif message.content == '>pool -bo9 -1':
            await message.channel.send('Generating best of 9 mappol; Mode 1: **5NM 2HD 2HR 3DT 1TB**')
        elif message.content == '>pool -bo9 -2':
            await message.channel.send('Generating best of 9 mappol; Mode 2: **4NM 2HD 2HR 2DT 2FM 1TB**')
        else:
            await message.channel.send('Command syntax incorrect; Type >help to see how the commands and formats work.')

    #request a bo11 mappol
    elif message.content.startswith('>pool -bo11'):
        if message.content == '>pool -bo11':
            await message.channel.send('Generating best of 11 mappol (not flagged, mode 1 as default.): **5NM 3HD 3HR 3DT 1TB**')
        elif message.content == '>pool -bo11 -1':
            await message.channel.send('Generating best of 11 mappol; Mode 1: **5NM 3HD 3HR 3DT 1TB**')
        elif message.content == '>pool -bo11 -2':
            await message.channel.send('Generating best of 11 mappol; Mode 2: **4NM 3HD 3HR 3DT 2FM 1TB**')
        else:
            await message.channel.send('Command syntax incorrect; Type >help to see how the commands and formats work.')

    #request a bo13 mappol
    elif message.content.startswith('>pool -bo13'):
        if message.content == '>pool -bo13':
            await message.channel.send('Generating best of 13 mappol (not flagged, mode 1 as default.): **6NM 3HD 3HR 4DT 1TB**')
        elif message.content == '>pool -bo13 -1':
            await message.channel.send('Generating best of 13 mappol; Mode 1: **6NM 3HD 3HR 4DT 1TB**')
        elif message.content == '>pool -bo13 -2':
            await message.channel.send('Generating best of 13 mappol; Mode 2: **5NM 3HD 3HR 3DT 3FM 1TB**')
        else:
            await message.channel.send('Command syntax incorrect; Type >help to see how the commands and formats work.')

    else:
        if message.content.startswith('>'):
            await message.channel.send('Command not found; Type >help to see how the commands and formats work.')

fline=open(apikey).readline().rstrip()
client.run(fline)