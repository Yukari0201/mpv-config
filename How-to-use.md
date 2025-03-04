# How to use? | 如何使用？

## Linux

在安装完成 mpv 和 git 后，运行：
```
cd ~/.config/mpv
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git .
```

### 然后根据自己的设备自行修改相关选项(见下)

(Tips: 命令行运行 `mpv --vulkan-device=help` 会列出所有可用的设备)

自行修改 `mpv.conf` 的以下部分：
```ini
# [自用] Linux 配置

gpu-api = vulkan
ao = alsa

## 多显卡设置(请自行更改显卡名称)
vulkan-device = 'NVIDIA GeForce RTX 4060 Laptop GPU'

script-opts-append = file_browser-root=~/,/,/mnt/,/run/media/
```

自行修改 `input.conf` 的以下部分：
```ini
## 切换渲染显卡
Ctrl+Alt+g cycle-values vulkan-device "Intel(R) Graphics (ADL GT2)" "NVIDIA GeForce RTX 4060 Laptop GPU"
```

## Windows

### 便携用户

在安装完成 mpv 和 git 后，打开 PowerShell 运行：
```
cd <你的 mpv 安装目录>
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git portable_config
git checkout windows
```
### [scoop](https://scoop.sh/) 用户

前提条件：安装了 `git` 和 `mpv-git`  
安装方式：
```
scoop install git
scoop bucket add extras
scoop install mpv-git
```


scoop 应用安装文件夹一般在 `C:\\Users\<你的用户名>\scoop`
```
cd <scoop 应用安装文件夹>\persist\mpv-git\portable_config
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git .
git checkout windows
```

### 然后根据自己的设备自行修改相关选项(见下)

(Tips: 命令行运行 `mpv --d3d11-adapter=help` 和 `mpv --vulkan-device=help` 会列出所有可用的设备)

自行修改 `mpv.conf` 的以下部分：
```ini
# [自用] Windows 配置

gpu-api = d3d11
snap-window = yes                       # [Windows独占] 贴边吸附
ao = wasapi

## 多显卡设置(请自行更改显卡名称)
d3d11-adapter = 'NVIDIA GeForce RTX 4060 Laptop GPU'
vulkan-device = 'NVIDIA GeForce RTX 4060 Laptop GPU'

script-opts-append = file_browser-root=~/,C:/,D:/
```

自行修改 `input.conf` 的以下部分：
```ini
## 切换渲染显卡
Ctrl+Alt+g cycle-values vulkan-device "Intel(R) UHD Graphics" "NVIDIA GeForce RTX 4060 Laptop GPU"
Ctrl+Alt+G cycle-values d3d11-adapter "Intel(R) UHD Graphics" "NVIDIA GeForce RTX 4060 Laptop GPU"
```
