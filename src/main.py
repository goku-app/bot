import json5
import os
import sys
import discord
from discord import app_commands
from discord.ext import commands

# === Load and validate config.jsonc ===
CONFIG_PATH = "src/config.jsonc"

try:
    with open(CONFIG_PATH, "r") as f:
        config = json5.load(f)
except FileNotFoundError:
    print(f"❌ {CONFIG_PATH} not found. Please create it.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Failed to load {CONFIG_PATH}: {e}")
    sys.exit(1)

TOKEN = config.get("token", "").strip()
ADMIN_ID = config.get("ADMIN_ID", "")
PROTECTED_SERVER_IDS = config.get("PROTECTED_SERVER_IDS", [])

if not TOKEN:
    print("❌ No token found. Please set 'token' in config.jsonc.")
    sys.exit(1)

if not ADMIN_ID:
    print("❌ No ADMIN_ID found. Please set 'ADMIN_ID' in config.jsonc.")
    sys.exit(1)

if not PROTECTED_SERVER_IDS:
    print("⚠️  No PROTECTED_SERVER_IDS found. Continuing without server protection.")

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

class SendButton(discord.ui.View):
    def __init__(self, text: str):
        super().__init__(timeout=None)
        self.text = text

    @discord.ui.button(label="Send", style=discord.ButtonStyle.success)
    async def send_message(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        await interaction.followup.send(self.text, ephemeral=False)

class KillButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Kill Server", style=discord.ButtonStyle.danger)
    async def kill_server(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()
        for _ in range(5):
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
    status_type_str = config.get("STATUS_TYPE", "watching").lower()
    custom_status = config.get("CUSTOM_STATUS", "dsc.gg/beignet")

    status_types = {
        "watching": discord.ActivityType.watching,
        "playing": discord.ActivityType.playing,
        "listening": discord.ActivityType.listening,
        "streaming": discord.ActivityType.streaming,
    }

    if status_type_str not in status_types:
        print(f"⚠️ Unknown STATUS_TYPE '{status_type_str}' in config.jsonc. Defaulting to 'watching'.")

    activity_type = status_types.get(status_type_str, discord.ActivityType.watching)

    await bot.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(type=activity_type, name=custom_status)
    )

    print(f"✅ Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} global commands!")
    except Exception as e:
        print(f"❌ Sync failed: {e}")


@bot.tree.command(name="kill", description="Kill the server")
async def kill(interaction: discord.Interaction):
    if interaction.guild and str(interaction.guild.id) in PROTECTED_SERVER_IDS:
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
    if interaction.guild and str(interaction.guild.id) in PROTECTED_SERVER_IDS:
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
    await interaction.response.defer(ephemeral=anonymous)

    if anonymous:
        await interaction.followup.send(
            content="click me please :3",
            view=SendButton(text),
            ephemeral=True
        )
    else:
        await interaction.followup.send(text, ephemeral=False)

bot.run(TOKEN)
