# Repository Guidelines

## Project Structure & Modules
- `config/`: 实验超参（maze2d、locomotion 等）与数据集特定覆写。
- `diffuser/`: 核心库——模型(`models/`)、数据集与归一化(`datasets/`)、采样/策略(`sampling/`, `guides/`)、环境封装与资产(`environments/`)、通用工具(`utils/`, 渲染、训练循环、配置解析)。
- `scripts/`: 运行入口（训练、规划、检查点转换）。
- 其他：`azure/` 部署脚本，`imgs/` 文档配图，`environment.yml` 环境定义，`setup.py` 包装入口。

## Build, Test, Dev Commands
- 创建环境：`conda env create -f environment.yml && conda activate safediffuser`。
- 安装：`pip install -e .`，另需 `pip install qpth cvxpy cvxopt`。
- 训练示例：`python scripts/train.py --config config.maze2d --dataset maze2d-large-v1`（maze2d）；`python scripts/train.py --dataset walker2d-medium-expert-v2`（locomotion）。
- 规划示例：`python scripts/plan_maze2d.py --config config.maze2d --dataset maze2d-large-v1 --logbase logs`。
- 检查点转换：`python scripts/convert_checkpoints.py`（迁移旧存档）。

## Coding Style & Naming
- 语言：Python，4 空格缩进，尽量保持函数/模块内的简短注释；避免冗长行（<=100 列）。
- 命名：文件/模块用小写下划线；类用 `CamelCase`，函数/变量用 `snake_case`；配置键与脚本参数保持一致。
- 配置：基于 `diffuser.utils.Parser/Config` 的字典式配置，新增超参时在对应 config 文件中添加，并确保脚本参数映射正确。

## Testing Guidelines
- 本仓库无专用测试框架；修改核心逻辑后至少运行一次相应脚本的“dry”流程（如加载模型、单步前向、短 rollout）。
- 建议保留最小重现命令（数据集、配置、种子）以便验证。

## Commit & PR
- 提交信息：简短祈使句，包含修改范围（如 `train: fix diffusion config loading`）。
- PR 要求：描述动机与主要改动，附上运行的命令/日志；如涉及可视化输出，附截图或路径；注明对配置、接口、依赖的破坏性变化。

## 环境与安全提示
- GPU/MuJoCo：运行前设置 `LD_LIBRARY_PATH` 以包含 GPU 驱动与 mujoco200 二进制（见 README 提示）；规划/训练默认使用 CUDA。
- 数据与权重：`logs/` 默认保存训练与可视化结果，注意磁盘占用；迁移旧 checkpoint 请先备份（脚本已自动生成 `old_*` 副本）。
