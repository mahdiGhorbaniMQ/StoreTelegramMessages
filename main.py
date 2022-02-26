from services.TelegramService import TelegramService
from services.DataBaseService import DataBaseService

api_id = 0000000
api_hash = 'api_hash'
phone = '+123456789'

db_connection_str = 'postgresql://username:password@localhost:5432/database-name'

db = DataBaseService(db_connection_str)
db.begin()
# db.get_all()

telegram = TelegramService(api_id, api_hash, phone, db)
telegram.begin()
