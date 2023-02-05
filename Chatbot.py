#Using RegEx to check if a string contains the specified search pattern
import re
import confusing_message1 as nonsense

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
    
#Creating our dictionary of medical related words to recognize
def check_all_messages(message):
    highest_prob_list = {}
    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('How can I help you?', ['need','help','assistance','want'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Please go to the nearest emergency room.', ['weakness', 'numbness', 'on', 'one', 'side', 'slurred', 
                                           'speech', 'fainting', 'change', 'in', 'mental', 'state','serious', 'burns', 'head', 'eye', 
                                           'injury', 'concussion', 'confusion', 'broken', 'bones', 'discolated','joints', 'fever', 'with', 
                                           'rash', 'stitches', 'lacerations', 'severe', 'Vaginal', 'bleeding', 'pregnancy'], 
                                            required_words=['weakness','numbness', 'wlurred','fainting', 'serious', 'burns', 
                                           'injury', 'concussion', 'confusion', 'broken', 'bones', 'discolated','joints', 
                                           'rash', 'stitches', 'lacerations', 'severe','bleeding'])
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('Please contact 911. You need to go to emergency room safely as soon as possible.', ['severe', 'chest', 'pain', 'bleeding', 'faint', 'vision', 
    'impaired', 'heart', 'attack', 'stroke'], 
    required_words=['chest', 'pain', 'bleeding', 'faint', 'vision', 'impaired', 'heart', 'attack', 'stroke'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    # print(highest_prob_list)
    # print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')

    return nonsense.unknown() if highest_prob_list[best_match] < 1 else best_match

#Splits user message into an array so that each word can be analyzed separately
def get_response(user_input):
    #split using common punctuations in messages
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response
    
#An infinite while true loop so chatbot can always get new responses
while True:
    print('Bot: ' + get_response(input('You: ')))
