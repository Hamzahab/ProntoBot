# ProntoBot
Chat Bot that assists in troubleshooting Tier 1/2 medical device problems

This application uses a Flask backend (python), mongodb dbms, and web app front end to 
converse with a chatbot regarding troubleshooting medical device of choice (currently one is available 
in database, is being updated).

Instructions
1 - clone repo
2 - install chatterbot module in virtualenv
3 - if mongodb installed, run main.py module. LocalHost will be used as front-end for the time being.
    if not, modify main.py file by commenting 'storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
    this will ensure that the database will be saved on sqlite in your local machine (if on mac). 
4 - Enter http://localhost:5002/ in web browser
5 - chat away
