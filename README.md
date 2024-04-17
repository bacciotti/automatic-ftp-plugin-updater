# Automatic Wordpress Plugin Updater via FTP

This Python script automates the process of updating a WordPress plugin across multiple sites simultaneously by extracting a zip file and uploading it to various servers via FTP. The primary goal is to streamline the plugin update process, particularly for plugins like Elementor PRO that cannot be automatically uploaded.

## Instructions

1. **Create FTP Accounts:**
   - Create an FTP account for each site you wish to update. It's recommended to set the same password for all accounts, as it will be uniquely defined in the `.env` file. Ensure that the FTP accounts specifically point to the `wp-content` folder of your WordPress installation.

2. **Clone This Repository:**
   - Clone this repository to your local machine.

```git clone https://github.com/bacciotti/automatic-ftp-plugin-updater.git```


3. **Rename and Configure Environment Variables:**
- Rename the `.env.example` file to `.env` and fill in the necessary information:
  - `FTP_PASSWORD`: Password for the FTP account.
  - `ZIP_FILE_PATH`: Path of the zip file you want to upload.
  - `ZIP_EXTRACT_FOLDER`: Folder where the zip file will be extracted.

4. **Update Site Information:**
- Populate the dictionary in the `map.py` file with the details of the sites you want to update. Note that the host and username are in the `map.py` file, while the password is in the `.env` file.

5. **Execute the Script:**
- Run the `start.py` file.

## Additional Information

**Virtual Environment:**
- It's recommended to use `pipenv` as a virtual environment to run the script.

**Python Version:**
- This script is developed using Python 3.12 and has not been tested on other versions.

**Process Speed:**
- Unfortunately, the process may be slow due to FTP transmission. It's advisable to let the script run and monitor the log.

**Contributions:**
- Pull requests (PRs) and issues are welcomed for improvements and bug fixes.

Feel free to customize and enhance the script according to your specific requirements. Happy updating!
