import os
import random
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

# Используем переменную окружения для токена
TOKEN_API = os.getenv("TOKEN_API")
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

ikb = InlineKeyboardMarkup(row_width=3)
ib1 = InlineKeyboardButton(text='🌏  inst  🌏',
                           url='https://www.instagram.com/')
ib2 = InlineKeyboardButton(text='🌏  vk  🌏',
                           url='https://m.vk.com/')
ib3 = InlineKeyboardButton(text='Леруси (vk)',
                           url='https://vk.com/wieerxxll')
ib4 = InlineKeyboardButton(text='Сашечки (vk)',
                           url='https://vk.com/sanqee')
ib5 = InlineKeyboardButton(text='Леруси (inst)',
                           url='https://www.instagram.com/valeria___wpwpqzzz')
ib6 = InlineKeyboardButton(text='Сашки (inst)',
                           url='https://www.instagram.com/sanqeq')
ikb.add(ib1, ib2).add(ib5, ib3).add(ib6, ib4)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb.add(KeyboardButton('приветики!'))
kb.insert(KeyboardButton('/help'))
kb.insert(KeyboardButton('люблю тебя'))
kb.add(KeyboardButton('❤️‍🔥'))
kb.insert(KeyboardButton('❤️‍🔥'))
kb.insert(KeyboardButton('❤️‍🔥'))
kb.add(KeyboardButton('прасти меня'))
kb.insert(KeyboardButton('стикеры'))
kb.insert(KeyboardButton('ссылочки'))
kb.add(KeyboardButton('Наши фоточки'))

kbp = ReplyKeyboardMarkup(resize_keyboard=True)
kb1 = KeyboardButton('Рандом')
kb2 = KeyboardButton('Главное меню')
kbp.add(kb1, kb2)

kbs = ReplyKeyboardMarkup(resize_keyboard=True)
ks1 = KeyboardButton('Рандомный стикер')
ks2 = KeyboardButton('Главное меню')
kbs.add(ks1, ks2)

help_com = '''
<b>/start</b> - <i>начало работы с лерочкой 😏</i>
<b>/help</b> - <i>список команд</i>
<b>приветики!</b> - <i>приветики, любимый!!!</i>
<b>люблю тебя</b> - <i>люблю тебя, сашулька!!!</i>
<b>прасти меня</b> - <i>када накасячили</i>
<b>стикеры</b> - <i>стикер красотке</i>
<b>Наши фоточки</b> - <i>наши классные фотачки</i>
<b>ссылочки</b> - <i>ссылачки на нас</i>'''

stickers = ['CAACAgIAAxkBAAEMef9mkFGyjxQ89lD1u_fKxZkEoOhTKgACfEcAAtWGYUj6wn-Pq9IZ_TUE',
            'CAACAgIAAxkBAAEMegFmkFG2oTUIt2d3hcfgqSrrZXtWOAACTRwAAqobYUsiwuQXCCxNUzUE',
            'CAACAgIAAxkBAAEMegNmkFG4R9-Hn2-yPlxkqiErnHAlHwACPRYAAvC4eEn_kTEuu-RcpTUE',
            'CAACAgQAAxkBAAEMegVmkFG71HTWxmhqMNcq0-i1qPKWDgACHQ4AAs_fKVFTzJID_-cAAYI1BA',
            'CAACAgIAAxkBAAEMegdmkFVkJKv-tTmQl5VwbF0gp1cF9AACDyoAAjLu0EsQ9mTvUtYZVTUE',
            'CAACAgIAAxkBAAEMeglmkFWHwyMKGJOQpZh44c0FfQKbgAACbBcAA76ZS3oEDWHeQnM-NQQ',
            'CAACAgIAAxkBAAEMegtmkFWy7QJ_te7XqF2M0xnGa8WOVwACBigAAo75-EoIsEvx04_XpzUE',
            'CAACAgIAAxkBAAEMeg1mkFXz7jE2b24d6qis_v6x5G9dQgACng4AAi9q4EkolEOQziPmFTUE',
            'CAACAgIAAxkBAAEMeg9mkFYMMB2AwFDe2OvTctxIh_FedQAC-hgAAlCx6Un0hgVIhUGOVjUE',
            'CAACAgIAAxkBAAEMehFmkFYRPSvdlKtMo3TjajEThZt_EwACvyMAAmyZMEgPBxQVKGpHTzUE',
            'CAACAgIAAxkBAAEMehNmkFYb4QKBTLnne-Y1PisKfYGP1gACdQEAAntOKhAvgHhHFVejfzUE',
            'CAACAgIAAxkBAAEMehVmkFZSyvkExPfE0a0jvQABvPMzL4EAApcAA2Kooyry5rUDWRhfzzUE',
            'CAACAgIAAxkBAAEMfm5mlE1HOxbQiHMtqpCEeOVRd0P4DQACwyoAAl9FUUi71E3UgtDaAjUE']

phot = ['https://i.pinimg.com/736x/e5/83/e9/e583e92f91478a94b65d9ccd42d09d17.jpg',
        'https://i.pinimg.com/736x/ee/cd/ce/eecdce01992471304d7ab46259fe91ad.jpg',
        'https://i.pinimg.com/736x/f7/0b/a8/f70ba89dea719eaafc4840172a44a9a2.jpg',
        'https://i.pinimg.com/736x/c8/a4/7a/c8a47a5f8aae89b2e030ff916be4273d.jpg',
        'https://i.pinimg.com/736x/7f/a3/8b/7fa38b65d2258eef944a4ffd07cd05e7.jpg',
        'https://i.pinimg.com/736x/aa/33/c9/aa33c92edb2c387a894daaef19cf952d.jpg',
        'https://i.pinimg.com/736x/5e/f3/05/5ef305c2c58e370f0b3de56f5da05e67.jpg',
        'https://i.pinimg.com/736x/47/16/d2/4716d2d1b5ac67c64e996d5904e7ed7a.jpg',
        'https://i.pinimg.com/736x/63/70/de/6370deddc25a990dfa73d6b7fa0e2604.jpg',
        'https://i.pinimg.com/736x/92/78/14/927814abc2d37d73a53912e4f2518d4a.jpg',
        'https://i.pinimg.com/originals/ba/f6/5e/baf65e26fc60e97b3fe6aa109603ed70.jpg',
        'https://i.pinimg.com/originals/ab/00/e0/ab00e00bdff495f539fccce6ac5057eb.jpg',
        'https://i.pinimg.com/originals/d6/73/23/d673234c6205947ac180b8553a44e4b1.jpg',
        'https://i.pinimg.com/originals/50/1f/65/501f657edd845423f187ab2ff9017431.jpg',
        'https://i.pinimg.com/originals/63/68/2e/63682e17379682a660925dfa59dff941.jpg',
        'https://i.pinimg.com/originals/4f/3f/f0/4f3ff0ecfaf1bf475eb6109687df2bd9.jpg',
        'https://i.pinimg.com/originals/84/05/5a/84055a47b97b560e1e508d38129303f5.jpg',
        'https://i.pinimg.com/originals/e5/60/0d/e5600d56f7251db8b4c8435c4704001b.jpg',
        'https://i.pinimg.com/originals/99/73/f0/9973f0d7d179a0c8f122e11346af2e08.jpg',
        'https://i.pinimg.com/originals/5d/01/d6/5d01d6dc6728a8e51f8b849d65975275.jpg',
        'https://i.pinimg.com/originals/7e/f7/74/7ef7747b1298b603c30ff21f26a243c2.jpg',
        'https://i.pinimg.com/originals/74/16/46/74164631af68109ce08f6d4dae3052c3.jpg',
        'https://i.pinimg.com/originals/2c/19/c4/2c19c49285e1ab765f9a447a3f0908ae.jpg',
        'https://i.pinimg.com/originals/cc/8b/98/cc8b9827bb5a2dff5695776a42d3ae86.jpg',
        'https://i.pinimg.com/originals/83/92/de/8392de0e120dba3dd84dd94997a4d8dd.jpg']

opis = ['ето мы с тобой такие футболисты крутецие😎😎😎😎',
        'ето я тебя целую а ты такая 😮😮😮😮😮',
        'ето я такой 🙄🙄🙄 а ты такая 😏😏😏',
        'ето ты собачка а я 😁😁😁😁',
        'ето мы с тобой такие милашки на аллее💘💘💘',
        'ето мы с тобой впервые едем на морько😎😎🤟🏻🤟🏻🤟🏻',
        'ето ты меня держишь силачка💪🏻💪🏻💪🏻',
        'ето мы с тобой сосём письки',
        'ето ты меня целуешь 😚😚 а я 😌😌😌 наслаждаюсь...',
        'ето мы с тобой счастливые песочек морько ты на меня залезла....🥹🥹🥹🥹',
        'ето мы с тобой розовые или фиолетовые 🩷💜🩷💜',
        'ето мы сидим на замочке и любимка меня цемает 😗😚😚',
        'а ето наше с тобой сокровище....💎💎💎',
        'ето ты мне подарила прикольную штучку и мы такие смешные в краске ❤️‍🔥❤️💖',
        'ето мы выбираем мне джинсы такие взрослые💗💗💋',
        'ето моя богиня заставила меня мыть посуду... моя любимка🥰😘😘',
        'ето мы с тобой в подвале самые счастливые🥺🥺😭',
        'ето наши браслетики🤩🤩🤩',
        'ето мы в подвальчике моя любимка наблюдает за мной❤️‍🔥❤️‍🔥❤️‍🔥',
        'ето мы у тебя лежим классные прикольные!! а она лицо закрывает...🤬🤬🤬🤬',
        'ето мы с тобой в касках в подвале работяги.... наша первая совместная фотка😁😁🥰',
        'ето мы с моей любимкой целуемся на великах на фоне заката....😍😍🔥🔥🔥',
        'ето я и моя пусичка катались на лисяпедах🚴🏻‍♀️🚴🏻🏆🥇🔥🔥',
        'ета мая девочка пожарила блинчик с сердечком!!! моя умничка!!!❤️❤️❤️❤️',
        'ета моё солнышко пожарила вот такого красивого котика!!!!🐈😻😻😻',
        'sdak']

photos = dict(zip(phot, opis))

@dp.message_handler(commands=['start'])
async def help_command(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text=help_com,
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text=help_com,
                           parse_mode='HTML',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(Text(equals='приветики!'))
async def he_command(message=types.Message):
    await message.reply(text='<b>Приветики, красотуля!</b>',
                        parse_mode='HTML',
                        reply_markup=kb)

@dp.message_handler(Text(equals='люблю тебя'))
async def love_command(message=types.Message):
    await message.reply(text='<b>я тоже тебя люблюююю!!!</b>',
                        parse_mode='HTML',
                        reply_markup=kb)

@dp.message_handler(Text(equals='прасти меня'))
async def pr_command(message=types.Message):
    await message.reply(text='<b>прости меня, моя зайка!🥹🥹🥹 я не хотел тебя обидеть, а когда мы ссоримся - помни, что я тебя очень сильно люблю и ценю, несмотря ни на что!💘💘💘💘 ты - самое ценное, что у меня есть, мое сокровище, мой билет в счастливую жизнь!!! я выиграл в лотерею и взял джек пот!💍💍💍💍💍💍 я обещаю, что буду любить тебя всю свою жизнь, давать всё, что только смогу, оберегать и ценить всю тебя!!!😘😘 каждый твой вгляд - это глоток жизни для меня!! я обожаю всё в тебе: твои шикарнейшие и глубокие глазки, твой аккуртненький маленький носик, твои самые сладкие на свете губки, твои милые щечки и прекрасные ушки!!! твоё тело и фигура это просто отпад!!!! ты у меня самая самая красивая моделька!!😍😍😍😍😍 ты очень-очень добрая и заботливая, я вижу, что ты готова ради меня на всё, и я тоже готов!!! не сомневайся!!🤬🤬🤬🤬🤬 ты очень многое сделала для меня, и ещё сделаешь я уверен!!!! скоро-скоро мы уедем куда-нибудь и отстроим наше гнёздышко, где мы будем выстраивать нашу совместную самую лучшую жизнь!!💞💞💞💞 у нас будет большой домище, во дворе будут расти цветочки, и по газончику будут бегать наши красивые детки!!! похожие на тебя, моё солнышко!!!!!🩷🩷🩷🩷🩷 а мы с тобой будем жарить шашлык и танцевать под музычку во дворе!!! это моя самая заветная мечта!!!!!!! и мы проживём самую счастливую жизнь!!!❤️‍🔥❤️‍🔥❤️‍🔥❤️‍🔥 это точно!!!! люблю тебя и целую, обнимаю крепка крепка, моё золотце!!!</b>',
                        parse_mode='HTML',
                        reply_markup=kb)

@dp.message_handler(Text(equals='стикеры'))
async def send_stiker(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text='<b>Здесь самые лучшие стикеры сашечки и лерочки😍😍😍</b>',
                           reply_markup=kbs,
                           parse_mode='HTML')

@dp.message_handler(Text(equals='Рандомный стикер'))
async def stik_command(message=types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker=random.choice(stickers))
    await message.delete()

@dp.message_handler(Text(equals='Наши фоточки'))
async def photo_command(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text='Здесь наши самые лучшие фоточки!!!',
                           reply_markup=kbp)

@dp.message_handler(Text(equals='Рандом'))
async def ph_send(message=types.Message):
    ikb1 = InlineKeyboardMarkup(row_width=3)
    ib1_1 = InlineKeyboardButton(text='❤️‍🔥',
                                 callback_data="like")
    ib1_2 = InlineKeyboardButton(text='💩',
                                 callback_data="dislike")
    ib1_3 = InlineKeyboardButton(text='✖️закрыть фотографию✖️',
                                 callback_data="✖️закрыть фотографию✖️")
    ikb1.add(ib1_1, ib1_2).add(ib1_3)
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         parse_mode='HTML',
                         reply_markup=ikb1)
    await message.delete()

@dp.message_handler(Text(equals='Главное меню'))
async def gl_men(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text='<b>Ты в главном меню</b>😍😍😍',
                           reply_markup=kb,
                           parse_mode='HTML')

@dp.callback_query_handler(text="✖️закрыть фотографию✖️")
async def cl_callback(callback: types.CallbackQuery):
    await callback.message.delete()

@dp.callback_query_handler()
async def photo_callback(callback: types.CallbackQuery):
    if callback.data == "like":
        await callback.answer(show_alert=True,
                              text='😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍ДААА!! МНЕ ТОЖЕ НРАВИТСЯ😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍😍')
    await callback.answer(show_alert=True,
                          text='ЛУЧШЕ ПЕРЕГОЛОСУЙ, А ТО ПРИДУШУ!!!🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬🤬')

@dp.message_handler(Text(equals='ссылочки'))
async def photo_command(message=types.Message):
    await bot.send_message(message.from_user.id,
                           text='<b>вот ссылочки на нас любимых:</b>',
                           parse_mode='HTML',
                           reply_markup=ikb)
    await message.delete()

@dp.message_handler(text='❤️‍🔥')
async def kb_stik(message=types.Message):
    await message.reply(text='<b>ето для красоты!!!</b>', parse_mode='HTML')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)