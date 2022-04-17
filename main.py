import mdptoolbox.example as mdpExamp
import mdptoolbox
import numpy as np

# number of states
STATES = 4

# number of actions
ACTIONS = 2
ACTION_FISH = 0
ACTION_NOT_FISH = 1

P = np.array([
    # P[0] = fish
    [
        [0, 0, 0, 0],    # empty
        [0.75, 0.25, 0, 0],  # low
        [0, 0.75, 0.25, 0],  # medium
        [0, 0, 0.4, 0.6]     # high
    ],
    # P[1] = not to fish
    [
        [0, 1, 0, 0],      # empty
        [0, 0.3, 0.7, 0],    # low
        [0, 0, 0.25, 0.75],  # medium
        [0, 0, 0.05, 0.95]   # high
    ]
])

