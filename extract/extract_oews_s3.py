import boto3
import io
import os
from dotenv import load_dotenv
from extract_oews import con

df_oews_data = con.execute("SELECT * FROM raw_oews_data").df()

buffer = io.StringIO()
df_oews_data.to_csv(buffer, index=False)

load_dotenv()
bucket = os.environ["S3_BUCKET"]  # set in .env, kept out of the repo

s3 = boto3.client("s3")
s3.put_object(Bucket=bucket, Key="raw/oews/oews_data.csv", Body=buffer.getvalue())
print("Uploaded oews_data to s3")