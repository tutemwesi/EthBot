import discord
from discord.ext import commands
import urllib.request
from urllib.request import urlopen
import json

# Headers are required to communicate with APIs 
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}

#API URLs - be sure to replace <wallet address> with the wallet you are interested in 
urlnano = "https://api.nanopool.org/v1/eth/user/<wallet address>/"
urleth = "https://api.kraken.com/0/public/Ticker?pair=ETHGBP"
urlbtc = "https://api.kraken.com/0/public/Ticker?pair=XBTGBP"


#This bit is shit and I'm sure there is a better way of doing it

reqnano = urllib.request.Request(urlnano, headers = headers)
reqeth = urllib.request.Request(urleth, headers = headers)
reqbtc = urllib.request.Request(urlbtc, headers = headers)

xeth = urllib.request.urlopen(reqeth)
xnano = urllib.request.urlopen(reqnano)
xbtc = urllib.request.urlopen(reqbtc)

datanano = xnano.read()
dataeth = xeth.read()
databtc = xbtc.read()

encodingnano = xnano.info().get_content_charset('utf-8')
encodingeth = xeth.info().get_content_charset('utf-8')
encodingbtc = xbtc.info().get_content_charset('utf-8')


ethprice = json.loads(dataeth.decode(encodingeth))
btcprice = json.loads(databtc.decode(encodingbtc))
hashrate = json.loads(datanano.decode(encodingnano))

#Obtain a token from the Discord API and set below  

TOKEN = 'Enter your Discord Token here'

description = '''EthBot'''
bot = commands.Bot(command_prefix='!', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)  
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")

@bot.command()
async def hash():
    """Show Average Hashrate"""
    await bot.say("Average 6hr Hashrate: " + str(hashrate['data']['avgHashrate']['h6']))

@bot.command()
async def balance():
    """Show Current Balance"""
    await bot.say("Current Balance: " + str(hashrate['data']['balance']))

@bot.command()
async def eth():
    """Show Current Eth to GBP Conversion Rate"""
    await bot.say("1.0 ETH = £" + str(ethprice['result']['XETHZGBP']['a'][0]))

@bot.command()
async def btc():
    """Show Current BTC to GBP Conversion Rate"""
    await bot.say("1.0 BTC = £" + str(btcprice['result']['XXBTZGBP']['a'][0]))


bot.run(TOKEN)
