from flask import Flask, render_template, session
from flask_socketio import SocketIO, emit

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('message')
def test_message(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    print('my_response',
         {'data': message['data'], 'count': session['receive_count']})
    emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})

if __name__ == '__main__':
    socketio.run(app, debug=True)
