from flask import Flask
app = Flask(__name__)

@app.route('/')
def ajedrez():
    import ajedrez
    player = ajedrez.player()
    return str(player)

if __name__ == '__main__':
    app.run()