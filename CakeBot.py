from datetime import date
import discord
import asyncio
user_list = [{"cakeDay": date(2000, 12, 31).isoformat(), "id": "<@000000000000000000>", "years": 19}, # Add desired users
             ]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.cakeday'):
        for i in user_list:
            if message.author.id == int(i["id"].strip("<@>")):
                j = i["cakeDay"]
                j = dateconvert(j)
                await message.channel.send("Your cakeday is " + j + "!!")
                break


def dateconvert(date): #method to display into a more user-friendly format "year-month-day" to "Month Day Year"
    date = date.replace("-", " ")
    list = date.split() #list[0] = year, list[1] = month, list[2] = day
    j = monthconvert(list[1]) + dayconvert(list[2]) + list[0]
    return j #j will be day, month, year combined

def monthconvert(month): #01 - 12
    if month == "01":
        return "January "
    if month == "02":
        return "February "
    if month == "03":
        return "March "
    if month == "04":
        return "April "
    if month == "05":
        return "May "
    if month == "06":
        return "June "
    if month == "07":
        return "July "
    if month == "08":
        return "August "
    if month == "09":
        return "September "
    if month == "10":
        return "October "
    if month == "11":
        return "November "
    if month == "12":
        return "December "


def dayconvert(day): #0x - xx
    if day == "01":
        return "1st "
    elif day == "02":
        return "2nd "
    elif day == "03":
        return "3rd "
    else:
        return day + "th "
    
@client.event
async def today_date():
    today = date.today().isoformat()
    return today

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await on_start()

@client.event
async def on_start():
    while True:
        for i in user_list:
            today = today_date()
            if await today == i["cakeDay"]:
                await announcement(i["id"], i["years"])
                update_years(i)
        await asyncio.sleep(86400) #change frequency that bot checks userlist for cakeday, recommended to check every 24 hours(86400 seconds default)

@client.event
async def announcement(userid, anniversary):
    channel = client.get_channel(0000000000) # change to desired channel id
    await channel.send(str(userid) + " is celebrating their cake day! They've used discord for " + str(anniversary) + " years now! @everyone" ) #change message


def update_years(user):
    user["years"] = user["years"] + 1

client.run('abc') #Add bot id

