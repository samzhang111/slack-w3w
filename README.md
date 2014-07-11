# Slack and What3Words

This is a Flask endpoint for Slack's Outgoing Webhooks that senses when
users type [What3Words](http://what3words.com) compatible addresses.

No API keys are needed!

Our team's instance is hosted live at
[dssg.herokuapp.com/receive](http://dssg.herokuapp.com/receive);
feel free to use it yourself. Just drop it into
[Outgoing Webhooks](https://dssg.slack.com/services/new/outgoing-webhook).

We haven't implemented support for OneWords yet, but feel free to submit a pull
request!

### Example use:

"Blah blah today we're going to get coffee at pass.hears.tiger"

Slack WebHooks sends a message to the channel that says:

"[http://w3w.co/pass.hears.tigers](http://w3w.co/pass.hears.tigers)"
