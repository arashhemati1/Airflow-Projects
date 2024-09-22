from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_alert():
    client = WebClient(token='YOUR_SLACK_API_TOKEN')
    try:
        response = client.chat_postMessage(
            channel='#alerts',
            text="Pipeline completed successfully!"
        )
    except SlackApiError as e:
        print(f"Error sending alert: {e.response['error']}")
