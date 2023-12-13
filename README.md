# My Friend's Twitter Bot (GCP based)

I developed a Twitter bot using the Markov chain model. The motivation behind this project was to put the skills I've been learning into practical use. This bot tweets in a manner reminiscent of my friend at specific intervals.

## Background
To optimize costs and explore new learning opportunities, I migrated the infrastructure technology from AWS to Google Cloud Platform (GCP). The technologies I used include Docker, Google Kubernetes Engine (GKE), and Google Cloud Storage.

I implemented scheduled tasks for the Twitter bot using GKE's CronJobs:
1. **fetch_tweets_cronjob**: Scheduled to run every Sunday night at midnight (Japan time).
   - Utilizes the Twitter API to fetch the latest tweets (up to 100) from my own Twitter account.
   - Appends the newly fetched tweets to the existing tweet data obtained from Google Storage.
   - Performs text preprocessing, including tokenization, to prepare the data for the Markov chain model.

2. **generate_tweets_cronjob**: Scheduled to run every morning at 7 AM (Japan time).
   - Uses the tweet data retrieved from Google Storage to automatically generate new tweets using the Markov chain model.
   - Tweets the generated content.

## Skills Used
- **Language:** Python (Markov chain)
- **Cloud Platform:** Google Cloud Platform (GCP) (Compute Engine, Cloud Storage, Container Registry, Google Kubernetes Engine - GKE)
- **Containerization & Orchestration:** Docker, Kubernetes

## Bot's Twitter Handle
Check out the bot's tweets here: [@UbotInSeattle](https://twitter.com/UbotInSeattle)

![Bot's Screenshot](https://github.com/codekakitai51/u_bot/assets/130334969/dab05e32-ab05-40ea-b2ad-91a285e0a968.png)

Feel free to explore the bot's tweets and its underlying technologies!
