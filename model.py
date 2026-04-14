import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# -----------------------------
# 1. PARAMETERS (CLEAN CALIBRATION)
# -----------------------------
# Only ONE constraint:
# P(0.70) = 0.50  → delta_Q = 0.4 * beta

beta = 20.0                      # network effect strength (free parameter)
delta_Q = 0.4 * beta            # derived from anchor condition

# -----------------------------
# 2. ADOPTION FUNCTION
# -----------------------------
def P(x):
    exponent = beta * (2 * x - 1) - delta_Q
    return 1 / (1 + np.exp(-exponent))

# -----------------------------
# 3. DERIVATIVE (for stability)
# -----------------------------
def dPdx(x):
    p = P(x)
    return 2 * beta * p * (1 - p)

# -----------------------------
# 4. FIND FIXED POINT (tipping)
# -----------------------------
def equilibrium_eq(x):
    return P(x) - x

# unbiased initial guess
threshold = fsolve(equilibrium_eq, 0.7)[0]

# stability check
slope = dPdx(threshold)
stability = "Unstable" if slope > 1 else "Stable"

# -----------------------------
# 5. STOCHASTIC SIMULATION
# -----------------------------
def simulate_market(x_start, steps=2000, dt=0.01, noise_sigma=0.02):
    x = x_start
    path = [x]

    for _ in range(steps):
        drift = (P(x) - x) * dt
        
        # Proper stochastic term (Wright-Fisher style + √dt)
        diffusion = noise_sigma * np.sqrt(x * (1 - x)) * np.sqrt(dt) * np.random.normal()
        
        x += drift + diffusion
        x = np.clip(x, 0, 1)
        path.append(x)

    return path

# -----------------------------
# 6. PHASE SPACE PLOT
# -----------------------------
x_range = np.linspace(0, 1, 500)
y_p = P(x_range)

# -----------------------------
# 7. PLOTTING
# -----------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# --- Plot 1: Deterministic ---
ax1.plot(x_range, y_p, label='$P(x)$', lw=2)
ax1.plot(x_range, x_range, '--', label='$y=x$')

ax1.axvline(threshold, color='red', linestyle=':', 
            label=f'Tipping ≈ {threshold:.2f}')

# Regions
ax1.fill_between(x_range, y_p, x_range,
                 where=(y_p > x_range),
                 alpha=0.1, label='Growth')

ax1.fill_between(x_range, y_p, x_range,
                 where=(y_p < x_range),
                 alpha=0.1, label='Decay')

# Annotation
ax1.annotate("Tipping Point",
             xy=(threshold, threshold),
             xytext=(threshold+0.05, threshold-0.15),
             arrowprops=dict(arrowstyle="->"))

ax1.set_title("Deterministic Phase Space")
ax1.set_xlabel("Market Share (x)")
ax1.set_ylabel("Adoption Probability")
ax1.legend()
ax1.grid(alpha=0.3)

# --- Plot 2: Stochastic ---
n_paths = 8

for start, col in [(threshold-0.01, 'orange'), (threshold+0.01, 'green')]:
    for _ in range(n_paths):
        path = simulate_market(start)
        ax2.plot(path, color=col, alpha=0.5)

ax2.axhline(threshold, color='red', linestyle=':', label='Separatrix')

ax2.set_title("Stochastic Trajectories Near Tipping Point")
ax2.set_xlabel("Time")
ax2.set_ylabel("Market Share (x)")
ax2.set_ylim(0, 1)
ax2.legend()
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# -----------------------------
# 8. OUTPUT
# -----------------------------
print("----- MODEL PARAMETERS -----")
print(f"Beta (network strength): {beta:.2f}")
print(f"Delta Q (quality gap): {delta_Q:.2f}")

print("\n----- RESULTS -----")
print(f"Tipping Point (x*): {threshold:.4f}")
print(f"Slope at x*: {slope:.4f}")
print(f"Stability: {stability}")
