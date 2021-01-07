import re
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import logging
logging.basicConfig(filename='outputnewcode.log',level=logging.DEBUG)

training_data = []

file = open('battery_failure.txt','r')

for statement in file:
    statement = statement.replace(". ", ".\n")
    is_q_or_a = re.search('(Q: \n A:)?(.+)', statement)
    if is_q_or_a:
        training_data.append(is_q_or_a.groups()[1])

print(training_data)

bot = ChatBot('ProntoBot',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.to_lower',

    ],
    logic_adapters=[
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'maximum_similarity_threshold': 0.60
    }

])
trainer = ListTrainer(bot)
trainer.train(training_data)

print("Type your question here...")
while True:
    try:
        bot_input = bot.get_response(input())
        print(bot_input.text)
        if '\\n' in bot_input.text:
            for part in bot_input.text.split("\\n"):
                print(part)

    # Press ctrl-c or ctrl-d to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break;


