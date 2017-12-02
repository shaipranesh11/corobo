from errbot import BotPlugin


class no_sir(BotPlugin):
  """do not use sir to sound more friendly"""  # Ignore QuotesBear

  def callback_message(self, msg):
    emots = [':D']
    if match_sir:
      self.send(
        msg.frm,
        '@{}, donot use \'sir\' in ur conversation. {}'.format(
          msg.frm.nick, emots[0]
				)
			)
