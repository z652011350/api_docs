#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
把整个项目里的 .md 文档按体积分包合并成若干个 bundle_XXX.md，
用于在 ChatGPT 中分批上传。

使用方法：
    1. 把本脚本放在 api_docs 项目根目录（能看到 ArkAnalyzer、classes 的那一层）
    2. 终端运行:  python3 pack_markdowns.py
    3. 生成的文件会放在 output_bundles/ 目录下
"""

import os
from pathlib import Path

# ===== 可调参数 =====

# 项目根目录（默认是脚本所在目录）
ROOT_DIR = Path(__file__).resolve().parent

# 输出目录
OUTPUT_DIR = ROOT_DIR / "output_bundles"

# 每个 bundle 目标最大大小（字节），默认 ~500 KB
MAX_BUNDLE_SIZE = 500 * 1024

# 是否排除某些目录（相对 ROOT_DIR 的路径前缀）
EXCLUDE_DIR_PREFIXES = [
    ".git",
    ".idea",
    ".vscode",
    "node_modules",
    # "_media",  # 如果不想把 _media 里的 md 合进去，可以取消注释这一行
]

# ===== 脚本实现 =====

def should_exclude(path: Path) -> bool:
    """判断是否要排除该路径（目录）。"""
    rel = path.relative_to(ROOT_DIR)
    first_part = rel.parts[0] if rel.parts else ""
    return first_part in EXCLUDE_DIR_PREFIXES


def collect_markdown_files(root: Path):
    """递归收集所有 .md 文件，按路径排序返回列表。"""
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirpath = Path(dirpath)

        # 处理排除目录
        dirnames[:] = [
            d for d in dirnames
            if not should_exclude(dirpath / d)
        ]

        for name in filenames:
            if name.lower().endswith(".md"):
                md_files.append(dirpath / name)

    md_files.sort()
    return md_files


def pack_markdowns(md_files):
    """把 md 文件分批打包到多个 bundle_XXX.md 中。"""
    OUTPUT_DIR.mkdir(exist_ok=True)

    bundle_index = 1
    current_size = 0
    bundle_lines = []

    def flush_bundle():
        nonlocal bundle_index, current_size, bundle_lines
        if not bundle_lines:
            return
        out_path = OUTPUT_DIR / f"bundle_{bundle_index:03d}.md"
        out_path.write_text("".join(bundle_lines), encoding="utf-8")
        print(f"生成: {out_path}  (约 {current_size} 字节)")
        bundle_index += 1
        current_size = 0
        bundle_lines = []

    for md_path in md_files:
        try:
            content = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # 如果遇到编码问题，可以根据实际情况调整
            content = md_path.read_text(encoding="utf-8", errors="ignore")

        rel_path = md_path.relative_to(ROOT_DIR)

        # 为每个文件加一个清晰的分隔头
        header = (
            "\n\n"
            "============================================================\n"
            f"## FILE: `{rel_path.as_posix()}`\n"
            "============================================================\n\n"
        )

        chunk = header + content + "\n\n"
        chunk_size = len(chunk.encode("utf-8"))

        # 如果当前 bundle 已经接近上限，则先写出当前 bundle
        if current_size + chunk_size > MAX_BUNDLE_SIZE and current_size > 0:
            flush_bundle()

        bundle_lines.append(chunk)
        current_size += chunk_size

    # 写出最后一个 bundle
    flush_bundle()


def main():
    print(f"项目根目录: {ROOT_DIR}")
    print("开始收集 Markdown 文件...")
    md_files = collect_markdown_files(ROOT_DIR)
    print(f"共找到 {len(md_files)} 个 .md 文件。")

    pack_markdowns(md_files)
    print("全部完成，bundle 文件保存在 output_bundles/ 目录中。")


if __name__ == "__main__":
    main()