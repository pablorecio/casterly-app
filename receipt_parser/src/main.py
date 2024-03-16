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

    obj = s3_client.get_object(Bucket=s3_bucket_name, Key=s3_file_name)
    body = obj["Body"]

    print(crawler_class.extract_items(body).model_dump_json())

    return {}
