# twitter-flask-render

A minimal Flask app for posting tweets via Webhook (for use with Google Apps Script or similar tools).

## Endpoints

- `POST /tweet` — JSON body: `{ "text": "your tweet here" }`
- `GET /` — Health check

## Deploy via Render

Include `render.yaml` and connect your GitHub repo to Render.

## Required environment variables

- `TWITTER_CONSUMER_KEY`
- `TWITTER_CONSUMER_SECRET`
- `TWITTER_ACCESS_TOKEN`
- `TWITTER_ACCESS_SECRET`
