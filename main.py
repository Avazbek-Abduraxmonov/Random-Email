import telebot
import requests
token = '7171130924:AAHwE5YcQRo41rkU7J1Y-er4ju8JWaAL1h8'

bot = telebot.TeleBot(token, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def welcome(msg):
    try:
        bot.send_message(msg.chat.id, '👋 Assalomu Aleykum botimizga xush kelibsiz!\n📩 Yangi Email olish uchun /add kommandasini yuboring!')
    except:
        bot.send_message(msg.chat.id, 'Xatolik!!!')
@bot.message_handler(commands=['add'])
def add_email(msg):
    try:
        url = "https://random-username-generate.p.rapidapi.com/"

        querystring = {"locale":"en_US","minAge":"18","maxAge":"50","domain":"ugener.com"}

        headers = {
        "X-RapidAPI-Key": "34fe6d2e50msh7e10501cd13c417p19e723jsnc12607a15468",
        "X-RapidAPI-Host": "random-username-generate.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        email = response.json().get('items').get('email')  # 'username' kalit so'zi ishlatilgan
        phone = response.json().get('items').get('phone')
        username = response.json().get('items').get('username')
        password = response.json().get('items').get('password')
        bot.send_message(msg.chat.id, f'📧 Email: {email}\n📞 Phone: {phone}\n🌐 Username: {username}\n❇ Password: {password}')    
    except:
        bot.send_message(msg.chat.id, '🚫 Xatolik boshqattan /add komandasini kiriting')
@bot.message_handler(func = lambda message: True)
def help_user(msg):
    try:
        bot.send_message(msg.chat.id, '📩 Email olishni xohlasangiz /add kommandasini yuboring!')
    except:
        bot.send_message(msg.chat.id, 'xatolik')

if __name__ == '__main__':
    bot.polling(none_stop=True)
