from core.logger import get_logger

logger = get_logger()

HOOK_PATTERNS = [
'Most people do not know this rule',
'This mistake costs money',
'Banks quietly charge this fee',
'This can freeze your account'
]

class HookGenerator:

    def generate(self, topic):

        hooks = [f'{h}: {topic}' for h in HOOK_PATTERNS]

        logger.info(f'Generated hooks for {topic}')
        return hooks
