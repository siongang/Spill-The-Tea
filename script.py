import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import graph

load_dotenv()
token = os.getenv('TOKEN')
image_path = "graph.png"


intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.guild_messages = True
intents.presences = True

bot = commands.Bot(command_prefix=["!","stt "], intents=intents)

# Custom HelpCommand
class CustomHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Bot Commands",description="Spill the tea in ur friend group!\n`The bot will map the 'connections' between ppl.\nif the value between 2 ppl is 1, it is 1 sided,\notherwise, if it is 2, its mu2al!`\n\n`bot prefix: '!' or 'stt '`", color=discord.Color.blue())


        instruction = "`type stt like [mention]`"
        embed.add_field(name="How to use !like", value=instruction, inline=False)

        commands = [  
            {"name": "like", "brief": "Submit your tea (smone u like) :)"},
            {"name": "reset", "brief": "Resets the image."},
            {"name": "help", "brief": "Shows the list of available commands."}
        ]

        command_list = "\n".join([f"`{cmd['name']}`: {cmd['brief']}" for cmd in commands])
        embed.add_field(name="Commands", value=command_list, inline=False)

        await self.get_destination().send(embed=embed)




# Set the custom help command
bot.help_command = CustomHelpCommand()


@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author != bot.user:
        await bot.process_commands(message)


@bot.command(brief="submit your crush")      
async def like(ctx, member: discord.Member):
    person1 = ctx.author.name
    person2 = member.name
    graph.connect(person1,person2)
    image = discord.File(image_path)
    await ctx.send(file=image)

@bot.command(brief="reset the image")
async def reset(ctx):
    if os.path.exists(image_path):
        os.remove(image_path)
        await ctx.send("map has been reset")
    else:
        await ctx.send(f"{image_path} does not exist.")



bot.run(token)