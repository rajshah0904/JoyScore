# JoyScore

### Inspiration
People often complain that their YouTube recommendations are solely based on what videos they've clicked on, including videos that they don't particularly enjoy and wouldn't appreciate similar recommendations for. To counteract the inefficiency in video recommendations, we decided to create a product that allows for more accurate suggestions to aid the existing YouTube recommendation algorithm. 

### What it does
JoyScore scans the user's face at frequent intervals throughout the duration of the video and determines a quantified value of the user's emotions at each interval. Then, it combines the values of the emotions to create a weighted average of their emotions, which represents their sentiment score. Last, it determines a qualitative value ranging from "Very Strongly Recommend" to "Very Strongly Do Not Recommend", upon which the YouTube Search Algorithm can use the information to aid in its recommendations.

### How we built it
First, we used the OpenCV python library and implemented a timing mechanism to take pictures of the user at given intervals during a video. Next, we utilized the YouTube Data API to determine the length of the video with the potential to harness more information for the algorithm. Then, we analyzed the Google Cloud VisionAI API's implementation in-code, and harnessed the technology to generate user sentiment reports. Last, we generated a weighted average of the user sentiments across all images collected to determine how a video made them feel, which could be used to create personalized video recommendations for.

