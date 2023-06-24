from datetime import datetime

def sample_responses(input_text: str):
    user_message = input_text.lower()

    if ("hello", "hi", "sup", "hey") in user_message:
        return "Hey yourself! How's life?"
    
    if ("who are you", "who are you?", "whoru", "wru", "what's your name?") in user_message:
        return "I'm YakariBot. Just checking the waters here!"
    
    if ("time", "date", "delta", "time?", "what time is it?") in user_message:
        return str(datetime.now().strftime("%d/%m/%y, %h:%m:%s"))
    
    return "Cut the bullshit! Behave yourself!"