# 项目配置说明

## ✨ 已完成的配置

### 1. 核心配置文件

- ✅ `index.html` - 主配置文件，包含所有 docsify 配置和插件
- ✅ `README.md` - 首页欢迎页面
- ✅ `_sidebar.md` - 侧边栏导航配置
- ✅ `_navbar.md` - 顶部导航栏配置
- ✅ `_404.md` - 404 错误页面
- ✅ `.nojekyll` - GitHub Pages 配置文件

### 2. 目录索引页面

- ✅ `大数据书籍/README.md` - 大数据书籍目录索引
- ✅ `烂笔头/README.md` - 烂笔头目录索引

### 3. 文档说明

- ✅ `DEPLOY.md` - 部署说明文档
- ✅ `PROJECT_INFO.md` - 本文件，项目配置说明

## 🎨 功能特性

### 已启用的插件

1. **搜索功能** - 全站搜索，支持中文
2. **代码高亮** - 支持多种编程语言（Java, Python, SQL, Bash, JavaScript, TypeScript, Go, Docker 等）
3. **代码复制** - 一键复制代码块
4. **分页导航** - 上一篇/下一篇导航
5. **侧边栏折叠** - 可折叠的侧边栏目录
6. **字数统计** - 显示文章字数和阅读时间
7. **Emoji 支持** - 支持 emoji 表情
8. **图片缩放** - 点击图片可放大查看
9. **返回顶部** - 快速返回页面顶部
10. **外链支持** - 外链在新标签页打开

### 自定义样式

- ✅ 主题色：绿色 (#42b983)
- ✅ 优化的搜索框样式
- ✅ 美化的代码块样式
- ✅ 优化的表格样式
- ✅ 自定义页脚
- ✅ 优化的侧边栏样式
- ✅ 美化的引用块样式

### 配置特性

- ✅ 自动生成目录（最多 4 级）
- ✅ 自动回到顶部
- ✅ 显示文档更新时间
- ✅ History 路由模式
- ✅ 404 页面处理
- ✅ 统一的侧边栏和导航栏

## 📁 目录结构

```
wjh9102.github.io/
├── index.html                          # 主配置文件
├── README.md                           # 首页
├── _sidebar.md                         # 侧边栏配置
├── _navbar.md                          # 顶部导航栏配置
├── _404.md                            # 404 页面
├── .nojekyll                          # GitHub Pages 配置
├── DEPLOY.md                          # 部署说明
├── PROJECT_INFO.md                    # 项目说明（本文件）
│
├── 大数据书籍/                         # 大数据笔记
│   ├── README.md                      # 目录索引
│   ├── Hadoop 权威指南/
│   │   ├── 01Hadoop 入门.md
│   │   ├── 02Hadoop 分布式文件系统.md
│   │   ├── ... (共 12 篇)
│   │   └── assets/                    # 图片资源
│   ├── 深入理解Kafka核心设计原理/
│   │   ├── 01初识Kafka.md
│   │   ├── 02生产者.md
│   │   ├── 03 消费者.md
│   │   └── assets/                    # 图片资源
│   └── ClickHouse原理解析与应用实践/
│       ├── 01ClickHouse 的前世今生.md
│       ├── ... (共 7 篇)
│       └── assets/                    # 图片资源
│
└── 烂笔头/                            # 经验笔记
    ├── README.md                      # 目录索引
    ├── ES 相关.md
    ├── 经验之谈（采坑日记）.md
    └── assets/                        # 图片资源
```

## 🚀 使用方法

### 本地预览

```bash
# 方法 1: 使用 docsify-cli
npm i docsify-cli -g
docsify serve .

# 方法 2: 使用 Python
python -m http.server 3000

# 方法 3: 使用 VS Code Live Server 插件
# 右键 index.html -> Open with Live Server
```

### 部署到 GitHub Pages

1. 推送代码到 GitHub 仓库
2. 在仓库设置中启用 GitHub Pages
3. 选择 main 分支作为源
4. 访问 https://wjh9102.github.io

详细说明请查看 [DEPLOY.md](DEPLOY.md)

## 📝 内容管理

### 添加新文章

1. 在对应目录下创建 Markdown 文件
2. 更新 `_sidebar.md` 添加链接
3. 如果是新分类，更新对应的 `README.md`

### 添加图片

1. 将图片放在对应目录的 `assets` 文件夹中
2. 在 Markdown 中使用相对路径引用：

```markdown
![图片描述](assets/image.png)
```

### 修改样式

在 `index.html` 的 `<style>` 标签中修改 CSS

### 修改配置

在 `index.html` 的 `window.$docsify` 对象中修改配置

## 🎯 导航结构

### 顶部导航栏（_navbar.md）

- 🏠 首页
- 📚 学习笔记
  - 大数据书籍
  - 烂笔头
- 🔗 链接
  - GitHub
  - Docsify 官网

### 侧边栏（_sidebar.md）

- 🏠 首页
- 📚 大数据书籍
  - Hadoop 权威指南（12 篇）
  - 深入理解 Kafka 核心设计原理（3 篇）
  - ClickHouse 原理解析与应用实践（7 篇）
- 📝 烂笔头
  - ES 相关
  - 经验之谈（采坑日记）

## 🔧 自定义建议

### 修改主题色

在 `index.html` 中修改：

```css
:root {
  --theme-color: #42b983;  /* 修改为你喜欢的颜色 */
  --theme-color-dark: #2c8c65;
}
```

### 修改网站标题

在 `index.html` 中修改：

```html
<title>我的个人笔记</title>
```

和

```javascript
window.$docsify = {
  name: '我的技术笔记',
  // ...
}
```

### 添加自定义域名

创建 `CNAME` 文件，内容为你的域名：

```
yourdomain.com
```

### 更换主题

修改 `index.html` 中的主题链接：

```html
<!-- 可选主题：vue.css, buble.css, dark.css, pure.css -->
<link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify@4/lib/themes/vue.css">
```

## 📊 统计信息

- **总文章数**: 22+ 篇
- **大数据书籍**: 22 篇
  - Hadoop 权威指南: 12 篇
  - Kafka: 3 篇
  - ClickHouse: 7 篇
- **烂笔头**: 2 篇
  - ES 相关
  - 经验之谈（25+ 个问题解决方案）

## 🔗 相关链接

- [Docsify 官方文档](https://docsify.js.org/)
- [Docsify 中文文档](https://docsify.js.org/#/zh-cn/)
- [GitHub Pages 文档](https://docs.github.com/cn/pages)

## 📮 联系方式

- GitHub: [wjh9102](https://github.com/wjh9102)

---

*最后更新: 2024-12-16*

