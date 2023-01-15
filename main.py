import aiocron
from pyrogram import Client

print('start . . .')


app = Client(
    name='pyrogram',
    api_id=0,            # CHANGE API_ID 
    api_hash='api_id',   # CHANGE API_HASH
    bot_token='TOKEN'    # CHANGE BOT TOKEN
)

USER = 0 # USER ID , @userinfobot GET USER ID
FILE = '/etc/x-ui/x-ui.db'

@aiocron.crontab('*/8 * * *')
async def sendfile():
    await app.send_document(USER,FILE)


if __name__ == '__main__':
    sendfile.start()
    sendfile.stop()
    
    
    
    
    
app.run()
