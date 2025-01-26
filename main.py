"""Main script for running the app in console."""

from logging import getLogger

from components.producer import CustomProducer
from constants.log_messages import INTERNAL_ERROR

# TODO:
config = {
    "bootstrap.servers": "localhost:9093"
}
logger = getLogger(__name__)

messages = ["hello world", "привет"]

topic = "test_topic"


if __name__ == "__main__":
    try:
        producer = CustomProducer(config)
        producer.send_messages(messages, topic)
    except BaseException:
        logger.error(INTERNAL_ERROR)
