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
current_iter = 1
for i in filelist:
    if i.endswith(".txt"):  # You could also add "and i.startswith('f')
        with open(Path + i, 'r') as f:
            for statement in f:
                # Here you can check (with regex, if, or whatever if the keyword is in the document.)
                #replacing newlines w/ breakpoints for html conversion
                statement = statement.replace("\n", "<br>")
                statement = statement.replace("\\n", "<br>")
                is_q_or_a = re.search('(Q:|A:)?(.+)', statement)
                # is_q_or_a = re.search(r'Q:(.+)\s A:(.+)',statement)
                if is_q_or_a:
                    training_data.append(is_q_or_a.groups()[1])
                    if(current_iter):
                        

                    print(is_q_or_a.groups()[1],'\n')
                    
def simple_q_a(count):
    if count%2 == 0:
        return True
                    
# print(training_data)
# bot = ChatBot('ProntoBot',
#     preprocessors=[
#         'chatterbot.preprocessors.clean_whitespace',
#         'chatterbot.preprocessors.to_lower',

#     ],
#     storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
#     logic_adapters=[
#         {
#         'import_path': 'chatterbot.logic.BestMatch',
#         'maximum_similarity_threshold': 0.85
#         }

# ])

# trainer = ListTrainer(bot)
# trainer.train(training_data)

# # trainer = ChatterBotCorpusTrainer(bot)

# # # trainer.train("chatterbot.corpus.troubleshooting")

# # trainer.train("chatterbot.corpus.english.greetings")


# trainer.export_for_training("training_log.json")

# app = Flask(__name__)
# app.static_folder = 'static'

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/get")
# def get_bot_response():
#     userText = request.args.get('msg')
#     bot_output = bot.get_response(userText)

#     if userText.lower() == 'yes' or userText.lower() == 'no':
#         return yes_no_feedback(userText,bot)    

#     return str(bot_output)

# def yes_no_feedback(user_input_statement,training_bot):
#     #user said yes
#     if user_input_statement.lower() == 'yes':
#         return training_bot.get_response('accutor 3').text
#     elif user_input_statement.lower() == 'no':
#         return training_bot.get_response('not accutor 3').text
#     return training_bot.get_response('unknown input').text


# if __name__ == "__main__":
#     app.run(debug=True,port=5002)



