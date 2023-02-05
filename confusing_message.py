import random

def unknown():
    response = ["Could you please re-phrase that? ", 
                "Sorry I can't really understand.",
                "Please call the customer service number at XXX-XXX-XXXX.",
                "What does that mean?"][random.randrange(4)]
    return response
