import requests
import telebot
import random

BOT_TOKEN = "6034597628:AAFhI0E-DLlCdS7fjTjPXHu3Glf5byyUCkM"
bot = telebot.TeleBot(BOT_TOKEN)

toppers = {'Nishant':'A6','Abhigna':'01','Abhirami':'04','Anushka':'11','Ateeq':'90','Nagarjuna':'96','Manoj':'85','Naveesh':'99',
           'Deepak':'74','Prajwal':'B1','Praneeth':'B3','Praveena':'B7','Tarun':'C1','Chetana':'E2',
           'Hitesh':'54','Ruby':'D7'}
@bot.message_handler(commands=['start']) 
def start(message): 
    bot.reply_to(message,"Hey!!")

@bot.message_handler(commands=['help']) 
def help(message): 
    bot.reply_to(message, bot.reply_to(message, "I support the following commands: \n /start \n /help \n /dmkd \n /sqat")) 

@bot.message_handler(commands=['dmkd'])
def dmkd(message):
    query = message.text.replace('/dmkd','').lower()
    query = ''.join(e for e in query if e.isalnum())
    bot.send_message(message.chat.id,"searching around 🔎.May take some time...")
    lst=[]

    for i in toppers.keys():
        url = f'https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/20951A05{toppers.get(i)}/LAB/SEM6/ACIC08/20951A05{toppers.get(i)}_{query}.pdf'
        r = requests.get(url)
        if r.status_code == 200:
            lst.append([url, i])
            break
    if lst:
        bot.send_document(message.chat.id,lst[0][0],None, f"{lst[0][1]}'s File. Here you go 😃")
    else:
        bot.send_message(message.chat.id,"Sorry,Ig the Dmkd legends didn't upload the file or didnt execute the code...yet😪")

@bot.message_handler(commands=['sqat'])
def sqat(message):
    query = message.text.replace('/sqat','').lower()
    query = ''.join(e for e in query if e.isalnum())
    bot.send_message(message.chat.id,"searching around 🔎,May take some time...")
    lst=[]

    for i in toppers.keys():
        url = f'https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/20951A05{toppers.get(i)}/LAB/SEM6/ACIC09/20951A05{toppers.get(i)}_{query}.pdf'
        r = requests.get(url)
        if r.status_code == 200:
            lst.append([url,i])
            break
    if lst:
        bot.send_document(message.chat.id,lst[0][0],None,f"{lst[0][1]}'s File.Here you go 😃")
    else:
        bot.reply_to(message,"Sorry,Ig Nishant  didnt even sent to us...yet 😪")

@bot.message_handler(commands=['get'])
def get(message):
    query = message.text.replace('/get','').lower()
    query = message.replace('[','')
    query = message.replace(']','')
    '''try:
        roll,subject,week = query.split()
        roll = roll.upper()
        if subject == 'dmkd':
            subject_id = 'ACI08'
            sem = 'SEM6'
        if subject == 'sqat':
            subject_id = 'ACI09'
            sem = 'SEM6'
        bot.reply_to(message,"Searching around 🔎...")
        lst = []
        url = f'https://iare-data.s3.ap-south-1.amazonaws.com/uploads/STUDENTS/{roll}/LAB/{sem}/{subject_id}/{roll}_{"week"+week}.pdf'
        r=requests.get(url)
        if r.status_code == 200:
            bot.send_document(message.chat.id,url,None,f"{roll}'s {subject.upper()} {'Week '+week} File. Here you go 😃")
        else:
        	bot.send_message(message.chat.id, "Sorry, looks like it isn't uploaded yet 😟")
    except:
        bot.send_message(message.chat.id, "Looks like a command error. Send something like this")
        bot.send_message(message.chat.id, "/get 20951a05B1 dmkd 2")'''

print("I am alive...")
bot.infinity_polling()
