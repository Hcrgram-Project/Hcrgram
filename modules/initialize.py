# Init
'''
.init:: Инициализировать юзербота \n\n<b>Использование</b>: <code>.init</code> <i>Конфигурация юзербота. Инициализация ботов</i>
'''

from telethon import events
import asyncio
from telethon.tl.functions.channels import JoinChannelRequest

def a(client):
	@client.on(events.NewMessage(pattern=r"\.init", outgoing=True))
	async def _(event):
		await event.edit('Инициализация...')
		chats = ['https://t.me/TeleScanOfficial', 'https://t.me/gta_search']
		bots = ['https://t.me/Hcrgram_osint_bot','https://t.me/Hcrgram_osint_2_bot','https://t.me/Hcrgram_osint_3_bot','https://t.me/ibhldr_bot']

		for link in chats:
			await client(JoinChannelRequest(link))
			chat = await client.get_entity(link)
			await asyncio.sleep(0.1)
			await client.edit_folder(chat, 1)

		for bot in bots:
			await client.send_message(bot,'/start')
			chat = await client.get_entity(bot)
			await asyncio.sleep(0.1)
			await client.edit_folder(chat, 1)
			await client.edit_folder(chat, 1)

		chat = await client.get_entity('https://t.me/gta_search_bot')
		await asyncio.sleep(0.1)
		await client.edit_folder(chat, 1)


		await event.edit('✅ Инициализация прошла успешно! \nНе удаляйте чатов в архиве!')



		


if __name__ == '__main__':
	try:
		a(client)
	except Exception as error:
		print(error)
