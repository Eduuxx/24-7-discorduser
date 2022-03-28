from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your discord user is now running, take care!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
