# Mediaspam
'''
.mediaspam:: Спамит любым видом медиа. \nИспользование <code>.mediaspam </code> <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс) 
'''
from asyncio import sleep
from telethon import events
import asyncio


def a(client):
	@client.on(events.NewMessage(pattern=r"\.mediaspam", outgoing=True))
	async def online(event):
		try:
			txt1 = event.message.message
		except:
			txt1 = event.original_update.message.message
		paytext=''.join(txt1.split(' ')[1:])
		message = event

		reply = await message.get_reply_message()
		if not reply:
			await message.edit("Ошибка!\n <code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>", parse_mode='html')
			return
		if not reply.media:
			await message.edit("Ошибка!\n <code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>", parse_mode='html')
			return
		media = reply.media
	
		# args = utils.get_args(message)
		args = paytext
		if not args:
			await message.edit("Ошибка!\n <code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>", parse_mode='html')
			return
		count = paytext
		if not count.isdigit():
			await message.edit("Ошибка!\n <code>.mediaspam <количество> + реплай на медиа(стикер/гиф/фото/видео/войс/видеовойс</code>", parse_mode='html')
			return
		count = int(count)
		
		await message.delete()
		for _ in range(count):
			await message.client.send_file(message.to_id, media)



if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
