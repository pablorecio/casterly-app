terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.40"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_s3_bucket" "user_receipts" {
  bucket = "casterly-user-receipts"

  tags = {
    Name = "User Receipts"
  }
}

resource "aws_s3_bucket_versioning" "versioning_user_receipts" {
  bucket = aws_s3_bucket.user_receipts.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "user_receipts_encryption" {
  bucket = aws_s3_bucket.user_receipts.bucket
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket" "lambda_deployments" {
  bucket = "casterly-lambda-deployments"

  tags = {
    Name = "Lambda Deployments"
  }
}

resource "aws_s3_bucket_versioning" "versioning_lambda_deployments" {
  bucket = aws_s3_bucket.lambda_deployments.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "lambda_deployments_encryption" {
  bucket = aws_s3_bucket.user_receipts.bucket
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

resource "aws_iam_policy" "iam_policy_for_lambda" {

  name        = "aws_iam_policy_for_terraform_aws_lambda_role"
  path        = "/"
  description = "AWS IAM Policy for managing aws lambda role"
  policy      = <<EOF
{
 "Version": "2012-10-17",
 "Statement": [
   {
     "Action": [
       "logs:CreateLogGroup",
       "logs:CreateLogStream",
       "logs:PutLogEvents"
     ],
     "Resource": "arn:aws:logs:*:*:*",
     "Effect": "Allow"
   }
 ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "attach_iam_policy_to_iam_role" {
  role       = aws_iam_role.iam_for_lambda.name
  policy_arn = aws_iam_policy.iam_policy_for_lambda.arn
}

# tflint-ignore: terraform_required_providers, terraform_unused_declarations
data "archive_file" "zip_the_python_code" {
  type        = "zip"
  source_dir  = "${path.module}/../invoice_parser/src/"
  output_path = "${path.module}/../invoice_parser/src/invoice-parser.zip"
}

resource "aws_lambda_function" "terraform_lambda_func" {
  filename      = "${path.module}/../invoice_parser/src/invoice-parser.zip"
  function_name = "InvoiceParser"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "lambda.lambda_handler"
  runtime       = "python3.12"
  depends_on    = [aws_iam_role_policy_attachment.attach_iam_policy_to_iam_role]
}

resource "aws_lambda_permission" "allow_bucket" {
  statement_id  = "AllowExecutionFromS3Bucket"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.terraform_lambda_func.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.user_receipts.arn
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.user_receipts.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.terraform_lambda_func.arn
    events              = ["s3:ObjectCreated:*"]
    filter_suffix       = ".pdf"
  }

  depends_on = [aws_lambda_permission.allow_bucket]
}
