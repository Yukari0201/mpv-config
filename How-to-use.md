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
cp proxy.exapmle.conf proxy.conf
```
- 并根据自己的设备自行更改以上文件的内容

---

## Windows

- 在“安装”完 mpv 和 git 之后，运行：
  - 你的 mpv 配置文件夹一般为 `mpv.exe` 同路径的 `portable_config` 文件夹，没有就新建一个
```
cd <你的 mpv 配置文件夹>
git clone --recurse-submodules https://github.com/Yukari0201/mpv-config.git .
```

- 然后：
```
cp device.exapmle.conf device.conf
cp file_browser.example.conf script-opts/file_browser.conf
cp proxy.exapmle.conf proxy.conf
```
- 并根据自己的设备自行更改以上文件的内容
