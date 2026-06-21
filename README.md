# AI Toolkit —— 我的 AI 开发入门工具包

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📖 项目简介

本项目是我学习 AI 开发的基础工具包，记录了从环境搭建到 Git 版本控制、再到 LLM 项目规范的完整实践过程。适合 AI 初学者快速建立自己的开发工作流。

*   **项目目标**：打造一个可复用的 AI 开发脚手架，包含 Python 环境配置、Git 分支管理模板、项目 README 规范。
*   **技术框架**：Python 3.10+、Anaconda、Git、VSCode。
*   **适用场景**：个人 AI 项目起步、团队开发规范参考、LLM 应用原型开发。

## 🚀 快速开始

### 环境准备
- Python 3.10 或更高版本（推荐使用 Anaconda 管理）
- Git 2.40+
- Visual Studio Code（推荐安装 Python 和 Jupyter 插件）

### 安装与部署

1. 克隆仓库到本地：
   ```bash
   git clone https://github.com/Qi686/ai-toolkit.git
   cd ai-toolkit
```

2. 创建 conda 虚拟环境（可选，推荐）：
   ```bash
   conda create -n ai-toolkit python=3.10
   conda activate ai-toolkit
   ```
3. 运行第一个脚本：
   ```bash
   python hello_ai.py
   ```
   输出：
   ```
   Hello AI!
   欢迎使用 ai-toolkit 项目
   ```

使用示例

```python
# hello_ai.py 是一个简单的入门脚本
print("Hello AI!")
print("欢迎使用 ai-toolkit 项目")
```

📚 Git 学习笔记

本项目包含了基础 Git 命令的实践，以下是核心流程：

命令 作用
git clone <url> 克隆远程仓库到本地
git checkout -b <branch> 创建并切换到新分支
git add . 将所有修改添加到暂存区
git commit -m "msg" 提交暂存区内容
git push origin <branch> 推送本地分支到远程
git merge <branch> 合并指定分支到当前分支
git pull 拉取远程更新

详细分支操作示例参见仓库中的提交历史。

## 📝 学习笔记

### Python 基础 - 变量与数据类型
- 演示文件：[variables_demo.py](variables_demo.py)
- 涵盖内容：变量赋值、字符串拼接、整数/浮点数、f-string。

### Python 基础 - 列表简介
- 演示文件：[list_demo.py](list_demo.py)
- 涵盖内容：创建列表、索引访问、修改元素、添加/删除元素、简单循环。

### Python 基础 - 操作列表
- 演示文件：[list_operations_demo.py](list_operations_demo.py)
- 涵盖内容：
  - 遍历（for循环、enumerate）
  - 切片（获取子集、复制列表）
  - 列表解析（条件过滤、数值运算）

  ### Python 基础 - if 语句
- 演示文件：[if_demo.py](if_demo.py)
- 涵盖内容：
  - 条件测试（相等、不等、数值比较、`and`/`or`、`in`/`not in`）
  - `if-elif-else` 多分支结构
  - 结合列表的实战应用

### Python 基础 - 字典
- 演示文件：[dict_demo.py](dict_demo.py)
- 涵盖内容：
  - 创建字典（`{}`、`dict()`）
  - 访问元素（`[]`、`get()`）
  - 修改和添加元素
  - 删除元素（`pop`、`popitem`、`del`、`clear`）
  - 遍历（`items()`、`keys()`、`values()`）
  - 字典嵌套（列表嵌套字典、字典嵌套列表）

## 📚 本周学习汇总 (Week 1 - Python 基础)

| 章节 | 核心内容 | 对应 Demo |
| :--- | :--- | :--- |
| 第1-2章 | 变量、简单数据类型、字符串拼接 | [variables_demo.py](demos/variables_demo.py) |
| 第3章 | 列表创建、访问、修改元素 | [list_demo.py](demos/list_demo.py) |
| 第4章 | 遍历、切片、列表解析 | [list_operations_demo.py](demos/list_operations_demo.py) |
| 第5章 | 条件测试、if-elif-else | [if_demo.py](demos/if_demo.py) |
| 第6章 | 字典增删改查、遍历、嵌套 | [dict_demo.py](demos/dict_demo.py) |
| 第7章 | 用户输入 (`input`)、`while` 循环、`break`/`continue` | [chapter7_user_input.py](demos/chapter7_user_input.py) |

### 🛠️ 本周优化亮点
- **结构优化**：所有功能模块化封装为函数，遵循单一职责原则。
- **标准化入口**：引入 `if __name__ == "__main__":`，增强脚本可读性和可导入性。
- **项目整理**：统一将脚本迁移至 `demos/` 目录，根目录保持清爽。

📄 开源协议

本项目基于 MIT 协议开源。你可以自由使用、修改和分发，但请保留版权声明。