from flask import Flask, request, jsonify
import os
import tweepy

app = Flask(__name__)

# Twitter認証情報（Renderの環境変数に設定）
consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_SECRET")

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

@app.route("/tweet", methods=["POST"])
def tweet():
    data = request.get_json()
    tweet_text = data.get("text")
    if not tweet_text:
        return jsonify({"error": "No text provided"}), 400

    try:
        api.update_status(tweet_text)
        return jsonify({"status": "success", "text": tweet_text}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "Flask Twitter Webhook is running!", 200

if __name__ == "__main__":
    app.run()
