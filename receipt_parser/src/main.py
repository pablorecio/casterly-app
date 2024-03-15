from src.parser.carrefour import ReceiptCrawler as CarrefourRC
from src.parser.mercadona import ReceiptCrawler as MercadonaRC


def lambda_handler(event, context):
    s3_bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    s3_file_name = event["Records"][0]["s3"]["object"]["key"]

    crawler_class = object
    if s3_file_name.startswith("mercadona"):
        crawler_class = MercadonaRC
    elif s3_file_name.startswith("carrefour"):
        crawler_class = CarrefourRC

    s3_path = f"s3://{s3_bucket_name}/{s3_file_name}"
    print(crawler_class.extract_items(s3_path).model_dump_json())

    return {}
