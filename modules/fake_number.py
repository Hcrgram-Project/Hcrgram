# Фейк
'''
.fake:: Фейк контакт. \n Использование: <code>.fake</code> <имя> <номер без +>
'''
from telethon import events
import asyncio
from telethon import types

def a(client):

	@client.on(events.NewMessage(pattern=r"\.fake", outgoing=True))
	async def _(event):
		args =	event.text.split(' ')
		if len(args)<3 or not args[-1].isdigit():
			await event.edit('<b>❌ Использовать с именем и номером! Пример:</b>\n<code>.fake Иванов Иван 7999999999</code>', parse_mode='html')
			return
		else:
			phone = args[-1]
			name = ' '.join(args[1: -1])
			await event.delete()

			await client.send_file(event.chat.id, types.InputMediaContact(
				phone_number=phone,
				first_name=name,
				last_name='',
				vcard=''
			))



if __name__ == '__main__':
	try:
		a(client)
	except:
		pass