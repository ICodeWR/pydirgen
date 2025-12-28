#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dir_gen_by_toml.py - TOML目录生成器
Python 3.11+ 纯标准库
"""

import argparse
import sys
from pathlib import Path

import tomllib


def main():
    # 命令行参数
    parser = argparse.ArgumentParser(description="TOML目录结构生成器")
    parser.add_argument("config", help="TOML配置文件 (.toml)")
    parser.add_argument("-o", "--output", default=".", help="输出目录")
    args = parser.parse_args()

    try:
        # 只支持TOML文件
        if not args.config.endswith(".toml"):
            print("错误: 只支持 .toml 文件")
            sys.exit(1)

        # 加载TOML配置
        with open(args.config, "rb") as f:
            config = tomllib.load(f)

        # 验证配置
        if "structure" not in config:
            print("错误: 配置文件缺少 'structure' 字段")
            sys.exit(1)

        # 创建项目目录
        project = config.get("project_name", "project")
        base = Path(args.output) / project

        # 递归创建目录结构
        stats = {"dirs": 0, "files": 0}

        def create(path: Path, content):
            if isinstance(content, dict):
                path.mkdir(parents=True, exist_ok=True)
                stats["dirs"] += 1
                for name, sub in content.items():
                    create(path / name, sub)
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                # 统一使用utf-8编码写入文件
                content_str = str(content) if content is not None else ""
                path.write_text(content_str, encoding="utf-8")
                stats["files"] += 1
                print(f"{path.name}")

        print(f"生成项目: {project}")
        create(base, config["structure"])

        # 输出结果
        print(f"\n完成!")
        print(f"位置: {base}")
        print(f"统计: {stats['dirs']}个目录, {stats['files']}个文件")

    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
