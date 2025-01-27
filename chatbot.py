import nltk
import random
from nltk.chat.util import Chat, reflections

# Define a set of patterns and responses
pairs = [
    (r'hi|hello|hey', ['Hello! How can I assist you today?', 'Hey! What can I do for you today?']),
    (r'what is your name?', ['I am an AI chatbot.', 'You can call me ChatBot.']),
    (r'how are you?', ['I am just a program, but I am doing well, thank you!', 'I am doing fine, thanks for asking!']),
    (r'(.*) your name?', ['My name is ChatBot.', 'I am called ChatBot.']),
    (r'quit', ['Bye! Have a nice day.', 'Goodbye! Take care.']),
    (r'(.*)', ['Sorry, I didn\'t understand that.', 'Could you please rephrase that?'])
]

# Create the chatbot using the defined patterns and responses
def chatbot():
    print("Hi! I'm your AI chatbot. Type 'quit' to exit.")  # Greet the user
    chat = Chat(pairs, reflections)
    chat.converse()

# Main function to start the chatbot
if __name__ == "__main__":
    chatbot()
