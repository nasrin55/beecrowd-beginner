tweet = input()

if len(tweet) > 140:
    print('MUTE')

elif len(tweet) <= 140:
    print('TWEET')