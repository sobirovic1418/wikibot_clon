import logging

import wikipedia

from head import dp,types,executor
import wikitest


@dp.message_handler(commands=["start","help"])
async def begib(message:types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\nwiki botimizga xush kelibsiz!!!")

@dp.message_handler()
async def sendWiki(message:types.Message):
    try:
        respond=wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu haqida ma'lumot topilmadi")



if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)