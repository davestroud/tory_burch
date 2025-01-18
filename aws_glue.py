import boto3

# Initialize the Boto3 client for AWS Glue
glue_client = boto3.client("glue")

# Define the crawler parameters
crawler_name = "your_crawler_name"
role_arn = "arn:aws:iam::your_account_id:role/your_glue_role"
database_name = "your_database_name"
s3_target_path = "s3://your-bucket-name/your-folder/"

# Create the crawler
response = glue_client.create_crawler(
    Name=crawler_name,
    Role=role_arn,
    DatabaseName=database_name,
    Targets={"S3Targets": [{"Path": s3_target_path}]},
    TablePrefix="your_table_prefix_",  # Optional: adds a prefix to the table names
    SchemaChangePolicy={
        "UpdateBehavior": "UPDATE_IN_DATABASE",
        "DeleteBehavior": "DEPRECATE_IN_DATABASE",
    },
    RecrawlPolicy={"RecrawlBehavior": "CRAWL_EVERYTHING"},
    Description="Crawler for cataloging data in S3",
    Tags={"Project": "YourProjectName"},
)

print(f"Crawler {crawler_name} created successfully.")
