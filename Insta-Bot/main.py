import config
from instapy import InstaPy

session = InstaPy(username = "wake_up_rahat_0.o" , password = "f#cku4422322321")
session.login()

session.like_by_tags(['python', 'flutter', 'Qt'], amount= 6)

session.set_do_follow(True, percentage=100)

session.set_do_comment(True , percentage=100)
session.set_do_comments(['Love it ! ' , 'Nice Post ...'])

session.end()


#used by only FireFox