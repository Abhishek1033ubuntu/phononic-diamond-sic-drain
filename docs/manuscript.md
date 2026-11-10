# Physical Elimination of Sensor Thermal Drift & Dynamic EMI via CVD Diamond / 4H-SiC Heterostructures and Anisotropic h-BN Phononic Waveguides

**Lead Author:** Abhishek Singh  
**ORCID:** [0009-0004-6913-096X](https://orcid.org/0009-0004-6913-096X)  
**Repository Archive:** [Abhishek1033ubuntu](https://github.com/Abhishek1033ubuntu)  
**Location:** Madhya Pradesh, India  

---

## Abstract

Digital Signal Processing (DSP) techniques, such as Kalman filtering and adaptive Least Mean Squares (LMS) algorithms, address sensor thermal drift and high-frequency noise by introducing computational latency, phase lag, and co-processor overhead. In high-power transient environments—such as 1.2-MW pulse-charging nodes operating at 1 Hz—localized $I^2R$ ohmic heating drives wide-bandgap (WBG) sensor channels beyond their phonon Umklapp scattering threshold ($T_{\text{crit}}$), triggering intrinsic carrier flooding and baseline offset wander. 

This paper presents a physical-layer mitigation architecture that eliminates thermal drift and dynamic Electromagnetic Interference (EMI) directly at the substrate interface. Utilizing Non-Equilibrium Molecular Dynamics (NEMD) in LAMMPS and 2D anisotropic heat transport modeling, we demonstrate that replacing metallic contact buffer layers with an all-covalent **CVD Diamond / 4H-SiC heterostructure** reduces interfacial Kapitza resistance to $8.710 \times 10^{-10} \text{ m}^2\cdot\text{K/W}$ and elevates interfacial thermal conductance to $1148.16 \text{ MW/m}^2\cdot\text{K}$. Paired with a patterned hexagonal Boron Nitride (h-BN) phononic crystal waveguide ($\alpha_r = 1.5 \times 10^{-4} \text{ m}^2/\text{s}$), localized thermal energy is laterally forwarded across a $0.54\text{ mm}$ footprint, preventing junction thermal pooling and maintaining purely Normal ($N$-process) ballistic phonon transport.

---

## 1. Thermodynamic Root Causes: Phonon Umklapp Collapse at the $\Phi$-Node

Sensor thermal drift is seeded at the **$\Phi$-Node**—the physical interface between the metallic contact and the semiconductor sensing channel where acoustic impedance mismatches induce phonon reflection.

In standard 4H-SiC channels, thermal transport is governed by the total scattering relaxation rate ($\tau_{\text{eff}}^{-1}$):

$$\frac{1}{\tau_{\text{eff}}} = \frac{1}{\tau_B} + \frac{1}{\tau_I} + \frac{1}{\tau_N} + \frac{1}{\tau_U}$$

For 4H-SiC ($\theta_D \approx 1200\text{ K}$), the critical threshold temperature where Umklapp scattering overtakes normal heat conduction occurs at:

$$T_{\text{crit}} \approx \frac{\theta_D}{3} \approx 400\text{ K} \quad (127^\circ\text{C})$$

When localized $I^2R$ transient heating pushes the junction temperature above $400\text{ K}$, back-scattering forces thermal conductivity to decay asymptotically ($\kappa(T) \propto 1/T$). The resulting trapped thermal energy excites intrinsic carriers across the 3.26 eV wide bandgap, causing the baseline channel resistance to drift non-linearly.

---

## 2. Atomistic NEMD Modeling: Metallic vs. CVD Diamond Thermal Drains

| Composite Buffer Interface | Interfacial $\Delta T$ | Kapitza Resistance ($R_k$) | Interfacial Conductance ($G$) | Transport Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **Ti/TiN to 4H-SiC** | $+24.60\text{ K}$ | $1.640 \times 10^{-8} \text{ m}^2\cdot\text{K/W}$ | $60.98 \text{ MW/m}^2\cdot\text{K}$ | Acoustic Impedance Limited |
| **CVD Diamond to 4H-SiC** | **$+1.31\text{ K}$** | **$8.710 \times 10^{-10} \text{ m}^2\cdot\text{K/W}$** | **$1148.16 \text{ MW/m}^2\cdot\text{K}$** | **Near-Ballistic ($N$-Process)** |

---

## 3. Macro-Scale Anisotropic Heat Forwarding in Patterned h-BN Substrates

Solving the 2D transient radial heat diffusion equation in cylindrical coordinates:

$$\frac{\partial T}{\partial t} = \alpha_r \left( \frac{\partial^2 T}{\partial r^2} + \frac{1}{r} \frac{\partial T}{\partial r} \right) + \alpha_z \frac{\partial^2 T}{\partial z^2}$$

The high in-plane diffusivity of the h-BN waveguide converts concentrated vertical heat accumulation into a two-dimensional radial plume, dissipating heat across a **$0.54\text{ mm}$ footprint**.

---

## 4. Multi-Physics Integration & Dynamic EMI Immunity

| Architecture / Metric | Standard Silicon Node | Wide-Bandgap (SiC + DSP) | **CVD Diamond / h-BN Heterostructure** |
| :--- | :--- | :--- | :--- |
| **Noise & Drift Mitigation** | Digital Low-Pass Filters | Software Kalman Filter | **Physical-Layer Phononic Drain & Dielectric Shield** |
| **Interfacial Conductance ($G$)** | $\sim 15 \text{ MW/m}^2\cdot\text{K}$ | $60.98 \text{ MW/m}^2\cdot\text{K}$ | **$1148.16 \text{ MW/m}^2\cdot\text{K}$** |
| **Kapitza Resistance ($R_k$)** | $\sim 6.6 \times 10^{-8} \text{ m}^2\cdot\text{K/W}$ | $1.640 \times 10^{-8} \text{ m}^2\cdot\text{K/W}$ | **$8.710 \times 10^{-10} \text{ m}^2\cdot\text{K/W}$** |
| **DSP Computational Overhead** | High | Moderate | **Zero (Hardware-Level Immunity)** |
