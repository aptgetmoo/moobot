"""moobot settings"""


# the log in details for the account moobot uses
# please use an API token if you can
# as email address / password based login is depricated
moobot_login = {
    'discord_token': 'whoops left token in here',
    'email': input(''),
    'password': input('')
}

# this is the "now playing" game
status_message = 'moobot development happening now :D'

database_file = 'moobot.db'

fixed_karma = {
    '1337': 1337
}

DEBUG = False

test = None
