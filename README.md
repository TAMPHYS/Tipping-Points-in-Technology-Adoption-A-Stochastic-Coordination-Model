# Tipping Points in Technology Adoption: A Stochastic Coordination Model

## Overview

This project studies how technologies become dominant in the presence of **network effects and uncertainty**, using the classic QWERTY vs DSK keyboard competition as a model system.

The core question is:

> *How much adoption is required for an inferior technology to become self-sustaining?*

We model this as a **stochastic dynamical system** with multiple equilibria and identify the tipping point where dominance shifts.

---

## Key Insight

In systems with network effects:

- Adoption reinforces further adoption  
- But intrinsic quality differences create opposing pressure  

This leads to:

> **Bistability** — two competing stable equilibria

- Low adoption → DSK dominates (technically superior)  
- High adoption → QWERTY dominates (network advantage)  

The transition between them occurs at a **tipping point (~72%)**, where the system becomes highly sensitive to fluctuations.

---

## Model

### Adoption Probability (Logit Choice)

We model user choice using a discrete choice framework:

P(x) = 1 / (1 + exp[-(β(2x - 1) - ΔQ)])

where:

- x: current market share of QWERTY  
- β: strength of network effects  
- ΔQ: intrinsic quality advantage of DSK  

---

### Dynamics

The evolution of adoption is governed by:

dx/dt = P(x) - x

This captures:

- positive feedback (network effects)  
- negative feedback (technical superiority)

---

### Stochastic Extension

To model real-world uncertainty:

dx = (P(x) - x) dt + σ dWₜ

where:

- σ: noise level  
- dWₜ: Brownian motion  

---

## Results

### 1. Multiple Equilibria

The system exhibits:

- Two **stable equilibria** (~0 and ~1)  
- One **unstable equilibrium** (~0.72) → tipping point  

---

### 2. Stochastic Trajectories

Near the tipping point:

- Small fluctuations determine outcome  
- Trajectories diverge toward different equilibria  

This demonstrates:

> **Sensitivity to initial conditions and noise**

---

### 3. Probability of Dominance

We compute:

P(QWERTY dominance | initial share x₀)

Result:

- S-shaped transition curve  
- Sharp change around ~72%  

Interpretation:

> The tipping point is not deterministic — it defines a **probabilistic transition region**

---

## Interpretation

The tipping point acts as a **separatrix** between two basins of attraction:

- Below it → system returns to DSK  
- Above it → system converges to QWERTY  

Under stochastic dynamics:

> The tipping point represents the region of **maximum uncertainty**, where outcomes become probabilistic.

---

## Code Structure

- `model.py`  
  Defines adoption function and stochastic dynamics  

- `analysis.py`  
  Generates:
  - adoption curves  
  - stochastic trajectories  
  - probability transition plot  

---

## How to Run

```bash
python analysis.py
