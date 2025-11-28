import matplotlib.pyplot as plt

# Create a figure with 1 row and 2 columns of subplots, 
# with the first subplot being 3 times wider than the second
fig, axs = plt.subplots(2, 2, gridspec_kw={'width_ratios': [1, 5]}, figsize=(10, 5))

# Plot on the subplots
axs[0,0].plot([1, 2, 3])
axs[0,0].set_title('Wider Subplot')

axs[1,1].bar(['A', 'B'], [5, 2])
axs[1,1].set_title('Narrower Subplot')

plt.tight_layout()
plt.show()