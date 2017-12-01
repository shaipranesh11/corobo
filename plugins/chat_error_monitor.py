import random
import re

from errbot import BotPlugin


class Coala_lowercase_c(BotPlugin):
    """coala is always written with a lower case c."""  # Ignore QuotesBear

    def callback_message(self, msg):
        emots = [':(', ':angry:', ':confounded:',
                 ':disappointed:', ':triumph:' , ':D']

        match_coala = re.search(r'(?:^|[^\w])C+[Oo]+[Aa]+[Ll]+[Aa]+(?:$|[^\w])',
                                msg.body)
        match_sir = 'sir' in msg.body
        if match_sir:
            self.send(
                msg.frm,
                '@{}, please do not use the word \'sir\' '
                'and be more informal to have more fun'.format(
                    msg.frm.nick, emots[5]
                )
            )
            
        if match_coala:
            self.send(
                msg.frm,
                '@{}, coala is always written with a lower case c. {}'.format(
                    msg.frm.nick, emots[random.randint(0, len(emots) - 1)]
                )
            )

        match_cep = re.search(r'(?:^|[^\w])CEP(?:$|[^\w])', msg.body)
        if match_cep:
            self.send(
                msg.frm,
                '@{}, cEP is always written with a lower case c.'.format(
                    msg.frm.nick
                )
            )
