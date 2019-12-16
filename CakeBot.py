from datetime import date
import discord
import asyncio
user_list = [{"cakeDay": date(2000, 12, 31).isoformat(), "id": "<@000000000000000000>", "years": 19}, # Add desired users
             ]

client = discord.Client()

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

