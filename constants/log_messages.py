"""Messages's templates for logging."""

INTERNAL_ERROR: str = "Internal error, sorry!"

DELIVERY_FAILED: str = "Message delivery failed"
DELIVERY_FAILED_2: str = DELIVERY_FAILED + ": {err}"

DELIVERY_SENT: str = \
    "Message delivered to topic {topic} and partition {partition}"
