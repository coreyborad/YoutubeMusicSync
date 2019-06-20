# YoutubeMusicSync

## 目的
可以每天同步特定的Youtube撥放清單中的音樂檔案到Linux伺服器，在同步至GoogleDrive上，讓用戶端(PC、Mobile)可以直接同步mp3檔案
Automatic sync Youtube's playlist mp3 file to Linux, also made on GoogleDrive. For Desktop or Phone can use Youtube music file

## 簡易架構圖
![image](https://github.com/coreyborad/YoutubeMusicSync/blob/master/images/Readme_1.png)

## 安裝需求

* Docker - Need install on host - [Github連結](https://github.com/docker/docker-ce)
* Docker-compose - Need install on host - [Github連結](https://github.com/docker/compose)
* Rclone - Need install on host - [Github連結](https://github.com/ncw/rclone)
* Youtube-dl - Already in Docker - [Github連結](https://github.com/ytdl-org/youtube-dl)

## 安裝環境 - 以 `Ubuntu 16.04` 為例子

### 1. 安裝 `Docker` - [安裝參考網址](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

增加 GPGKey

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

增加 Docker repository

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

更新 Package

    sudo apt-get update

安裝 Docker

    sudo apt-get install -y docker-ce

將當前 User 加入 Docker group

    sudo usermod -aG docker $(whoami)

### 2. 安裝 `Docker-compose` - [安裝參考網址](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

下載 Docker-compose，並移動到 bash 目錄使得docker-compose可以直接變成指令操作

    sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

變更docker-compose的權限，使其可被執行

    sudo chmod +x /usr/local/bin/docker-compose

### 3. 安裝 `Rclone`

這邊可以參考官方提供的安裝方式

    https://rclone.org/install/

或者，可以直接執行官方提供的安裝Scripts

    curl https://rclone.org/install.sh | sudo bash

安裝完成後，執行看看 `Rclone` 是否安裝完畢

    ubuntu@corey:~$ rclone -V
    rclone v1.48.0
    - os/arch: linux/amd64
    - go version: go1.12.6

### 4. 使用 `Rclone` 設定要與 `GoogleDrive` 連結

輸入下面指令設定 `Rclone` Config

    rclone config

會出現下列選項，請選擇 `n`

    n) New remote
    s) Set configuration password
    q) Quit config

接著輸入名稱，可以隨便輸入

    name> googledrive
    
接著會出現要你選擇的雲端服務，選擇 第12 `GoogleDrive` 

    Type of storage to configure.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
    1 / A stackable unification remote, which can appear to merge the contents of several remotes
       \ "union"
    2 / Alias for an existing remote
       \ "alias"
     3 / Amazon Drive
       \ "amazon cloud drive"
     4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
       \ "s3"
     5 / Backblaze B2
       \ "b2"
     6 / Box
       \ "box"
     7 / Cache a remote
       \ "cache"
     8 / Dropbox
       \ "dropbox"
     9 / Encrypt/Decrypt a remote
       \ "crypt"
    10 / FTP Connection
       \ "ftp"
    11 / Google Cloud Storage (this is not Google Drive)
       \ "google cloud storage"
    12 / Google Drive
       \ "drive"
    13 / Hubic
       \ "hubic"
    14 / JottaCloud
       \ "jottacloud"
    15 / Koofr
       \ "koofr"
    16 / Local Disk
       \ "local"
    17 / Mega
       \ "mega"
    18 / Microsoft Azure Blob Storage
       \ "azureblob"
    19 / Microsoft OneDrive
       \ "onedrive"
    20 / OpenDrive
       \ "opendrive"
    21 / Openstack Swift (Rackspace Cloud Files, Memset Memstore, OVH)
       \ "swift"
    22 / Pcloud
       \ "pcloud"
    23 / QingCloud Object Storage
       \ "qingstor"
    24 / SSH/SFTP Connection
       \ "sftp"
    25 / Webdav
       \ "webdav"
    26 / Yandex Disk
       \ "yandex"
    27 / http Connection
       \ "http"

不用輸入Client ID，按下  `Enter` 

    Google Application Client Id
    Setting your own is recommended.
    See https://rclone.org/drive/#making-your-own-client-id for how to create your own.
    If you leave this blank, it will use an internal key which is low performance.
    Enter a string value. Press Enter for the default ("").
    client_id>

不用輸入Client ID，按下  `Enter` 

    Google Application Client Secret
    Setting your own is recommended.
    Enter a string value. Press Enter for the default ("").
    client_secret>

選擇 `Full access`

    Scope that rclone should use when requesting access from drive.
    Enter a string value. Press Enter for the default ("").
    Choose a number from below, or type in your own value
     1 / Full access all files, excluding Application Data Folder.
       \ "drive"
     2 / Read-only access to file metadata and file contents.
       \ "drive.readonly"
       / Access to files created by rclone only.
     3 | These are visible in the drive website.
       | File authorization is revoked when the user deauthorizes the app.
       \ "drive.file"
       / Allows read and write access to the Application Data folder.
     4 | This is not visible in the drive website.
       \ "drive.appfolder"
       / Allows read-only access to file metadata but
     5 | does not allow any access to read or download file content.
       \ "drive.metadata.readonly"
    scope> 1

留白，按 `Enter` 繼續

    ID of the root folder
    Leave blank normally.
    Fill in to access "Computers" folders. (see docs).
    Enter a string value. Press Enter for the default ("").
    root_folder_id>

留白，按 `Enter` 繼續

    Service Account Credentials JSON file path
    Leave blank normally.
    Needed only if you want use SA instead of interactive login.
    Enter a string value. Press Enter for the default ("").
    service_account_file>

不需要進階設定，選擇 `n`

    Edit advanced config? (y/n)
    y) Yes
    n) No
    y/n> n

選擇 `n` ，因為是在remote的機器上

    Remote config
    Use auto config?
     * Say Y if not sure
     * Say N if you are working on a remote or headless machine
    y) Yes
    n) No
    y/n> n

會要求你與你的 `Google`帳號要權限，將出現的網址貼在瀏覽器，最後你會拿到一組 `Token` ，貼在後面

    If your browser doesn't open automatically go to the following link: https://accounts.google.com/o/oauth2/auth?access_type=offline&client_id=XXXXXXXXasdasdasdXXXXXXXXXXXXXXXXXXXXXX
    Log in and authorize rclone for access
    Enter verification code>(Token貼在這)

選擇 `n`

    Configure this as a team drive?
    y) Yes
    n) No
    y/n> n

可以對照一下config，沒問題選擇 `y`

    --------------------
    [googledrive]
    type = drive
    scope = drive
    token = {"access_token":"balala"}
    --------------------
    y) Yes this is OK
    e) Edit this remote
    d) Delete this remote
    y/e/d> y

選擇 `q` ，離開設定

    e) Edit existing remote
    n) New remote
    d) Delete remote
    r) Rename remote
    c) Copy remote
    s) Set configuration password
    q) Quit config
    e/n/d/r/c/s/q> q

### 5. 開啟 `Container`

..待補圖
