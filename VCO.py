import matplotlib.pyplot as plt
import numpy as np

# Voltage values
voltages = [
    0, 0.165, 0.33, 0.495, 0.66, 0.825, 0.99, 1.155, 1.32, 1.485, 1.65,
    1.815, 1.98, 2.145, 2.31, 2.475, 2.64, 2.805, 2.97, 3.135, 3.3
]

# Frequency values as strings with units
freq_strs = [
    "325.51897Hz", "19.006276KHz", "1.1691991MHz", "30.54338MHz", "185.41959MHz", 
    "443.15085MHz", "733.36039MHz", "1.0233869GHz", "1.3068509GHz", "1.5624731GHz", 
    "1.7944664GHz", "1.9244444GHz", "2.1121951GHz", "2.2205128GHz", "2.3093333GHz", 
    "2.4394366GHz", "2.5101449GHz", "2.5470588GHz", "2.5850746GHz", "2.5850746GHz", 
    "2.5850746GHz"
]

# Convert all frequencies to GHz
freq_ghz = []
for f in freq_strs:
    if 'GHz' in f:
        freq_ghz.append(float(f.replace('GHz', '')))
    elif 'MHz' in f:
        freq_ghz.append(float(f.replace('MHz', '')) / 1000)
    elif 'KHz' in f:
        freq_ghz.append(float(f.replace('KHz', '')) / 1_000_000)
    elif 'Hz' in f:
        freq_ghz.append(float(f.replace('Hz', '')) / 1_000_000_000)

# Define custom ticks
x_ticks = np.arange(0, 3.4, 0.165)  # X-axis ticks at 0.165V intervals
y_ticks = np.arange(0, max(freq_ghz) + 0.1, 0.1)  # Y-axis ticks at 0.1 GHz

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(voltages, freq_ghz, marker='o', color='blue', linestyle='-')
plt.title('Voltage vs Frequency of VCO')
plt.xlabel('Voltage (V)')
plt.ylabel('Frequency (GHz)')
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
