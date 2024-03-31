import logging
import tempfile

import boto3
from botocore.exceptions import ClientError
from src.parser.carrefour import CarrefourReceiptParser
from src.parser.mercadona import MercadonaReceiptParser

logger = logging.getLogger()
logger.setLevel("INFO")
s3_client = boto3.client("s3")

DL_BUCKET = "casterly-app-dl-dev"


def lambda_handler(event, context):
    s3_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]

    splitted_file_name = s3_file_name.split("/")
    user_id = splitted_file_name[0]
    store_name = splitted_file_name[1]

    parser_class = object
    if store_name == "mercadona":
        logger.info("Mercadona receipt")
        parser_class = MercadonaReceiptParser
    elif store_name == "carrefour":
        logger.info("Carrefour receipt")
        parser_class = CarrefourReceiptParser
    else:
        logger.error("Unexpected store '%s'", store_name)
        raise Exception(f"Unexpected store name '{store_name}'")

    with tempfile.NamedTemporaryFile(mode="w+b") as f:
        file_path = f"s3://{s3_bucket_name}/{s3_file_name}"
        logger.info("Downloading file %s", file_path)

        try:
            s3_client.download_fileobj(s3_bucket_name, s3_file_name, f)
        except ClientError:
            logger.error("Failed to download file %s", file_path)
            raise

        receipt = parser_class(f.name).get_receipt_model()

    output_json = receipt.model_dump_json()
    logger.info(output_json)
    s3_client.put_object(
        Bucket=DL_BUCKET,
        Key=f"user_id={user_id}/store_name={store_name}/{receipt.datetime}.json",
        Body=output_json,
    )

    return 200, {"result": "success"}
