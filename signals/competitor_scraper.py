import subprocess
import json

class CompetitorScraper:

    def __init__(self):

        self.channels = [
            "https://www.youtube.com/@BossWallah/videos"
        ]


    def scrape(self):

        videos = []

        for channel in self.channels:

            cmd = [
                "yt-dlp",
                "--dump-json",
                "--flat-playlist",
                channel
            ]

            result = subprocess.run(cmd, capture_output=True, text=True)

            lines = result.stdout.splitlines()

            for line in lines[:30]:

                data = json.loads(line)

                videos.append({
                    "title": data.get("title"),
                    "url": "https://youtube.com/watch?v=" + data.get("id")
                })

        return videos
