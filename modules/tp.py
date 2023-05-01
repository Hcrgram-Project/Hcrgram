# Type2
'''
.tp:: Анимация для текста. \n\n<b>Использование:</b> \n<code>.tp</code> ваштекст
'''

from telethon import events
import asyncio

def a(client):
    @client.on(events.NewMessage(pattern=r"\.tp (.*)", outgoing=True))
    async def _(event):
        if event.fwd_from:
            return
        input_str = event.pattern_match.group(1)
        typing_symbol = "<"
        DELAY_BETWEEN_EDITS = 0.1
        previous_text = ""
        await event.edit(typing_symbol)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        for character in input_str:
            previous_text = previous_text + "" + character
            typing_text = previous_text + "" + typing_symbol
            await event.edit(f'<b>{typing_text}</b>', parse_mode='html')
            await asyncio.sleep(DELAY_BETWEEN_EDITS)

if __name__ == '__main__':
    try:
        a(client)
    except:
        pass