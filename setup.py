import boto3
import json
from botocore.exceptions import ClientError

# Initialize the IAM client
iam_client = boto3.client("iam")

# Define the role name
role_name = "ToryBurchRole"  # Replace with your desired role name

# Define the trust policy for the role
trust_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },  # Replace with the appropriate service
            "Action": "sts:AssumeRole",
        }
    ],
}

# Create the IAM role
try:
    create_role_response = iam_client.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust_policy),
        Description="Role for Your Project",
    )
    print(f"Role '{role_name}' created successfully.")
except ClientError as e:
    print(f"Error creating role: {e}")
    exit(1)

# List of required policies
required_policies = [
    "AdministratorAccess",
    "SecretsManagerReadWrite",
    "IAMFullAccess",
    "AmazonS3FullAccess",
    "AmazonAthenaFullAccess",
    "ComprehendFullAccess",
    "AmazonEC2ContainerRegistryFullAccess",
    "AmazonRedshiftFullAccess",
    "AWSStepFunctionsFullAccess",
    "AmazonKinesisFullAccess",
    "AmazonKinesisFirehoseFullAccess",
    "AmazonKinesisAnalyticsFullAccess",
]

# Attach the required policies to the role
for policy_name in required_policies:
    policy_arn = f"arn:aws:iam::aws:policy/{policy_name}"
    try:
        iam_client.attach_role_policy(RoleName=role_name, PolicyArn=policy_arn)
        print(f"Attached policy '{policy_name}' to role '{role_name}'.")
    except ClientError as e:
        print(f"Error attaching policy '{policy_name}': {e}")
