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
                is_q_or_a = re.search('(Q:|A:)?(.+)', statement)
                # is_q_or_a = re.search(r'Q:(.+)\s A:(.+)',statement)
                if is_q_or_a:
                    training_data.append(is_q_or_a.groups()[1])

bot = ChatBot('ProntoBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.to_lower',

    ],
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'maximum_similarity_threshold': 0.85
    }

])

trainer = ListTrainer(bot)
trainer.train(training_data)

trainer = ChatterBotCorpusTrainer(bot)

# trainer.train("chatterbot.corpus.troubleshooting")

trainer.train("chatterbot.corpus.english.greetings")


trainer.export_for_training("new_export.json")

app = Flask(__name__)
app.static_folder = 'static'
 
@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_output = bot.get_response(userText)

    if userText.lower() == 'yes' == userText.lower() == 'no':
        return yes_no_feedback(userText,trainer)    

    return str(bot_output)

def yes_no_feedback(user_input_statement,my_trainer):
    #user said yes
    if user_input_statement.text.lower() == 'yes':
        return my_trainer.get_response('accutor 3')
    elif user_input_statement.text.lower() == 'no':
        return my_trainer.get_response('not accutor 3')
    return my_trainer.get_response('unknown input')


if __name__ == "__main__":
    app.run(debug=True,port=5002)



    