from flask import Flask, render_template, request
import os
import re
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

import logging
logging.basicConfig(filename='output.log',level=logging.DEBUG)
training_data = []

Path = "/Users/hamzahabdullahi/Desktop/Python/ChatBot/Code/troubleshooting/"

filelist = os.listdir(Path)
for i in filelist:
    if i.endswith(".txt"):  # You could also add "and i.startswith('f')
        with open(Path + i, 'r') as f:
            for statement in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
                statement = statement.replace(". ", ".\n")
                is_q_or_a = re.search('(Q: \n A:)?(.+)', statement)
                if is_q_or_a:
                    training_data.append(is_q_or_a.groups()[1])

# Create a new ChatBot instance
# bot = ChatBot(
#     'Terminal',
#     # storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#     logic_adapters=[
#         'chatterbot.logic.BestMatch'
#     ],
#     # database_uri='mongodb://localhost:27017/chatterbot-database'
# )

bot = ChatBot('ProntoBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.to_lower',

    ],
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'maximum_similarity_threshold': 0.60
    }

])

trainer = ListTrainer(bot)
trainer.train(training_data)

trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.troubleshooting")

trainer.train("chatterbot.corpus.english.greetings")



# print('Hi, please tell me the name and/or model No. of the device in question today ')

# # main loop
# while True:
#     try:
#         bot_input = bot.get_response(input())
#         print(bot_input)

#     except(KeyboardInterrupt, EOFError, SystemExit):
#         trainer.export_for_training("new_export.json")
#         break

app = Flask(__name__)
app.static_folder = 'static'

    
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_input = bot.get_response(userText)
    if '\\n' in bot_input.text:
        string = '-'.join(bot_input.text.split("\\n")) 
        print(';hi')

        return 
    return str(bot_input)

if __name__ == "__main__":
    app.run(debug=True,port=5002)
