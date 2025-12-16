# 🛠️ 脚本工具说明

本项目提供了多个实用脚本，帮助你快速管理和维护 docsify 文档站点。

## 📜 脚本列表

| 脚本名称 | 功能 | 推荐度 | 说明 |
|---------|------|--------|------|
| `update_nav.py` | 自动更新导航 | ⭐⭐⭐⭐⭐ | Python 版本，功能最完整 |
| `update_nav.sh` | 自动更新导航 | ⭐⭐⭐⭐ | Shell 版本，无需 Python |
| `start.sh` | 本地预览 | ⭐⭐⭐⭐⭐ | 启动本地开发服务器 |

## 🚀 快速开始

### 1️⃣ 添加新笔记后自动更新导航

```bash
# 推荐：使用 Python 版本（功能最完整）
python3 update_nav.py

# 或者：使用 Shell 版本（无需 Python）
./update_nav.sh
```

### 2️⃣ 本地预览网站

```bash
./start.sh
```

访问 http://localhost:3000

### 3️⃣ 完整工作流

```bash
# 1. 创建新文章
vim doc/烂笔头/新文章.md

# 2. 自动更新导航
python3 update_nav.py

# 3. 本地预览
./start.sh

# 4. 提交到 GitHub
git add .
git commit -m "添加新文章"
git push
```

## 📖 详细说明

### `update_nav.py` - 导航自动更新脚本 ⭐ 推荐

**功能**：
- 🔍 自动扫描 `doc` 目录下的所有 Markdown 文件
- 📝 自动生成 `_sidebar.md`（侧边栏）
- 🧭 自动生成 `_navbar.md`（顶部导航栏）
- 📊 显示目录结构和统计信息
- 🎨 支持自定义图标

**使用方法**：
```bash
python3 update_nav.py
```

**运行效果**：
```
============================================================
🚀 Docsify 导航自动更新脚本
============================================================

📂 扫描 doc 目录结构...

📊 目录结构:
------------------------------------------------------------
📁 大数据书籍/
  📁 Hadoop 权威指南/
    📄 01Hadoop 入门.md
    ...
📁 烂笔头/
  📄 ES 相关.md
  ...
------------------------------------------------------------

📊 统计: 共 5 个目录, 24 个文件

✅ 侧边栏已更新: _sidebar.md
✅ 顶部导航栏已更新: _navbar.md
```

**自定义图标**：

编辑 `update_nav.py` 中的 `CATEGORY_ICONS` 字典：

```python
CATEGORY_ICONS = {
    '大数据书籍': '📚',
    '烂笔头': '📝',
    'Hadoop 权威指南': '🐘',
    '你的新分类': '🎯',  # 添加新图标
}
```

---

### `update_nav.sh` - Shell 版本

**功能**：与 Python 版本类似，但使用 Shell 实现

**优点**：
- ✅ 无需 Python 环境
- ✅ 执行速度快
- ✅ 适合简单场景

**使用方法**：
```bash
./update_nav.sh
```

---

### `start.sh` - 本地预览脚本

**功能**：启动本地开发服务器

**支持的方式**（按优先级）：
1. docsify-cli（如果已安装）
2. Python 3
3. Python 2

**使用方法**：
```bash
./start.sh
```

然后访问 http://localhost:3000

---

## 💡 使用场景

### 场景 1：添加单篇文章

```bash
# 1. 创建文章
vim doc/烂笔头/Redis实战.md

# 2. 更新导航
python3 update_nav.py

# 3. 预览效果
./start.sh
```

### 场景 2：添加新的书籍分类

```bash
# 1. 创建目录和文章
mkdir -p "doc/大数据书籍/Flink实战"
vim "doc/大数据书籍/Flink实战/01Flink入门.md"

# 2. （可选）添加图标
# 编辑 update_nav.py，在 CATEGORY_ICONS 中添加：
# 'Flink实战': '🌊',

# 3. 更新导航
python3 update_nav.py

# 4. 预览
./start.sh
```

### 场景 3：批量添加文章

```bash
# 1. 批量创建
touch doc/烂笔头/MySQL优化.md
touch doc/烂笔头/Nginx配置.md
touch doc/烂笔头/Docker实战.md

# 2. 编写内容...

# 3. 一键更新
python3 update_nav.py

# 4. 预览和提交
./start.sh
```

---

## ⚙️ 配置说明

### 目录结构要求

```
doc/
├── 大数据书籍/
│   ├── Hadoop 权威指南/
│   │   ├── 01章节.md
│   │   └── assets/          # 图片资源（会被自动排除）
│   └── Kafka/
└── 烂笔头/
    ├── 文章.md
    └── assets/              # 图片资源（会被自动排除）
```

**重要**：
- ✅ 所有笔记必须放在 `doc` 目录下
- ✅ 图片放在 `assets` 文件夹（会被自动排除）
- ✅ 文件名支持中文和空格（空格会自动编码为 `%20`）

### 排除规则

默认排除的文件和目录（在 `update_nav.py` 中配置）：

```python
EXCLUDE_DIRS = {'.git', '.github', 'node_modules', 'assets', '.DS_Store'}
EXCLUDE_FILES = {'README.md', '.DS_Store'}
```

---

## 🔧 常见问题

### Q: 脚本无法执行？

```bash
# 添加执行权限
chmod +x update_nav.py
chmod +x update_nav.sh
chmod +x start.sh
```

### Q: Python 版本要求？

Python 3.6 或更高版本：

```bash
python3 --version
```

### Q: 如何修改图标？

编辑 `update_nav.py` 中的 `CATEGORY_ICONS` 字典。

### Q: 如何自定义导航？

1. 运行脚本生成基础导航
2. 手动编辑 `_sidebar.md` 或 `_navbar.md` 进行微调
3. 注意：下次运行脚本会覆盖手动修改

### Q: 新增文章后导航没更新？

确保：
1. 文件在 `doc` 目录下
2. 文件以 `.md` 结尾
3. 运行了更新脚本
4. 刷新浏览器缓存（Ctrl+F5）

---

## 📚 更多文档

- [脚本使用说明.md](脚本使用说明.md) - 详细的脚本使用指南
- [快速开始.md](快速开始.md) - 快速上手指南
- [DEPLOY.md](DEPLOY.md) - 部署说明
- [PROJECT_INFO.md](PROJECT_INFO.md) - 项目配置详情

---

## 🎯 最佳实践

### 1. 每次添加文章后立即更新

```bash
python3 update_nav.py && ./start.sh
```

### 2. 使用 Git 别名

在 `~/.gitconfig` 中添加：

```ini
[alias]
    update = !python3 update_nav.py && git add _sidebar.md _navbar.md
```

然后可以使用：

```bash
git update
```

### 3. 创建快捷命令

在 `~/.bashrc` 或 `~/.zshrc` 中添加：

```bash
alias docs-update='cd ~/path/to/wjh9102.github.io && python3 update_nav.py'
alias docs-preview='cd ~/path/to/wjh9102.github.io && ./start.sh'
```

---

## 📝 总结

使用这些脚本，你的工作流程将变得非常简单：

```bash
写文章 → 运行脚本 → 预览效果 → 提交代码
```

**一行命令搞定**：

```bash
python3 update_nav.py && ./start.sh
```

就是这么简单！✨

---

*如有问题，请查看 [脚本使用说明.md](脚本使用说明.md) 获取更详细的帮助。*

