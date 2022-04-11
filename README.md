# JoyScore

### Inspiration
A member of our group indicated that they often get YouTube recommendations solely based on what videos they've clicked on, even videos they don't like and wouldn't appreciate similar recommendations for. To counteract the slight inefficiency in video recommendations, we decided to create a product that allows for more accurate suggestions to aid the existing YouTube recommendation algorithm.

### What it does
JoyScore scans the user's face at frequent intervals throughout the duration of the video and determines a quantified value of the user's emotions at each interval. Then, it combines the values of the emotions to create a weighted average of their emotions, which represents their sentiment score. Last, it determines a qualitative value ranging from "Very Strongly Recommend" to "Very Strongly Do Not Recommend", upon which the YouTube Search Algorithm can use the information to aid in its recommendations.

### How we built it
First, we used the OpenCV python library and implemented a timing mechanism to take pictures of the user at given intervals during a video. Next, we utilized the YouTube Data API to determine the length of the video with the potential to harness more information for the algorithm. Then, we analyzed the Google Cloud VisionAI API's implementation in-code, and harnessed the technology to generate user sentiment reports. Last, we generated a weighted average of the user sentiments across all images collected to determine how a video made them feel, which could be used to create personalized video recommendations for them.

### Challenges we ran into
Surprisingly, the vast majority of our errors originated from simple mistakes resulting from a combination of the exhausting conditions of the hackathon and the pressure to deliver a completed product in 24 hours. More importantly, we had plenty of issues in harnessing the information the two APIs delivered to us; after some persistent Googling and caffeinated code review sessions, we were able to overcome them. The hardest part of our project was determining the weights for each emotion; we had lots of trouble determining which emotions matter more than others at first, but we were able to settle on a range of positive and negative weights to assign to each emotion in order to produce an accurate sentiment score that represented the user's emotion appropriately.

### Accomplishments that we're proud of
Honestly, we're just proud of the fact that we were able to deliver our desired product in 24 hours. This was a time crunch and a half, and considering the fact that this was our first hackathon, we're proud of our accomplishment in completing our project.

### What we learned
Really, the most important thing we learned was persistence. We ran into lots of errors in implementing technologies we had little to no experience with and often struggled to overcome those challenges. However, in 24 hours, we learned how to implement Google Cloud APIs, utilize Jupyter Notebook efficiently, create a web app to display our project, and much more.

### What's next for JoyScore
JoyScore's potential for scalability is immense; with slight adjustments, JoyScore can be implemented on nearly every platform for live sentiment analysis, aiding corporations in determining optimal recommendation algorithms.

### Presentation
https://docs.google.com/presentation/d/1Poggs3klNelaZOwd0sZoWmNtK88-MKgKUBtcS13WURU/edit?usp=sharing
