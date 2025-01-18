from sqlalchemy import create_engine

# Replace with your actual Redshift credentials
username = "your_username"
password = "your_password"
host = "your_cluster_endpoint"
port = "5439"  # Default Redshift port
database = "your_database_name"

# Create the connection string
connection_string = (
    f"redshift+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Create the SQLAlchemy engine
engine = create_engine(connection_string)
