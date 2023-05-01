# Снос
'''
.report:: Массовые жалобы\n\n<b>Использование</b>: \n<code>.report</code><кол-во раз> <Комментарий к жалобе>(по желанию)
'''
import asyncio
from telethon import events
from asyncio import sleep
import random
from telethon import events, types, functions, errors, TelegramClient


reasons = [
types.InputReportReasonChildAbuse(),
types.InputReportReasonCopyright(),
types.InputReportReasonFake(),
types.InputReportReasonPornography(),
types.InputReportReasonSpam(),
types.InputReportReasonViolence(),
types.InputReportReasonOther()]



def a(client):
	@client.on(events.NewMessage(pattern=r"\.report", outgoing=True))
	async def _(event):
		args = str(event.message.text).split(' ')
		if len(args) < 2:
			times = 1
		else: 
			if args[1].isdigit():
				times=int(args[1])


		if len(args) < 3:

			comment = 'Delete chat!'
		else:
			comment = ' '.join(args[2:])
		for i in range(times):
			for reason in reasons:
			
				result = await client(
					functions.account.ReportPeerRequest(
						peer=event.peer_id,
						reason=reason,
						message=comment
					)
				)
				try:
					reason_text = str(reason).replace('InputReportReason','').replace('()','')
					await event.edit(f'Жалоба {reason_text} отправлена!')
				except Exception as e:
					print(e)

		await event.edit(f'<b>Жалобы ({int(times)*7}) успешно отправлены!</b>',parse_mode='html')


		
		
 


if __name__ == '__main__':
	try:
		a(client)
	except:
		pass
