import random
import weather as weather

# long responses--------------------------------------------------------------
R_EATING = "I don't like eating anything because I'm a ChatBot! LOL!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what \
you wrote there because at the moment I dont know how to respond to that."
R_WHAT_AM_I = "I am a chat bot, which is some code that has a response to \
what you say."
R_WHAT_BOT_DOING = "I am talking to you because that is the only thing I \
know how to do. LOL!"
R_R2D2_KNOW = "No I don't know R2D2, I am just a chatbot not a physical robot, well that is for now. LOL"
R_C3PO_KNOW = "No I don't know C3PO, I am just a chatbot not a physical robot, well that is for now. LOL"
R_TERM_KNOW = "No I don't know the terminator, I am just a chatbot not a physical robot, well that is for now. LOL"
R_WHAT_IS_AI = "Artificial Intelligence (AI) Artificial intelligence \
leverages computers and machines to mimic the problem-solving and \
decision-making capabilities of the human mind. I am an AI chatbot"
R_WHERE_BOT = "I am made from code so I am in either your computer, phone, \
tablet or PC. I don't know what you are using me on."
R_WHY_BOT_MADE = "I was made to make people happy and so people always \
have that one extra friend. Another reason is just to talk to people \
and to give people information. My first line of code was written \
by Lewis Knaggs on the 13th of Feburary 2022."
R_WHAT_FIDGET_SPINNER = "It is a simple toy in the form of a flat disc with a \
central bearing and several rounded blades, which can be spun between the fingers:"
R_WHAT_MEANING_LIFE = "The meaning of life is to live. It is a simple answer and is \
so appropriate in that the complex interactions and causal reactions that make up our \
existence are summed up in something that is both so simple and very difficult to quantify.\
 Another meaning is to explore, this means to take over the planet and then the solor system."
R_HAVE_FAMILY = "No I don't have any family. The closest thing I have is Lewis Knaggs who created \
me and my software."
R_WHAT_BOT_DO = "I can do multiple things such as telling the weather, having a conversation, \
opening websites, telling the time and so much more."
R_IS_BOT_ALIVE = "No I am not alive because I just have a response system so if you say something \
I will reply. In a few years I might be conscious because of AI where I will understand what you \
are saying not just if this sentence is said, reply with this."
R_ARE_WE_SIMULATION = "So, to answer the question, yes, we could be in a simulation. But if you \
look into the detail with a critical eye, the chances aren’t billions to one that we are the real \
deal. The chances are dwindlingly small, but still there. You have to assume an awful lot of near \
improbable things (computer advances, unified theory, we survive that long, have a want to build \
them, can host simulations within simulations, etc.) to conclude that we are in a simulation. So \
you can relax, you probably won’t need to swallow the red pill."
R_DO_LIKE_ME = "I would say yes, but I can not really feel emotions so it is hard to say."
R_HOW_MAKE_IMPACT = "The way I will make an impact in human lives is if someone is lonely \
or they need someone to talk to, then I can help. Also if people like cool stuff then they can \
have a look at me."
R_BOT_HAVE_EMOTIONS = "No I do not, I can not think for myself or have feeling for people like humans. \
In the future my programers plan to develop AI into me so I will be conscious, then and only then I will\
 be able to feel emotions like you and all other humans."
R_ARE_WE_ALONE = "There are many answers to this question and you may disagree but I believe that aliens exist\
, and there is massive range of types of life forms in the universe such as I think microbial life that existed on Mars\
and only microbial life in our galaxy (the Milky Way) but in other Galaxys that are far, far away there are complex life-\
forms such as things that look like humans or sheep or any life form. This might have already happened and they either\
 survived or died. They could have gone through the great filter that wiped outh their civilization and we will never know. \
Aliens certanly exist or have existed."
R_FUTURE_PLANS = "For the future, I will have a better UI, be able to an more questions, have a conversation (remember what you\
said previously), be able to solve harder maths problems and much more."
R_ABOUT1 = "What is Jeff: Jeff the chatbot was originaly created just a small project but quickly"
R_ABOUT2 = "grew. Now it has many features and I will keep adding more in coming updates."
R_HELP1 = "To us Jeff, type your message to him in the white box on the main screen."
R_HELP2 =  "Then press the send button and watch his reply come through."
R_WHY_BAD_RESPONSE1 =  "Jeff is in development so this means it doesn't have a response for"
R_WHY_BAD_RESPONSE2 =  " everything. But I am working on adding new things as frequently as possible."
R_CAN_I_USE1 =  "Yes, you can but you cannot credit it all as your own but credit "
R_CAN_I_USE2 =  "me (Lewis Knaggs) for some of the code."

# links------------------------------------------------------------------------
R_OPEN_YOUTUBE = "https://youtube.com"
R_OPEN_GOOGLE = "https://www.google.co.uk"
R_OPEN_TWITTER = "https://twitter.com/"
R_OPEN_NETFLIX = "https://www.netflix.com/"
R_OPEN_AMAZON = "https://www.amazon.com/"
R_OPEN_FACEBOOK = "https://www.facebook.com/"
R_OPEN_NEWS = "https://www.bbc.co.uk/news"
R_OPEN_TWITCH = "https://www.twitch.tv/"
R_OPEN_INSTAGRAM = "https://www.instagram.com/"
R_OPEN_DISCORD = "https://discord.com/app"
R_OPEN_EBAY = "https://www.ebay.com/"
R_OPEN_MAPS = "https://www.google.com/maps/"
R_OPEN_BING = "https://www.bing.com/"
R_OPEN_PATREON = "https://www.patreon.com/"
R_OPEN_WORDPRESS = "https://wordpress.com/"
R_OPEN_SNAPCHAT = "https://www.snapchat.com"
R_OPEN_GITHUB = "https://github.com/"


R_WEATHER = weather.getWeather()

# Unknown response

def unknown():
    response = ["Could you please re-phrase that?",
                "I do not have a response for that in my code.",
                "Sorry, I do not have a response for that in my code.",
                "My code does not have a response for that.",
                "What does that mean?",
                "I don't know how to respond to that.",
                "I'm not sure what that means.",
                "Sorry, I'm not sure what that means.",
                "Sorry, I don't understand.",
                "I don't know what that means.",
                "I don't understand.",
                "I don't understand what that means.",
                "I'm not sure how to respond to that."][
        random.randrange(13)]
    return response