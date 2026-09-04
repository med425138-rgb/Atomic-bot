import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Bot Online: {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} commands")
    except Exception as e:
        print(f"❌ Error: {e}")

@bot.tree.command(name="ping", description="Test l-bot status")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! L-bot khddam 24/7 mn Cloud!")

@bot.tree.command(name="register", description="Register team f Scrim")
async def register(interaction: discord.Interaction, team_name: str, captain: discord.Member):
    embed = discord.Embed(
        title="🔥 Registration Free Fire",
        description=f"L-team **{team_name}** t-sjjlat b success!",
        color=discord.Color.green()
    )
    embed.add_field(name="Capitaine", value=captain.mention)
    await interaction.response.send_message(embed=embed)

TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
