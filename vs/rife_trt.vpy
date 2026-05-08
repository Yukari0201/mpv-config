import os
import vapoursynth as vs
from vapoursynth import core
import vsmlrt

clip = video_in

w, h = clip.width, clip.height
# 向上取整：1920*1080>===>1920*1152
# w = ((w + 127) // 128) * 128
# h = ((h + 127) // 128) * 128
# 向下取整：1920*1080>===>1920*1024
w = (w // 128) * 128
h = (h // 128) * 128

clip = core.resize.Bicubic(clip, width=w, height=h, format=vs.RGBS, matrix_in_s="709")

clip = vsmlrt.RIFE(
    clip,
    model=4251,  # 模型版本
    multi=2,  # 补帧倍速
    backend=vsmlrt.Backend.TRT(  # 使用的后端
        engine_folder=os.environ.get("HOME") + "/.cache/mpv/vapoursynth",  # .engine 文件目录
        device_id=0,  # 使用的显卡序号：0=第一张显卡
        workspace=None,  # 分配显存的大小：None=自动
        num_streams=4,  # 显卡线程数：1~8
        max_aux_streams=1,  # 最大辅助流数：1~8
        fp16=True,  # 是否使用fp16加速：提升性能但会轻微降低质量
        force_fp16=True,  # 强制使用fp16精度
        use_cuda_graph=True,  # 是否使用cuda加速
        # use_cublas=True,  # 是否使用cuBLAS库：优化矩阵运算
        # use_cudnn=True,  # 是否使用cuDNN库：优化卷积神经网络
        # use_edge_mask_convolutions=True,  # 是否使用边缘掩码卷积：降低性能但减少模糊和重影
        # use_jit_convolutions=True,  # 是否使用即时编译卷积：提升性能但会增加编译时间
        # static_shape=True,  # 是否使用即时编译卷积：提升性能但会增加编译时间
        # heuristic=True,  # 是否使用启发式算法：TRT自动选择最佳算法
        # short_path=True,  # 是否使用短路径优化：减少重复计算
        # builder_optimization_level=5,  # 构建器优化等级：0~5
        # tiling_optimization_level=2,  # 平铺优化等级：0~2
    ),
)

clip = core.resize.Bicubic(clip, format=vs.YUV420P10, matrix_s="709")

clip.set_output()

# 查看模型列表
# python3 -c "import sys;sys.path.append('/usr/lib/vapoursynth');import vsmlrt;[print(f'{m.value:>4} = {m.name}') for m in vsmlrt.RIFEModel]"

# 查看后端列表
# python3 -c "import sys; sys.path.append('/usr/lib/vapoursynth'); import vsmlrt; print(*[b for b in dir(vsmlrt.Backend) if not b.startswith('_')], sep='\n')"
