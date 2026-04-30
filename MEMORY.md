# MEMORY.md - Long-term Memory

## 偏好 & 规则

- **Memos 时间显示**：所有 Memos 记录的时间字段（createTime、updateTime 等）均为 UTC，展示时必须转换为北京时间（UTC+8）给达叔看。
- **Memos 交易记录标签**：涉及交易记录时，在 memos 中增加记录必须补充 `#trade` 标签。
- **IMA 想去的餐厅笔记**：当达叔发来想去的餐厅信息时，默认更新到 IMA 笔记《想去的餐厅》（note_id: `7454524851634077`）。更新前先读取原文，保留已有内容，在末尾追加/整理新餐厅信息；不要误写到知识库。当前已知内容包括福满面、铁屋。

## 工具 & 配置

- **Memos**：`MEMOS_URL=http://192.168.5.10:5230/`，skill 在 `/home/ralmia/.openclaw/skills/openclaw-skills-memos/`
- **IMA 知识库 ID**：`hSR70WQcK-lJ9h___KeBMlt0C6Sxoutl35eMZhi6cXQ=`
