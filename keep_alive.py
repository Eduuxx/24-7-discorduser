from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your ID is now Active 24/7! Do join our Server and Subscribe our channel if you want to Watch More Such Videos!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
