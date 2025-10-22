import numpy as np
from scipy.stats import norm

import matplotlib.pyplot as plt

def plot_normal_pdf():

	normal_dist = norm(loc=0, scale=1)

	x = np.linspace(-4, 4, 750)

	pdf_values = normal_dist.pdf(x)

	plt.figure(figsize=(8, 6))
	plt.plot(x, pdf_values, 'r-', lw=2, label='Normal PDF')
	plt.title('Probability Density Function of a Standard Normal Distribution')
	plt.xlabel('X-values')
	plt.ylabel('Probability Density')
	plt.grid(True)
	plt.legend()
	plt.show()


plot_normal_pdf()