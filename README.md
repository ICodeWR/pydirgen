<div align="center">
  <img src="assets/logo.png" width=256></img>
<p><strong>PyDirGen</strong>：超精简目录结构生成器</p>

<!-- [English](README.en.md) | 简体中文 -->
</div>

# PyDirGen - 超精简目录结构生成器

## 简介

一个轻量级的Python工具，通过JSON或TOML配置文件自动生成项目目录结构。

## 特点
- 🚀 **极简代码**: 每个版本 < 60行
- 📦 **零依赖**: 仅使用Python标准库
- ⚡ **快速使用**: 简单的命令行接口
- 🔧 **灵活配置**: 支持JSON和TOML格式


## 项目目录结构

```
pydirgen/
├── README.md              # 项目文档
├── pyproject.toml         # 项目配置（含依赖）
├── assets/                # 资源文件目录
├── examples/              # 示例配置
│   ├── simple.json
│   └── simple.toml
├── dir_gen_by_json.py     #使用JSON格式配置文件的练习代码实现
├── dir_gen_by_toml.py     #使用TOML格式配置文件的练习代码实现
├── dir_gen.py             #配置文件格式二合一的练习代码实现
└── LICENSE                #开源协议文件，本例使用Apache License Version 2.0
```

## 安装

无需安装！直接下载Python文件即可使用：

```bash
# 克隆仓库
git clone https://github.com/ICodeWR/pydirgen.git

cd pydirgen
```

## 使用

```bash
# 使用二合一版本（推荐）
python dir_gen.py examples/simple.json -o ./output
python dir_gen.py examples/simple.toml -o ./output

# 或使用特定版本
python dir_gen_by_json.py examples/simple.json -o ./output
python dir_gen_by_toml.py examples/simple.toml -o ./output
```

## 配置语法

### JSON配置文件核心字段详解

#### 1. **project_name** (必需)
```json
"project_name": "MyPythonApp"
```
- **类型**: 字符串
- **说明**: 项目名称，将作为输出目录的名称
- **规则**: 
  - 不能包含路径分隔符 (`/`, `\`)
  - 建议使用字母、数字、下划线、连字符
  - 长度建议 1-50 字符

#### 2. **structure** (必需)
```json
"structure": {
  // 目录和文件定义
}
```
- **类型**: 对象
- **说明**: 定义项目目录结构的根节点
- **规则**:
  - 必须是对象类型
  - 不能为空对象 `{}`（至少定义一个项目）
  - 支持无限层级嵌套

---

### JSON配置目录结构节点类型

#### 类型1: 目录节点 (Directory Node)
```json
{
  "src": {                    // 键: 目录名
    "main.py": "内容"        // 值: 对象，包含子项
  }
}
```
**特征**:
- 值类型为 `object` 或 `null`
- 包含子节点（文件或子目录）
- 生成时会创建对应目录

**示例**:
```json
"docs": {                    // 创建 docs 目录
  "api": {                   // 创建 docs/api 子目录
    "index.md": "# API"      // 在 docs/api 中创建文件
  }
}
```

#### 类型2: 文件节点 (File Node)
```json
{
  "README.md": "# 项目文档"  // 键: 文件名, 值: 字符串
}
```
**特征**:
- 值类型为 `string`
- 无子节点
- 生成时会创建对应文件并写入内容

**示例**:
```json
"main.py": "print('Hello')",        // 普通文件
".gitignore": "*.pyc\n__pycache__/", // 点开头文件
"空文件.txt": ""                     // 空内容文件
```

---


### TOML 配置文件规范

#### 基本要求
- 文件后缀：`.toml`
- 编码：UTF-8
- 支持TOML v1.0格式

---


#### 必需部分

##### 1. `project_name` - 项目名称
```toml
project_name = "我的项目"  # 将作为生成的文件夹名
```

##### 2. `[structure]` - 结构定义表（核心）
```toml
[structure]  # 必须要有这个表
```

---



#### TOML配置结构定义方法（两种方式）

##### 方式1：点号分隔路径（推荐）
```toml
# 创建：src/main.py
src."main.py" = "print('Hello')"

# 创建：tests/test_basic.py  
tests."test_basic.py" = "def test():\n    assert True"

# 创建：docs/api/README.md
docs.api."README.md" = "# API文档"
```

- 文件名需要用""包裹


##### 方式2：TOML表嵌套

```toml
[structure.src]
main.py = "print('Hello')"

[structure.src.utils]  # 创建 src/utils 目录
helpers.py = "def help():\n    return True"

[structure.tests]
test_main.py = "import unittest"
```

---

## 许可证
本项目采用[Apache License 2.0](LICENSE)许可。请参阅随附的[LICENSE](LICENSE)文件以获取详细信息。

---

## 贡献者
**感谢以下人员的贡献！**
- [ICodeWR](https://github.com/ICodeWR) - 主要开发者

## 贡献指南
我们欢迎并感谢所有形式的贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何贡献代码、报告问题或提出建议。

---

## 行为准则
我们遵循 [行为准则](CODE_OF_CONDUCT.md) 来维护一个友好和包容的社区环境。欢迎所有贡献者共同努力，保持这个空间的积极与健康。

---

## 交流
如需交流，有如下交流方式：
- 邮件：3892493481@qq.com
- 其他：可关注公众号私信交流。

<div align="center">
  <img src="assets/ICodeWR.jpg" width=256></img>
  <p><strong>ICodeWR</strong>: 编程实践记录与分享、倡导编程为己赋能、提供可运行的代码与实现思路。 </p>
</div>

---
