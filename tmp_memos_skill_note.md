# Memos 技能整理说明

## 一、目标

这篇笔记整理当前与 **Memos** 相关的技能、安装、配置、验证结果，以及实际踩到的问题和修复方法，便于后续直接复用。

## 二、涉及的技能与位置

### 1) Memos 技能
- 技能名：`openclaw-skills-memos`
- 安装目录：`/home/ralmia/.openclaw/skills/openclaw-skills-memos`
- 主要脚本：`/home/ralmia/.openclaw/skills/openclaw-skills-memos/memos.py`
- 来源页面：<https://lobehub.com/skills/openclaw-skills-memos/skill.md>

### 2) LobeHub Marketplace 注册信息
- 已通过 LobeHub Marketplace 完成注册与安装流程
- 客户端凭据保存位置：`/home/ralmia/.lobehub-market/credentials.json`

## 三、当前环境与配置

### 1) Memos 服务地址
- `MEMOS_URL=http://192.168.5.10:5230/`

### 2) Skill 运行所需环境变量
这个技能要求至少以下环境变量：

- `MEMOS_URL`
- `MEMOS_TOKEN`

其中：
- `MEMOS_URL` 用于指定 Memos 服务地址
- `MEMOS_TOKEN` 用于调用 Memos API

## 四、技能安装过程摘要

执行逻辑大致是：

1. 访问 LobeHub 上该 skill 的说明页
2. 按说明完成 Marketplace 注册
3. 安装 `openclaw-skills-memos`
4. 读取安装后的 `SKILL.md`
5. 再根据 `SKILL.md` 检查运行依赖与环境变量

最终确认：
- skill 已成功安装
- `SKILL.md` 已读取
- 运行前必须有 `MEMOS_URL` 和 `MEMOS_TOKEN`

## 五、实际验证过程

### 1) Token 验证
已拿到有效的 `MEMOS_TOKEN`，并只用于本次运行时验证，没有写入记忆文件。

### 2) 连通性验证
已确认：
- Memos 服务可访问
- Token 有效
- 可以成功调用 API

### 3) 创建测试 memo
已成功创建测试 memo：
- memo 名称：`memos/65`
- uid：`9u9wqStSJUJc6Ghfb7qPxY`
- 访问链接：<http://192.168.5.10:5230/memos/9u9wqStSJUJc6Ghfb7qPxY>

测试内容：

```text
Memos skill smoke test from OpenClaw
#openclaw
```

## 六、发现的技能问题

在实际验证过程中，发现这个 skill 自带两个明显 bug。

### Bug 1：`list_memos()` 参数传递错误

#### 问题现象
执行 `list` 时，脚本没有正确把查询参数传给 requests，导致行为异常。

#### 根因
`list_memos()` 调用 `_request()` 时，参数位置写错了，`params` 没有作为真正的查询参数传递。

#### 修复方式
将：

```python
return _request("GET", "/api/v1/memos", params=params)
```

改为：

```python
return _request("GET", "/api/v1/memos", data=None, params=params)
```

#### 影响
不修的话，`list` 功能会不稳定或直接失败。

---

### Bug 2：`MEMOS_URL` 尾斜杠导致请求路径变成 `//api/...`

#### 问题现象
当 `MEMOS_URL` 使用：

```text
http://192.168.5.10:5230/
```

也就是带尾部 `/` 时，skill 内部直接做字符串拼接：

```python
BASE_URL + endpoint
```

最终会变成：

```text
http://192.168.5.10:5230//api/v1/memos
```

服务端会把这个请求当成前端路由或其他页面请求处理，返回 HTML，而不是 JSON，最后脚本在 JSON 解析阶段报错。

#### 修复方式
将：

```python
BASE_URL = os.getenv("MEMOS_URL")
```

改为：

```python
BASE_URL = (os.getenv("MEMOS_URL") or "").rstrip("/")
```

#### 影响
不修的话，只要环境变量里 URL 带尾 `/`，就可能直接炸。

## 七、当前本地已做的修复

安装目录中的 `memos.py` 已经完成本地修复，包括：

1. `MEMOS_URL` 启动时去掉尾斜杠
2. `list_memos()` 正确传递 `params`

也就是说，**当前这台机器上的已安装版本已经可以正常用**。

## 八、当前可用能力

修复并验证后，当前 skill 已可正常完成至少以下操作：

- 列出 memo（`list`）
- 创建 memo（`create`）

如果后续这个 skill 还支持更多动作，也建议先按同样方式做一次最小验证再正式投入使用。

## 九、使用建议

### 建议 1：把 token 配成正式环境变量
当前 token 已验证有效，但如果以后希望长期稳定调用，最好把以下变量正式配置好：

```bash
export MEMOS_URL="http://192.168.5.10:5230/"
export MEMOS_TOKEN="<你的token>"
```

或者写到系统/服务的环境配置里，而不是每次临时注入。

### 建议 2：保留对时间字段的显示规则
Memos 返回的时间字段（例如 `createTime`、`updateTime`）是 **UTC**。
后续给达叔展示时，应该统一转换为 **北京时间（UTC+8）**。

### 建议 3：交易记录要补 `#trade`
如果后续用 Memos 记交易类内容，写入时需要补上：

```text
#trade
```

## 十、结论

当前 Memos 相关能力已经打通，状态如下：

- LobeHub Marketplace：已注册
- `openclaw-skills-memos`：已安装
- `SKILL.md`：已读取
- `MEMOS_TOKEN`：已验证有效
- Memos API：已打通
- 测试 memo：已成功创建
- 安装 skill 自带 bug：已在本地修复

所以，**现在已经可以继续稳定地用 Memos 做记录**。
