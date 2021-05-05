from yesnostruc import solution_dict
from flask import Flask, render_template, request, session

import os
import re
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot.conversation import Statement
import logging

app = Flask(__name__)
app.static_folder = 'static'

#initializing chatbot
bot = ChatBot('ProntoBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.to_lower',

    ],
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
        'import_path': 'chatterbot.logic.BestMatch',
        'maximum_similarity_threshold': 0.60
        }

])

def setup():
    logging.basicConfig(filename='output.log',level=logging.DEBUG)
    # last_response = ''
    
    #setting training as corpus trainer
    trainer = ChatterBotCorpusTrainer(bot)

    #training on special corpi of data
    trainer.train("chatterbot.corpus.Accutor_3")

    # trainer.train("chatterbot.corpus.english.greetings")


    trainer.export_for_training("training_log.json")
    return bot


@app.route("/")
def run():
    session['last_response'] = ''
    return render_template("index.html")



@app.route("/get")
def get_bot_response():
    # getting input from front end
    userStatement = request.args.get('msg')

    if userStatement.lower() == 'did not work':
        #if last response provided exists in solution path, get its next solution
        if  session['last_response'] in solution_dict:
            bot_output = bot.generate_response(Statement(text = solution_dict.get(session['last_response'])))
            print("confidence value is " + str(bot_output.confidence))
            session['last_response'] = bot_output.text
            bot_output = bot_output.text.capitalize()
        else:
            bot_output = 'Cannot assist in this'

    elif userStatement.lower() == 'worked':
         bot_output = "Perfect! I'm happy to have been a help"
    else:
        # print('in here')
        bot_output = bot.generate_response(Statement(text=userStatement))
        print("confidence value is " + str(bot_output.confidence) + "\n" +"Statement persona is: " + bot_output.persona)
        # bot_output.id = 3
        session['last_response'] = bot_output.text
        bot_output = bot_output.text.capitalize()

    return str(bot_output)



if __name__ == "__main__":    
    #initializing Flask backend
    setup()
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(debug=True,port=5000)



