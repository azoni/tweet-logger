from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS # type: ignore
from sqlalchemy import create_engine, desc # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from models import Base, ChatLog
from config import DATABASE_URL
import os

app = Flask(__name__)
CORS(app)

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

@app.route('/logs/latest', methods=['GET'])
def get_latest_log():
    session = Session()
    log = session.query(ChatLog).order_by(desc(ChatLog.timestamp)).first()
    session.close()
    if log:
        return jsonify({
            "id": log.id,
            "user_message": log.user_message,
            "assistant_reply": log.assistant_reply,
            "timestamp": log.timestamp.isoformat()
        })
    else:
        return jsonify({"message": "No logs found."}), 404
    
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)