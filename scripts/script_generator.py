from core.logger import get_logger

logger = get_logger()

class ScriptGenerator:

    def generate(self, topic, hook):

        script = f'''
{hook}

Here is the situation: {topic}.

Most people don't realize this rule until they face a charge or restriction.

If this happens, there can be financial consequences.

Always check the rule before performing the transaction.
'''

        return script
