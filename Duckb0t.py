import telebot
from telebot import types
import random

bot=telebot.TeleBot('5808738937:AAF6f0r9GfRLHMDxUqCtvnkgawLmfYdhF3A')


"""Функция на проверку буквы"""
def receiving_a_response(message,words,word_1,word_2,count,count_of_checking_words,count_of_right_answers,count_of_answers):	
	if message.text=="СТОП":
		test_finish(message,count_of_right_answers,count_of_answers)
		return

	let=message.text
	word_2=word_1.replace("..", let)
	if words==word_2:
		bot.send_message(message.from_user.id, "Правильно")
		count_of_right_answers+=1
	else:	
		bot.send_message(message.from_user.id, "Неправильно")
	count_of_answers+=1
	test(message,words,word_1,word_2,count,count_of_checking_words,count_of_right_answers,count_of_answers)


"""Создание списка слов для теста пользователем через телеграмм"""
@bot.message_handler(content_types=["text"], commands=["user_test_for_Russia_language"])
def user_test_for_Russia_language(message):
	user_dictionary_words=[]
	bot.send_message(message.from_user.id, "Чтобы создать свой тест вводите по одному слову и нужную гласную, которую бот и будет проверять делайте заглавной(см скриншот).\n Чтобы прекратить ввод слов напишите СТОП.")
	primer = open('C:/Users/kmkar/CAKE_PROGRAMMER/python/Telegram bot/images/primer.PNG', 'rb')
	bot.send_photo(message.from_user.id, primer)
	while message.text!="СТОП":
		user_dictionary_words.append(message.text)
	bot.send_message(message.from_user.id, user_dictionary_words)


"""Запуск готовго теста, который изначально лежит в боте"""
@bot.message_handler(content_types=["text"], commands=["test_Russia_language"])
def test_Russia_language(message):

	Dictionary_words=["кОмпьютер","кОнкурент","кОрзина","кОролевство","лАбиринт","лИнгвистический","мЕтафора",
"нОвелла","обАяние","орАнжерея","ориЕнтир","ошЕломлённый","панОрама","парашЮт","подрАжание","порАзительный",
"правИльный","примИтивный","рЕализм","рЕжиссёрский","рестАврация","рОвесники","сИреневый","сокрОвенные (мечты)",
"стадИон","стрЕмиться","тАлант","трАдиционный","трОллейбусный (парк)","фестИваль","кОмфортный","кОнференция",
"кОричневый","крОмешная (тьма)","лЕлеять (мечту)","насЕкомое","обАняние","оптИмистичный","орИгинальный","офИцерский",
"пАлисадник","панОрамный","пЕйзаж","пессИмистический","покОление","посЕщать","разбОгатеть","рЕалистичный",
"резИденция","рЕцензент","сИмптомы","(в) смЯтении","спАртакиада","стИпендия","сувЕренитет","тОржественный",
"трЕвожиться","унИчтожать"]

	global dictionary_words
	dictionary_words=Dictionary_words
	count_of_right_answers=0
	count_of_answers=0

	markup_0 = types.ReplyKeyboardMarkup()
	Button_0=types.KeyboardButton('СТАРТ')

	markup_0.row(Button_0)

	bot.send_message(message.from_user.id, "Нажмите кнопку начать", reply_markup=markup_0)

	global words
	count=0
	count_of_checking_words=0

	for words in dictionary_words:
		word_1=""
		word_2=""
		C=len(words)
		for i in range(0,C):
			letter=words[i]
			if letter.istitle()==True:
				word_1=word_1+".."
			else:
				word_1=word_1+letter

	bot.register_next_step_handler(message,test,words,word_1,word_2,count,count_of_checking_words,count_of_right_answers,count_of_answers)


"""Основной алгоритм теста"""
def test(message,words,word_1,word_2,count,count_of_checking_words,count_of_right_answers,count_of_answers):
	"""Функция выдачи рандомных индексов"""
	len_dictionary_words=len(dictionary_words)
	random_variable_for_index=random.randint(0,len_dictionary_words-1)
	count=random_variable_for_index

	words=dictionary_words[count]
	dictionary_words.pop(count)
	word_1=""
	word_2=""
	CON=len(words)
	for i in range(0,CON):
		letter=words[i]
		if letter.istitle()==True:
			word_1=word_1+".."
		else:
			word_1=word_1+letter

	markup = types.ReplyKeyboardMarkup()
	Button_1=types.KeyboardButton('О')
	Button_2=types.KeyboardButton('А')
	Button_3=types.KeyboardButton('Е')
	Button_4=types.KeyboardButton('И')
	Button_5=types.KeyboardButton('Ю')
	Button_6=types.KeyboardButton('У')
	Button_7=types.KeyboardButton('Ё')
	Button_8=types.KeyboardButton('Я')
	Button_9=types.KeyboardButton("СТОП")

	markup.row(Button_1,Button_3, Button_5, Button_7)
	markup.row(Button_2, Button_4, Button_6, Button_8)
	markup.row(Button_9)

	if len_dictionary_words==1:
		test_finish(message,count_of_right_answers,count_of_answers)
		return
	else:
		bot.send_message(message.from_user.id, word_1, reply_markup=markup)
		bot.register_next_step_handler(message,receiving_a_response,words,word_1,word_2,count,count_of_checking_words,count_of_right_answers,count_of_answers)



"""Функция завершения теста"""
def test_finish(message,count_of_right_answers,count_of_answers):
	markup_welcome = types.ReplyKeyboardMarkup()
	Button_welcome=types.KeyboardButton('/commands')

	markup_welcome.row(Button_welcome)
	variable_of_procent_of_right_answers=(count_of_right_answers/count_of_answers)*100//1
	bot.send_message(message.from_user.id, "Тест закончился")
	bot.send_message(message.from_user.id, "Всего правильных:")
	bot.send_message(message.from_user.id, f"{count_of_right_answers} из {count_of_answers} вопросов\n ({variable_of_procent_of_right_answers}% правильных)",reply_markup=markup_welcome)







"""Функция запуска бота и приветствие пользователя"""
@bot.message_handler(commands=["start"])
def welcome(message):
	markup_welcome = types.ReplyKeyboardMarkup()
	Button_welcome=types.KeyboardButton('/commands')

	markup_welcome.row(Button_welcome)

	stic = open('C:/Users/kmkar/CAKE_PROGRAMMER/python/Telegram bot/images/welcome.webp', 'rb')
	bot.send_sticker(message.from_user.id, stic,reply_markup=markup_welcome)
	bot.send_message(message.from_user.id, "Приветсвую!\n Я Duckbot - твой путеводитель в изучении русского языка\nЧтобы узнать мои команды введи:\n /commands".format(message.from_user.id, bot.get_me()), parse_mode="html")


"""Показывает все доступные команды"""
@bot.message_handler(commands=["commands"])
def commands(message):
	markup_commands = types.ReplyKeyboardMarkup()
	Button_commands=types.KeyboardButton('/test_Russia_language')

	markup_commands.row(Button_commands)

	bot.send_message(message.from_user.id, "Доступные команды:\n /test_Russia_language - запускает готовый тест по русскому языку",reply_markup=markup_commands)
	
	markup_commands = types.ReplyKeyboardMarkup()
	Button_commands=types.KeyboardButton('/test_Russia_language')

	markup_commands.row(Button_commands)


bot.polling(none_stop=True, interval=0)
