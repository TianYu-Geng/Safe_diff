import mujoco_py
import os

# 1. 加载模型
# 这里依然使用自带的 humanoid.xml
model_path = os.path.join(mujoco_py.utils.discover_mujoco(), "model", "humanoid.xml")
model = mujoco_py.load_model_from_path(model_path)
sim = mujoco_py.MjSim(model)

# 2. 创建可视化窗口
viewer = mujoco_py.MjViewer(sim)

print("✅ 模拟开始！请看弹出的窗口。")
print("提示：你可以用鼠标【左键拖动】旋转视角，【右键拖动】缩放，【按空格键】暂停。")

# 3. 无限循环
while True:
    # --- 每一轮开始前，重置物理状态 ---
    sim.reset()
    
    # 打印一下，让你知道新的一轮开始了
    print("🔄 重置模拟，新的一轮开始...")

    # --- 这一轮模拟运行 1000 步 ---
    for i in range(1000):
        sim.step()       # 物理计算一步
        viewer.render()  # 渲染画面
        
        # 如果你觉得跑得太快看不清，可以取消下面这行的注释来强制降速
        # import time; time.sleep(0.002)

    # 循环结束后，会自动回到 while True 开头，再次执行 sim.reset()