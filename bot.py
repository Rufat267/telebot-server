from aiogram import types,Bot,Dispatcher,executor

import qrcode

Bot = Bot("7970851723:AAFMOLB1smzWNR75MJYXCAjbVo9U7ZGYGaY")
dp = Dispatcher(Bot)

@dp.message_handler()
async def send_qrcode(sms:types.Message):
    img = qrcode.make(sms.text)
    img.save('some_file.png')
    with open('some_file.png','rb') as image:
        await sms.answer_photo(caption='qr code',photo=types.InputFile(image))
# @dp.callback_query_handler()
# async def send_whatever(call:types.CallbackQuery):
#     user_id = call.from_user.id
#     data = call.data
#     image = open("some_file.png")
#     if data=='qrcode':
#         await (
#             chat_id=user_id,
#             text='Bizde tomendegi qrcode  turleri bar:',
#             reply_markup=qrcode 
#         )
if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)