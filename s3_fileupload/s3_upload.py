from boto3.session import Session
import os
class s3_upload:
    def __init__(self):

        self.AWS_ACCESS_KEY_SS = os.environ.get(f'AWS_ACCESS_KEY_SS')
        self.AWS_SECRET_KEY_SS = os.environ.get(f'AWS_SECRET_KEY_SS')

    def put_in_s3(self,file_path,**kwargs):
        session = Session(aws_access_key_id=self.AWS_ACCESS_KEY_SS, aws_secret_access_key=self.AWS_SECRET_KEY_SS)
        s3 = session.resource('s3')
        bucket = '*****'
        s3_file_path = file_path
        file_name = file_path[file_path.rfind('/') + 1:]
        object = s3.Object(bucket, file_name).upload_file(s3_file_path)
    
