import sys
import numpy as np
import matplotlib.pyplot as plt

# zeroes = np.zeros(3)
# print(zeroes)



sys.exit(0)

# x = np.array([815, 24, -97.10])
adani_green_energy_price_earnings_ratio = [815, 24, -97.10]
implied_downside = -97.10

x_labels = ('Actual', 'Industry Avg.', 'Implied Downside')

fig, ax = plt.subplots()
bar_colors = ['tab:orange', 'tab:orange', 'tab:red']

ax.bar(x_labels, adani_green_energy_price_earnings_ratio, color=bar_colors)

ax.set_ylabel('P/E Ratio')
ax.set_xlabel('Adani Green Energy')
plt.show()