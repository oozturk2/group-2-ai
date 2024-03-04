from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, send, emit



app = Flask(__name__)
CORS(app)
socketio = SocketIO(app,  cors_allowed_origins="*")



@socketio.on('message')
def messages(message):
    send(message, broadcast=True)



if __name__=="__main__":
    socketio.run(app, debug=True)