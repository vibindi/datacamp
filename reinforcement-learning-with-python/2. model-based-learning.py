import gymnasium as gym

env = gym.make('FrozenLake', is_slippery=True) # turn to stochastic
print(env.action_space) # 4
print(env.observation_space) # 16
print(env.unwrapped.P)
# env.unwrapped.P[state][action] --> (probability, s', r, terminal?)