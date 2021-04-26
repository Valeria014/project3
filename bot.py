from telegram.ext import *
from telegram import *
from datetime import timedelta, datetime
import re


def sleep(update, context):
    try:
        moment = []
        momentime = []
        list = update.message.text
        time_in = re.split(r'[: ]+', list)
        hour = int(time_in[1])
        minut = int(time_in[2])
        print(hour)
        if hour > 24 or minut > 60:
            update.message.reply_text('Ошибка, время введено некорректно')
        else:
            time = timedelta(hours=hour, minutes=minut)
            interval = time - timedelta(hours=1, minutes=30)
            moment.append(str(interval).replace("-1 day,", " "))
            for i in range(5):
                interval = interval - timedelta(hours=1, minutes=30)
                moment.append(str(interval).replace("-1 day,", " "))
            momentime.append("; ".join(moment))
            update.message.reply_text(momentime)
            update.message.reply_text(
        '*обратите внимание: результат рассчитан без учета времени на засыпание. Отнимите еще 10-20 минут,'
        ' в течение которых вы засыпаете.')

    except:
        update.message.reply_text('Произошла ошибка.')


def start(update, context):
    update.message.reply_text(
        'Приветсвую, я бот, который поможет вам определиться с временем, в которое лучше проснуться ')
    update.message.reply_text(
        'Введете время, в которое хотите проснуться. Перед временем напишите "/sleep", например "/sleep 7:00".')



def creator(update, bot):
    update.message.reply_text(
        'Бот создан как проект для яндекс лицея ')
    update.message.reply_text(
        'О создателе: '
        'Меня зовут Валерия. '
        'Приятно познакомиться. Рекламная интеграция: '
        'Моя группа в вк: https://vk.com/babyeel слушайте и наслаждайтесь песнями. '
        'Вк: https://vk.com/babyel1 '
        'Тикток: https://vm.tiktok.com/ZSJBuT2ad/ 😈')
    #тут должен быть вывод моей фотографии )))
    #update.bot.send_photo(chat_id=bot.message.chat.id, photo=open('https://ic.wampi.ru/2021/04/24/creator.png', 'rb'))


def aboutthebot(update, bot):
    update.message.reply_text(
        'Когда человек засыпает, он проходит несколько циклов из '
        'чередующихся медленной и быстрой фаз сна. Если вы проснетесь в период '
        'медленной фазы, то будете ощущать тяжесть, разбитость и усталость. '
        'Вам будет сложнее пробудиться и встать с кровати, чего не произойдет, '
        'если проснуться в конце быстрой фазы. Вот почему так важно '
        'соблюдать режим сна.')
    update.message.reply_text(
        'В калькуляторе сна онлайн учитывается продолжительность циклов, '
        'которые длятся в среднем 90 минут. Вам необходимо указать время, '
        'когда вы планируете лечь спать, затем калькулятор обозначит благоприятное время, '
        'когда лучше подняться утром, чтобы чувствовать себя полноценно '
        'отдохнувшим. Бот также напоминает о времени на засыпание, ')


def main():
    updater = Updater('1702435770:AAEZbU9fC074ZaGrelsMMWQrg6Hbgy1En_M', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("sleep", sleep))
    dp.add_handler(CommandHandler("creator", creator))
    dp.add_handler(CommandHandler("aboutthebot", aboutthebot))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()