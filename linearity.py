import numpy as np
import matplotlib.pyplot as plt

# Voltage and frequency data in usable range
voltages = [
    0.825, 0.99, 1.155, 1.32, 1.485, 1.65, 1.815, 1.98, 2.145, 2.31, 2.475
]
freqs = [
    0.443, 0.733, 1.023, 1.307, 1.562, 1.794, 1.924, 2.112, 2.220, 2.309, 2.439
]

# Calculate ideal frequencies
kv_avg = (2.439 - 0.443) / (2.475 - 0.825)  # 1.2097 GHz/V
f_ideal = [0.443 + kv_avg * (v - 0.825) for v in voltages]

# Calculate deviation
deviations = [actual - ideal for actual, ideal in zip(freqs, f_ideal)]
abs_devs = [abs(d) for d in deviations]
max_dev = max(abs_devs)
linearity_error = (max_dev / (2.439 - 0.443)) * 100

# Find the voltage with max deviation
max_dev_index = abs_devs.index(max_dev)
max_dev_voltage = voltages[max_dev_index]
max_dev_actual = freqs[max_dev_index]
max_dev_ideal = f_ideal[max_dev_index]

# Plot actual and ideal
plt.figure(figsize=(12, 6))
plt.plot(voltages, freqs, 'bo-', label='Actual Frequency')
plt.plot(voltages, f_ideal, 'r--', label='Ideal Linear Response')
plt.plot(max_dev_voltage, max_dev_actual, 'ks', label=f'Max Deviation @ {max_dev_voltage}V')

# Annotate the max deviation point
plt.annotate(f"Max Deviation: {max_dev_actual - max_dev_ideal:.3f} GHz",
             xy=(max_dev_voltage, max_dev_actual),
             xytext=(max_dev_voltage + 0.05, max_dev_actual - 0.2),
             arrowprops=dict(arrowstyle='->'))

# Axes setup
x_ticks = np.arange(0, 3.4, 0.165)
y_ticks = np.arange(0, max(freqs) + 0.1, 0.1)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.title(f'VCO Linearity Assessment\nMax Deviation = {max_dev:.3f} GHz, Linearity Error = {linearity_error:.1f}%')
plt.xlabel('Voltage (V)')
plt.ylabel('Frequency (GHz)')
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
