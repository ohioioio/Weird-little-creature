
# This example requires the 'message_content' intent.
from dotenv import load_dotenv
import discord
from discord import app_commands
import os
import threading
from datetime import datetime
import random

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        
        print(f'Logged on as {self.user}!')
        await tree.sync(guild=discord.Object(id=1055287764775620638))

    


    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.all()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name = "thought", description = "Get a random thought out of the weird little guy's head", guild=discord.Object(id=1055287764775620638)) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def think(interaction):
    funnytable = [
        "https://pbs.twimg.com/media/Ff0spOnWAAAPaMr?format=jpg&name=large", 
        "ah yes the anime beam struggle, or as I like to call it, reverse tug-of-war", 
        "I'm always committing to the bit (The bit is that I try a little more each day, and slowly accumulate a repertoire of experience through honest to goodness ambition)", 
        "Wouldn't it be funny if we standardized an XYZ coordinate format for 3D space and then placed those three letters totally randomly on keyboards so that blender users will always scale their objects in the wrong direction on the first try? It would be SO funny guys", 
        "Shark Tank but it's a bunch of genies you have to pitch your wish to, and the only rule is you can't ask for more than 50% equity stake in the benefits of your wish", 
        "[guy who just invented the light spectrum but forgot to add the last color in] W-well, actually, pink isn't real. Because of wavelengths, you see. And not just because I forgot to add it to our magic rainbow gradient", 
        "In our classist economy, we fund sidewalks for the slowest of walkers- and running tracks for the fastest of sprinters. I ask you, what are we building for the skippers & hoppers among us? Are they not, too, entitled to a path designed for medium-paced movement?",
        "I'll be starting a Podcast called \"The Skinner Box\" and filling it with constant ad-rolls so the listener will have to mash the skip button 10 different times before hearing the definition of operant conditioning",
        "https://media.discordapp.net/attachments/965046723942690887/1088903753324843128/IMG_5287.jpg",
        "https://media.discordapp.net/attachments/965046723942690887/1088888841169027243/BE822805-25B5-4384-818F-0C3F685CBB54.jpg",
        "https://youtu.be/nZyyBqNLLZQ",
        "https://pbs.twimg.com/media/FsDmk1paQAY0ie7?format=png&name=small",
        "https://pbs.twimg.com/media/FsAp-8LaQAAJNWs?format=jpg&name=900x900"
    ]
    await interaction.response.send_message(random.choice(funnytable))







client.run(DISCORD_TOKEN)


