from pathlib import Path
import os
import map as sites
from ftp import FTPUploader, ZipExtractor
from dotenv import load_dotenv

load_dotenv()

"""
Extract the zip file and upload the files to the FTP server
"""
ZipExtractor.extract(os.getenv("ZIP_FILE_PATH"),os.getenv("ZIP_EXTRACT_FOLDER"))
for site in sites.map:
    ftp_uploader = FTPUploader(host=sites.map[site]["host"], username=sites.map[site]["username"])
    ftp_uploader.upload(Path(__file__).parent.resolve() / os.getenv("ZIP_EXTRACT_FOLDER"), 'plugins')
