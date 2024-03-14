# Casterly: groceries parser

This project contains all the components required to process different groceries
receipts and store them in a queryable and standard format. Initially, this is built
taking Spain's Mercadona as the base.

## Initial concept

As a first iteration I am just building the Python code to extract the wanted data
for every receipt: items, date, total amount, etc...

In future iterations, this code will turn into an AWS lambda function that will get
executed when new files land in a certain S3 bucket. Ideally we want to build a complete
pipeline that will receive the email with the receipt and landing the data into a DWH.

Lastly, we will want to serve this information via an API and/or present it in a consumable
way for the users.

<!-- BEGIN_TF_DOCS -->
## Requirements

No requirements.

## Providers

No providers.

## Modules

No modules.

## Resources

No resources.

## Inputs

No inputs.

## Outputs

No outputs.
<!-- END_TF_DOCS -->
