# Tagall
"""
.tagall:: Тегает всех учасников чата \n\n<b>Использование:</b> \n<code>.tagall</code> кол-во упомянутых учасников в одном сообщении
"""
from telethon import events


def a(client):
	@client.on(events.NewMessage(pattern=r"\.tagall", outgoing=True))
	async def tagallcmd(event):
		global args
		args = ''
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		if len(txt1.split(' ')) != 1:
			args = txt1.split(' ')[1]
		global tag_
		tag_ = 5
		notext = False
		if args:
			if args.isdigit():
				tag_ = int(args)

				
		await event.delete()
		chat = await event.get_chat()
		all = client.iter_participants(chat.id)
		chunk = []
		def chunks(lst, n):
			for i in range(0, len(lst), n):
				yield lst[i:i + n]

		notifies = []
		async for user in all:
			notifies.append("<a href=\"tg://user?id="+ str(user.id) +"\">\u206c\u206f</a>")
		chunkss = list(chunks(notifies, tag_))
		await event.delete()
		for chunk in chunkss:
			await client.send_message(chat.id, '\u206c\u206f'.join(chunk), parse_mode='html')


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass