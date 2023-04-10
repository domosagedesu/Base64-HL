#
# Properly populate the 'URL' fields before removing comments from the embed blocks
# Otherwise the bot will not be capable of responding
#

# Ensure you are using Hikari & Lightbulb
# Import the relevant library
import base64

#
# Init your Bot instance here
#

# Automated transcoding via string recognition
@bot.listen()
async def msg(event: hikari.GuildMessageCreateEvent):
    # Encoded string to match
    encodedStr = ['aHR0cHM6Ly9']
    if event.author.is_bot:
        return          
    elif event.message.attachments:
        return
    elif any(x in event.content for x in encodedStr):
        lookURL=(base64.b64decode(event.content).decode('ascii'))
    else: 
        return         
    embed = hikari.Embed()
    #embed.set_author(name='YOURNAME', url='YOURNAMEURL', icon='URL')
    embed.color = '11806A'
    embed.add_field('Detected Base64', event.content)
    embed.add_field('Decoded Base64', f'{lookURL}')
    #embed.set_thumbnail('URL')
    embed.set_footer('Developed by @domosagedesu')
    await event.message.respond(embed)

# Manual transcoding via slash commands

@bot.command
@lightbulb.command('base', 'Handles Base64.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def b64(ctx):
    pass

@b64.child
@lightbulb.option('url', 'URL to be decoded.')
@lightbulb.command('decode', 'Decodes Base64.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def decode(ctx):
    decUrl = ctx.options.url
    decodedUrl=(base64.b64decode(decUrl).decode('ascii'))
    embed = hikari.Embed()
    #embed.set_author(name='YOURNAME', url='YOURNAMEURL', icon='URL')
    embed.color = '9B59B6'
    embed.add_field('Encoded Base64', decUrl)
    embed.add_field('Decoded Base64', f'{decodedUrl}')
    #embed.set_thumbnail('URL')
    embed.set_footer('Developed by @domosagedesu')
    await ctx.respond(embed)

@b64.child
@lightbulb.option('url', 'URL to be encoded.')
@lightbulb.command('encode', 'Encodes Base64.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def encode(ctx):
    encUrl = ctx.options.url.encode("utf-8")
    encodedURL=(base64.b64encode(encUrl).decode('ascii')) 
    embed = hikari.Embed()
    #embed.set_author(name='YOURNAME', url='YOURNAMEURL', icon='URL')
    embed.color = 'E91E63'
    embed.add_field('Raw input', ((encUrl).decode('ascii')))
    embed.add_field('Encoded Base64', f'{encodedURL}')
    #embed.set_thumbnail('URL')
    embed.set_footer('Developed by @domosagedesu')
    await ctx.respond(embed)

bot.run()