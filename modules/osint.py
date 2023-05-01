# Osint
'''
.phone</code> <code>.id</code> <code>.ip</code>:: Пробив по osint ботам. \n\n<b>Использование</b>: \n<code>.phone</code> <i>Поиск по телефону</i>\n<code>.id</code> <i>id телеграм пользователя</i>\n<code>.ip</code> <i>ipaddress</i>
'''

from telethon import events
import asyncio
import re
import os
import requests, json


def get_tuples_until_myid(lst):
    new_lst = []
    for tpl in lst:
        if tpl[0] == 5:
            break
        new_lst.append(tpl)
    return new_lst

def a(client):
	@client.on(events.NewMessage(pattern=r"\.id", outgoing=True))
	async def _(event):

		args = event.text.split(' ')
		print(args)
		if len(args) <2 or not args[-1].isdigit():
			await event.edit('<b>❌ Использовать с ID! Пример:</b>\n<code>.id 1234567</code>', parse_mode='html')
			return
		elif "+" in args[-1]:
			await event.edit('<b>❌ Для поиска по номеру используйте команду</b><code>.phone</code> <i>номер</i>')
		else:
			id_to_search = args[-1]

		async def search_quickosint(id_to_search):
			await client.send_message('https://t.me/Hcrgram_osint_bot','/start')
			await client.send_message('https://t.me/Hcrgram_osint_bot',f'#id{id_to_search}')
			await asyncio.sleep(3)
			message_from_bot = [i.text async for i in client.iter_messages('https://t.me/Hcrgram_osint_bot', limit=1)][0]
			pat = r'\n-----'#r'(.|\n)+(?=-----)'
			a = re.split(pat, message_from_bot)
			message_from_bot = a[0]

			return message_from_bot

		async def search_gta(id_to_search):
			await client.send_message('https://t.me/Hcrgram_osint_2_bot','/start')
			await asyncio.sleep(1)
			await client.send_message('https://t.me/Hcrgram_osint_2_bot',f'{id_to_search}')
			await asyncio.sleep(1)
			message_from_bot = [i async for i in client.iter_messages('https://t.me/Hcrgram_osint_2_bot', limit=1)][0]
			await asyncio.sleep(0.5)
			await message_from_bot.click(0)

			await asyncio.sleep(3)
			message_from_bot = [i.text async for i in client.iter_messages('https://t.me/Hcrgram_osint_2_bot', limit=1)][0]
			if 'Как увеличить лимит?' in message_from_bot:
				return 'Лимиты в боте закончились'
			return message_from_bot

		async def search_telescan(id_to_search):
			await client.send_message('https://t.me/Hcrgram_osint_3_bot','/start')
			await asyncio.sleep(3)
			await client.send_message('https://t.me/Hcrgram_osint_3_bot',f'{id_to_search}')
			await asyncio.sleep(3)
			message_from_bot = []
			async for i in client.iter_messages('https://t.me/Hcrgram_osint_3_bot', limit=3):
				if not 'Я не нашёл' in i.text and not 'запросов' in i.text and not 'запрещён' in i.text and not id_to_search == i.text:
					message_from_bot.append(i.text)
					print(i.text)
				else:

					message_from_bot.append("Не найдено информации")

			print(message_from_bot)

			# message_from_bot = [i.text if not i.text in ['Я не нашёл','запросов','запрещён','Запускаю','Количество'] else None async for i in client.iter_messages('https://t.me/Hcrgram_osint_3_bot', limit=2)][0]
			return max(message_from_bot).replace('__','').replace('**','')

		async def search_insight(id_to_search):
			myid = (await client.get_me()).id
			bot = 'https://t.me/ibhldr_bot'
			await client.send_message(bot,'/start')
			await asyncio.sleep(3)
			await client.send_message(bot,f'{id_to_search}')
			await asyncio.sleep(5)
			messages1 = []
			async for i in client.iter_messages(bot, limit=10):
				try: 
					i.from_id.user_id
					break
				except:
					d = i.text.replace('__','').replace('**','')
					forb_phrases = [
						'Моя база',
						'Данные обновлены.',
						'❌',
						'unamer_bot',
						'Подсказка'
					]

					if not d in forb_phrases:
						messages1.append(d)

			return reversed(messages1)


		await event.edit('🔲🔲🔲🔲\n<b>Прогресс: 0%</b>', parse_mode='html')
		qos = await search_quickosint(id_to_search)
		qos = qos.replace('__','').replace('**','').replace('`','')
		await event.edit('⬛️🔲🔲🔲\n<b>Прогресс: 25%</b>', parse_mode='html')
		gta = await search_gta(id_to_search)
		gta = gta.replace('__','').replace('**','').replace('`','')
		await event.edit('⬛️⬛️🔲🔲\n<b>Прогресс: 50%</b>', parse_mode='html')
		telescan = await search_telescan(id_to_search)
		await event.edit('⬛️⬛️⬛️🔲\n<b>Прогресс: 75%</b>', parse_mode='html')
		insight = await search_insight(id_to_search)
		await event.edit('🟩🟩🟩🟩\n<b>Прогресс: 100%</b>', parse_mode='html')
		await asyncio.sleep(0.6)
		await event.edit('⬇️\n<b>Отправка файла...</b>⬇️', parse_mode='html')

		if f'{id_to_search}.txt' in os.listdir('deanons'):
			os.remove(f'deanons/{id_to_search}.txt')

		with open(f'deanons/{id_to_search}.txt', 'a+', encoding='utf-8') as file:
			file.write(f'QUICK OSINT: ------------------')
			file.write(f'\n{qos}')
			file.write(f'\n\n\nGTA SEARCH: ------------------')
			file.write(f'\n{gta}')
			file.write(f'\n\n\nTELESCAN: ------------------')
			file.write(f'\n{telescan}')
			file.write(f'\n\n\nINSIGHT: ------------------')
			sss = '\n'.join(insight)
			file.write(f"\n{sss}")

		await event.delete()

		

		await client.send_file(
			event.chat.id,
			file=f'deanons/{id_to_search}.txt', 
			caption=f'<b>Результаты поиска в Osint ботах по ID: </b><code>{id_to_search}</code>', 
			parse_mode='html'
		)

	@client.on(events.NewMessage(pattern=r"\.phone", outgoing=True))
	async def _(event):

		args = event.text.split(' ')
		print(args)
		if len(args) <2 or not args[-1].replace('+','').isdigit():
			await event.edit('<b>❌ Использовать с номером! Пример:</b>\n<code>.phone +1234567</code>', parse_mode='html')
			return
		else:
			id_to_search = args[-1].replace('+','')

		async def search_quickosint(id):
			await client.send_message('https://t.me/Hcrgram_osint_bot','/start')
			await client.send_message('https://t.me/Hcrgram_osint_bot',f'+{id_to_search}')
			await asyncio.sleep(3)
			message_from_bot = [i.text async for i in client.iter_messages('https://t.me/Hcrgram_osint_bot', limit=1)][0]
			pat = r'\n-----'
			a = re.split(pat, message_from_bot)
			message_from_bot = a[0]

			return message_from_bot

		async def search_gta(id):
			await client.send_message('https://t.me/Hcrgram_osint_2_bot','/start')
			await asyncio.sleep(1)
			await client.send_message('https://t.me/Hcrgram_osint_2_bot',f'+{id_to_search}')

			await asyncio.sleep(3)
			message_from_bot = [i.text async for i in client.iter_messages('https://t.me/Hcrgram_osint_2_bot', limit=1)][0]
			if 'Как увеличить лимит?' in message_from_bot:
				return 'Лимиты в боте закончились'
			return message_from_bot



		await event.edit('🔲🔲🔲🔲\n<b>Прогресс: 0%</b>', parse_mode='html')
		qos = await search_quickosint(id_to_search)
		qos = qos.replace('__','').replace('**','').replace('`','')
		await event.edit('⬛️🔲🔲🔲\n<b>Прогресс: 25%</b>', parse_mode='html')
		gta = await search_gta(id_to_search)
		await event.edit('🟩🟩🟩🟩\n<b>Прогресс: 100%</b>', parse_mode='html')
		await asyncio.sleep(0.6)
		await event.edit('⬇️\n<b>Отправка файла...</b>⬇️', parse_mode='html')

		if f'{id_to_search}.txt' in os.listdir('deanons'):
			os.remove(f'deanons/id_{id_to_search}.txt')

		with open(f'deanons/{id_to_search}.txt', 'a+', encoding='utf-8') as file:
			file.write(f'QUICK OSINT: ------------------')
			file.write(f'\n{qos}')
			file.write(f'\n\n\nGTA SEARCH: ------------------')
			file.write(f'\n{gta}')

		await event.delete()

		

		await client.send_file(
			event.chat.id,
			file=f'deanons/{id_to_search}.txt', 
			caption=f'<b>Результаты поиска в Osint ботах по номеру: </b><code>{id_to_search}</code>', 
			parse_mode='html'
		)


	@client.on(events.NewMessage(pattern=r"\.ip", outgoing=True))
	async def _(event):

		args = event.text.split(' ')
		print(args)
		if len(args) <2:
			await event.edit('<b>❌ Использовать с IP! \nПример:</b>\n<code>.ip 123.456.789.021</code>', parse_mode='html')
			return
		else:
			ip = args[-1]

		data = requests.get(f"http://ip-api.com/json/{ip}").json()

		await event.edit(
			f"<b><u>⚡️ Цель:</u></b> <code>{ip}</code>"
			f"\n\n<b>🗄 Провайдер (ISP):</b> <code>{data['isp']}</code>"
			f"\n<b>👥 Организация:</b> <code>{data['org']}</code>"
			f"\n<b>🏴 Страна:</b> <code>{data['country']}</code>"
			f"\n<b>🌇 Город:</b> <code>{data['city']}</code>"
			f"\n<b>📌 Регион:</b> <code>{data['region']}</code>"
			f"\n<b>📍 Широта:</b> <code>{data['lat']}</code>"
			f"\n<b>📍 Долгота:</b> <code>{data['lon']}</code>"
			f'''\n\n<b>🗺 Карты:</b> <a href="https://www.google.com/maps/place/{data['lat']}+{data['lon']}">ссылка</a>''',
			parse_mode='html')




		


if __name__ == '__main__':
	try:
		a(client)
	except Exception as e:
		print(e)
		pass
