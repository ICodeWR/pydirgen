#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright © 2025 码上工坊（微信公众号，头条号同名）

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Module/Script Name: dir_gen.py
# Author: 码上工坊 (微信公众号，头条号同名）
# Created: 2025-05
# Description: 目录结构生成器脚本（配置文件使用JSON格式）。

import argparse
import json
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="JSON目录生成器")
    parser.add_argument("config", help="JSON配置文件")
    parser.add_argument("-o", "--output", default=".", help="输出目录")
    args = parser.parse_args()

    try:
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)

        # 验证配置
        if "structure" not in config:
            print("错误: 缺少 'structure' 字段")
            sys.exit(1)

        # 设置输出路径
        project_name = config.get("project_name", "my_project")
        output_dir = Path(args.output) / project_name

        # 创建目录结构
        created = create_structure(output_dir, config["structure"])

        print(f"完成! 创建 {created['dirs']}个目录, {created['files']}个文件")
        print(f"位置: {output_dir}")

    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)


def create_structure(base: Path, structure: dict, stats: dict = None):
    if stats is None:
        stats = {"dirs": 0, "files": 0}

    for name, content in structure.items():
        path = base / name

        if isinstance(content, dict):
            # 创建目录
            path.mkdir(parents=True, exist_ok=True)
            stats["dirs"] += 1
            print(f"{path}")

            # 递归创建子内容
            create_structure(path, content, stats)
        else:
            # 创建文件
            path.parent.mkdir(parents=True, exist_ok=True)
            content_str = str(content) if content is not None else ""
            path.write_text(content_str, encoding="utf-8")
            stats["files"] += 1
            print(f"  {name}")

    return stats


if __name__ == "__main__":
    main()
