# mpv-config

个人自用 mpv 配置（目前边用边改）

## [mpv.conf](./mpv.conf)

最初是基于 [MPV_lazy main分支](https://github.com/hooke007/MPV_lazy/blob/main/portable_config/mpv.conf) 魔改而来。

### [profiles.conf](./profiles.conf)

mpv.conf

```conf
include = "~~/profiles.conf"
```

用来放置 普通 profile 和 auto profile，避免干扰到默认配置

## [input.conf](./input.conf)

只是加了着色器相关的内容，以及一点点个性化改动

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
| ACNet | https://github.com/TianZerL/ACNetGLSL |
| AMD-FSR | https://gist.github.com/agyild/82219c545228d70c5604f865ce0b0ce5 |
| ~~antiring.hook~~ | https://github.com/haasn/gentoo-conf/blob/xor/home/nand/.mpv/shaders/antiring.hook |

</details>

### 用到的[脚本](./scripts/)

| 脚本 | 用途 | 补充说明 |
| ---- | ---- | ------- |
| [Playlistmanager](https://github.com/jonniek/mpv-playlistmanager) | 播放列表增强 |  |
| [osc.lua](https://github.com/po5/thumbfast/blob/vanilla-osc/player/lua/osc.lua) |（见下） | 仅仅是 [mpv的内置OSC](https://github.com/mpv-player/mpv/blob/master/player/lua/osc.lua) 添加了 thumbfast 支持 |
| [thumbfast](https://github.com/po5/thumbfast) | 在进度条上显示视频缩略图 |  |
| [quality-menu](https://github.com/christoph-heinrich/mpv-quality-menu) | 运行时更改在线音视频流质量的菜单 | 在 mpv.conf 中写一行 `--script-opts-append=ytdl_hook-all_formats=yes` 可以部分代替这个脚本，参见 https://mpv.io/manual/master/#options-all-formats |
| [file-browser](https://github.com/CogentRedTester/mpv-file-browser) | 简单的文件浏览器 | 需手动在 `~~/scripts` 目录（在Linux上可以 `cd ~/.config/mpv/scripts`）运行 `git clone https://github.com/CogentRedTester/mpv-file-browser.git file-browser` 以“安装” <br> 以后更新在 `~~/scripts/file-browser` 目录运行 `git pull` 即可 <br> --- <br> 如果和我一样想用 Git 来备份配置文件，请参考Git官方文档 [7.11 Git 工具 - 子模块](https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97) <br> --- <br> 需要自行配置 scripts-opts/file_browser.conf 中的 root=，详见：https://github.com/CogentRedTester/mpv-file-browser/blob/master/docs/file_browser.conf |
| [MPV-Play-BiliBili-Comments (bilibiliAssert)](https://github.com/itKelis/MPV-Play-BiliBili-Comments) | 将B站xml格式弹幕转换为ass格式 | ~~需要 [Play-With-MPV](https://github.com/LuckyPuppy514/Play-With-MPV)~~ 现已兼容 [yt-dlp](https://github.com/yt-dlp/yt-dlp) |

<details>
<summary><strong><code>[点击展开] 曾经用过但不常用的脚本，已移除/考虑未来移除</code></strong></summary>

| 脚本 | 用途 | 补充说明 |
| ---- | ---- | ------- |
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
- https://www.bilibili.com/read/readlist/rl617174
- https://github.com/stax76/awesome-mpv
- https://artoriuz.github.io/blog/mpv_upscaling.html
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

## TODOs

兼容 Windows（  
某人转到 Linux 就过河拆桥了（（（  

~~同时避免出现 [`d56a04b`](https://github.com/Yukari0201/mpv-config/commit/d56a04b6bf0ef649524fa46b0f795c737f0165c1) 这样智障的错误~~
