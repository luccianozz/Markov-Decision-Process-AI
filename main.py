import mdptoolbox
import numpy as np

# number of states
STATES = 4

# number of actions
ACTIONS = 2
ACTION_FISH = 0
ACTION_NOT_FISH = 1

# probability of states based on the actions
P = np.array([

    # P[0] = Fish
    [
        [0, 1, 0, 0],        # 0 = empty

        [0.75, 0.25, 0, 0],  # 1 = low

        [0, .75, .25, 0],    # 2 medium

        [0, .6, .4, 0],      # 3 high

    ],
    # P[1] = Not Fish
    [
        [0, 1, 0, 0],        # 0 = empty

        [0, 0.3, 0.7, 0],    # 1 = low

        [0, 0, .25, 0.75],   # 2 medium

        [0, 0, .05, 0.95],   # 3 high

     ]

])

# [0] = Fish
# [1] = NOT Fish

# reward values based on possible actions
R = np.array([
    [-200, -200],

    [5, 0],

    [10, 0],

    [50, 0]
])

print("P = ", P)
print("R = ", R)

# discount and number of periods variables
Discount = 0.9
NumPeriods = 10

# Value Iteration code
print("\nValue iteration:")
print("-----------------------------------")
vi = mdptoolbox.mdp.ValueIteration(P, R, Discount, NumPeriods)
vi.setVerbose()
vi.run()
print("\noptimal value function = ", vi.V)
print("optimal policy = ", vi.policy)


# Policy Iteration code
print("\nPolicy Iteration:")
print("-----------------------------------")
pi = mdptoolbox.mdp.PolicyIteration(P, R, Discount)
pi.setVerbose()
pi.run()
print("\noptimal value function = ", pi.V)
print("optimal policy = ", pi.policy)