print('Импортирую модули...')
import discord
from discord.ext import commands
import random
import string
import os
import shutil
print('Успешно!')

print('Творим Говно...')
def createwallet(user_idi):
    os.mkdir(f'{dbfolder}//userbal//{user_idi}')
    balancefile = open(f'{dbfolder}//userbal//{user_idi}//balance.txt', 'w')
    balancefile.write('0')
    balancefile.close()
    
def generate_checkid(length=8):
    characters = string.ascii_letters + string.digits
    precheckid = ''.join(random.choice(characters) for _ in range(length))
    return precheckid

dbfolder = ".//database"

botcurrency = "ScrewCoin"

prefix = "w!"

admins = ['758627807818678293', '1065647424061849682', '885126796440395778', '1132291939455205386'] # цыфры в строчках пиздец!!!!!!

botver = "0.1.3"

print('Успешно!')

print('Создаю экземпляр бота...')
bot = commands.Bot(command_prefix=str(prefix))
print('Успешно!')

@bot.event
async def on_ready():
    print(f'Бот {bot.user.name} был запущен успешно!')

@bot.command()
async def balance(ctx, option=None, otheruserid=None, amount=None):
    '''Баланс вашего кошелька.'''
    user_id = str(ctx.author.id)
    try:
        balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'r')
        userbalance = str(float(balancefile.read()))
        balancefile.close()
        if option == "add":
            if user_id in admins:
                strotheruserid = str(otheruserid)
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'r')
                userbalance = str(float(balancefile.read()))
                balancefile.close()
                tempvari = float(userbalance) + float(amount)
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'w')
                balancefile.write(str(tempvari))
                balancefile.close()
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'r')
                userbalance = str(float(balancefile.read()))
                balancefile.close()
        if option == "set":
            if user_id in admins:
                strotheruserid = str(otheruserid)
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'r')
                userbalance = str(float(balancefile.read()))
                balancefile.close()
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'w')
                balancefile.write(str(amount))
                balancefile.close()
                balancefile = open(f'{dbfolder}//userbal//{strotheruserid}//balance.txt', 'r')
                userbalance = str(float(balancefile.read()))
                balancefile.close()
        if option == "create":
            if user_id in admins:
                strotheruserid = str(otheruserid)
                createwallet(strotheruserid)
        await ctx.reply(f'У вас {userbalance} {botcurrency}')
    except:
        print('')
        try:
            createwallet(user_id)
            print('')
            balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'r')
            userbalance = str(float(balancefile.read()))
            balancefile.close()
            await ctx.reply(f'У вас {userbalance} {botcurrency}')
        except Exception as e:
            await ctx.reply(f'Хм... Что-то пошло не так.\n{e}')
            
@bot.command()
async def check(ctx, option=None, amount=None, usersamount=None): #amount является гибридной хернёй для create, activate и delete
    '''Создаёт, активирует и удаляет чек.'''
    user_id = str(ctx.author.id)
    try:
        stramount = str(float(amount))
    except:
        stramount = str(amount)
    strusersamount = str(usersamount)
    try:
        balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'r')
        userbalance = str(balancefile.read())
        balancefile.close()
    except:
        print('')
        try:
            createwallet(user_id)
            balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'r')
            userbalance = str(float(balancefile.read()))
            balancefile.close()
        except Exception as e:
            await ctx.reply(f'Хм... Что-то пошло не так.\n{e}')
    if option == "create":
        if amount == None:
            await ctx.reply(f'Вот так должна выглядить команда для создания чека: {prefix}check create [Количество] [Количество пользователей которые могут активировать чек]\nЕсли что ваш баланс: {userbalance} {botcurrency}')
        else:
            if usersamount == None:
                await ctx.reply(f'Нет количества пользователей которые могут активировать чек.')
            else:
                if float(amount) <= 0 or int(usersamount) <= 0:
                    await ctx.reply(f'Отличная попытка слушай.')
                else:
                    if float(amount) >= float(userbalance) + 1:
                        await ctx.reply(f'У вас недостаточно {botcurrency}.')
                    else:
                        checkid = str(generate_checkid())
                        os.mkdir(f'{dbfolder}//checks//{checkid}')
                        os.mkdir(f'{dbfolder}//checks//{checkid}/activatedby')
                        checkamountfile = open(f'{dbfolder}//checks//{checkid}//checkamount.txt', 'w')
                        checkamountfile.write(str(amount))
                        checkamountfile.close
                        checkusersamountfile = open(f'{dbfolder}//checks//{checkid}//checkusersamount.txt', 'w')
                        checkusersamountfile.write(str(usersamount))
                        checkusersamountfile.close
                        checkownerfile = open(f'{dbfolder}//checks//{checkid}//checkowner.txt', 'w')
                        checkownerfile.write(user_id)
                        checkownerfile.close
                        tempvari = float(userbalance) - float(amount)
                        balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'w')
                        balancefile.write(str(tempvari))
                        balancefile.close()
                        tempvarii = float(amount) / int(usersamount)
                        stramountoneact = str(tempvarii)
                        checkamountoneactfile = open(f'{dbfolder}//checks//{checkid}//checkamountoneact.txt', 'w')
                        checkamountoneactfile.write(str(tempvarii))
                        checkamountoneactfile.close
                        activatedfileo = open(f'{dbfolder}//checks//{checkid}//activatedby//{user_id}', 'w')
                        activatedfileo.write('1')
                        activatedfileo.close()
                        await ctx.reply(f'Чек создан на {stramount} {botcurrency}!\nМогут активировать {strusersamount} пользователей.\nСумма одной активации: {stramountoneact} {botcurrency}\nID Чека: {checkid}\n{prefix}check activate {checkid}')
    elif option == "activate":
        if amount == None:
            await ctx.reply(f'Вот так должна выглядить команда для активаций чека: {prefix}check activate [ID Чека]')
        else:
            try:
                try:
                    activatedfile = open(f'{dbfolder}//checks//{amount}//activatedby//{user_id}', 'r')
                    activatedfile.close()
                    await ctx.reply(f'Вы уже активировали этот чек.')
                except:
                    checkamountoneactfile = open(f'{dbfolder}//checks//{amount}//checkamountoneact.txt', 'r')
                    amountoneact = str(checkamountoneactfile.read())
                    checkamountoneactfile.close()
                    checkusersamountfileo = open(f'{dbfolder}//checks//{amount}//checkusersamount.txt', 'r')
                    usersamounto = checkusersamountfileo.read()
                    checkusersamountfileo.close()
                    tempvariii = float(userbalance) + float(amountoneact)
                    balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'w')
                    balancefile.write(str(tempvariii))
                    balancefile.close()
                    activatedfile = open(f'{dbfolder}//checks//{amount}//activatedby//{user_id}', 'w')
                    activatedfile.write('1')
                    activatedfile.close()
                    await ctx.reply(f'Вы получили {amountoneact} {botcurrency}!')
                    file_count = sum([len(files) for _, _, files in os.walk(f'{dbfolder}//checks//{amount}//activatedby//')])
                    if int(file_count) == int(usersamounto) + 1:
                        shutil.rmtree(f'{dbfolder}//checks//{amount}//')
            except:
                await ctx.reply(f'К сожалению этого чека не существует.')
                
    elif option == "delete":
        if amount == None:
            await ctx.reply(f'Вот так должна выглядить команда для удаления чека: {prefix}check delete [ID Чека]')
        else:
            try:
                checkownerfile = open(f'{dbfolder}//checks//{amount}//checkowner.txt', 'r')
                checkowner = checkownerfile.read()
                checkownerfile.close()
                if user_id == checkowner or user_id in admins:
                    checkamountfileo = open(f'{dbfolder}//checks//{amount}//checkamount.txt', 'r')
                    amounto = checkamountfileo.read()
                    checkamountfileo.close()
                    tempvaro = float(userbalance) + float(amounto)
                    if user_id in admins:
                        balancefileo = open(f'{dbfolder}//userbal//{checkowner}//balance.txt', 'r')
                        userbalance = str(float(balancefileo.read()))
                        balancefileo.close()
                        tempvaroo = float(userbalance) + float(amounto)
                        balancefileo = open(f'{dbfolder}//userbal//{checkowner}//balance.txt', 'w')
                        balancefileo.write(str(tempvaroo))
                        balancefileo.close()
                        await ctx.reply(f'<@{checkowner}> получил свои {amounto} {botcurrency} назад!')
                    else:
                        balancefile = open(f'{dbfolder}//userbal//{user_id}//balance.txt', 'w')
                        balancefile.write(str(tempvaro))
                        balancefile.close()
                        await ctx.reply(f'Вы получили {amounto} {botcurrency} назад!')
                    shutil.rmtree(f'{dbfolder}//checks//{amount}//')
                    await ctx.reply(f'Чек был удалён.\nID Чека: {amount}')
                else:
                    await ctx.reply(f'Вы не владелец чека.\nID Чека: {amount}')
            except:
                await ctx.reply(f'К сожалению этого чека не существует.')
    else:
        await ctx.reply(f'Есть 3 опции:\ncreate\nactivate\ndelete\n\nПример: {prefix}check create 12 5')
        

@bot.command()
async def about(ctx):
    '''О боте.'''
    await ctx.reply(f'Данный бот основан на Stupid Discord Wallet.\nЭтот бот умеет только хранить ваши {botcurrency}, создавать и активировать чеки.\nЭто простой фэйковый крипто-кошелёк официально продать или купить {botcurrency} нельзя.\nРазработчики - @drel69 (TG)\n\nО проекте:\nStupid Discord Wallet был сделан с нуля не используя исходники самого Stupid Wallet в телеграме.\nПроект Open-Source поэтому каждый может его запустить со своими плюшками ({prefix}github)\n\n Версия бота: {botver}')
    
@bot.command()
async def github(ctx):
    '''Github Бота.'''
    await ctx.reply(f'https://github.com/drel4/stupid_discord_wallet')

print('Запускаю наконец бота...')
bottokenfile = open(f'token.txt', 'r')
bottoken = bottokenfile.read()
bottokenfile.close()
bot.run(bottoken)
