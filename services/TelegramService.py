from telethon.sync import TelegramClient, events
from .DataBaseService import DataBaseService
from model.Message import Message


class TelegramService(object):
    api_id: str
    api_hash: str
    phone: str
    client: TelegramClient
    db: DataBaseService

    def __init__(self, api_id, api_hash, phone, db):
        self.api_id = api_id
        self.api_hash = api_hash
        self.phone = phone
        self.client = TelegramClient('session', api_id, api_hash)
        self.db = db

    def begin(self):
        self.connect()
        self.on_message()
        self.start()

    def connect(self):
        self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.phone)
            self.client.sign_in(self.phone, input('Enter the code: '))

    def start(self):
        self.client.start()
        self.client.run_until_disconnected()

    def on_message(self):
        @self.client.on(events.NewMessage())
        async def store(event):
            message = Message()
            await message.parse(event, self.client)
            print(message.__repr__())
            print("__________________________________________")
            await self.db.store_message(message)
            # if message.file_name is not None:
            #     self.db.store_file(message.file_name)





