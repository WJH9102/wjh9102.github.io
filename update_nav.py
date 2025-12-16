#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
自动更新 docsify 导航栏和侧边栏脚本
用法: python3 update_nav.py
"""

import os
import re
import hashlib
from pathlib import Path

# 配置
ROOT_DIR = Path(__file__).parent
DOC_DIR = ROOT_DIR / "doc"
SIDEBAR_FILE = ROOT_DIR / "_sidebar.md"
NAVBAR_FILE = ROOT_DIR / "_navbar.md"

# 需要排除的文件和目录
EXCLUDE_DIRS = {'.git', '.github', 'node_modules', 'assets', '.DS_Store'}
EXCLUDE_FILES = {'README.md', '.DS_Store'}

# 目录图标映射（精确匹配）
CATEGORY_ICONS = {
    '大数据书籍': '📚',
    '烂笔头': '📝',
    'Hadoop 权威指南': '🐘',
    '深入理解Kafka核心设计原理': '📨',
    'ClickHouse原理解析与应用实践': '🗄️',
}

# 关键词图标映射（模糊匹配）
KEYWORD_ICONS = {
    # 大数据相关
    'hadoop': '🐘',
    'kafka': '📨',
    'clickhouse': '🗄️',
    'spark': '⚡',
    'flink': '🌊',
    'hive': '🐝',
    'hbase': '📊',
    'zookeeper': '🦓',
    
    # 数据库相关
    'mysql': '🐬',
    'redis': '🔴',
    'mongodb': '🍃',
    'elasticsearch': '🔍',
    'es': '🔍',
    'oracle': '🔶',
    'postgresql': '🐘',
    
    # 编程语言
    'java': '☕',
    'python': '🐍',
    'javascript': '💛',
    'go': '🐹',
    'scala': '🔺',
    
    # 框架和工具
    'spring': '🍃',
    'docker': '🐳',
    'kubernetes': '☸️',
    'k8s': '☸️',
    'nginx': '🟢',
    'tomcat': '🐱',
    'maven': '📦',
    'git': '🔀',
    
    # 其他技术
    'linux': '🐧',
    'shell': '💻',
    'network': '🌐',
    'security': '🔒',
    'api': '🔌',
    'microservice': '🔧',
    '微服务': '🔧',
    
    # 通用关键词
    '入门': '🚀',
    '基础': '📖',
    '进阶': '📈',
    '实战': '⚔️',
    '原理': '🔬',
    '架构': '🏗️',
    '优化': '⚡',
    '部署': '🚀',
    '配置': '⚙️',
    '安装': '📥',
    '问题': '❓',
    '解决': '✅',
    '经验': '💡',
    '总结': '📝',
}

# 文件夹图标映射（根据关键词）
FOLDER_KEYWORD_ICONS = {
    # 技术相关
    'java': '☕',
    'spring': '🍃',
    'python': '🐍',
    'javascript': '💛',
    'typescript': '💙',
    'go': '🐹',
    'rust': '🦀',
    'cpp': '⚙️',
    'c++': '⚙️',
    
    # 数据库和大数据
    'mysql': '🐬',
    'redis': '🔴',
    'mongodb': '🍃',
    'elasticsearch': '🔍',
    'hadoop': '🐘',
    'kafka': '📨',
    'clickhouse': '🗄️',
    'spark': '⚡',
    'flink': '🌊',
    
    # 开发工具
    'docker': '🐳',
    'kubernetes': '☸️',
    'k8s': '☸️',
    'git': '🔀',
    'nginx': '🟢',
    'tomcat': '🐱',
    
    # 项目类型
    'interview': '💼',
    '面试': '💼',
    'test': '🧪',
    '测试': '🧪',
    'demo': '🎮',
    'example': '📝',
    '示例': '📝',
    
    # 内容类型
    '学习': '📚',
    '笔记': '📓',
    '文档': '📄',
    '资料': '📑',
    '教程': '📖',
    '总结': '📝',
    '经验': '💡',
    '项目': '🚀',
    '工具': '🔧',
    '配置': '⚙️',
    '部署': '🚀',
    '运维': '🔧',
    '监控': '📊',
    '日志': '📋',
    '接口': '🔌',
    'api': '🔌',
    '设计': '🎨',
    '架构': '🏗️',
    '算法': '🧮',
    '数据结构': '🗂️',
    '前端': '🎨',
    '后端': '⚙️',
    '全栈': '🌐',
    '移动端': '📱',
    'web': '🌐',
    'app': '📱',
}

# 默认文件夹图标池（随机选择）
RANDOM_FOLDER_ICONS = [
    '📂', '🗂️', '📁', '🗃️', '📦', '🎁', '🎀', '🎊',
    '🌟', '⭐', '✨', '💫', '🌈', '🎯', '🎪', '🎭',
    '🔮', '💎', '🏆', '🎖️', '🏅', '🥇', '🥈', '🥉',
]

# 文件随机图标池（用于没有匹配到特定图标的文件）
RANDOM_FILE_ICONS = [
    '📝', '📃', '📋', '📄', '📑', '📜', '📰', '🗒️',
    '📌', '📍', '🔖', '🏷️', '💼', '📂', '🗂️', '📁',
    '💡', '⭐', '✨', '🎯', '🎨', '🎪', '🎭', '🎬',
    '🔥', '💎', '🌟', '⚡', '🚀', '🎉', '🎊', '🎈',
    '📚', '📖', '📕', '📗', '📘', '📙', '📓', '📔',
    '🔧', '🔨', '⚙️', '🛠️', '⚒️', '🔩', '⚗️', '🧪',
    '💻', '⌨️', '🖥️', '🖱️', '💾', '💿', '📀', '🗄️'
]


def get_random_icon_for_file(filename):
    """
    根据文件名生成一个稳定的随机图标
    使用哈希确保同一文件名总是得到相同的图标
    """
    # 使用文件名的哈希值来选择图标，确保稳定性
    hash_value = int(hashlib.md5(filename.encode()).hexdigest(), 16)
    icon_index = hash_value % len(RANDOM_FILE_ICONS)
    return RANDOM_FILE_ICONS[icon_index]


def get_random_icon_for_folder(foldername):
    """
    根据文件夹名生成一个稳定的随机图标
    使用哈希确保同一文件夹名总是得到相同的图标
    """
    # 使用文件夹名的哈希值来选择图标，确保稳定性
    hash_value = int(hashlib.md5(foldername.encode()).hexdigest(), 16)
    icon_index = hash_value % len(RANDOM_FOLDER_ICONS)
    return RANDOM_FOLDER_ICONS[icon_index]


def get_icon(name, is_file=False):
    """
    获取目录或文件对应的图标
    :param name: 文件或目录名称
    :param is_file: 是否为文件
    :return: 图标字符
    """
    name_lower = name.lower()
    
    # 1. 精确匹配（优先级最高）
    if name in CATEGORY_ICONS:
        return CATEGORY_ICONS[name]
    
    # 2. 关键词匹配
    if is_file:
        # 文件使用文件关键词匹配
        for keyword, icon in KEYWORD_ICONS.items():
            if keyword in name_lower:
                return icon
    else:
        # 文件夹使用文件夹关键词匹配
        for keyword, icon in FOLDER_KEYWORD_ICONS.items():
            if keyword in name_lower:
                return icon
    
    # 3. 返回随机图标
    if is_file:
        # 文件使用随机图标（基于文件名哈希，保证稳定）
        return get_random_icon_for_file(name)
    else:
        # 文件夹使用随机图标（基于文件夹名哈希，保证稳定）
        return get_random_icon_for_folder(name)


def clean_filename(filename):
    """清理文件名，去除 .md 后缀"""
    return filename.replace('.md', '')


def get_display_name(filename):
    """获取显示名称"""
    # 去除 .md 后缀
    name = clean_filename(filename)
    return name


def url_encode_path(path):
    """对路径中的空格进行 URL 编码"""
    return path.replace(' ', '%20')


def scan_directory(directory, base_path=""):
    """
    递归扫描目录，返回文件树结构
    返回格式: {
        'name': '目录名',
        'path': '相对路径',
        'type': 'dir' or 'file',
        'children': [...]
    }
    """
    items = []
    
    try:
        entries = sorted(os.listdir(directory))
    except PermissionError:
        return items
    
    for entry in entries:
        # 跳过排除的文件和目录
        if entry in EXCLUDE_DIRS or entry in EXCLUDE_FILES or entry.startswith('.'):
            continue
        
        full_path = directory / entry
        relative_path = os.path.join(base_path, entry) if base_path else entry
        
        if full_path.is_dir():
            # 递归处理子目录
            children = scan_directory(full_path, relative_path)
            if children:  # 只添加非空目录
                items.append({
                    'name': entry,
                    'path': relative_path,
                    'type': 'dir',
                    'children': children
                })
        elif full_path.is_file() and entry.endswith('.md'):
            items.append({
                'name': entry,
                'path': relative_path,
                'type': 'file'
            })
    
    return items


def generate_sidebar_content(tree, level=0):
    """生成侧边栏内容"""
    lines = []
    indent = '  ' * level
    
    for item in tree:
        if item['type'] == 'dir':
            # 目录标题（不是链接，只是分组标题）
            icon = get_icon(item['name'], is_file=False)
            lines.append(f"{indent}* {icon} {item['name']}")
            lines.append("")  # 空行
            # 递归处理子项
            lines.extend(generate_sidebar_content(item['children'], level + 1))
        else:
            # 文件链接
            display_name = get_display_name(item['name'])
            icon = get_icon(item['name'], is_file=True)
            encoded_path = url_encode_path(f"doc/{item['path']}")
            lines.append(f"{indent}* [{icon} {display_name}]({encoded_path})")
    
    return lines


def get_first_file_in_tree(tree):
    """递归获取树中的第一个文件"""
    for item in tree:
        if item['type'] == 'file':
            return item
        elif item['type'] == 'dir' and item['children']:
            result = get_first_file_in_tree(item['children'])
            if result:
                return result
    return None


def generate_navbar_content(tree):
    """生成顶部导航栏内容"""
    lines = [
        "* [🏠 首页](/)",
        "",
        "* 📚 学习笔记"
    ]
    
    # 获取一级分类
    for item in tree:
        if item['type'] == 'dir':
            icon = get_icon(item['name'], is_file=False)
            # 查找该分类下的第一个文件
            first_file = get_first_file_in_tree(item['children'])
            if first_file:
                # 链接到第一个文件
                encoded_path = url_encode_path(f"doc/{first_file['path']}")
                lines.append(f"  * [{icon} {item['name']}]({encoded_path})")
            else:
                # 如果没有文件，保持原来的目录链接
                encoded_path = url_encode_path(f"doc/{item['path']}/")
                lines.append(f"  * [{icon} {item['name']}]({encoded_path})")
    
    lines.extend([
        "",
        "* 🔗 链接",
        "  * [GitHub](https://github.com/wjh9102)",
        "  * [Docsify 官网](https://docsify.js.org/)"
    ])
    
    return lines


def update_sidebar():
    """更新侧边栏"""
    print("📝 开始更新侧边栏...")
    
    if not DOC_DIR.exists():
        print(f"❌ 错误: doc 目录不存在: {DOC_DIR}")
        return False
    
    # 扫描目录结构
    tree = scan_directory(DOC_DIR)
    
    if not tree:
        print("⚠️  警告: doc 目录为空")
        return False
    
    # 生成侧边栏内容
    lines = ["<!-- _sidebar.md -->", "", "* [🏠 首页](/)", ""]
    lines.extend(generate_sidebar_content(tree))
    
    # 写入文件
    content = '\n'.join(lines) + '\n'
    SIDEBAR_FILE.write_text(content, encoding='utf-8')
    
    print(f"✅ 侧边栏已更新: {SIDEBAR_FILE}")
    return True


def update_navbar():
    """更新顶部导航栏"""
    print("📝 开始更新顶部导航栏...")
    
    if not DOC_DIR.exists():
        print(f"❌ 错误: doc 目录不存在: {DOC_DIR}")
        return False
    
    # 扫描目录结构（只需要一级）
    tree = scan_directory(DOC_DIR)
    
    if not tree:
        print("⚠️  警告: doc 目录为空")
        return False
    
    # 生成导航栏内容
    lines = generate_navbar_content(tree)
    
    # 写入文件
    content = '\n'.join(lines) + '\n'
    NAVBAR_FILE.write_text(content, encoding='utf-8')
    
    print(f"✅ 顶部导航栏已更新: {NAVBAR_FILE}")
    return True


def show_tree_structure(tree, level=0):
    """显示目录树结构（用于调试）"""
    indent = "  " * level
    for item in tree:
        if item['type'] == 'dir':
            print(f"{indent}📁 {item['name']}/")
            show_tree_structure(item['children'], level + 1)
        else:
            print(f"{indent}📄 {item['name']}")


def main():
    """主函数"""
    print("=" * 60)
    print("🚀 Docsify 导航自动更新脚本")
    print("=" * 60)
    print()
    
    # 检查 doc 目录
    if not DOC_DIR.exists():
        print(f"❌ 错误: doc 目录不存在: {DOC_DIR}")
        print("请确保在项目根目录运行此脚本")
        return
    
    # 扫描并显示目录结构
    print("📂 扫描 doc 目录结构...")
    tree = scan_directory(DOC_DIR)
    print()
    print("📊 目录结构:")
    print("-" * 60)
    show_tree_structure(tree)
    print("-" * 60)
    print()
    
    # 统计信息
    def count_items(tree):
        files = 0
        dirs = 0
        for item in tree:
            if item['type'] == 'dir':
                dirs += 1
                f, d = count_items(item['children'])
                files += f
                dirs += d
            else:
                files += 1
        return files, dirs
    
    file_count, dir_count = count_items(tree)
    print(f"📊 统计: 共 {dir_count} 个目录, {file_count} 个文件")
    print()
    
    # 更新侧边栏
    sidebar_success = update_sidebar()
    print()
    
    # 更新顶部导航栏
    navbar_success = update_navbar()
    print()
    
    # 总结
    print("=" * 60)
    if sidebar_success and navbar_success:
        print("✅ 所有导航文件已成功更新！")
        print()
        print("📝 下一步:")
        print("  1. 检查生成的 _sidebar.md 和 _navbar.md")
        print("  2. 运行 ./start.sh 预览效果")
        print("  3. 提交更改: git add . && git commit -m '更新导航' && git push")
    else:
        print("❌ 更新过程中出现错误，请检查上面的错误信息")
    print("=" * 60)


if __name__ == "__main__":
    main()

