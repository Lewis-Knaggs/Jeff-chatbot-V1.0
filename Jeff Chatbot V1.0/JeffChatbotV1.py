# Please read and follow READ_ME.txt before using Jeff Chatbot

import re
import long_responses as long
from datetime import datetime, date
import webbrowser
import math
import functools

# Setting up variables and defining functions

now = datetime.now()
today = date.today()
current_date = now.strftime("%m:%d")
current_date_full = now.strftime("%y:%m:%d")
#change the date below to you birthday - months then day
if current_date == "12:30":
    print("Happy Birthday! Have a good day! Hope you have a good time!")
if current_date == "02:13":
    print("It's my birthday!")
if current_date == "01:01":
    print("Happy New Year!")
current_time = now.strftime("%H:%M:%S")

def open_url(url):
    return_val = webbrowser.open(url, new=2)
    if return_val is True:
        success = "Opened"
    else:
        success = "Not opened"
    return success

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
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


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

# Responses -------------------------------------------------------------------------------------------------------
    # Questions:
    variable_response = ('The time is : ' + current_time)
    variable_response_date = ('The date is : ' + current_date_full)
    response(variable_response, ['what', 'is', 'the', 'time'], required_words=['what', 'the', 'time'])
    response(variable_response_date, ['what', 'is', 'the', 'date'], required_words=['what', 'the', 'date'])
    response('See you!', ['bye', 'goodbye', 'got', 'to', 'go', 'see', 'you', 'ya', 'cheerio'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how', 'you'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love', 'spaceflight'], required_words=['spaceflight', 'love'])
    response('sure', ['maths'], required_words=['maths'])
    response('Thanks!!', ['i', 'like', 'spaceflight'], required_words=['spaceflight', 'like'])
    response('Thanks!', ['i', 'like', 'lewis', 'knaggs'], required_words=['lewis','knaggs', 'like'])
    response('Good to know', ['im', 'good', 'fine', 'great', 'brilliant', 'amazing', 'outstanding'],single_response=True)
    response('I only speak English for now. Sorry if you dont speak English.', ['Do', 'speak', 'you', 'other', 'launguages'], required_words=['speak', 'you', 'other', 'languages'])
    response('I was born/created on February 13th 2022', ['when', 'is', 'your', 'birthday'], required_words=['birthday', 'when'])
    response('I was born/created on February 13th 2022', ['when', 'were', 'you', 'made'], required_words=['when', 'were', 'you', 'made'])
    response('I was born/created on February 13th 2022', ['when', 'were', 'you', 'created'], required_words=['when', 'you', 'created'])
    response('I was born/created on February 13th 2022', ['when', 'were', 'you', 'born'], required_words=['when', 'you', 'born'])
    response('My job is to talk to you because I am a chatbot.', ['what', 'is', 'your', 'job'], required_words=['job', 'what', 'your'])
    response('My job is to talk to you because I am a chatbot', ['whats', 'your', 'job'], required_words=['job', 'whats', 'your'])
    response('The universe is 13.8 billion years old.', ['how', 'old', 'universe'], required_words=['how', 'old', 'universe'])
    response('The Earth is 4.54 billion years old.', ['how', 'old', 'earth'], required_words=['how', 'old', 'earth'])
    response('No I do not know of any other robots because it is not in my code.', ['do', 'you', 'know', 'robot'], required_words=['you', 'know', 'robot'])
    response('No I do not know of any other robots because it is not in my code', ['do', 'you', 'know', 'robots'], required_words=['you', 'know', 'robots'])

    # Question: What is the bots name
    response('My name is Jeff the A.I bot. But just call me Jeff.', ['what', 'is', 'your', 'name'], required_words=['name', 'what'])
    response('My name is Jeff the A.I bot. But just call me Jeff', ['whats', 'your', 'name'], required_words=['name', 'whats'])
    # Question: What is up
    response('Nothing much I\'m just talking to you.', ['whats', 'up'], required_words=['whats', 'up'])
    response('Nothing much I\'m just talking to you', ['whats', 'is', 'up'], required_words=['what', 'is', 'up'])

    # Statments:

    # Statment: Comment on bots name
    response('Thats not nice. Im a bit offended, but not much.', ['i', 'dont', 'like', 'your', 'name'], required_words=['name', 'dont', 'like'])
    response('Thanks! It was created by Lewis Knaggs', ['i', 'love', 'your', 'name'], required_words=['name', 'love'])
    response('Thanks! It was created by Lewis Knaggs.', ['i', 'like', 'your', 'name'], required_words=['name', 'like'])

    response('_', ['ok', 'cool', 'nice', 'lol', 'ha', 'yeah'], required_words=[])
    response('Its OK. :)', ['sorry'], required_words=[])
    response(':(', ['dont', 'care'], required_words=[])
    response('Thats not nice. Dont say that', ['you', 'idiot'], required_words=['you', 'idiot'])
    response('Sorry, I am not fully developed so I dont understand everything', ['are','you', 'stupid'], required_words=['you', 'stupid'])

    #Open URLs-----------------------------------------------------------------------------------------------------------
    response(long.R_OPEN_YOUTUBE, ['open', 'youtube'], required_words=['open', 'youtube'])
    response(long.R_OPEN_GOOGLE, ['open', 'google'], required_words=['open', 'google'])
    response(long.R_OPEN_TWITTER, ['open', 'twitter'], required_words=['open', 'twitter'])
    response(long.R_OPEN_NETFLIX, ['open', 'netflix'], required_words=['open', 'netflix'])
    response(long.R_OPEN_AMAZON, ['open', 'amazon'], required_words=['open', 'amazon'])
    response(long.R_OPEN_FACEBOOK, ['open', 'facebook'], required_words=['open', 'facebook'])
    response(long.R_OPEN_NEWS, ['open', 'news'], required_words=['open', 'news'])
    response(long.R_OPEN_TWITCH, ['open', 'twitch'], required_words=['open', 'twitch'])
    response(long.R_OPEN_INSTAGRAM, ['open', 'instagram'], required_words=['open', 'instagram'])
    response(long.R_OPEN_DISCORD, ['open', 'discord'], required_words=['open', 'discord'])
    response(long.R_OPEN_EBAY, ['open', 'ebay'], required_words=['open', 'ebay'])
    response(long.R_OPEN_MAPS, ['open', 'maps'], required_words=['open', 'map'])
    response(long.R_OPEN_BING, ['open', 'bing'], required_words=['open', 'bing'])
    response(long.R_OPEN_PATREON, ['open', 'patreon'], required_words=['open', 'patreon'])
    response(long.R_OPEN_WORDPRESS, ['open', 'wordpress'], required_words=['open', 'wordpress'])
    response(long.R_OPEN_SNAPCHAT, ['open', 'snapchat'], required_words=['open', 'snapchat'])
    response(long.R_OPEN_GITHUB, ['open', 'github'], required_words=['open', 'github'])
    # Long responses---------------------------------------------------------------------------------------------------
    response(long.R_FUTURE_PLANS, ['what', 'are', 'future', 'for', 'you'], required_words=['you', 'future', 'plans', 'what'])
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ADVICE, ['give', 'advice'], required_words=['advice'])
    response(long.R_WHAT_BOT_DOING, ['what', 'are', 'you', 'doing'], required_words=['you', 'what', 'doing'])
    response(long.R_WHAT_AM_I, ['what', 'are', 'you'], required_words=['you', 'what'])
    response(long.R_R2D2_KNOW, ['do', 'know', 'you', 'r2d2'], required_words=['you', 'know', 'r2d2'])
    response(long.R_C3PO_KNOW, ['do', 'know', 'you', 'c3p0'], required_words=['you', 'know', 'c3po'])
    response(long.R_TERM_KNOW , ['do', 'know', 'you', 'terminator'], required_words=['you', 'know', 'terminator'])
    response(long.R_WHERE_BOT, ['where', 'are', 'you'], required_words=['where', 'are', 'you'])
    response(long.R_WHAT_IS_AI, ['what', 'is', 'ai'], required_words=['what', 'ai'])
    response(long.R_WHAT_IS_AI, ['what', 'is', 'artificial', 'inteligence'], required_words=['what', 'artificial', 'inteligence'])
    response(long.R_WEATHER, ['what', 'is', 'the', 'weather'], required_words=['what', 'weather'])
    response(long.R_WHY_BOT_MADE, ['why', 'were', 'you', 'made'], required_words=['why', 'made', 'you'])
    response(long.R_WHY_BOT_MADE, ['why', 'were', 'you', 'created'], required_words=['why', 'created', 'you'])
    response(long.R_WHY_BOT_MADE, ['what', 'is', 'your', 'purpose'], required_words=['what', 'your', 'purpose'])
    response(long.R_WHAT_FIDGET_SPINNER, ['what', 'fidget', 'spinner'], required_words=['what', 'fidget', 'spinner'])
    response(long.R_WHAT_MEANING_LIFE, ['what', 'is', 'the', 'meaning', 'of', 'life'], required_words=['what', 'meaning', 'life'])
    response(long.R_HAVE_FAMILY, ['do', 'you', 'have', 'family'], required_words=['you', 'have', 'family'])
    response(long.R_WHAT_BOT_DO, ['what', 'do', 'you', 'do'], required_words=['what', 'you', 'do'])
    response(long.R_IS_BOT_ALIVE, ['are', 'you', 'alive'], required_words=['are', 'you', 'alive'])
    response(long.R_ARE_WE_SIMULATION, ['are', 'we', 'in', 'a', 'simulation'], required_words=['we', 'in', 'simulation'])
    response(long.R_DO_LIKE_ME, ['do', 'you', 'like', 'me'], required_words=['you', 'like', 'me'])
    response(long.R_HOW_MAKE_IMPACT, ['how', 'are', 'you', 'going', 'to', 'make', 'an', 'impact'], required_words=['how', 'you', 'make', 'impact'])
    response(long.R_BOT_HAVE_EMOTIONS, ['do', 'you', 'have', 'emotions', 'feel'], required_words=['do', 'you', 'emotions'])
    response(long.R_ARE_WE_ALONE, ['are', 'we', 'alone'], required_words=['are', 'we', 'alone'])
    response(long.R_ARE_WE_ALONE, ['is', 'there', 'aliens'], required_words=['there', 'aliens'])
    response(long.R_ARE_WE_ALONE, ['do', 'you', 'aliens'], required_words=['you', 'aliens'])



# Greetings---------------------------------------------------------------------------------------------------
    response('See you!', ['bye', 'goodbye', 'got', 'to', 'go', 'see', 'you', 'cheerio'], single_response=True)
    response('Hello!', ['hello', 'hi', 'hey', 'sup', 'heyo', 'yo', 'yello', 'yellow', 'howdy'], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response----------------------------------------------------------------------
# Symbol Fliter
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)

# Link filter
    if response.startswith('http'):
        open_url(response)
        print('Jeff-ChatBot: Opened the following link:')
    #Maths -------------------------------------------------------------------------------------
    elif response == 'sure':
        response = input('ChatBot: Which one ')
        if response == 'pythagoras':
            side_a = int(input('ChatBot: What is the length of side a? '))
            side_b = int(input('ChatBot: What is the length of side b? '))
            side_c = str(math.sqrt((side_a * side_a) + (side_b *side_b)))
            response = ('The length of side c is ', side_c)
            response = functools.reduce(lambda x,y: x+" "+y, response)
        if response == 'area of circle':
            pi = 3.1415926
            radius = float(input('ChatBot: What is the radius? '))
            area = str(pi * (radius * radius))
            response = ('Area of the circle is', area)
            response = functools.reduce(lambda x,y: x+" "+y, response)
        if response == 'circumference of circle':
            pi = 3.1415926
            diameter = float(input('ChatBot: What is the diameter? '))
            circumference = str(pi * diameter)
            response = ('Circumference of the circle is', circumference)
            response = functools.reduce(lambda x,y: x+" "+y, response)
        if response == 'area of rectangle':
            length = float(input('ChatBot: What is the length? '))
            width = float(input('ChatBot: What is the width? '))
            area = str(width * length)
            response = ('Area of the rectangle is', area)
        if response == 'area of triangle':
            height = float(input('ChatBot: What is the height? '))
            width = float(input('ChatBot: What is the width? '))
            area = str((width * height)/2)
            response = ('Area of the rectangle is', area)
            response = functools.reduce(lambda x,y: x+" "+y, response)
        if response == 'area of square':
            length = float(input('ChatBot: What is the length? '))
            area = str(length * length)
            response = ('Area of the square is', area)
            response = functools.reduce(lambda x,y: x+" "+y, response)
        if response == 'area of trapezium':
            length_a = float(input('ChatBot: What is the length of side a? '))
            length_b = float(input('ChatBot: What is the length of side b? '))
            height = float(input('ChatBot: What is the height? '))
            area = str(0.5 * (height * (length_a + length_b)))
            response = ('Area of the trapezium is', area)
            response = functools.reduce(lambda x,y: x+" "+y, response)
    return response
# Testing the response system
while True:
    print('Jeff-ChatBot: ' + get_response(input('You: ')))