# pairwise-multicam-timecode-sync

## 领域

游戏、图形与多媒体

## 主题

多机位时间码同步

## 说明

时钟漂移、直达声对齐与关键帧切换。

初始状态下 `media/multicam_timecode_sync.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
