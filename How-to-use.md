# How to use? | 如何使用？

## Linux

- 在安装完成 mpv 和 git 后，运行：
```
cd ~/.config/mpv
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git .
```
- 然后：
```
cp device.exapmle.conf device.conf
cp file_browser.example.conf script-opts/file_browser.conf
```
- 并根据自己的设备自行更改 `device.conf` 和 `script-opts/file_browser.conf` 文件的内容

---

## Windows

- 在“安装”完 mpv 和 git 之后，运行：
  - 你的 mpv 配置文件夹一般为 `mpv.exe` 同路径的 `portable_config` 文件夹，没有就新建一个
```
cd <你的 mpv 配置文件夹>
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git .
git checkout windows
```

- (可选)由于我可能不会及时更新 windows 分支的内容，所以推荐各位 `git checkout windows` 后手动运行如下命令，同步 main 分支的内容
```
git merge main
```
- 然后：
```
cp device.exapmle.conf device.conf
cp file_browser.example.conf script-opts/file_browser.conf
```
- 并根据自己的设备自行更改 `device.conf` 和 `script-opts/file_browser.conf` 文件的内容
