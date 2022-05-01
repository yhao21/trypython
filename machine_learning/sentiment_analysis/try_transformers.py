

from transformers import pipeline



reviews = [
        "Service is good and all I'm just concerned about having a camera in the patient's room... since when that is necessary? How that patient's privacy is respected? I don't understand. When they ask you to get naked and cover yourself with a piece of cloth are there security guys watching the show? OMG this is wrong in so many levels... This is a HIPAA violation. Cameras can't be installed on exam rooms. It is called A.B.",
        "We just had the most amazing breakfast! My husband had Eggs Benedict and I had Huevos Ranchero. Both were excellent in!\nThe staff was outstanding. We were...",
        "They really do have the best breakfast. A large menu, with unique items you can't get anywhere else in Cody. This may be the ONLY place where you can get...",
        "It has been a long time since I have eaten at a subway. Today I ate at the one on Center Street. It was clean. There were some very nice ladies working...",
        "Great service! The poor girl working was the only one there today and the line was super long. She was very quick and apologetic that there was no one else..."
        ]

sentiment_pipeline = pipeline("sentiment-analysis")
for review in reviews:

    result = sentiment_pipeline(review)
    print(result)
#[{'label': 'NEGATIVE', 'score': 0.9912099838256836}]
#[{'label': 'POSITIVE', 'score': 0.9998795986175537}]
#[{'label': 'NEGATIVE', 'score': 0.963663637638092}]
#[{'label': 'POSITIVE', 'score': 0.992476761341095}]
#[{'label': 'NEGATIVE', 'score': 0.9841775894165039}]
