# Line
'''
.line:: Анимация для текста. \n Использование: <code>.line</code> ваштекст
'''
from telethon import events
import asyncio
from collections import deque

def a(client):

	@client.on(events.NewMessage(pattern=r"\.line", outgoing=True))
	async def _(event):
		if event.fwd_from:
			return
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message


		text = ' '.join(str(txt1).split(' ')[1:])
		deq = deque(list(text))
		for _ in range(len(deq)+1):
			await asyncio.sleep(0.1)
			try:
				await event.edit(f'''{"".join(deq)}''')
			except:
				pass
			deq.rotate(1)


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass