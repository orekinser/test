import discord
from discord.ext import commands
from discord import Option
import random
from keep_alive import keep_alive
import datetime
from discord.utils import get



server_ids = [872055834425835560]
bot = commands.Bot(command_prefix="#", intents=discord.Intents.all())


@bot.command()
async def test2(ctx):
  await ctx.send("```The command works now.```")


@bot.slash_command(guild_ids=server_ids, name="join", description="")
async def join(ctx):
  channel = ctx.author.voice.channel
  await channel.connect()
  await ctx.send("```ㄟ嘿我進來囉！```")


@bot.event
async def on_ready():
  print("Stay with me~~")
  await bot.change_presence(status=discord.Status.idle,
                            activity=discord.Game("AFK in 死人群組"))


keep_alive()


@bot.slash_command(guild_ids=server_ids, name="test", description="測試指令專用的指令")
async def test(ctx):
  await ctx.respond("The command works now.")


@bot.slash_command(guild_ids=server_ids,
                   name="say",
                   description="機器人幫你說你不敢說的。")
async def say(ctx, say):
  await ctx.send(f"{say}")


@bot.slash_command(guild_ids=server_ids,
                   name="avatar",
                   description="查找腦纏人們的豬鼻頭像。")
async def avatar(ctx, member: discord.Member = None):
  if member == None:
    member = ctx.author
  embed = discord.Embed(title=f"這就是你要的 <@{member.name}> 頭像:",
                        url="https://youtu.be/dQw4w9WgXcQ",
                        color=discord.Color.random(),
                        timestamp=datetime.datetime.now())
  embed.set_image(url=f"{member.display_avatar}")
  await ctx.send(embed=embed)


@bot.slash_command(guild_ids=server_ids,
                   name="nothing",
                   description="你無聊到要跟機器人聊天。")
async def nothing(ctx):
  response = [
    '低能', '腦殘', '破腦', '沒媽', '死媽', '廢物', '憨兒', '林老師卡好', '喜憨', '沒爸', '沒老二閉嘴',
    '沒懶趴閉嘴', '幹林娘機掰', '幼華幼華 又油又滑', '讀松山工農都...', '閉嘴啦', '憨包一個', '你死好', '你媽逼',
    '傻逼', '臭甲', '小雞雞', '喔', '嗯', '呃', '阿', '屁眼', '睪丸', '我在打R6', '我是終極梁雲翔！',
    '呃呃', '奶頭', '阿不是阿', '呃據我所知', '🤖', '大便', 'OK掛機', '馬子狗死好'
  ]
  await ctx.respond(f"{random.choice(response)}")


@bot.slash_command(guild_ids=server_ids,
                   name="purge",
                   description="清理一些弱智多餘的訊息。")
async def purge(ctx, messages: Option(int,
                                      description="你需要刪除多少訊息?",
                                      required=True)):
  amount = await ctx.channel.purge(limit=messages)
  await ctx.defer()
  await ctx.respond(f"已經幫你這個懶狗清理 **{len(amount)}** 條訊息")


@bot.slash_command(guild_ids=server_ids,
                   name="applies",
                   description="向管理員申請禁言腦攤人。")
async def applies(ctx, member: Option(discord.Member, required=True),
                  reason: Option(str, required=True),
                  minutes: Option(int, required=True)):
  await ctx.send(
    f"<@{ctx.author.id}>申請**蘇蘇大將軍**將<@{member.id}>禁言{minutes}分鐘，委託原因:{reason}")
  await ctx.respond("好好好")


@bot.slash_command(guild_ids=server_ids,
                   name="decides",
                   description="你太過廢物甚至沒有主見。")
async def decides(ctx, choice1: Option(required=True),
                  choice2: Option(required=True),
                  choice3: Option(required=False),
                  choice4: Option(required=False)):
  if choice3 == choice4 == None:
    response = [choice1, choice2]
    await ctx.respond(f"根據我的巨根呢 我覺得要選**{random.choice(response)}**")
  else:
    response = [choice1, choice2, choice3, choice4]
    await ctx.respond(f"巨根縮汁 我認為要選**{random.choice(response)}**")


@bot.slash_command(guild_ids=server_ids,
                   name="ama",
                   description="這不是ChatGPT 我不明白。")
async def ama(ctx, question: Option(required=True)):
  response = [
    '你說的對，但是《你說的對》是由你說的對自主研發的一款全新你說的對。你說的對發生在一個被稱作「你說的對」的你說的對世界，在這裡被你說的對選中的你說的對將被授予「你說的對」，引導你說的對之力。你將扮演一位名為「你說的對」的神秘角色，在自由的旅行中邂逅你說的對、你說的對的你說的對們，和你說的對一起擊敗你說的對，尋找失散的你說的對，同時，逐步發掘「你說的對」的真相。',
    '每個人都不得不面對這些問題。在面對這種問題時，務必詳細考慮你這個問題的各種可能。若能夠欣賞到你這個問題的美，相信我們一定會對你這個問題改觀。李奧貝納曾說過，我所享有的任何成就，完全歸因於對客戶與工作的高度責任感，不惜付出自我而成就完美的熱情，以及絕不容忍馬虎的想法，草率粗心的工作，與差強人意的作品。這啟發了我。',
    '在這種困難的抉擇下，本人思來想去，寢食難安。儘管如此，我們仍然需要對你這個問題保持懷疑的態度。',
    '富蘭克林曾經說過，絕望毀掉了一些人，而傲慢則毀掉了許多人。這似乎解答了我的疑惑。由於，海涅說過一句發人省思的話，人生是疾病，世界是醫院，而死是我們的醫生。但願諸位理解後能從中有所成長。探討你這個問題時，如果發現非常複雜，那麼想必不簡單。',
    '關我屁事', '好好好你說的都對', '阿然後呢 問我幹嘛', '夠可悲才會去問機器人意見', '喔是這樣是不是 第一次聽說欸', '040',
    '喔是喔', '恩恩 對阿怎麼會這樣呢', '好啊都這樣啊都問一些怪怪的問題啊', '你這不是問題啊!', '我是蘇子睿',
    '這個問題個人覺得非常有哲理', '什麼懶洨問題啊媽的', '你不要那麼智障好不好', '好 你從桃園新竹 你從桃園新竹 你從桃園新竹',
    'Ask me anything except the question stupid like this.', '말보다는행동이지',
    '咿咿啊啊喔喔啊', '啦啦啦啦啦 我是蘇子睿'
  ]
  await ctx.respond(
    f"根據你這低能的問題:「{question}」 我的答案是:**{random.choice(response)}**")


@bot.slash_command(guild_ids=server_ids,
                   name="sign",
                   description="向這群組宣告傻逼上線了。")
async def sign(ctx, claim: Option(str,
                                  description="來看看你要發表什麼宣言",
                                  required=True)):
  embed = discord.Embed(title=f"{ctx.author.name}上線了!",
                        url="https://youtu.be/dQw4w9WgXcQ",
                        description="讓我們來看看他說了什麼。",
                        color=discord.Color.random(),
                        timestamp=datetime.datetime.now())
  embed.set_author(name=f"{ctx.author.display_name}",
                   icon_url=f"{ctx.author.display_avatar}")
  embed.set_thumbnail(url=f"{ctx.guild.icon}")
  embed.add_field(name="宣告內容:", value=f"{claim}", inline=True)
  await ctx.send(embed=embed)


@bot.event
async def on_message(message):
  message.content = (message.content.lower())
  if "我是蘇子睿" in message.content:
    if message.author == bot.user:
      return
    else:
      await message.reply("我是蘇子睿！")

  if message.content == "幹":
    response = [
      '我放屁了', '嘖', '氣別', '😡', '別急', '別氣', 'ㄏ', '呃呃', '惱羞?'
    ]
    if message.author == bot.user:
      return
    else:
      await message.channel.send(f"{random.choice(response)}")

  if bot.user.mentioned_in(message):
    response = ['?', '蛤', 'wuh?', 'huh?', 'hi', '弱智一個']
    await message.reply(f"{random.choice(response)}")

  if "你媽" in message.content:
    response = [
      '沒媽閉嘴', '我是你媽', '你媽逼蛋', '傻子', '林紋如是我', '我是謝佳芸', '超你媽逼', '我是你爸', '你媽死了'
    ]
    if message.author == bot.user:
      return
    else:
      await message.channel.send(f"{random.choice(response)}")

  if message.content == "喔":
    response = ['喔屁', '喔啥', '豬頭皮', '蛤', '豬腦', '040']
    if message.author == bot.user:
      return
    else:
      await message.channel.send(f"{random.choice(response)}")

  if "屁" in message.content:
    response = ['我屁股是甜的', '想幹你屁', '沒屁閉嘴', '欸我放屁了', '你屁眼夠臭']
    if message.author == bot.user:
      return
    else:
      await message.channel.send(f"{random.choice(response)}")


bot.run(
  'ODM4Mjg4NDUzMDMxODIxMzE0.GS7ML8.U9tFAO2nEbhOjX03cRivapUU34A7dgHcebQkcQ')

#-----------------------------------------------------------------------------
