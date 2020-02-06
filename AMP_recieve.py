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
import env_user

con_str = 'amqps://' + env_user.AMQP_USER + ':' + env_user.AMQP_PASS + '@export-streaming.eu.amp.cisco.com:443'

connection = pika.BlockingConnection(pika.URLParameters(con_str))

channel = connection.channel()

channel.queue_declare(queue="event_stream_829", durable=True, passive=True)


def callback(ch, method, properties, body):
    print("\n [x] Received %r" % body)


channel.basic_consume(
    queue="event_stream_829", on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')

channel.start_consuming()