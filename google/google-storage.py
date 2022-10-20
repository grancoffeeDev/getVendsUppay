import os
import pathlib
import mimetypes
from google.cloud import storage

#https://www.youtube.com/watch?v=1cDqRrw3t9o&ab_channel=JieJenn

STORAGE_CLASSES = ('STANDARD','NEARLINE','CODLINE','ARCHIVE')

class GCStorage:
    def __init__(self, storage_client) -> None:
        self.clint = storage_client
        
working_dir = pathlib.Path.cwd()
files_folder = working_dir.joinpath('My Files')
downloads_folder = working_dir.joinpath('Downloaded')
bucket_name = 'gc_rawdata'