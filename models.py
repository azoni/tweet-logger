from sqlalchemy import Column, Integer, String, Text, DateTime # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from datetime import datetime

Base = declarative_base()

class ChatLog(Base):
  __tablename__ = 'chat_logs'
  id = Column(Integer, primary_key=True)
  user_message = Column(Text)
  assistant_reply = Column(Text)
  timestamp = Column(DateTime, default=datetime.utcnow)

