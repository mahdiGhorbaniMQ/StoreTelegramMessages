from telethon.tl.types import Channel
from telethon import utils
from sqlalchemy import *

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sender_first_name = Column(String)
    sender_last_name = Column(String)
    sender_username = Column(String)
    chat_title = Column(String)
    file_name = Column(String)
    message = Column(String)
    date = Column(String)

    async def parse(self, event, client):
        self.message = str(event.message.message)
        self.date = str(event.date)
        sender = await event.get_sender()
        self.sender_username = str(sender.username)
        if type(sender) is not Channel:
            self.sender_first_name = str(sender.first_name)
            self.sender_last_name = str(sender.last_name)

        chat_from = event.chat if event.chat else (await event.get_chat())
        chat_title = utils.get_display_name(chat_from)
        self.chat_title = str(chat_title)

        if event.message.media is not None:
            self.file_name = await client.download_media(event.message)

    def __repr__(self):
        return "sender_first_name: '%s' \n" \
               "sender_last_name: '%s' \n" \
               "sender_username: '%s' \n" \
               "chat_title: '%s' \n" \
               "message_content: '%s' \n" \
               "date: '%s' \n" \
               "file_name: '%s'" % (self.sender_first_name,
                                    self.sender_last_name,
                                    self.sender_username,
                                    self.chat_title,
                                    self.message,
                                    self.date,
                                    self.file_name)
