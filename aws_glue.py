# TODO: Review this code, may be redundant; I created glue in AWS Portal

# import boto3

# # Initialize the Boto3 client for AWS Glue
# glue_client = boto3.client("glue")

# # Define the crawler parameters
# crawler_name = "tory_burch_crawler"
# role_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
# database_name = "fashion200k_db"
# s3_target_path = "s3://tory-burch/athena-query-results/"

# # Create the crawler
# response = glue_client.create_crawler(
#     Name=crawler_name,
#     Role=role_arn,
#     DatabaseName=database_name,
#     Targets={"S3Targets": [{"Path": s3_target_path}]},
#     TablePrefix="your_table_prefix_",  # Optional: adds a prefix to the table names
#     SchemaChangePolicy={
#         "UpdateBehavior": "UPDATE_IN_DATABASE",
#         "DeleteBehavior": "DEPRECATE_IN_DATABASE",
#     },
#     RecrawlPolicy={"RecrawlBehavior": "CRAWL_EVERYTHING"},
#     Description="Crawler for cataloging data in S3",
#     Tags={"Project": "YourProjectName"},
# )

# print(f"Crawler {crawler_name} created successfully.")
