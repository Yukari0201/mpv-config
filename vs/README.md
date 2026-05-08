# vapoursynth filter

本目录存放一些自用 vs 滤镜

~~当前仅在 Linux 上测试过，未来会写 Windows 的教程（挖坑）~~ 坑已经填了

## RIFE 补帧

修改自：https://www.bilibili.com/opus/1143203531262525449

- [rife_trt.vpy](rife_trt.vpy)
  - **NVIDIA Only**
  - 依赖：[vs-mlrt](https://github.com/AmusementClub/vs-mlrt)
  - Install depends:
    - Arch Linux:
      1. Install VapourSynth
          ```shell
          sudo pacman -U https://archive.archlinux.org/packages/v/vapoursynth/vapoursynth-73-2-x86_64.pkg.tar.zst
          ```
      2. Install vs-mlrt and RIFE models
          ```shell
          yay -S vapoursynth-plugin-mlrt-trt-runtime-git vapoursynth-plugin-mlrt-ext-models-rife
          ```
    - Windows:
      1. Install Python
          ```pwsh
          sudo scoop install python -g
          sudo reg import "C:\ProgramData\scoop\apps\python\current\install-pep-514.reg"
          ```
      2. Install VapourSynth: https://github.com/vapoursynth/vapoursynth/releases/tag/R73
          - 本人仅提供安装版教程，便携版请举一反三
          - 安装版本人仅测试过 **默认路径的为所有用户安装**，**更改了安装路径的** 或 **仅为当前用户安装** 路径不同
      3. Install vs-mlrt: https://github.com/AmusementClub/vs-mlrt/releases
          - 你需要下载以下文件:
            ```
            vsmlrt-windows-x64-tensorrt.<version>.7z.*
            ```
          - 解压 vsmlrt-windows-x64-tensorrt.<version>.7z.* 到 `C:\Program Files\VapourSynth\plugins`
          - Tip: 其实符号链接也可以用哒，我让AI写了一个脚本，见 [syslink.ps1](../syslink.ps1)  
            **记得改 `$SourceDir` ！！！**
          - 将 `vsmlrt.py` 符号链接到 `C:\ProgramData\scoop\persist\python\Lib\site-packages\vsmlrt.py`  
            **！！！如果使用了 `syslink.ps1` ，请将 `C:\Program Files\VapourSynth\plugins\vsmlrt\vsmlrt.py` 更改为你的 `vsmlrt.py` 的实际路径！！！**
            ```pwsh
            sudo pwsh -c 'New-Item -ItemType SymbolicLink -Path "C:\ProgramData\scoop\persist\python\Lib\site-packages\vsmlrt.py" -Target "C:\Program Files\VapourSynth\plugins\vsmlrt\vsmlrt.py"'
            ```
      4. Install RIFE models: https://github.com/AmusementClub/vs-mlrt/releases/download/external-models
          - 你至少需要下载以下文件:
            ```
            rife_v4.25_lite.7z
            ```
          - 解压 rife_v4.25_lite.7z\rife\rife_v4.25_lite.onnx 到 `C:\Program Files\VapourSynth\plugins\models\rife`
          - Tip: 符号链接的话，解压到 `$SourceDir\models\rife` 也行的

- [rife_ncnn.vpy](rife_ncnn.vpy)
  - 依赖：[VapourSynth-RIFE-ncnn-Vulkan](https://github.com/styler00dollar/VapourSynth-RIFE-ncnn-Vulkan)
  - Install depends:
    - Arch Linux:
      1. Install VapourSynth
          ```shell
          sudo pacman -U https://archive.archlinux.org/packages/v/vapoursynth/vapoursynth-73-2-x86_64.pkg.tar.zst
          ```
      2. Install VapourSynth-RIFE-ncnn-Vulkan
          ```shell
          yay -S vapoursynth-plugin-rife-ncnn-vulkan
          ```