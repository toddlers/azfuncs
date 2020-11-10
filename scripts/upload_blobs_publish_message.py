#!/usr/bin/env python
from azure.storage.blob import BlobServiceClient
from azure.storage.queue import (
        QueueClient,
        BinaryBase64EncodePolicy,
        BinaryBase64DecodePolicy
)
import os,,sys
from time import sleep


INPUT_CONTAINER_NAME='inputitems'
OUTPUT_CONTAINER_NAME='outputitems'
STORAGE_ACCOUNT_NAME='<>'
QUEUE_NAME='<>'
AZURE_STORAGE_CONNECTION_STRING='DefaultEndpointsProtocol=https;AccountName=<ACCOUNT_NAME>;AccountKey=<SECRET>;EndpointSuffix=core.windows.net'

blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# Create a file in local data directory to upload and download
local_path = "~/Downloads"
local_file_name = sys.argv[1]
upload_file_path = os.path.join(local_path, local_file_name)

# Create a blob client using the local file name as the name for the blob
blob_client = blob_service_client.get_blob_client(container=INPUT_CONTAINER_NAME, blob=local_file_name)

# delete the blob if it exists with the same name
if blob_client.exists():
    blob_client.delete_blob()
    
print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

# Upload the created file
with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)
print("\nListing blobs...")

# get the container client
input_container_client = blob_service_client.get_container_client(INPUT_CONTAINER_NAME)
output_container_client = blob_service_client.get_container_client(OUTPUT_CONTAINER_NAME)

# List the blobs in the container
blob_list = input_container_client.list_blobs()
print(f'\nListing blobs in {INPUT_CONTAINER_NAME}')
for blob in blob_list:
    print("\t" + blob.name)
    
# The input is not a valid Base-64 string as it contains a non-base 64 character, more than two padding characters,
# or an illegal character among the padding characters.

queue_client = QueueClient.from_connection_string(
    AZURE_STORAGE_CONNECTION_STRING,
    QUEUE_NAME
    )
    

# Setup Base64 encoding and decoding functions
queue_client.message_encode_policy = BinaryBase64EncodePolicy()
queue_client.message_decode_policy = BinaryBase64DecodePolicy()

print("\nAdding message: " + local_file_name)

message_bytes = local_file_name.encode('ascii')
queue_client.send_message(queue_client.message_encode_policy.encode(content=message_bytes))

# Peek at the first message
messages = queue_client.peek_messages()
for peeked_message in messages:
    print(f'\nPeeked message in queue  named {QUEUE_NAME} : {peeked_message.content}')
    
# wait for some time to let the function finished
sleep(20)
# List the blobs in the container
blob_list = output_container_client.list_blobs()
print(f'\nListing blobs in {OUTPUT_CONTAINER_NAME}')
for blob in blob_list:
    print("\t" + blob.name)
