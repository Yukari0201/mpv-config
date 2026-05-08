# vapoursynth filter

本目录存放一些自用 vs 滤镜

当前仅在 Linux 上测试过，未来会写 Windows 的教程（挖坑）

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