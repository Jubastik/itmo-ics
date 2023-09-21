from asyncio import sleep


async def del_message_by(message, seconds):
    await sleep(seconds)
    await message.delete()
