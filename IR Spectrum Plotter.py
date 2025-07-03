import matplotlib.pyplot as plt
import numpy as np
import os

# Ask user for file path
print("Hello GitHub :)")
filepath = input("Please enter the full path to your IR spectrum .dat file: ").strip()

# Load the data
try:
    xy_data = np.loadtxt(filepath)
    x, y = zip(*xy_data)
except Exception as e:
    print(f"Error reading the file: {e}")
    exit()

# Plot the spectrum
plt.figure(figsize=(10, 4))
plt.plot(x, [-val for val in y], color='blue')
plt.xlabel(r"$\tilde{\nu}\ /\ \mathrm{cm}^{-1}$")
plt.ylabel("Transmittance")
plt.title("IR Spectrum")
plt.gca().invert_xaxis()
plt.grid(True)

plt.show()