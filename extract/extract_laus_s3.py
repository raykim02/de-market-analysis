import boto3
import io
import os
from dotenv import load_dotenv
from extract_laus import extract_laus, series_ids
import pandas as pd

df_lookup, df_data = extract_laus(series_ids)

buffer = io.StringIO()
df_data.to_csv(buffer, index=False)

load_dotenv()
bucket = os.environ["S3_BUCKET"]  # set in .env, kept out of the repo

s3 = boto3.client("s3")
s3.put_object(Bucket=bucket, Key="raw/laus/laus_data.csv", Body=buffer.getvalue())
print("Uploaded to s3")