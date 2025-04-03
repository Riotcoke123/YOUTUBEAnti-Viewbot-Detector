import requests
import time
import json
from googleapiclient.discovery import build

# Set up YouTube API
API_KEY = "APIKEY"
CHANNEL_ID = "UCLleZKzwtLupGj6fXySbvuA"

# Initialize YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_live_video_id(channel_id):
    request = youtube.search().list(
        part="id",
        channelId=channel_id,
        type="video",
        eventType="live"
    )
    response = request.execute()
    if response["items"]:
        return response["items"][0]["id"]["videoId"]
    return None

def get_stream_data(video_id):
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=video_id
    )
    response = request.execute()
    if "items" in response and response["items"]:
        details = response["items"][0]["liveStreamingDetails"]
        return int(details.get("concurrentViewers", 0)), details.get("activeLiveChatId", None)
    return 0, None

def get_chat_messages(live_chat_id):
    request = youtube.liveChatMessages().list(
        liveChatId=live_chat_id,
        part="snippet,authorDetails",
        maxResults=200
    )
    response = request.execute()
    messages = response.get("items", [])
    unique_users = {msg["authorDetails"]["channelId"] for msg in messages if "authorDetails" in msg}
    return len(messages), len(unique_users)

def detect_viewbot(viewers, chat_messages, unique_chatters):
    if viewers == 0:
        return "No active stream.", 0, 0
    
    chat_rate = chat_messages / max(viewers, 1)  # Prevent division by zero
    real_viewers = unique_chatters * 3  # Estimate: Assuming 1 chatter per 3 real viewers
    bot_viewers = max(viewers - real_viewers, 0)
    
    if viewers > 100 and chat_rate < 0.02:
        return "Potential viewbot detected: High viewers but low chat activity.", real_viewers, bot_viewers
    return "Viewer activity seems normal.", real_viewers, bot_viewers

def save_data(data):
    with open("C:\\Users\\srrm4\\Desktop\\data.json", "w") as f:
        json.dump(data, f, indent=4)

def main():
    video_id = get_live_video_id(CHANNEL_ID)
    if not video_id:
        print("No live stream detected.")
        return
    
    viewers, chat_id = get_stream_data(video_id)
    if chat_id:
        chat_messages, unique_chatters = get_chat_messages(chat_id)
        result, real_viewers, bot_viewers = detect_viewbot(viewers, chat_messages, unique_chatters)
        data = {
            "viewers": viewers,
            "real_viewers": real_viewers,
            "bot_viewers": bot_viewers,
            "chat_messages": chat_messages,
            "unique_chatters": unique_chatters,
            "detection": result
        }
        save_data(data)
        print(f"Viewers: {viewers}, Real Viewers: {real_viewers}, Bot Viewers: {bot_viewers}, Chat Messages: {chat_messages}, Unique Chatters: {unique_chatters}, Detection: {result}")
    else:
        print("Chat data unavailable.")

if __name__ == "__main__":
    while True:
        main()
        time.sleep(60)  # Run every minute
