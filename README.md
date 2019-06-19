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

### 4. 使用 `Rclone` 設定要與 `GoogleDrive` 同步的資料夾

..待補圖

### 5. 開啟 `Container`

..待補圖
