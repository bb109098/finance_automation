import requests
from core.logger import get_logger

logger = get_logger()

class SignalScraper:

    def fetch_google_news(self):

        url = "https://news.google.com/rss/search?q=banking+fraud+india&hl=en-IN&gl=IN&ceid=IN:en"

        try:
            response = requests.get(url, timeout=10)
            return response.text
        except Exception as e:
            logger.error(f"News fetch error: {e}")
            return None

    def parse_rss(self, xml):

        import xml.etree.ElementTree as ET

        signals = []

        try:
            root = ET.fromstring(xml)

            for item in root.iter("item"):

                title = item.find("title").text
                link = item.find("link").text

                signals.append({
                    "source": "google_news",
                    "title": title,
                    "url": link
                })

        except Exception as e:
            logger.error(f"RSS parse error: {e}")

        return signals

    def run(self):

        xml = self.fetch_google_news()

        if not xml:
            return []

        signals = self.parse_rss(xml)

        logger.info(f"Collected {len(signals)} signals")

        return signals