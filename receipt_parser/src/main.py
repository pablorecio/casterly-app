import json
import logging
import tempfile

import boto3
from botocore.exceptions import ClientError
from src.parser.carrefour import CarrefourReceiptCrawler
from src.parser.mercadona import MercadonaReceiptCrawler

logger = logging.getLogger()
logger.setLevel("INFO")
s3_client = boto3.client("s3")


def lambda_handler(event, context):
    s3_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]

    crawler_class = object
    if s3_file_name.startswith("mercadona"):
        logger.info("Mercadona receipt")
        crawler_class = MercadonaReceiptCrawler
    elif s3_file_name.startswith("carrefour"):
        logger.info("Carrefour receipt")
        crawler_class = CarrefourReceiptCrawler

    with tempfile.NamedTemporaryFile(mode="w+b") as f:
        file_path = f"s3://{s3_bucket_name}/{s3_file_name}"
        logger.info("Downloading file %s", file_path)

        try:
            s3_client.download_fileobj(s3_bucket_name, s3_file_name, f)
        except ClientError:
            logger.error("Failed to download file %s", file_path)
            raise

        receipt = crawler_class.extract_items(f.name)
        logger.info(receipt.model_dump_json())

    return json.loads(receipt.model_dump_json())
