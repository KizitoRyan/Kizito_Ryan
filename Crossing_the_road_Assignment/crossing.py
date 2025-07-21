import random

# Environment: Road with 5 positions
class RoadEnv:
    def __init__(self, length=5):
        self.length = length
        self.start_pos = 0
        self.goal_pos = length - 1
        self.agent_pos = self.start_pos

    def reset(self):
        self.agent_pos = self.start_pos
        return self.agent_pos

    def step(self, action):
        # Action: 0 = left, 1 = right
        if action == 0:
            self.agent_pos = max(0, self.agent_pos - 1)
        elif action == 1:
            self.agent_pos = min(self.length - 1, self.agent_pos + 1)

        # Reward logic
        if self.agent_pos == self.goal_pos:
            reward = 10  # Reached goal
            done = True
        else:
            reward = -1  # Step cost
            done = False

        return self.agent_pos, reward, done

# Q-learning agent
class QLearningAgent:
    def __init__(self, state_size, action_size, alpha=0.1, gamma=0.9, epsilon=0.1):
        self.q_table = [[0 for _ in range(action_size)] for _ in range(state_size)]
        self.alpha = alpha      # Learning rate
        self.gamma = gamma      # Discount factor
        self.epsilon = epsilon  # Exploration rate

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice([0, 1])  # Explore
        return self.q_table[state].index(max(self.q_table[state]))  # Exploit

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state][action]
        target = reward + self.gamma * max(self.q_table[next_state])
        self.q_table[state][action] += self.alpha * (target - predict)

# Training the agent
env = RoadEnv()
agent = QLearningAgent(state_size=env.length, action_size=2)

episodes = 100

for episode in range(episodes):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.learn(state, action, reward, next_state)
        state = next_state

# Testing the agent
state = env.reset()
done = False
actions_taken = []

while not done:
    action = agent.choose_action(state)
    actions_taken.append('right' if action == 1 else 'left')
    state, _, done = env.step(action)

# Output results
print("Learned Q-table:")
for i, row in enumerate(agent.q_table):
    print(f"State {i}: {row}")

print("\nActions taken to reach goal:")
print(" -> ".join(actions_taken))