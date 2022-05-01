import text2emotion as emotion
import nltk

#
#  >>> import nltk
#  >>> nltk.download('omw-1.4')
#

#nltk.download('omw-1.4')




text = "Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary? How that patient's privacy is respected? I don't understand. When they ask you to get naked and cover yourself with a piece of cloth are there security guys watching the show? OMG this is wrong in so many levels... This is a HIPAA violation. Cameras can't be installed on exam rooms. It is called A.B."


reviews = [
        "Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary? How that patient's privacy is respected? I don't understand. When they ask you to get naked and cover yourself with a piece of cloth are there security guys watching the show? OMG this is wrong in so many levels... This is a HIPAA violation. Cameras can't be installed on exam rooms. It is called A.B.",
        "We just had the most amazing breakfast! My husband had Eggs Benedict and I had Huevos Ranchero. Both were excellent in!\nThe staff was outstanding. We were...",
        "They really do have the best breakfast. A large menu, with unique items you can't get anywhere else in Cody. This may be the ONLY place where you can get...",
        "It has been a long time since I have eaten at a subway. Today I ate at the one on Center Street. It was clean. There were some very nice ladies working...",
        "Great service! The poor girl working was the only one there today and the line was super long. She was very quick and apologetic that there was no one else..."
        ]

for review in reviews:
    print(emotion.get_emotion(review))


#user_emotion = emotion.get_emotion(text)
#print(type(user_emotion))

#a = {'Happy': 0.18, 'Angry': 0.0, 'Surprise': 0.18, 'Sad': 0.18, 'Fear': 0.45}
#values = max(list(a.values()))
#
#
#
#print(values)














