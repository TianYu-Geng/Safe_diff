# SafeDiffuser 仓库总览

## 顶层结构
- `config/`：不同任务的实验超参。
- `diffuser/`：核心库（模型、数据集、采样与策略、环境封装、渲染资产、工具函数）。
- `scripts/`：训练、规划、检查点转换等可执行脚本。
- 其他：`azure/`（Azure 启动/下载脚本）、`imgs/`（文档配图）、`environment.yml`（环境依赖）、`setup.py`/`diffuser.egg-info/`（打包元数据）。

## `config/`
- 以 Python 字典形式定义实验配置，供 `diffuser.utils.Parser`/`Config` 解析，自动拼装数据集、模型、扩散、训练/规划流程。
- `maze2d.py`：maze2d 任务的基础配置与覆写（`maze2d_umaze_v1`、`maze2d_large_v1`），包含渲染器选择、归一化器、时域长度、扩散步数、日志路径，以及用 `watch` 自动生成实验名。
- `locomotion.py`：步行/跑步等 locomotion 任务的训练默认值（如 `TemporalUnet` + `GaussianDiffusion`、损失权重、数据加载、horizon、训练/保存频率），并提供 `halfcheetah_medium_expert_v2` 覆写示例。

## `diffuser/`
- 实现扩散模型的训练与规划。
- `models/`：神经架构（如 `TemporalUnet`）和扩散封装（`GaussianDiffusion`）及相关时间/噪声调度辅助。
- `datasets/`：数据集封装（`GoalDataset`、`SequenceDataset`、D4RL 适配）、归一化与预处理工具，提供观测/动作维度、轨迹采样接口。
- `sampling/` 与 `guides/`：将已训练的扩散模型变为行动策略的采样/引导逻辑，核心策略在 `guides/policies.py`。
- `environments/`：环境封装与 MuJoCo 资产（hopper、walker2d、half-cheetah、ant 等）以及 maze2d 渲染/注册。
- `utils/`：公共基础设施（配置/解析、日志与进度、训练循环、序列化、渲染、计时、git 工具、云/Colab、数组变换、IQL 等）；`utils/setup.py` 提供包相关辅助。
- 根部 `__init__.py` 暴露环境模块；`__pycache__/` 存放编译缓存。

## `scripts/`
- `train.py`：训练入口；基于配置构建数据集/渲染器/模型/扩散/Trainer，先做前后向自检，再按 epoch 训练并按计划保存/采样。
+- `plan_maze2d.py`：maze2d 规划与可视化；加载预训练扩散实验，构造 `Policy`，跑一幕（可条件化），输出合成图/扩散轨迹视频，并记录安全/ELBO 信息。
- `convert_checkpoints.py`：旧版 checkpoint 迁移；重写类路径与字段名并备份原文件，方便兼容最新代码。
