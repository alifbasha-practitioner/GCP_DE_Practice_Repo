from google.cloud import storage
from google.cloud import bigquery

# Initialize clients
storage_client = storage.Client()
bigquery_client = bigquery.Client()

# GCS Example
BUCKET_NAME = "your-bucket-name"  # Replace with your GCS bucket name
bucket = storage_client.bucket(BUCKET_NAME)

# Upload a file (example)
def upload_to_gcs(bucket, filename, data):
    blob = bucket.blob(filename)
    blob.upload_from_string(data)
    print(f"File {filename} uploaded to gs://{BUCKET_NAME}/{filename}.")

# BigQuery Example
DATASET_ID = "your_dataset"  # Replace with your BigQuery dataset ID
TABLE_ID = "your_table"      # Replace with your BigQuery table ID

def insert_data_to_bigquery(dataset_id, table_id, row_data):
    table_ref = bigquery_client.dataset(dataset_id).table(table_id)
    errors = bigquery_client.insert_rows(table_ref, [row_data])
    if errors:
        print(f"Encountered errors while inserting rows: {errors}")
    else:
        print("Data inserted successfully into BigQuery.")



if __name__ == "__main__":
    # Example usage:
    upload_to_gcs(bucket, "test.txt", "Hello, Cloud Storage!")
    insert_data_to_bigquery(DATASET_ID, TABLE_ID, {"message": "Hello, BigQuery!"})
    print("Cloud Run Job completed.")
