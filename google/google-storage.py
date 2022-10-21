import os
import pathlib
import mimetypes
from google.cloud import storage
import json
import jsonlines

#https://www.youtube.com/watch?v=1cDqRrw3t9o&ab_channel=JieJenn
#https://googleapis.dev/python/storage/latest/blobs.html#google.cloud.storage.blob.Blob.upload_from_string
#https://googleapis.dev/python/storage/latest/buckets.html#google.cloud.storage.bucket.Bucket.blob

STORAGE_CLASSES = ('STANDARD','NEARLINE','CODLINE','ARCHIVE')

class GCStorage:
    def __init__(self, storage_client) -> None:
        self.client = storage_client
        
    def create_bucket(self, bucket_name, storage_class, bucket_location='southamerica-east1'):
        bucket = self.client.bucket(bucket_name)
        bucket.storage_class = storage_class
        return self.client.create_bucket(bucket, bucket_location)
    
    def get_bucket(self, bucket_name):
        return self.client.get_bucket(bucket_name)
    
    def list_bucket(self):
        buckets = self.client.list_buckets()
        bucket_lst = []
        for b in buckets:
           bucket_lst.append(b.name)
           
        return bucket_lst
        
    def test(self, json_text):
        with jsonlines.open(json_text, 'w') as w:
            w.write_all(json_text)
        return w
    

#variables
#working_dir = pathlib.PureWindowsPath('C:/Users/Home/Documents/google teste/')
#files_folder = 'C:\Users\Home\Documents\google teste\upload'
#downloads_folder = 'C:\Users\Home\Documents\google teste\download'
bucket_name = 'gc_api_demo'
project_id = 'vmgc-e-commerce'
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./google/vmgc-gcs.json"

#GCS instance
storage_client = storage.Client(project_id)
gcs = GCStorage(storage_client)

#create cloud storage bucket
if not bucket_name in gcs.list_bucket():
    bucket_gcs = gcs.create_bucket(bucket_name, STORAGE_CLASSES[0])
else:
    bucket_gcs = gcs.get_bucket(bucket_name)
    
#upload
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
json_object = json.dumps(dictionary)

#blob.upload_from_filename('./google/dummy.json',content_type='application/json')

blob = bucket_gcs.blob('YYdummy.json')
blob.upload_from_string(json_object, content_type='application/json')
