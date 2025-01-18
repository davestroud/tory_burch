# import boto3
# import json
# from botocore.exceptions import ClientError

# # Initialize the IAM client
# iam_client = boto3.client("iam")


# def create_role(role_name, trust_policy):
#     try:
#         create_role_response = iam_client.create_role(
#             RoleName=role_name,
#             AssumeRolePolicyDocument=json.dumps(trust_policy),
#             Description="Role for accessing AWS resources",
#         )
#         print(f"Role '{role_name}' created successfully.")
#         return create_role_response["Role"]["Arn"]
#     except ClientError as e:
#         print(f"Error creating role: {e}")
#         exit(1)


# if __name__ == "__main__":
#     role_name = "ToryBurchRole"
#     trust_policy = {
#         "Version": "2012-10-17",
#         "Statement": [
#             {
#                 "Effect": "Allow",
#                 "Principal": {"Service": "ec2.amazonaws.com"},
#                 "Action": "sts:AssumeRole",
#             }
#         ],
#     }
#     create_role(role_name, trust_policy)
