# import libraries
from chatterbot import ChatBot
from chatterbot.conversation import Statement

# this stuff because it hides a useless error :D
import logging
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)

# import the trainer so we can train
from chatterbot.trainers import ChatterBotCorpusTrainer

# make a bot
chatbot = ChatBot("bot")

# create the trainer
trainer = ChatterBotCorpusTrainer(chatbot)

# actually train it on some data
trainer.train("chatterbot.corpus.english")

# simple while loop to get input then respond
while True:
    question = input("Question: ")
    response = chatbot.get_response(question)
    print(response)