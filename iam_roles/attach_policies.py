# import boto3
# from botocore.exceptions import ClientError

# # Initialize the IAM client
# iam_client = boto3.client("iam")


# def attach_policy_to_role(role_name, policy_arn):
#     try:
#         iam_client.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
#         print(f"Attached policy '{policy_arn}' to role '{role_name}'.")
#     except ClientError as e:
#         print(f"Error attaching policy '{policy_arn}': {e}")


# if __name__ == "__main__":
#     role_name = "ToryBurchRole"
#     policies = [
#         "arn:aws:iam::aws:policy/AdministratorAccess",
#         "arn:aws:iam::aws:policy/AmazonS3FullAccess",
#         "arn:aws:iam::aws:policy/AmazonAthenaFullAccess",
#         "arn:aws:iam::aws:policy/AmazonGlueFullAccess",
#         # Add other policies as needed
#     ]

#     for policy_arn in policies:
#         attach_policy_to_role(role_name, policy_arn)
