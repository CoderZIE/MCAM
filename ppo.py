import numpy as np
import gym
from gym import spaces
from stable_baselines3 import PPO
from moo import *
import csv

# Define a custom environment for PPO
class ConfigEnv(gym.Env):
    def __init__(self):
        super(ConfigEnv, self).__init__()
        # Action space: each parameter can be 0, 1, or 2
        self.action_space = spaces.MultiDiscrete([3, 3, 3])
        # Observation space (state): Placeholder for simplicity, not used here
        self.observation_space = spaces.Box(low=0, high=2, shape=(3,), dtype=np.int32)
        # Internal state to keep track of the current configuration
        self.current_config = None

    def reset(self):
        # Reset the environment to an initial state (random configuration)
        self.current_config = np.random.randint(0, 3, size=(3,))
        return self.current_config

    def step(self, action):
        # Apply the action (configuration choice)
        self.current_config = action  # Actions already range from 0 to 2
        # Evaluate the configuration using the objective function
        error, latency, area, power = multi_objective_function(self.current_config)
        # Reward is the negative of the power (minimize power)
        reward = -power
        # In this simple task, we can consider the episode as done after one step
        done = True
        # Additional info (can be used for debugging or analysis)
        info = {"error": error, "latency": latency, "area": area, "power": power}
        return self.current_config, reward, done, info

# Instantiate the environment
env = ConfigEnv()

# Train the PPO model
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1)

# Test the trained model
obs = env.reset()
best_config = None
best_power = float("inf")

for _ in range(10):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if info["power"] < best_power:
        best_power = info["power"]
        best_config = obs

# Print the best configuration
error, latency, area, power = multi_objective_function(best_config)
print("Best configuration found by PPO:")
print(f"Params: {best_config}, Error: {error}, Latency: {latency}, Area: {area}, Power: {power}")
