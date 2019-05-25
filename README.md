# YoutubeMusicSync

## 目的
可以每天同步特定的Youtube撥放清單中的音樂檔案到Linux伺服器，在同步至GoogleDrive上，讓用戶端(PC、Mobile)可以直接同步mp3檔案
Automatic sync Youtube's playlist mp3 file to Linux, also made on GoogleDrive. For Desktop or Phone can use Youtube music file

## 簡易架構圖
![image](https://github.com/coreyborad/YoutubeMusicSync/blob/master/images/Readme_1.png)

## 安裝需求

* Docker - Need install on host [Github連結](https://github.com/docker/docker-ce)
* Docker-compose - Need install on host [Github連結](https://github.com/docker/compose)
* Rclone - Need install on host [Github連結](https://github.com/ncw/rclone)
* Youtube-dl - Already in Docker [Github連結](https://github.com/ytdl-org/youtube-dl)

## 安裝環境 - 以 Ubuntu 16.04 為例子

### 1. 安裝 Docker
#### [參考網址](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04)

* 增加GPGKey
``` curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - ```

* 增加Docker repository
``` sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" ```

* 更新Package
``` sudo apt-get update ```

* 安裝Docker
``` sudo apt-get install -y docker-ce ```

* 將當前User加入 docker group
``` sudo usermod -aG docker $(whoami) ```
