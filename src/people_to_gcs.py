import csv
from google.cloud import storage

# Step 1: Create the CSV file
data = [
    ["name", "age", "DOB", "occupation"],
    ["alif", 26, "28-11-1998", "Software engineer"],
    ["jagannatham", 35, "29-11-1998", "Senior Software engineer"]
]

csv_filename = "people_data.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Step 2: Upload to GCS
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name} in bucket {bucket_name}.")

# Example usage (replace with your actual bucket name and path)
upload_to_gcs("alif_bkt_sample", csv_filename, "alif_bkt_sample/people_data.csv")
