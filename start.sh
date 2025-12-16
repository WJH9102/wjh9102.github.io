#!/bin/bash

# 本地预览脚本

echo "🚀 启动 Docsify 本地预览服务..."
echo ""

# 检查是否安装了 docsify-cli
if command -v docsify &> /dev/null; then
    echo "✅ 使用 docsify-cli 启动服务"
    echo "📍 访问地址: http://localhost:3000"
    echo ""
    docsify serve .
# 检查是否安装了 Python 3
elif command -v python3 &> /dev/null; then
    echo "✅ 使用 Python 3 启动服务"
    echo "📍 访问地址: http://localhost:3000"
    echo ""
    python3 -m http.server 3000
# 检查是否安装了 Python 2
elif command -v python &> /dev/null; then
    echo "✅ 使用 Python 2 启动服务"
    echo "📍 访问地址: http://localhost:3000"
    echo ""
    python -m SimpleHTTPServer 3000
else
    echo "❌ 错误: 未找到可用的服务器"
    echo ""
    echo "请安装以下工具之一："
    echo "  1. docsify-cli: npm i docsify-cli -g"
    echo "  2. Python 3: https://www.python.org/downloads/"
    echo ""
    exit 1
fi

