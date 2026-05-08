# mpv-config

个人自用 mpv 配置（目前边用边改）

主要用于 Arch Linux  

排版以 VSCode/VSCodium + Noto Sans Mono CJK SC 为准。

## 如何使用？

首先，我**不推荐**你直接使用我的配置文件。  
我建议你根据我的配置文件的注释以及文末[推荐阅读](#推荐阅读)的文章来自行定制自己的配置文件。

如果你非要使用我的配置(~~自寻不快~~)，请看 [How to use? | 如何使用？](How-to-use.md)

并且建议安装[推荐字体](#字体)

## 字体

我的配置文件用到了 [汉仪正圆-65S](https://pan.acgrip.com/?dir=%E8%B6%85%E7%BA%A7%E5%AD%97%E4%BD%93%E6%95%B4%E5%90%88%E5%8C%85%20XZ/%E5%AE%8C%E6%95%B4%E5%8C%85/Hanyi%20Fonts%EF%BC%88%E6%B1%89%E4%BB%AA%EF%BC%89/%E7%AE%80%E7%B9%81), [Noto Sans CJK SC 和 Noto Sans CJK SC Mono](https://github.com/notofonts/noto-cjk/tree/main/Sans#downloading-noto-sans-cjk) 字体，各位请自行下载安装。

## 着色器 脚本

### 用到的[着色器](./shaders/)

| 名称 | 链接 |
| --- | --- |
| Anime4K | https://github.com/bloc97/Anime4K |
| igv-FSRCNN | https://github.com/igv/FSRCNN-TensorFlow |
| KrigBilateral | https://gist.github.com/igv/a015fc885d5c22e6891820ad89555637 |
| acme-0.5x.hook | https://gist.github.com/bjin/15f307e7a1bdb55842bbb663ee1950ed |

<details>
<summary><strong><code>[点击展开] 曾经用过但不常用的着色器，已移除/考虑未来移除</code></strong></summary>

| 名称 | 链接 |
| --- | --- |
| ~~ACNet~~ | https://github.com/TianZerL/ACNetGLSL |
| ~~AMD-FSR~~ | https://gist.github.com/agyild/82219c545228d70c5604f865ce0b0ce5 |
| ~~antiring.hook~~ | https://github.com/haasn/gentoo-conf/blob/xor/home/nand/.mpv/shaders/antiring.hook |

</details>

### 用到的第三方脚本（[scripts](./scripts/) & [scripts-git](./scripts-git/)）

| 脚本 | 用途 | 补充说明 |
| :---: | ---- | ------- |
| [osc.lua](https://github.com/Yukari0201/mpv-osc-thumbfast/blob/main/osc.lua) |（见下） | [mpv的内置OSC](https://github.com/mpv-player/mpv/blob/master/player/lua/osc.lua) 添加了 thumbfast 支持，另有一些微不足道的改动 <br> 参考甚至很大一部分程度上复制了 [thumbfast 的 vanilla-osc 分支](https://github.com/po5/thumbfast/blob/vanilla-osc/player/lua/osc.lua)  |
| [thumbfast](https://github.com/po5/thumbfast) | 在进度条上显示视频缩略图 |  |
| [quality-menu](https://github.com/christoph-heinrich/mpv-quality-menu) | 运行时更改在线音视频流质量的菜单 | 在 mpv.conf 中写一行 `--script-opts-append=ytdl_hook-all_formats=yes` 可以部分代替这个脚本，参见 https://mpv.io/manual/master/#options-all-formats <br> 我个人**使用 git submodule 进行管理** |
| [file-browser](https://github.com/CogentRedTester/mpv-file-browser) | 简单的文件浏览器 | **如果自行安装**，需手动在 `~~/scripts` 目录（在Linux上可以 `cd ~/.config/mpv/scripts`）运行 `git clone https://github.com/CogentRedTester/mpv-file-browser.git file-browser` 以“安装” <br> 以后更新在 `~~/scripts/file-browser` 目录运行 `git pull` 即可 <br> --- <br> 如果和我一样想用 Git 来备份配置文件，请参考Git官方文档 [7.11 Git 工具 - 子模块](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97) <br> --- <br> 需要自行配置 scripts-opts/file_browser.conf 中的 root=，详见：https://github.com/CogentRedTester/mpv-file-browser/blob/master/docs/file_browser.conf |
| [MPV-Play-BiliBili-Comments (bilibiliAssert)](https://github.com/itKelis/MPV-Play-BiliBili-Comments) | 将B站xml格式弹幕转换为ass格式 | ~~需要 [Play-With-MPV](https://github.com/LuckyPuppy514/Play-With-MPV)~~ 现已兼容 [yt-dlp](https://github.com/yt-dlp/yt-dlp) <br> 我个人**使用 git submodule 进行管理** |
| [sub-fonts-dir-auto.lua](https://github.com/fbriere/mpv-scripts/blob/master/scripts/sub-fonts-dir-auto.lua) | 自动加载播放文件下的字体目录 |  Doc: https://github.com/fbriere/mpv-scripts/blob/master/doc/sub-fonts-dir-auto.md <br> 会覆盖 `~~/fonts` 目录 |
| [inputevent.lua](https://github.com/natural-harmonia-gropius/input-event) | 增强 mpv 的 input.conf | 我用此脚本实现两个功能（详细参见 [input.conf](input.conf)）： <br> 长按右方向键倍速播放，释放恢复 <br> 单击鼠标左键暂停，双击全屏 |

<details>
<summary><strong><code>[点击展开] 曾经用过但不常用的脚本，已移除/考虑未来移除</code></strong></summary>

| 脚本 | 用途 | 补充说明 |
| ---- | ---- | ------- |
| [~~Playlistmanager~~](https://github.com/jonniek/mpv-playlistmanager) | 播放列表增强 | 可被 [select.lua](https://mpv.io/manual/master/#select) 代替(快捷键：`g-p`) |
| [~~autoload~~](https://github.com/mpv-player/mpv/blob/master/TOOLS/lua/autoload.lua) | 自动添加同目录的文件到播放列表 | 已被 [`--autocreate-playlist`](https://mpv.io/manual/master/#options-autocreate-playlist) 代替 <br> --- <br> Playlistmanager 可以代替 autoload，参见 [playlistmanager.conf](https://github.com/jonniek/mpv-playlistmanager/blob/master/playlistmanager.conf) 中的 `loadfiles_on_start` 和 `key_loadfiles` <br> |
| [~~webm~~](https://github.com/ekisu/mpv-webm) | 用于裁剪视频片段 | 输出文件较大时性能表现不理想；我不常用 |
| [~~webm-zh~~](https://github.com/FinnRaze/mpv-webm-zh) | webm 的汉化版 | 同上 |
| [~~webtorrent-mpv-hook~~](https://github.com/mrxdst/webtorrent-mpv-hook) | 让 mpv 实现 torrent 边下边播 | 该 js 脚本相比于其他脚本略显麻烦 |

</details>

---

## 推荐阅读

这部分的文章我是我或多或少参考过的，特此鸣谢

### 有用的链接

- https://mpv.io/manual/master/
- https://hooke007.github.io/
- https://www.bilibili.com/read/readlist/rl502769
- https://www.bilibili.com/read/readlist/rl617174 - 略有过时
- https://github.com/stax76/awesome-mpv
- https://artoriuz.github.io/blog/mpv_upscaling.html
- https://www.bilibili.com/opus/1143203531262525449
- ...

### 别人的配置文件，可以用来参考

排序不分先后，但我可能会把 相关联/风格类似 的放在一块儿

- 开发者 hassn 用过的配置（[已过时](https://github.com/haasn/gentoo-conf#readme)） https://github.com/haasn/gentoo-conf/blob/xor/home/nand/.mpv/config
- 开发者 Argon- 的个人配置 https://github.com/Argon-/mpv-config
- hooke007 - MPV_lazy 配置文件中文注释 https://github.com/hooke007/MPV_lazy/blob/main/portable_config/mpv.conf
- dyphire https://github.com/dyphire/mpv-config
- FinnRaze https://github.com/FinnRaze/mpv-player-config
- GreatRunoob https://github.com/GreatRunoob/mpv-configuration
- ...

## 本人的拙作（如果你不嫌弃，可以参考一下）

- [优化 mpv 播放器的在线视频体验](https://yukari0201.github.io/posts/mpv-streaming-media/) | [Bilibili 版本（**不会**及时更新）](https://www.bilibili.com/read/cv40918035)
- [为 mpv 播放器添加长按倍速功能](https://yukari0201.github.io/posts/adding-long-press-speed-control-to-mpv-player/) | [Bilibili 版本（**不会**及时更新）](https://www.bilibili.com/read/cv41770211)
