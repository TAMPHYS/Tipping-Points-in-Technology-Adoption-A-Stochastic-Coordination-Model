import numpy as np

# -----------------------------
# PARAMETERS
# -----------------------------
beta = 22
sigma = 0.02

T = 2000
dt = 0.01
steps = int(T / dt)

# -----------------------------
# ADOPTION FUNCTION
# -----------------------------
def P(x):
    return 1 / (1 + np.exp(-beta * (2*x - 1.4)))

# -----------------------------
# DETERMINISTIC DRIFT
# -----------------------------
def drift(x):
    return P(x) - x

# -----------------------------
# STOCHASTIC SIMULATION
# -----------------------------
def simulate(x_init):
    x = x_init
    traj = []

    for _ in range(steps):
        dx = drift(x) * dt + sigma * np.sqrt(dt) * np.random.randn()
        x += dx
        x = np.clip(x, 0, 1)
        traj.append(x)

    return np.array(traj)

# -----------------------------
# FINAL STATE ONLY
# -----------------------------
def simulate_final(x_init):
    x = x_init

    for _ in range(steps):
        dx = drift(x) * dt + sigma * np.sqrt(dt) * np.random.randn()
        x += dx
        x = np.clip(x, 0, 1)

    return x
