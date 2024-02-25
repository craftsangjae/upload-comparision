from dotenv import load_dotenv
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
import boto3
from botocore.exceptions import NoCredentialsError
import os
import time


load_dotenv()


# boto3 클라이언트 설정
s3_client = boto3.client('s3',
                         endpoint_url='http://minio:9000',
                         aws_access_key_id='minio-access-key',
                         aws_secret_access_key='minio-secret-key',
                         region_name='us-east-1',
                         use_ssl=False)


def upload_file_to_minio(file_path, bucket_name, object_name):
    global s3_client
    try:
        # 파일 업로드
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File {file_path} uploaded to {bucket_name}/{object_name}")
    except NoCredentialsError:
        print("Credentials not available")


class MyHandler(FTPHandler):
    def on_file_received(self, file):
        # 파일 업로드가 완료된 시간을 기록
        end_time = time.time()
        elapsed_time = end_time - self.start_time
        print(f"File {file} upload completed. Time taken: {elapsed_time} seconds.")
        bucket_name = 'ftp-bucket'
        object_name = file.split('/')[-1]  # 파일 이름만 추출
        upload_file_to_minio(file, bucket_name, object_name)


    def ftp_STOR(self, file, mode='w'):
        # 파일 업로드가 시작된 시간을 기록
        self.start_time = time.time()
        # 원래의 STOR 명령 처리 호출
        return super().ftp_STOR(file, mode)
def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "password", "./", perm="elradfmw")
    handler = MyHandler
    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 60010)

    server = FTPServer(("0.0.0.0", 21), handler)
    server.serve_forever()

if __name__ == "__main__":
    main()