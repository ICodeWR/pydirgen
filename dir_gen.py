#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
dir_gen.py - Python 3.11+ 纯标准库目录生成器
支持 JSON 和 TOML 配置文件
"""

import argparse
import json
import sys
from pathlib import Path

import tomllib


def main():
    # 命令行参数
    parser = argparse.ArgumentParser(description="目录结构生成器")
    parser.add_argument("config", help="配置文件 (.json/.toml)")
    parser.add_argument("-o", "--output", default=".", help="输出目录")
    args = parser.parse_args()

    try:
        # 加载配置
        if args.config.endswith(".json"):
            with open(args.config, "r", encoding="utf-8") as f:
                config = json.load(f)
        else:
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
                if not isinstance(content, str):
                    content = str(content)
                path.write_text(content, encoding="utf-8")
                stats["files"] += 1
                print(f"{path.name}")

        print(f"生成项目: {project}")
        create(base, config["structure"])

        # 输出结果
        print(f"\n完成!")
        print(f"位置: {base}")
        print(f"统计: {stats['dirs']}个目录, {stats['files']}个文件")

    except FileNotFoundError:
        print(f"错误: 配置文件 '{args.config}' 不存在")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"错误: JSON 配置文件格式错误 - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
