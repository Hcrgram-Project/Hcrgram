# Sms
'''
.sms:: Отправка сообщения по тайм ауту. \n\n<b>Использование:</b> \n<code>.sms</code> <время в секундах> <сообщение>
'''


import asyncio
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.sms", outgoing=True))
	async def _(event):
		try:
			try:
				txt1 = event.message.message
			except:
				txt1 = event.original_update.message.message

			time = int(txt1.split(' ')[1])
			spam_message = ' '.join(txt1.split(' ')[2:])
			if spam_message or time:
				await event.delete()
				await asyncio.sleep(time)
				await event.respond(spam_message)
			else:
				await event.edit('<b>Использование:</b> \n<code>.sms</code> <время в секундах> <сообщение>',parse_mode='html')
		except Exception as e:
			try:
				await event.edit('<b>Использование:</b> \n<code>.sms</code> <время в секундах> <сообщение>',parse_mode='html')
			except:
				pass
			print(e)

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass