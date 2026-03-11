import json
import random
from signals.signal_scraper import SignalScraper
from signals.competitor_scraper import CompetitorScraper
from topics.topic_generator import TopicGenerator
from topics.topic_scoring import TopicScorer
from hooks.hook_generator import HookGenerator
from scripts.script_generator import ScriptGenerator
from media.scene_planner import ScenePlanner
from core.logger import get_logger

logger = get_logger()

class Pipeline:

    def run(self):

        logger.info("Starting pipeline")

        news_scraper = SignalScraper()
        news_signals = news_scraper.run()

        competitor_scraper = CompetitorScraper()
        competitor_signals = competitor_scraper.scrape()

        signals = news_signals + competitor_signals

        logger.info(f"{len(signals)} total signals collected")

        topic_engine = TopicGenerator()
        topics = topic_engine.generate(signals)

        scorer = TopicScorer()
        topics = scorer.rank_topics(topics)

        topic = random.choice(topics)

        hook_engine = HookGenerator()
        script_engine = ScriptGenerator()
        scene_engine = ScenePlanner()

        hooks = hook_engine.generate(topic)

        script = script_engine.generate(topic, hooks[0])

        scenes = scene_engine.generate(topic, script)

        output = {
            "topic": topic,
            "script": script,
            "scenes": scenes
        }

        with open("scene_output.json", "w", encoding="utf-8") as f:
            json.dump(output, f, indent=4)

        logger.info("Scene output saved")
