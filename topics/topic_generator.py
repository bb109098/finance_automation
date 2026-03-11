from core.logger import get_logger

logger = get_logger()

PATTERNS_BY_OBJECT = {
    "ATM withdrawal": ["limit penalty", "hidden rule fee"],
    "UPI transfer": ["scam money drain", "mistake money loss"],
    "Credit card": ["mistake money loss", "hidden rule fee"],
    "Loan EMI": ["limit penalty", "hidden rule fee"],
    "Debit card": ["mistake money loss", "hidden rule fee"],
    "Savings account": ["hidden rule fee", "limit penalty"],
    "KYC verification": ["rule account block"],
    "Bank locker": ["liability limit rule"],
    "Bank fraud": ["scam money drain"],
    "Bank scam": ["scam money drain"],
    "OTP fraud": ["scam money drain", "mistake money loss"],
    "Bank transaction": ["hidden rule fee"]
}

OBJECT_KEYWORDS = {
    "atm": "ATM withdrawal",
    "cash": "ATM withdrawal",
    "upi": "UPI transfer",
    "payment": "UPI transfer",
    "credit": "Credit card",
    "card": "Credit card",
    "loan": "Loan EMI",
    "emi": "Loan EMI",
    "debit": "Debit card",
    "savings": "Savings account",
    "account": "Savings account",
    "kyc": "KYC verification",
    "locker": "Bank locker",
    "fraud": "Bank fraud",
    "scam": "Bank scam",
    "otp": "OTP fraud",
    "transaction": "Bank transaction"
}

class TopicGenerator:

    def detect_object(self, text):

        text = text.lower()
        matches = []

        for key, value in OBJECT_KEYWORDS.items():
            if key in text:
                matches.append(value)

        return list(set(matches))


    def generate(self, signals):

        topics = []

        for s in signals:

            title = s.get("title", "")
            objects = self.detect_object(title)

            if not objects:
                continue

            for obj in objects:

                patterns = PATTERNS_BY_OBJECT.get(obj, [])

                for pattern in patterns:

                    topic = f"{obj} {pattern}"
                    topics.append(topic)

        topics = list(set(topics))

        logger.info(f"Generated {len(topics)} topics from signals")

        return topics
