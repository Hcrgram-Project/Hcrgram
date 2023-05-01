# Mozgoeb
'''
.zaeb:: Делает упоминания человека в чате. \n\n<b>Использование</b>: \n<code>.zaeb</code> кол-во раз \n Если не указать, то упомянет 50 раз
'''
from asyncio import sleep
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.zaeb", outgoing=True))
	async def _(event):
		reply = await event.get_reply_message()
		if not reply:
			await event.edit("<b>Использовать в ответ на сообщение!</b>", parse_mode='html')
			return
		id = reply.from_id
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		args = txt1.split(' ')
		count = 50
		if args:
			if args[-1].isdigit():
				if int(args[-1]) < 0:
					count = 50
				else:
					count = int(args[-1])
		txt = f'<a href="tg://user?id={id}">Ебем мозги)</a>'
		await event.delete()
		for _ in range(count):
			await sleep(0.3)
			msg = await event.client.send_message(event.to_id, txt, parse_mode='html')
			await sleep(0.3)
			await msg.delete()

	

if __name__ == '__main__':
	try:
		a(client)
	except:
		pass