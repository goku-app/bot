import discord
from discord import app_commands
from discord.ext import commands

TOKEN = open("TOKEN.txt").read().strip()
if not TOKEN:
    print("No token was found. Please put your Discord's Bot Token in src/TOKEN.txt")
    exit()

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

BLOCKED_SERVER_ID = 1265386644953895094  # The server where commands should be disabled

class SendButton(discord.ui.View):
    def __init__(self, text: str):
        super().__init__(timeout=None)
        self.text = text

    @discord.ui.button(label="Send", style=discord.ButtonStyle.success)
    async def send_message(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await interaction.followup.send(self.text, ephemeral=False)  # Send publicly

class KillButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kill Server", style=discord.ButtonStyle.danger)
    async def kill_server(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        for _ in range(5):  # Loop 5 times
            await interaction.followup.send(
                "# THIS SERVER IS BEING RAIDED BY TEAM BEIGNET ☠️☠️\n\n"
                "# FREE RAID BOT IN SERVER 🤖\n\n"
                "# WORKING 24/7 ✅\n\n"
                "# FREE FOR EVERYONE ✅\n\n"
                "# CUSTOM MESSAGES ✅\n\n"
                "# JOIN OUR DISCORD SERVER: DSC.GG/BEIGNET 🍩\n\n"
                "||https://discord.gg/sc5tfyEUqD||\n\n"
                "# @everyone @here",
                ephemeral=False
            )

class KillCustomButton(discord.ui.View):
    def __init__(self, text: str):
        super().__init__(timeout=None)
        self.text = text

    @discord.ui.button(label="Kill Server", style=discord.ButtonStyle.danger)
    async def spam_text(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        
        for _ in range(5):
            await interaction.followup.send(self.text, ephemeral=False)

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle, 
        activity=discord.Activity(type=discord.ActivityType.watching, name="dsc.gg/beignet")
    )
    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} global commands!")
    except Exception as e:
        print(f"❌ Sync failed: {e}")

@bot.tree.command(name="kill", description="Kill the server")
async def kill(interaction: discord.Interaction):
    if interaction.guild and interaction.guild.id == BLOCKED_SERVER_ID:
        await interaction.response.send_message(
            "❌ This command is disabled in this server.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        content="click me please :3",
        view=KillButton(),  
        ephemeral=True
    )

@bot.tree.command(name="kill-custom", description="Kill the server using a custom message")
@app_commands.describe(text="The message to spam")
async def kill_custom(interaction: discord.Interaction, text: str):
    if interaction.guild and interaction.guild.id == BLOCKED_SERVER_ID:
        await interaction.response.send_message(
            "❌ This command is disabled in this server.",
            ephemeral=True
        )
        return

    await interaction.response.send_message(
        content="click me please :3",
        view=KillCustomButton(text),  
        ephemeral=True
    )
    
@bot.tree.command(name="help", description="Show help information")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**Made by Jack le Beignet**\n\nFor help & questions, please reach out to our Discord Server: https://discord.gg/sc5tfyEUqD",
        ephemeral=True
    )

@bot.tree.command(name="send", description="Send a message with or without anonymity")
@app_commands.describe(text="The message to send", anonymous="Send anonymously?")
async def send(interaction: discord.Interaction, text: str, anonymous: bool = False):
    await interaction.response.defer()

    if anonymous:
        await interaction.response.send_message(
            content="click me please :3",
            view=SendButton(text),
            ephemeral=True
        )
    else:
        await interaction.followup.send(text, ephemeral=False)

bot.run(TOKEN)
