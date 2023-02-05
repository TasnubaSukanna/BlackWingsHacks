#Using RegEx to check if a string contains the specified search pattern
import re
import long_responses as long

#Splits user message into an array so that each word can be analyzed separately
def get_response(user_input):
    #split using common punctuations in messages
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    
#An infinite while true loop so chatbot can always get new responses
while True:
    print('Bot: ' + get_response(input('You: ')))
