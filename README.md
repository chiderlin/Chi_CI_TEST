## PJ83_DB_API

使用功能API進行自動化部署的研究。


### 任務:
主要研究使用docker架設gitlab, gitlab-runner設定,
並使用gitlab-ci.yml 及 compose.yml 腳本執行自動化部署到遠端docker。

### 結論:
已成功部署，幾點需要注意:
1. 目前只能先建好image 安裝好需要的環境，先行pull到docker image.
2. 要被部署的那端server，先行建好git clone的資料夾位置，在用腳本進行傳輸。

可參考yml檔。

### 主要原因:
目前研究的exector 使用 docker，
在runner一執行的時候就會跑到container裡面，無法使用docker login & docker push & docker pull 把需要的image用腳本拉下來。

可能要了解其他exector的不同，改變exector。(shell or something...?)
