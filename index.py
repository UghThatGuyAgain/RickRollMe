import twitter, time
from pygame import mixer
api = twitter.Api()

mixer.init()
mixer.music.load("rickroll.mp3")
print(api.VerifyCredentials())
recentMention = ""
i = 0
while True:
    i = 1
    mentions = api.GetMentions(since_id=1009604523982286848, trim_user=True)
    print(mentions)
    if recentMention == mentions[0]:
        print("recent mention is the same")
        time.sleep(13)
        continue
    recentMention = mentions[0]
    time.sleep(13)
    if i == 0:
        continue
    print("recent mention is DIFFERENT")
    mixer.music.play()
    continue
