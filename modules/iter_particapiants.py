# Parsing
'''
.iter:: Парсинг учасников чата \n\n<b>Использование</b>: \n<code>.iter</code> <i>-n</i>\n Используя аргумент -n будут получены только учасники с открытыми номерами
'''
from asyncio import sleep
from telethon import events
import os


def a(client):
	@client.on(events.NewMessage(pattern=r"\.iter", outgoing=True))
	async def _(event):
		args = event.text.split(' ')
		# if len(args)>2:

		await event.delete()
		chat = await event.get_chat()
		
		users = client.iter_participants(chat.id)
		# print(users)
		a = open(f'{event.chat.id}_result.txt', 'a', encoding='utf-8')
		async for i in users:
			num = False

			if args[-1] == "-n":
				num = True

			if num and i.phone or not num:
				try:
					a.write(f'{str(i.id)}; {str(i.first_name)}; {str(i.last_name)}; {str(i.username)}; {str(i.phone)}\n')
				except:
					pass
		
		a.close()
		try:
			await client.send_file("me", f'{event.chat.id}_result.txt', caption=f"Дамп чата ({str(event.chat.title)})      {str(event.chat.id)}")
			os.remove(f'{event.chat.id}_result.txt')
		except:
			pass




	

if __name__ == '__main__':
	try:
		a(client)
	except:
		pass