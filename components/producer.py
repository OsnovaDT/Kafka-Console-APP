"""Contain a custom producer class."""

from logging import getLogger

from confluent_kafka import Producer
from confluent_kafka.cimpl import Message

from constants.log_messages import (
    DELIVERY_FAILED, DELIVERY_FAILED_2, DELIVERY_SENT
)
from constants.constants import REQUIRED_CONFIG_ARGS
from custom_types import ConfigType
from exceptions import ConfigIncorrectError

logger = getLogger(__name__)


class CustomProducer:
    """Custom producer that send messages to the topic."""

    def __init__(self, config: ConfigType) -> None:
        """Create custom producer with config params."""

        if self._is_config_incorrect(config):
            raise ConfigIncorrectError(config)

        self.__producer = Producer(config)

    def send_messages(self, messages: list[str], topic: str) -> None:
        """Send messages to the topic."""

        try:
            for msg in messages:
                self.__producer.poll(0)
                self.__producer.produce(
                    topic,
                    msg.encode("utf-8"),
                    callback=self._send_messages_callback,
                )

            self.__producer.flush()
        except BaseException:
            logger.exception(DELIVERY_FAILED)

    def _send_messages_callback(self, err: str | None, msg: Message) -> None:
        """Handle message sending result."""

        if err is not None:
            logger.error(DELIVERY_FAILED_2.format(err=err))
        else:
            logger.info(
                DELIVERY_SENT.format(
                    topic=msg.topic(), partition=msg.partition()
                )
            )

    def _is_config_incorrect(self, config: ConfigType) -> bool:
        """Check is config contain all required args."""

        unspecified_required_args = set(REQUIRED_CONFIG_ARGS) - set(config)
        return len(unspecified_required_args) > 0
