# 使用:
# sudo pwsh syslink.ps1

# 1. 定义源目录和 VapourSynth 插件目录
$SourceDir = "D:\vsmlrt"
$PluginsDir = "C:\Program Files\VapourSynth\plugins"

# 2. 检查源目录是否存在
if (-not (Test-Path $SourceDir)) {
    Write-Error "错误: 源目录 $SourceDir 不存在！"
    exit
}

# 3. 获取源目录下所有的文件和文件夹（不包括源目录本身）
$Items = Get-ChildItem -Path $SourceDir

foreach ($item in $Items) {
    $targetPath = Join-Path $PluginsDir $item.Name
    
    # 如果目标位置已存在同名文件/文件夹，先删除旧的链接或文件
    if (Test-Path $targetPath) {
        Write-Host "正在清理旧项目: $($item.Name)" -ForegroundColor Gray
        Remove-Item -Path $targetPath -Recurse -Force
    }

    # 根据类型创建链接
    if ($item.PSIsContainer) {
        # 如果是文件夹，创建 Junction (目录联接)
        New-Item -ItemType Junction -Path $targetPath -Value $item.FullName | Out-Null
        Write-Host "已链接目录: $($item.Name)" -ForegroundColor Cyan
    } else {
        # 如果是文件，创建 SymbolicLink (符号链接)
        New-Item -ItemType SymbolicLink -Path $targetPath -Value $item.FullName | Out-Null
        Write-Host "已链接文件: $($item.Name)" -ForegroundColor Green
    }
}

Write-Host "`n所有内容已成功链接到 plugins 根目录！" -ForegroundColor Yellow