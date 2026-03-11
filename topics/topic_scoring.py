from core.logger import get_logger

logger = get_logger()

class TopicScorer:

    def score_topic(self, topic):

        score = 0

        topic_lower = topic.lower()

        if "fraud" in topic_lower or "scam" in topic_lower:
            score += 30

        if "fee" in topic_lower or "penalty" in topic_lower:
            score += 25

        if "mistake" in topic_lower or "money loss" in topic_lower:
            score += 25

        if "loan" in topic_lower or "credit" in topic_lower:
            score += 10

        score += 10

        return score


    def rank_topics(self, topics):

        scored = []

        for t in topics:
            s = self.score_topic(t)
            scored.append((t, s))

        scored.sort(key=lambda x: x[1], reverse=True)

        return [x[0] for x in scored]
