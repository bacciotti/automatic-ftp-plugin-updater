import os
import zipfile
from dotenv import load_dotenv
import ftputil

load_dotenv()

"""
Class to upload files to an FTP server
"""
class FTPUploader:
    def __init__(self, host=None, username=None, password=None, port=21):
        print(f"Connecting to {host}...")
        self.host = host if host else os.getenv("FTP_HOST")
        self.username = username if username else os.getenv("FTP_USER")
        self.password = password if password else os.getenv("FTP_PASSWORD")
        self.port = port

    def upload(self, local_path, remote_path):
        with ftputil.FTPHost(self.host, self.username, self.password, self.port) as ftp_host:
            self._ftp_upload(ftp_host, local_path, remote_path)

    def _ftp_upload(self, ftp_host, src_path, dst_path=None):
        if dst_path is None:
            dst_path = ftp_host.curdir

        if src_path.is_dir():
            if not ftp_host.path.exists(dst_path):
                ftp_host.mkdir(dst_path)

            for src_child in src_path.iterdir():
                if src_child.is_dir():
                    dst_child = ftp_host.path.join(dst_path, src_child.stem)
                    self._ftp_upload(ftp_host, src_child, dst_child)
                else:
                    if src_child.name != ".DS_Store":
                        dst_child = ftp_host.path.join(dst_path, src_child.name)
                        ftp_host.upload(src_child, dst_child)
                        print(f"Sending: {src_child}")
        else:
            print(f"src_path: '{src_path}' must be an existing directory!")


class ZipExtractor:
    @staticmethod
    def extract(zip_file_path, extract_folder):
        try:
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)
            print("ZIP file extracted successfully.")
        except Exception as e:
            print(f"Some error occurred extracting the ZIP file: {e}")
