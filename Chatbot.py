#Using RegEx to check if a string contains the specified search pattern
import re
import confusing_message as nonsense

#Calculates the probability that the user message is the corresponds to the predefined list of recognized and required words
def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Increases certainty if the any word in the user message exists in recognized words
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

#Splits user message into an array so that each word can be analyzed separately
def get_response(user_input):
    #split using common punctuations in messages
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    
#An infinite while true loop so chatbot can always get new responses
while True:
    print('Bot: ' + get_response(input('You: ')))
