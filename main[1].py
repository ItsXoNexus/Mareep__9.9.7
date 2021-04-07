import discord, os, requests, json, time, random, asyncio
from discord.ext import commands
from keep_alive import keep_alive
client = discord.Client()
waterType = random.randint(0, 5)
cosupport = '<@&825719558538002433>'
support = '<@&825544367925231636>'
supportA = '<@719729047848091689>'
supportB = '<@737731464665366608>'
bots = '<@&825720124224045066>'
mareepers = '<@&825588286079893554>'
mod = '<@&827572289045266463>'
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))
userList = []
bot = commands.Bot(command_prefix='//')
@client.event
async def on_message(message):
  global battleCode
  global mb
  if message.author == client.user:
    return
  msg = message.content.lower()
  if str(message.author) not in userList:
    userList.append(str(message.author))
    print(userList)
  if msg.startswith('mare') and msg.endswith('ep'):
    await message.channel.send('Mareeep! <:mareeep:824399111977304064>')
  if msg == '//help':
    embed = discord.Embed(title="MareeepBot Commands", description="Hello! I'm MareeepBot! \nHere are the commands:\n//help - view commands!\n//hello - Mareep will greet you!\n//battle - Mareep battles a water type pokemon!\n//mbaccount - Shows MareeepBot\'s user name and account number\n//lesson - Learn something new about pokémon!\n//stats - view Mareep\'s stats\n//stats2 - see more of Mareep\'s stats!\n//pokeball - Captures 1 of 23 pokémon there are! The number of pokémon will increase as time goes on!\n//ping - ping urself lol\n//ping ms - See your ping :D", colour = 0x3498db)
    await message.channel.send(embed=embed)

  if 'best' in msg:
    await message.channel.send('Mareep\'s the best because I say so lol.')
  if msg == '//hello' or 'hello' in msg or 'hi' in msg or msg == '//hi' or msg == '//hiya' or msg == '//hey' or msg == '//hai' or 'hiya' in msg or 'hey' in msg or 'hai' in msg:
	  await message.channel.send(file=discord.File('hello.jpg'))
  if msg == '//battle':
    waterType = random.randint(1, 5)
    waterList = ["Squirtle", "Gyrados", "Buizel", "Poliwag", "Seaking"]
    if waterType == 1:
      waterPoke = waterList[0]
      opponent = "[SlippySquirt USA :flag_us:]"
    if waterType == 2:
      waterPoke = waterList[1]
      opponent = "[SnakyGyro Greece :flag_gr:]"
    if waterType == 3:
      waterPoke = waterList[2]
      opponent = "[SurfingOtter Australia :flag_au:]"
    if waterType == 4:
      waterPoke = waterList[3]
      opponent = "[WackyWagger Britain :flag_gb:]"
    if waterType == 5:
      waterPoke = waterList[4]
      opponent = "[KillaWail Norway :flag_no:]"
    await message.channel.send('Finding opponent... ' + opponent + ' Type START BATTLE to continue!')
  if msg == 'start battle':
    waterType = random.randint(1, 5) 
    waterList = ["Squirtle", "Gyrados", "Buizel", "Poliwag", "Seaking"]
    if waterType == 1:
      waterPoke = waterList[0]
    if waterType == 2:
      waterPoke = waterList[1]
    if waterType == 3:
      waterPoke = waterList[2]
    if waterType == 4:
      waterPoke = waterList[3]
    if waterType == 5:
      waterPoke = waterList[4]
    await message.channel.send('Mareep used Thunder Shock!')
    await message.channel.send(waterPoke + ' used Water Gun!')

    await message.channel.send('Mareep used Electro Ball!')
    await message.channel.send(waterPoke + ' fainted! You won! :trophy:')
  if 'bwuh' in msg or 'bruh' in msg:
    await message.channel.send('bwuh right back at ya - Mareep')
  if msg == "//mbaccount":
    await message.channel.send("MareeepBot#0231")
  if 'sure' in msg:
    await message.channel.send("Yes, I'm sure. Believe me!")
  if client.user.mentioned_in(message):
	  await message.channel.send("WHY U PING POOR MAREEP!?")
	  await message.channel.send(message.author.mention)
	  await message.channel.send(message.author.mention)
	  await message.channel.send(message.author.mention)
	  await message.channel.send(message.author.mention)
	  await message.channel.send(message.author.mention)
  if msg == '//stats':
	  embed = discord.Embed(title="Mareep's Stats (Page 1)", description="Type: Electric\nHeight: 2 feet (0.6 meters)\nWeight: 17.2 pounds (7.8 kilograms)\nAbility: Static (may paralyze enemies on contact)\nHidden Ability: Plus\nGender Ratio: 50% male | 50% female\nEgg Groups: Monster/Field", color=0x3498db)
	  await message.channel.send(embed=embed)
  if msg == '//stats2' or msg == '//stats 2':
	  embed = discord.Embed(title="Mareep's Stats (Page 2)", description="Health: 55\nAttack: 40\nDefense: 40\nSpecial Attack: 65\nSpecial Defense: 45\nSpeed: 35", color=0x3498db)
	  await message.channel.send(embed=embed)
  if msg == '//lesson':
    lessonChance = random.randint(1, 11)
    if lessonChance == 1:
      await message.channel.send("Pokémon were invented by someone who had a hobby of collecting insects and loved anime!")
    if lessonChance == 2:
      await message.channel.send("The most common type of Pokémon is actually water-type!")
    if lessonChance == 3:
      await message.channel.send("Rhydon was the first Pokémon to ever be created.Bulbasaur was thefirst Pokemon in the Pokedex, But  According to Pokémon legend, however, Arceus was the first Pokémon!")
    if lessonChance == 4:
      await message.channel.send("Slowbro is the ONLY Pokémon that can devolve!")
    if lessonChance == 5:
      await message.channel.send("The Pokémon named Zubat doesn't have any eyes! If you didn't realize, take a closer look!")
    if lessonChance == 6:
      await message.channel.send("The gender of Pikachu and be determined by its tail!")
    if lessonChance == 7:
      await message.channel.send("Charmander has the longest name of all the unevolved starters!")
    if lessonChance == 8:
      await message.channel.send("Eevee has the most amount of evolutions in the Pokémon world!")
    if lessonChance == 9:
      await message.channel.send("The Pokémon named Spearow is colorblind!")
    if lessonChance == 10:
      await message.channel.send("Pokéballs were invented because of Primeape!")
    if lessonChance == 11:
       await message.channel.send("Bulbasaur is the first Pokémon that appears in the pokedex!")
  if msg == '//pokeball' or msg == '//pokéball' or msg == "//pokball" or msg == "//pokeeball" or msg == "//pokeballl":
    pokeballchance = random.randint(1, 23)
    pokemonball = ['Clefairy', 'Pikachu', 'Gligar', 'Jigglypuff', 'Incineroar', 'Eevee', 'Mewtwo', 'Snorlax', 'Hitmonchan', 'Gengar', 'Ditto', 'Lucario', 'Bulbasaur', 'Rhydon', 'Garchomp', 'Rayquaza', 'Arceus', 'Lapras', 'Lugia', 'Slowking', 'Dragonite', 'Blaziken', 'Chespin', 'Bulbasaur','Ivysaur', 'Venusaur', 'Squirtle','Wartortle','Blastoise','Charmander','Charmeleon', 'Charizard', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pigey','Pidgeotto', 'Pidgeot','Raticate' ,'Rattata', 'Spearow', 'Fearow', '	Ekans', 'Arbok', 'Pichu','Greninja','Raichu','Sandshrew', 'Sandslash','Nidoran ♀', 'Nidorina', 'Nidoqueen', 'Nidoran ♂', 'Nidorino','	Nidoking', 'Clefairy', 'Clefable','Vulpix','Ninetales','Scizor','Ralts','Kirlia','Gardevoir','Gallade','Ampharos','Rowlet','Dartrix','Decidueye' ]
    if pokeballchance == 1:
      pokemoncapture = pokemonball[0]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 2:
      pokemoncapture = pokemonball[1]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 3:
      pokemoncapture = pokemonball[2]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 4:
      pokemoncapture = pokemonball[3]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 5:
      pokemoncapture = pokemonball[4]
      await message.channel.send("You threw a pokéball and you captured an " + pokemoncapture + "!")
    if pokeballchance == 6:
      pokemoncapture = pokemonball[5]
      await message.channel.send("You threw a pokéball and you captured an " + pokemoncapture + "!")
    if pokeballchance == 7:
      pokemoncapture = pokemonball[6]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 8:
      pokemoncapture = pokemonball[7]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 9:
      pokemoncapture = pokemonball[8]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 10:
      pokemoncapture = pokemonball[9]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 11:
      pokemoncapture = pokemonball[10]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 12:
      pokemoncapture = pokemonball[11]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 13:
      pokemoncapture = pokemonball[12]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 14:
      pokemoncapture = pokemonball[13]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 15:
      pokemoncapture = pokemonball[14]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 16:
      pokemoncapture = pokemonball[15]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 17:
      pokemoncapture = pokemonball[16]
      await message.channel.send("You threw a pokéball and you captured an " + pokemoncapture + "!")
    if pokeballchance == 18:
      pokemoncapture = pokemonball[17]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 19:
      pokemoncapture = pokemonball[18]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 20:
      pokemoncapture = pokemonball[19]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 21:
      pokemoncapture = pokemonball[20]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 22:
      pokemoncapture = pokemonball[21]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
    if pokeballchance == 23:
      pokemoncapture = pokemonball[22]
      await message.channel.send("You threw a pokéball and you captured a " + pokemoncapture + "!")
  if msg == "//ping":
    await message.channel.send(message.author.mention)
  if 'dang' in msg or 'darn' in msg:
    await message.channel.send('dang it, darn it, i don\'t know what to say! - Mareep')
  if msg == '//support':
    await message.channel.send("The code for the support server is KudMVdyK")
  if msg == '//ping ms' or msg == '//pingms':
	  await message.channel.send('Pong! `{0}ms`'.format(int(round(client.latency, 3) * 1000)))
  if msg == '//del':
	  await message.delete(message)
	  await message.channel.send('Message deleted!')

keep_alive()
client.run(os.getenv('token'))