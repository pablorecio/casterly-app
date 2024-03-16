import tempfile

import boto3
from src.parser.carrefour import ReceiptCrawler as CarrefourRC
from src.parser.mercadona import ReceiptCrawler as MercadonaRC

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    s3_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]

    crawler_class = object
    if s3_file_name.startswith("mercadona"):
        crawler_class = MercadonaRC
    elif s3_file_name.startswith("carrefour"):
        crawler_class = CarrefourRC

    with tempfile.TemporaryFile(mode="w+b") as f:
        s3_client.download_fileobj(s3_bucket_name, s3_file_name, f)

        print(crawler_class.extract_items(f.name).model_dump_json())

    return {}
