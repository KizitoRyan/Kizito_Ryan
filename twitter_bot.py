import os
import tweepy
import logging
from dotenv import load_dotenv
from datetime import datetime
from functools import wraps

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def require_connection(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.client:
            logger.error("No Twitter connection")
            return
        return func(self, *args, **kwargs)
    return wrapper

class TwitterReader:
    def __init__(self):
        # Load API credentials
        self.api_key = os.getenv('TWITTER_API_KEY')
        self.api_secret = os.getenv('TWITTER_API_SECRET')
        self.access_token = os.getenv('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        self.bearer_token = os.getenv('TWITTER_BEARER_TOKEN')

        required_keys = {
            'TWITTER_API_KEY': self.api_key,
            'TWITTER_API_SECRET': self.api_secret,
            'TWITTER_ACCESS_TOKEN': self.access_token,
            'TWITTER_ACCESS_TOKEN_SECRET': self.access_token_secret,
            'TWITTER_BEARER_TOKEN': self.bearer_token,
        }

        missing = [key for key, val in required_keys.items() if not val]
        if missing:
            logger.error(f"Missing required environment variables: {', '.join(missing)}")
            self.client = None
            return

        try:
            self.client = tweepy.Client(
                bearer_token=self.bearer_token,
                consumer_key=self.api_key,
                consumer_secret=self.api_secret,
                access_token=self.access_token,
                access_token_secret=self.access_token_secret
            )
            me = self.client.get_me()
            if me.data:
                logger.info("Connected to Twitter successfully")
                self.user_id = me.data.id
                self.username = me.data.username
            else:
                logger.error("Could not fetch user details")
                self.client = None
        except Exception as e:
            logger.error("Failed to connect to Twitter API", exc_info=True)
            self.client = None

    @require_connection
    def read_my_tweets(self, count=10):
        try:
            tweets = self.client.get_users_tweets(
                id=self.user_id,
                max_results=count,
                tweet_fields=['created_at', 'public_metrics', 'text']
            )

            if not tweets.data:
                print("📭 No tweets found on your account!")
                return

            for i, tweet in enumerate(tweets.data, 1):
                created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M")
                metrics = tweet.public_metrics
                print(f"\n🐦 Tweet {i}:")
                print(f"📅 Date: {created_at}")
                print(f"📝 Content: {tweet.text}")
                print(f"📊 Stats: {metrics['like_count']} likes, {metrics['retweet_count']} retweets, {metrics['reply_count']} replies")
                print(f"🔗 URL: https://twitter.com/{self.username}/status/{tweet.id}")
        except Exception as e:
            logger.error("Error reading tweets", exc_info=True)

    @require_connection
    def search_my_tweets(self, keyword):
        try:
            query = f"from:{self.username} {keyword}"
            tweets = self.client.search_recent_tweets(
                query=query,
                max_results=10,
                tweet_fields=['created_at', 'public_metrics']
            )

            if not tweets.data:
                print(f"🔍 No tweets found containing '{keyword}'")
                return

            for i, tweet in enumerate(tweets.data, 1):
                created_at = tweet.created_at.strftime("%Y-%m-%d %H:%M")
                metrics = tweet.public_metrics
                print(f"\n🐦 Match {i}:")
                print(f"📅 Date: {created_at}")
                print(f"📝 Content: {tweet.text}")
                print(f"❤️ Likes: {metrics['like_count']}")
        except Exception as e:
            logger.error("Error searching tweets", exc_info=True)

    @require_connection
    def get_account_stats(self):
        try:
            user = self.client.get_user(
                username=self.username,
                user_fields=['public_metrics', 'created_at', 'description']
            )

            if user.data:
                metrics = user.data.public_metrics
                created_at = user.data.created_at.strftime("%Y-%m-%d")
                print(f"\n📊 ACCOUNT STATS:")
                print(f"👤 Username: @{user.data.username}")
                print(f"📝 Display Name: {user.data.name}")
                print(f"📅 Created: {created_at}")
                print(f"📝 Bio: {user.data.description or 'No bio'}")
                print(f"👥 Followers: {metrics['followers_count']:,}")
                print(f"👤 Following: {metrics['following_count']:,}")
                print(f"🐦 Tweets: {metrics['tweet_count']:,}")
                print(f"📋 Listed: {metrics['listed_count']:,}")
        except Exception as e:
            logger.error("Error fetching account stats", exc_info=True)

    @require_connection
    def post_tweet(self, content):
        try:
            response = self.client.create_tweet(text=content)
            print(f"✅ Tweet posted: https://twitter.com/{self.username}/status/{response.data['id']}")
        except Exception as e:
            logger.error("Failed to post tweet", exc_info=True)


def main():
    reader = TwitterReader()
    if not reader.client:
        print("Cannot continue without Twitter connection.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Read my recent tweets")
        print("2. Search my tweets")
        print("3. Show my account stats")
        print("4. Post a new tweet")
        print("5. Exit")

        choice = input("\nChoose (1-5): ")

        if choice == "1":
            try:
                count = int(input("How many tweets to read? (1-100): "))
                if 1 <= count <= 100:
                    reader.read_my_tweets(count)
                else:
                    print("Please enter a number between 1 and 100")
            except ValueError:
                print("Please enter a valid number")

        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            reader.search_my_tweets(keyword.strip())

        elif choice == "3":
            reader.get_account_stats()

        elif choice == "4":
            content = input("Enter your tweet: ")
            if content.strip():
                reader.post_tweet(content.strip())
            else:
                print("Tweet content cannot be empty")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
