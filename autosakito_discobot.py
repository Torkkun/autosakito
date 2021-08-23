import discord
import time
from datetime import datetime
from discord.ext import commands, tasks
import Login

if __name__ == '__main__':
    TOKEN = "TOKEN"
    CHANNEL_ID = 831261636076634196
    client = discord.Client()

    @client.event
    async def on_message(message):
        if message.author.bot:
            return
        
        if message.content == 'ヘルプ':
            embed = discord.Embed(title="キーワード一覧", description="ポイント\nガチャる\nボーナス")
            await message.channel.send(embed=embed)

        #全合計ポイントを取得する
        if message.content == 'ポイント':
            point = Login.my_points(1)
            npoint = "現在のポイントの合計は" + point
            await message.channel.send(npoint)
            if int(point) >= 10:
                point = int(point) // 10
                ms = "引換券ガチャが" + str(point) + "回引ける"
                await message.channel.send(ms)

        #引換券ガチャをする
        if message.content == "ガチャる":
            point = Login.my_points(1)
            roop = int(point)//10
            if roop > 0:
                for i in range(roop):
                    ms = Login.ticket_gatya()
                    mms = ms + "です"
                    await message.channel.send(mms)
            else:
                await message.channel.send(str(point) + "ポイントしかないから引けないよ")
            
            Login.mypageclick()

        #ボーナスガチャ
        if message.content == 'ボーナス':
            bpointT = Login.my_points(2)
            bpt = "貯まっているポイント券は" + bpointT + "枚です"
            bpointD = Login.my_points(3)
            bpd = "ボーナスガチャまでは残り" + bpointD + "です"
            await message.channel.send(bpt + '\n' + bpd)

    #一日一回行うタスク
    @tasks.loop(minutes=1)
    async def dayonece():
        now = datetime.now().strftime('%H:%M')
        if now == '07:00':
            oldpoint = Login.my_points(1)
            channel = client.get_channel(CHANNEL_ID)
            Login.pointgatya()
            newpoint = int(Login.my_points(1)) - int(oldpoint)
            await channel.send(newpoint + "\n" + "ガチャ終了")

    #@tasks.loop(hours=1)
    #async def dayonece():
    #    channel = client.get_channel(CHANNEL_ID)
    #    result = Login.pointgatya()
    #    await channel.send(result + "\n" + "ガチャ終了")

    @dayonece.before_loop
    async def before_dayonce():
        await client.wait_until_ready()

    dayonece.start()

    client.run(TOKEN)

