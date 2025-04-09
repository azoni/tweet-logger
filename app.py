from flask import Flask, request, jsonify # type: ignore
from sqlalchemy import create_engine # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from models import Base, ChatLog
from config import DATABASE_URL

app = Flask(__name__)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

@app.route('/log', methods=['POST'])
def log_conversation():
    data = request.json
    user_message = data.get("user_message")
    assistant_reply = data.get("assistant_reply")

    session = Session()
    entry = ChatLog(user_message=user_message, assistant_reply=assistant_reply)
    session.add(entry)
    session.commit()
    session.close()

    return jsonify({"message": "Logged successfully."})

if __name__ == '__main__':
    app.run(debug=True)
