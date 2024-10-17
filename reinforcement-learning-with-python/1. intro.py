import gymnasium as gym
import matplotlib.pyplot as plt

env = gym.make('MountainCar', render_mode='rgb_array')
state_info = env.reset(seed=42)
plt.imshow(env.render())
plt.show()
state, reward, terminated, truncated, info = env.step(1) # enter action