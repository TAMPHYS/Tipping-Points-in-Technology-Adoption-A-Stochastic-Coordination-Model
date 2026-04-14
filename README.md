# Tipping Points in Technology Adoption: A Stochastic Coordination Model

## Overview

This project studies how technologies become dominant in the presence of **network effects and uncertainty**, using the classic QWERTY vs DSK keyboard competition as a model system.

The central question is:

> *At what point does a technology become self-sustaining despite being intrinsically inferior?*

We model this as a **nonlinear stochastic dynamical system**, where adoption evolves through feedback and random fluctuations.

---

## Key Insight

In systems with strong network effects:

- Adoption reinforces further adoption (positive feedback)  
- Intrinsic quality differences create opposing pressure (negative feedback)  

This leads to:

> **Bistability** — two competing stable equilibria

- Low adoption → DSK dominates (technical superiority)  
- High adoption → QWERTY dominates (network effects)  

Between them lies a **tipping point**, where outcomes become highly sensitive to small fluctuations.

---

## Model

### Adoption Probability (Logit Choice Model)

We model the probability of choosing QWERTY as:

P(x) = 1 / (1 + exp[-(β(2x - 1) - ΔQ)])

where:

- x: current market share of QWERTY  
- β: strength of network effects  
- ΔQ: intrinsic quality advantage of DSK  

---

### Calibration

We impose a single anchor condition:

P(0.70) = 0.50  

This implies:

ΔQ = 0.4 β  

This ensures that at 70% adoption, network advantage and technical superiority exactly balance.

> The tipping point is **not imposed** — it emerges from the model.

---

### Dynamics

The deterministic evolution is:

dx/dt = P(x) - x  

- P(x) > x → growth (QWERTY expands)  
- P(x) < x → decay (DSK recovers)  

---

### Stochastic Extension

To incorporate uncertainty:

dx = (P(x) - x) dt + σ √(x(1 - x)) dWₜ  

- σ: noise strength  
- dWₜ: Brownian motion  

This introduces randomness in adoption decisions.

---

## Results

### 1. Emergent Tipping Point

The tipping point x* is obtained by solving:

P(x*) = x*  

It appears as an **unstable equilibrium**, where:

P′(x*) > 1  

This is the **separatrix** between two regimes.

---

### 2. Phase Space Behavior

- Below x*: system drifts toward DSK (restoring force)  
- Above x*: system moves toward QWERTY (positive feedback)  

---

### 3. Stochastic Dynamics

Near the tipping point:

- Small fluctuations determine outcome  
- Trajectories diverge into different equilibria  

This demonstrates:

> **Noise-driven selection between competing technologies**

---

## Interpretation

The tipping point is not a fixed deterministic boundary, but a **region of maximum sensitivity**:

- Below it → system reverts  
- Above it → system locks in  
- Near it → outcomes are probabilistic  

This is analogous to:

- phase transitions  
- metastability  
- barrier crossing in stochastic systems  

---

## Code Structure

- `qwerty_model.py`  
  Contains:
  - adoption function  
  - equilibrium computation  
  - stochastic simulation  
  - plotting (phase space + trajectories)

---


# <img width="1489" height="590" alt="image" src="https://github.com/user-attachments/assets/c909be0c-cbe3-4e67-be8e-02a6bc27e7c9" />

---


