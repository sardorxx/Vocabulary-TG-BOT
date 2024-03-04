from datetime import datetime
from random import randrange

from aiogram import Router, types, F
from aiogram.filters import CommandStart

from database import Session, Vocabulary, User

session = Session()

router = Router()


def get_words():
    an = []
    while True:
        res = randrange(1, 3057)
        words = session.query(Vocabulary).filter(Vocabulary.v_id == res).all()
        print(words)
        word = str(words[0]).split(' ', 1)[1]
        an.append(f"{word}")
        if len(an) == 30:
            www = "✅✅✅✅✅✅✅✅✅✅✅✅✅✅✅\n"
            for i in an:
                www = www + i
            return www


@router.message(CommandStart())
async def start_handler(message: types.Message, bot):
    user = 0
    result = session.query(User).filter(User.user_id == message.from_user.id).all()
    if result:
        user = int(str(result[0]).split(' ')[0])

    if message.from_user.id != user:
        user = User(user_id=message.from_user.id, username=message.from_user.username, day_word=False, day="no")
        session.add(user)
        session.commit()
        await bot.send_message(text=f"Welcome {message.from_user.username}🎉", chat_id=message.chat.id)
        await bot.send_message(text=f"Learn english and russian vocabulary with Daily Vocabulary🤗",
                               chat_id=message.chat.id)

    else:
        await bot.send_message(text=f"Hello {message.from_user.username}", chat_id=message.chat.id)
        await bot.send_message(text=f"Learn english and russian vocabulary with Daily Vocabulary🤗",
                               chat_id=message.chat.id)


@router.message(F.text == '/vocabulary')
async def word_handler(message: types.Message, bot):
    user = 0
    day = ""
    today = ""
    result = session.query(User).filter(User.user_id == message.from_user.id).all()
    if result:
        user = int(str(result[0]).split(' ')[0])
        day = str(datetime.now().date())
        today = str(str(result[0]).split(' ')[3])

    if message.from_user.id == user and day != today:
        await bot.send_message(text=f"{get_words()}", chat_id=message.chat.id)
        (session.query(User).filter(User.user_id == message.from_user.id).update
         ({'day': day}))
        session.commit()
        await bot.send_message(text="Here is your vocabulary for this day👌", chat_id=message.chat.id)
    else:
        await bot.send_message(text=f"Today you have got daily Words already", chat_id=message.chat.id)


@router.message(F.text == '/add')
async def word_handler(message: types.Message, bot):
    if message.from_user.id == "2134194986+":
        with open('clean_data1.txt', 'r') as f:
            for j, line in enumerate(f):
                word = Vocabulary(v_id=j + 1, name=line)
                session.add(word)
                session.commit()
        await bot.send_message(text=f"Your vocabulary added successfully", chat_id=message.chat.id)
    else:
        await bot.send_message(text="This function not work for you", chat_id=message.chat.id)


@router.message(F.text)
async def word_handler(message: types.Message, bot):
    await bot.send_message(text=f"""I can not understand the message🙁!!!""", chat_id=message.chat.id)
