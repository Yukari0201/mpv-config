import vapoursynth as vs
from vapoursynth import core

clip = video_in

w, h = clip.width, clip.height
# 向上取整：1920*1080>===>1920*1088
w = ((w + 63) // 64) * 64
h = ((h + 63) // 64) * 64
# 向下取整：1920*1080>===>1920*1024
# w = (w // 64) * 64
# h = (h // 64) * 64

clip = core.resize.Bicubic(clip, width=w, height=h, format=vs.RGBS, matrix_in_s="709")

clip = core.rife.RIFE(
    clip,
    model=15,  # 模型版本
    factor_num=2,  # 补帧倍速
    gpu_id=1,  # 使用的显卡序号：0=第一张显卡
    gpu_thread=1,  # 显卡线程数：1~8
    tta=False,  # 是否使用tta：对每帧进行8次不同变换处理，然后取平均值
    uhd=False,
    sc=False,  # 是否使用场景检测
    skip=False,  # 是否跳过插入静态帧(需要 VMAF 插件)
    skip_threshold=60,  # 跳过插入静态帧的检测阈值：默认60
)

clip = core.resize.Bicubic(clip, format=vs.YUV420P10, matrix_s="709")

clip.set_output()

# 查看插件github页面
# https://github.com/styler00dollar/VapourSynth-RIFE-ncnn-Vulkan
