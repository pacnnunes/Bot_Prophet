import telebot
import difflib

bot = telebot.TeleBot("<token>")

# Define uma função que será chamada quando o usuário enviar a mensagem /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Por favor, envie exatamente dois nomes, separados por vírgula, para comparar.")
    bot.reply_to(message, "Por exemplo: João, Maria")
# Define uma função que será chamada quando o usuário enviar uma mensagem de texto
@bot.message_handler(func=lambda message: True)
@bot.message_handler(func=lambda message: True)
def comparar_nomes(message):
    nomes = message.text.lower().split(", ")
    print(nomes)

    if len(nomes) != 2:
        bot.reply_to(message, "Por favor, envie exatamente dois nomes para comparar.")
    else:
        nome1, nome2 = nomes
        if "João" in nomes and "Maria" in nomes:
            pontuacao = 100
            bot.reply_to(message, "Vocês combinam muito!")
        else:
            pontuacao = 0
            bot.reply_to(message, "Pense bem, vocês não combinam!")

        bot.reply_to(message, f"A pontuação de similaridade entre {nome1} e {nome2} é: {pontuacao}")

# Inicia o bot
bot.polling()
