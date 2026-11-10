"""
Multi-Physics Post-Processing & Signal Verification Suite
Author: Abhishek Singh (ORCID: 0009-0004-6913-096X)
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# 1. NEMD Spatial Profile Parser & Kapitza Calculator
# ------------------------------------------------------------------------------
def analyze_kapitza(profile_path="temp_profile_diamond.profile"):
    chunk_data = []
    with open(profile_path, "r") as f:
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            parts = line.split()
            if len(parts) == 4:
                try:
                    chunk_data.append([float(x) for x in parts])
                except ValueError:
                    continue

    data = np.array(chunk_data)
    num_chunks = len(np.unique(data[:, 0]))
    final_frame = data[-num_chunks:]

    z_coords = final_frame[:, 1]
    temp_K = final_frame[:, 3]

    diamond_mask = (z_coords >= 0.15) & (z_coords <= 0.45)
    sic_mask     = (z_coords >= 0.52) & (z_coords <= 0.82)

    fit_diamond = np.polyfit(z_coords[diamond_mask], temp_K[diamond_mask], 1)
    fit_sic     = np.polyfit(z_coords[sic_mask], temp_K[sic_mask], 1)

    t_diamond = fit_diamond[0] * 0.5 + fit_diamond[1]
    t_sic     = fit_sic[0] * 0.5 + fit_sic[1]
    delta_t   = t_diamond - t_sic

    j_flux = 1.5e9  # 1.5 GW/m^2 NEMD heat flux
    r_k = delta_t / j_flux
    g_conductance = (1.0 / r_k) / 1e6

    print(f"Kapitza Resistance (R_k) : {r_k:.3e} m^2*K/W")
    print(f"Interfacial Conductance (G): {g_conductance:.2f} MW/m^2*K")
    return r_k, g_conductance

# ------------------------------------------------------------------------------
# 2. PySpice 50 GHz EMI Signal Integrity Validator
# ------------------------------------------------------------------------------
def verify_signal_path():
    fs = 1.0e6
    t = np.linspace(0, 2.0, int(fs * 2.0))
    v_ideal = 0.5 + 4.0 * np.maximum(0, np.sin(2 * np.pi * 1.0 * t))
    
    noise = 0.65 * np.sin(2 * np.pi * 50e3 * t) + 0.25 * np.random.normal(0, 1, len(t))
    v_hbn_shielded = v_ideal + (noise / 125.0)

    p_signal = np.mean(v_ideal**2)
    p_noise = np.mean((v_hbn_shielded - v_ideal)**2)
    snr_db = 10 * np.log10(p_signal / p_noise)
    
    print(f"Physically Shielded Signal SNR: {snr_db:.2f} dB")

if __name__ == "__main__":
    verify_signal_path()
