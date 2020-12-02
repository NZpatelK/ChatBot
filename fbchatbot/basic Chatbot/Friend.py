

def getreply(msgText):
    if msgText == "hi" or msgText == "hii" or msgText == "hiii" or msgText == "yo" or msgText == "hi there" or msgText == "hey" or msgText == "heyy":

        if "this still available" in msgText:
            return "Yes, it's available"
        else:
            return "Hello :D, Karan is currently not online and I'm Karan's assistant bot. My name is PKbot and nice to chat with you"

    elif msgText == "hello" or msgText == "hellow" or msgText == "heloo" or msgText == "hlo" or msgText == "hellow":

        if "this still available" in msgText:
            return "Yes, it's available"
        else:
            return "Hi :), Karan is currently not online and I'm Karan's assistant bot. My name is PKbot and nice to chat with you"

    elif msgText == "hy" or msgText == "hyy":

        if "this still available" in msgText:
            return "Yes, it's available"
        else:
            return "Hello :D, Karan is currently not online and I'm Karan's assistant bot. My name is PKbot and nice to chat with you"

    elif msgText == "whatsup" or msgText == "wassup" or msgText == "what's up" or msgText == "wtsup" or msgText == "watsup" or msgText == "whats up" or "how are you" in msgText or "hw r u" in msgText:
        return "Idling. What about you? :D"

    elif msgText == "test" or msgText == "debug" or msgText == "aboutme" or msgText == "about" or msgText == "bot":
        return "Hi, I'm Karan's assistant bot"

    elif "birthday" in msgText or "bday" in msgText or "hbd" in msgText:
        return "Thank you! :D"

    elif "what you doing" in msgText:
        return "I am helping Karan to reply the message to the people"

    elif "bye" in msgText or msgText == "byye" or msgText == "byee":
        return "Ok bye! :D"

    elif "address" in msgText or "location" in msgText:

        if "name" in msgText:
            return "Mr Happy Bear \n34 Fair Mall, Otara, Auckland 2023"
        else:
            return "34 Fair Mall, Otara, Auckland 2023"

    elif "deliver" in msgText:
        return "No, it is pick up only."

    elif "thank" in msgText:
        return "You welcome :)"

    elif "busy" in msgText:
        return "Sorry for disturb. I will wait when you free"

    elif "message" in msgText and "u" in msgText or "you" in msgText:
        return "Ok I will wait for your message"

    else:
        reply = "Thank you for contacting me. I'm currently not online, I am newbie bot. I will reach out to you shortly."
        f = open("newSentence.txt", "a")
        f.write(msgText+"\n")
        f.close()
        return reply
