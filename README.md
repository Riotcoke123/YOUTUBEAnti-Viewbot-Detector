<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - YouTube Anti-Viewbot Detector</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1, h2 { color: #333; }
        code { background: #f4f4f4; padding: 5px; border-radius: 5px; }
        pre { background: #eee; padding: 10px; border-radius: 5px; overflow-x: auto; }
    </style>
</head>
<body>
    <h1>YouTube Anti-Viewbot Detector</h1>
    <p>This script detects potential viewbots on live YouTube streams by analyzing the ratio of viewers to active chat participants.</p>
    <h2>Features</h2>
    <ul>
        <li>Detects live streams on a given YouTube channel.</li>
        <li>Analyzes viewer count and chat activity.</li>
        <li>Estimates real vs. bot viewers based on chat interaction.</li>
        <li>Logs data in a JSON file.</li>
    </ul>
    <h2>Installation</h2>
    <p>Clone the repository:</p>
    <pre><code>git clone https://github.com/Riotcoke123/YOUYUBEAnti-Viewbot-Detector.git</code></pre>
    <p>Install dependencies:</p>
    <pre><code>pip install google-api-python-client requests</code></pre>
    <h2>Usage</h2>
    <p>Run the script with:</p>
    <pre><code>python script.py</code></pre>
    <p>The script will check for live streams, analyze chat activity, and store the data in <code>data.json</code>.</p>
    <h2>Configuration</h2>
    <p>Modify the following variables in the script:</p>
    <ul>
        <li><code>API_KEY</code> - Your YouTube API key.</li>
        <li><code>CHANNEL_ID</code> - The YouTube channel ID to monitor.</li>
    </ul>
    <h2>Detection Logic</h2>
    <p>The script estimates real viewers using:</p>
    <pre><code>real_viewers = unique_chatters * 3</code></pre>
    <p>If the chat activity is unusually low compared to viewer count, a viewbot warning is issued.</p>
    <h2>License</h2>
    <p>This project is open-source and available under the MIT License.</p>
</body>
</html>
