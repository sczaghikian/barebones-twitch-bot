import os
from twitchio.ext import commands

print("Hello, asshole!")
print(f"irc_token: {os.environ['TMI_TOKEN']}")
print(f"name = {os.environ['BOT_NAME']}")

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NAME'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NAME']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NAME'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi, @{ctx.author.name}!")


@bot.command(name='test')
async def test(ctx):
    await ctx.send('test passed!')


@bot.command(name="wtf")
async def wtf(ctx):
    await ctx.send("What's really the sitch here tho")


if __name__ == "__main__":
    bot.run()
