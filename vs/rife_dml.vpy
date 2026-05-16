import vapoursynth as vs
from vapoursynth import core
import vsmlrt

clip = video_in
source_fmt = clip.format

src_w, src_h = clip.width, clip.height
# 向上取整：1920*1080>===>1920*1152
w = ((src_w + 127) // 128) * 128
h = ((src_h + 127) // 128) * 128
# 向下取整：1920*1080>===>1920*1024
# w = (src_w // 128) * 128
# h = (src_h // 128) * 128

clip = core.resize.Bilinear(clip, width=w, height=h, format=vs.RGBH, matrix_in_s="709")

clip = vsmlrt.RIFE(
    clip,
    model=4251,  # 模型版本
    multi=2,  # 补帧倍速
    backend=vsmlrt.BackendV2.ORT_DML(  # 使用的后端
        device_id=1,
        num_streams=1,
        fp16=True,
        output_format=1,
    ),
)

clip = core.resize.Bilinear(clip, width=src_w, height=src_h, format=(source_fmt if source_fmt else vs.YUV420P10), matrix_s="709")

clip.set_output()

# 查看模型列表
# python -c "import vsmlrt;[print(f'{m.value:>4} = {m.name}') for m in vsmlrt.RIFEModel]"

# 查看后端列表
# python -c "import vsmlrt; print(*[b for b in dir(vsmlrt.BackendV2) if not b.startswith('_')], sep='\n')"
