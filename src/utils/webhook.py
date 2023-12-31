import os
import json
import requests
from src.utils.temp_db import temp_data
from src.utils.error_handling import error_handler
from src.config.logger import Logger

logger = Logger()


# This method is responsible to call webhook API:
def call_webhook_with_success(response):
    logger.info("Function call_webhook_with_success method called", response)
    id = temp_data.get('id')
    webhookUrl = temp_data.get('webhookUrl')
    if webhookUrl:
        payload = json.dumps({
            "id": id,
            "status": response.get("status"),
            "data": response.get("data")
        })
        resp = requests.post(webhookUrl, data=payload)
        return resp
    else:
        logger.info("Webhook URL not found in environment variable")
        return None


# This method is responsible for handle error and call webhook:
def call_webhook_with_error(error, code: int):
    logger.info("Function call_webhook_with_error method called", error)
    response = {"status": "failed", "data": {"reason": error}}
    call_webhook_with_success(response)
    raise error_handler(error, code)
