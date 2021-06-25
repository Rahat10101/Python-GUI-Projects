import copy
from random import *

word_dict = {
    'adjective':['greedy','abrasive','grubby','groovy','rich','harsh','tasty','slow'],
    'city name':['Chicago','New York','Charlotte','Indianapolis','Louisville','Denver'],
    'noun':['people','map','music','dog','hamster','ball','hotdog','salad'],
    'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
    'sports noun':['ball','mit','puck','uniform','helmet','scoreboard','player']
}

story = (
    "One day my {} friend and I decided to go to the {} game in {}. "+
    "We really wanted to see the {} play the {}. So, we {} our {} \n"+
    "down to the {} and bought some {}s. We got into the game and \n"+
    "it was a lot of fun. We ate some {} {} and drank some {} {}. \n"+
    "We had a great time! We plan to go again next year! \n"
)

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('sports noun', local_dict),
        get_word('city name', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('action verb', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict)
)

story_1 = create_story()
print(story_1)
print()

story_2 = create_story()
print(story_2)
print()


