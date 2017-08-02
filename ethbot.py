import discord
from discord.ext import commands
import urllib.request
from urllib.request import urlopen
import json

#Set Discord API bot token here
TOKEN = ''

description = '''EthBot'''
bot = commands.Bot(command_prefix='?', description=description)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

#Set the wallet address under URL for each instance
@bot.command()
async def balance():
	"""Show Current Balance"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    url = "https://api.nanopool.org/v1/eth/user/Wallet Address /"
    req = urllib.request.Request(url, headers = headers)
    x = urllib.request.urlopen(req)
    data = x.read()
    encoding = x.info().get_content_charset('utf-8')
    balance = json.loads(data.decode(encoding))
    await bot.say("Current Balance: " + str(balance['data']['balance']))

@bot.command()
async def hashrate():
	"""Show Current Hashrate"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    url = "https://api.nanopool.org/v1/eth/user/Wallet Address /"
    req = urllib.request.Request(url, headers = headers)
    x = urllib.request.urlopen(req)
    data = x.read()
    encoding = x.info().get_content_charset('utf-8')
    hashrate = json.loads(data.decode(encoding))
    await bot.say("Current Hashrate: " + str(hashrate['data']['avgHashrate']['h6']))

@bot.command()
async def eth():
	"""Show Current Eth to GBP Conversion Rate"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    url = "https://api.kraken.com/0/public/Ticker?pair=ETHGBP"
    req = urllib.request.Request(url, headers = headers)
    x = urllib.request.urlopen(req)
    data = x.read()
    encoding = x.info().get_content_charset('utf-8')
    ethprice = json.loads(data.decode(encoding))
    await bot.say("1.0 ETH = £" + str(ethprice['result']['XETHZGBP']['a'][0]))

@bot.command()
async def btc():
	"""Show Current BTC to GBP Conversion Rate"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    url = "https://api.kraken.com/0/public/Ticker?pair=ETHGBP"
    req = urllib.request.Request(url, headers = headers)
    x = urllib.request.urlopen(req)
    data = x.read()
    encoding = x.info().get_content_charset('utf-8')
    btcprice = json.loads(data.decode(encoding))
    await bot.say("1.0 BTC = £" + str(btcprice['result']['XXBTZGBP']['a'][0]))


bot.run(TOKEN)
