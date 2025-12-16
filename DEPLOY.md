# 部署说明

## 本地预览

### 方法一：使用 docsify-cli

1. 安装 docsify-cli

```bash
npm i docsify-cli -g
```

2. 在项目根目录运行

```bash
docsify serve .
```

3. 访问 http://localhost:3000

### 方法二：使用 Python 简易服务器

```bash
# Python 3
python -m http.server 3000

# Python 2
python -m SimpleHTTPServer 3000
```

然后访问 http://localhost:3000

### 方法三：使用 VS Code Live Server 插件

1. 安装 Live Server 插件
2. 右键 index.html，选择 "Open with Live Server"

## 部署到 GitHub Pages

### 1. 推送代码到 GitHub

```bash
git add .
git commit -m "Update docs"
git push origin main
```

### 2. 配置 GitHub Pages

1. 进入 GitHub 仓库设置页面
2. 找到 "Pages" 选项
3. Source 选择 "main" 分支
4. 点击 "Save"

### 3. 访问网站

等待几分钟后，访问：
- https://wjh9102.github.io

## 自定义域名（可选）

如果你有自己的域名：

1. 在项目根目录创建 `CNAME` 文件，内容为你的域名：

```
yourdomain.com
```

2. 在域名服务商处添加 DNS 记录：

```
类型: CNAME
主机记录: @
记录值: wjh9102.github.io
```

## 目录结构

```
.
├── index.html          # 入口文件
├── README.md           # 首页内容
├── _sidebar.md         # 侧边栏配置
├── _navbar.md          # 顶部导航栏配置
├── _404.md            # 404 页面
├── .nojekyll          # GitHub Pages 配置
├── 大数据书籍/         # 大数据笔记目录
│   ├── README.md
│   ├── Hadoop 权威指南/
│   ├── 深入理解Kafka核心设计原理/
│   └── ClickHouse原理解析与应用实践/
└── 烂笔头/            # 经验笔记目录
    ├── README.md
    ├── ES 相关.md
    └── 经验之谈（采坑日记）.md
```

## 注意事项

1. 确保所有文件使用 UTF-8 编码
2. Markdown 文件名中的空格会被 URL 编码，建议使用 `%20` 或 `-` 替代
3. 图片路径使用相对路径，确保在 GitHub Pages 上也能正常显示
4. 修改配置后需要刷新浏览器缓存才能看到效果

## 常见问题

### 1. 页面显示 404

- 检查文件路径是否正确
- 确保 `.nojekyll` 文件存在
- 检查 GitHub Pages 是否已启用

### 2. 侧边栏不显示

- 检查 `_sidebar.md` 文件是否存在
- 确保 `index.html` 中 `loadSidebar: true`

### 3. 搜索功能不工作

- 确保引入了搜索插件
- 检查浏览器控制台是否有错误

### 4. 图片无法显示

- 检查图片路径是否正确
- 确保图片文件已提交到 Git
- 使用相对路径而非绝对路径

## 更新日志

- 2024-12-16: 初始化项目，配置基础功能
- 添加了搜索、代码高亮、分页导航等插件
- 完善了侧边栏和顶部导航栏配置

