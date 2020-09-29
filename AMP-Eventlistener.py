"""Sample AMQP Listener for AMP for Endpoint.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pika
import logging
import time
import json
import requests
from logging import handlers
from logging.handlers import RotatingFileHandler
import env_user

# Webex setup
def webexsend(MESSAGE_TEXT):
    URL = env_user.WEBEX_URL
    ACCESS_TOKEN = env_user.WEBEX_ACCESSTOKEN
    ROOM_ID = env_user.WEBEX_ROOMID

    headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN,
               'Content-type': 'application/json;charset=utf-8'}
    post_data = {'roomId': ROOM_ID,
                 'text': MESSAGE_TEXT}

    requests.request("post", URL, headers=headers, json=post_data)


# Logging configuration
amp_logger = logging.getLogger('AMPLogger')
amp_logger.setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler('Logs/amp4e.log', maxBytes=2000000)
handler = logging.handlers.SysLogHandler(address = '/dev/log')
amp_logger.addHandler(handler)
logging.basicConfig(filename = 'Logs/amp4e.log', level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S')

# AMQP setup
con_str = 'amqps://' + env_user.AMQP_USER + ':' + env_user.AMQP_PASS + '@export-streaming.eu.amp.cisco.com:443'

connection = pika.BlockingConnection(pika.URLParameters(con_str))

channel = connection.channel()

channel.queue_declare(queue=env_user.AMQP_STREAM, durable=True, passive=True)

# Define the callback fire off logging and webexsend()
def callback(ch, method, properties, body):
    logging.info(" [x] Received meth:\t%r" % method)
    logging.info(" [x] Received prop:\t%r" % properties)
    logging.info(" [x] Received body:\t%r" % body)

    evntJSON=json.loads(body)

    webexsend(MESSAGE_TEXT=evntJSON['event_type']+ "\t on Client: " + evntJSON['computer']['hostname'])

channel.basic_consume(
    queue=env_user.AMQP_STREAM, on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
logging.info(" [*] Waiting for messages...")
try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
connection.close()
