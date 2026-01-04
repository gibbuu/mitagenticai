import os
import certifi

# Point Python's SSL to certifi's CA bundle so HTTPS certs verify on macOS
os.environ.setdefault('SSL_CERT_FILE', certifi.where())

from dotenv import load_dotenv
import discord

# Load environment variables from .env file
load_dotenv()

# Set up intents for the bot
intents = discord.Intents.default()
intents.message_content = True #Ensure Bot can read message content discord

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Respond to messages that start with '!hello'
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))