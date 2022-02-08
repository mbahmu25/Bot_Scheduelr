import discord 
import os
from dotenv import load_dotenv
import random
from discord.ext import commands, tasks
import datetime
from pytz import timezone
from threading import Timer


date = ''
jam = ''
hari = ''
menit = ''
sekon =''
est= ''
def updateW():
    global date,jam,hari,menit,est,sekon
    date = datetime.datetime.now(timezone("Asia/Jakarta"))
    hari = date.strftime("%A")
    hari = str(hari)
    jam = int(date.hour)
    menit = int(date.minute)
    sekon = int(date.second)
    est = (jam) ** (menit) + sekon
    nomhar = 0
    Timer(1,updateW).start()

    return date,jam,hari,menit,est,sekon
    pass
updateW()

bot = discord.Client()
test = commands.Bot(command_prefix='$')

AGM = "htps://meet.google.com/wom-feik-xkk"
PKN = "https://meet.google.com/szz-ieak-xtt"
IND = "https://meet.google.com/rnc-anic-ekg"
MAT = "https://meet.google.com/nxa-shot-pxx"
SJR = "https://meet.google.com/ebn-sgni-qoo"
BIW = "https://meet.google.com/xmj-qqqe-hid"
BIM = "https://meet.google.com/ybf-ehio-yyt"
SEN = "https://meet.google.com/uek-znxn-bjc"
PJOK = "https://meet.google.com/lookup/c2rv2ndzrm"
PKWU = "https://meet.google.com/fpd-wunq-mar"
BJW = "https://meet.google.com/qos-srgr-qcr"
BMAN = "https://meet.google.com/zxr-rfgd-dwm"
BIO = "https://meet.google.com/exc-vdbj-pay"
FIS = "https://meet.google.com/eux-emoq-uaz"
KIM = "https://zoom.us/j/9434703170pwd=UjlYOVIrdE5vMGJmWkZvS09tVW1Udz09"
BK = "https://meet.google.com/bzn-wyec-whf"

daftar = [
[[7,25,PKWU],[8,45,BIO],[10,5,MAT],[11,35,BIM]],
[[7,25,KIM],[8,45,BJW],[10,5,BIW],[11,35,IND]],
[[7,10,FIS],[8,25,PKN],[9,40,BK],[11,0,AGM]],
[[7,10,KIM],[8,25,BMAN],[9,40,SEN],[11,0,MAT]],
[[7,25,MAT],[8,45,FIS],[10,5,MAT]],
[[7,25,PJOK],[8,45,SJR],[10,5,BIO]]
]

#daftar[x][y][z][a][b]
#[x]=hari,[y]=blok,[z]=jam,[a]=menit,[b]=mapel

intents = discord.Intents.none()
intents.members = True
intents.guilds = True
intents.messages = True
@bot.event
#when the bot started running, print its name, id etc
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(bot.user.name)
    print("Userid: ",end='')
    print(bot.user.id)

@bot.event  

async def on_message(message):
    
    if message.content == "tes":
        await message.channel.send("lulus {0.author.mention}".format(message))
      
    if message.content == "Tes":
      await message.channel.send("Masuk")

@tasks.loop(seconds = 1) # repeat after every 10 seconds
async def myLoop():
    global date,jam,hari,menit,est,sekon
    await bot.wait_until_ready()
    channel = bot.get_guild(792772629462515733).get_channel(792772631160946691)
    nom = 3
    c = 0 
    for x in range(4):
        if ((daftar[nom][x][0] ** daftar[nom][x][1]) + sekon) == est:
            c = x+1
            await channel.send("Pelajaran Blok %i akan segera dimulai\nLink : %s" % (c, daftar[nom][x][2]))
            pass
        elif jam == 13 and menit == 00:
            break
    if hari == "Monday" :
        nom = 0
    elif hari == "Tuesday" :
        nom = 1
    elif hari == "Wednesday" :
        nom = 2
    elif hari == "Thursday" :
        nom = 3
    elif hari == "Friday" :
        nom = 4
    elif hari == "Saturday" :
        nom = 5

    if  hari == "Tuesday" and jam == 12 and menit == 31 and sekon == 25:
        cock = 0
        await channel.send("Pelajaran Blok %i akan segera dimulai\nLink : %s" % (c, daftar[1][0][2]))

    if  hari == "Tuesday" and jam == 12 and menit == 32 and sekon == 25:
        cock = 0
        await channel.send("Pelajaran Blok %i akan segera dimulai\nLink : %s" % (c, daftar[1][1][2]))



myLoop.start()
bot.run("OTQwMjY0NjA3NDYzOTMxOTM0.YgE3pw.FfgmbSxT8b02iy4Fkt6FO-phh90")    