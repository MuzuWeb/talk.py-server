from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "It works !"

@app.route('/messages')
def messages():
    file = open("data/messages.txt", "r")
    msg = file.read()
    file.close()

    return f"{msg}"

@app.route('/api/send', methods=['GET', 'POST'])
def contact():
    if request.method == "GET":
        username = request.args['username']
        message = request.args['message']
        file = open("data/messages.txt", "a")
        file.write(("\n" + username + " : " + message + "\n"))
        file.close()
        return "200"
    elif request.method == "POST":
        request_data = request.get_json()
        username = request_data['username']
        message = request_data['message']
        if message == "/clearchat":
            os.remove("data/messages.txt")
            deleted = open("data/messages.txt", "w")
            deleted.write("Chat cleared !\n\n")
            deleted.close()
        if message == "/help":
            help = open("data/messages.txt", "a")
            help.write(("\nHelp menu :\n/reload : refresh the chat to see new messages\n/exit : quit the chat\n/clearchat : clear the chat, warning : abuse may result in something not good for you.\n"))
            help.close()
        file = open("data/messages.txt", "a")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        file.write(("\n" + "<" + username + "> " + " : " + f"{current_time}" + " : \n" + ">" + message + "\n"))
        file.close()
        return "200"
        




if __name__ == "__main__":
    app.run(port=8080)
