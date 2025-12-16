#!/bin/bash

# Docsify 导航自动更新脚本 (Shell 版本)
# 用法: ./update_nav.sh

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 配置
DOC_DIR="doc"
SIDEBAR_FILE="_sidebar.md"
NAVBAR_FILE="_navbar.md"

echo "============================================================"
echo "🚀 Docsify 导航自动更新脚本 (Shell 版本)"
echo "============================================================"
echo ""

# 检查 doc 目录
if [ ! -d "$DOC_DIR" ]; then
    echo -e "${RED}❌ 错误: doc 目录不存在${NC}"
    exit 1
fi

# 函数：URL 编码空格
urlencode_space() {
    echo "$1" | sed 's/ /%20/g'
}

# 函数：生成侧边栏
generate_sidebar() {
    echo "📝 生成侧边栏..."
    
    cat > "$SIDEBAR_FILE" << 'EOF'
<!-- _sidebar.md -->

* [🏠 首页](/)

EOF

    # 遍历 doc 目录
    cd "$DOC_DIR"
    
    # 大数据书籍
    if [ -d "大数据书籍" ]; then
        echo "* 📚 大数据书籍" >> "../$SIDEBAR_FILE"
        echo "" >> "../$SIDEBAR_FILE"
        
        # Hadoop 权威指南
        if [ -d "大数据书籍/Hadoop 权威指南" ]; then
            echo "  * 🐘 Hadoop 权威指南" >> "../$SIDEBAR_FILE"
            find "大数据书籍/Hadoop 权威指南" -maxdepth 1 -name "*.md" -type f | sort | while read -r file; do
                filename=$(basename "$file" .md)
                filepath=$(urlencode_space "doc/$file")
                echo "    * [$filename]($filepath)" >> "../$SIDEBAR_FILE"
            done
            echo "" >> "../$SIDEBAR_FILE"
        fi
        
        # Kafka
        if [ -d "大数据书籍/深入理解Kafka核心设计原理" ]; then
            echo "  * 📨 深入理解 Kafka 核心设计原理" >> "../$SIDEBAR_FILE"
            find "大数据书籍/深入理解Kafka核心设计原理" -maxdepth 1 -name "*.md" -type f | sort | while read -r file; do
                filename=$(basename "$file" .md)
                filepath=$(urlencode_space "doc/$file")
                echo "    * [$filename]($filepath)" >> "../$SIDEBAR_FILE"
            done
            echo "" >> "../$SIDEBAR_FILE"
        fi
        
        # ClickHouse
        if [ -d "大数据书籍/ClickHouse原理解析与应用实践" ]; then
            echo "  * 🗄️ ClickHouse 原理解析与应用实践" >> "../$SIDEBAR_FILE"
            find "大数据书籍/ClickHouse原理解析与应用实践" -maxdepth 1 -name "*.md" -type f | sort | while read -r file; do
                filename=$(basename "$file" .md)
                filepath=$(urlencode_space "doc/$file")
                echo "    * [$filename]($filepath)" >> "../$SIDEBAR_FILE"
            done
            echo "" >> "../$SIDEBAR_FILE"
        fi
    fi
    
    # 烂笔头
    if [ -d "烂笔头" ]; then
        echo "* 📝 烂笔头" >> "../$SIDEBAR_FILE"
        find "烂笔头" -maxdepth 1 -name "*.md" -type f | sort | while read -r file; do
            filename=$(basename "$file" .md)
            filepath=$(urlencode_space "doc/$file")
            echo "  * [$filename]($filepath)" >> "../$SIDEBAR_FILE"
        done
        echo "" >> "../$SIDEBAR_FILE"
    fi
    
    cd ..
    
    echo -e "${GREEN}✅ 侧边栏已更新: $SIDEBAR_FILE${NC}"
}

# 函数：生成顶部导航栏
generate_navbar() {
    echo "📝 生成顶部导航栏..."
    
    cat > "$NAVBAR_FILE" << 'EOF'
* [🏠 首页](/)

* 📚 学习笔记
EOF

    cd "$DOC_DIR"
    
    # 添加一级目录
    if [ -d "大数据书籍" ]; then
        echo "  * [📚 大数据书籍](doc/大数据书籍/)" >> "../$NAVBAR_FILE"
    fi
    
    if [ -d "烂笔头" ]; then
        echo "  * [📝 烂笔头](doc/烂笔头/)" >> "../$NAVBAR_FILE"
    fi
    
    cd ..
    
    cat >> "$NAVBAR_FILE" << 'EOF'

* 🔗 链接
  * [GitHub](https://github.com/wjh9102)
  * [Docsify 官网](https://docsify.js.org/)
EOF

    echo -e "${GREEN}✅ 顶部导航栏已更新: $NAVBAR_FILE${NC}"
}

# 函数：统计文件
count_files() {
    echo ""
    echo "📊 统计信息:"
    echo "------------------------------------------------------------"
    
    if [ -d "$DOC_DIR" ]; then
        md_count=$(find "$DOC_DIR" -name "*.md" -type f | wc -l | tr -d ' ')
        dir_count=$(find "$DOC_DIR" -type d | wc -l | tr -d ' ')
        echo "  📁 目录数: $dir_count"
        echo "  📄 Markdown 文件数: $md_count"
    fi
    
    echo "------------------------------------------------------------"
    echo ""
}

# 主流程
main() {
    # 统计文件
    count_files
    
    # 生成侧边栏
    generate_sidebar
    echo ""
    
    # 生成顶部导航栏
    generate_navbar
    echo ""
    
    # 完成
    echo "============================================================"
    echo -e "${GREEN}✅ 所有导航文件已成功更新！${NC}"
    echo ""
    echo "📝 下一步:"
    echo "  1. 检查生成的 _sidebar.md 和 _navbar.md"
    echo "  2. 运行 ./start.sh 预览效果"
    echo "  3. 提交更改: git add . && git commit -m '更新导航' && git push"
    echo "============================================================"
}

# 运行主函数
main

