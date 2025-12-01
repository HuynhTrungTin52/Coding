import math
import numpy as np
import matplotlib.pyplot as plt

def generator_data(a, b, n):
    return np.linspace(a, b, n)

X = generator_data(4, 6, 100)
print("Mảng X đã được tạo với {} phần tử từ {} đến {}".format(len(X), X[0], X[-1]))

#1. Uniform Distribution - PDF
def pmf_uniform_cont(a, b, x):
    if isinstance(x, np.ndarray):
        result = np.zeros_like(x)
        mask = (x >= a) & (x <= b)  # Kiểm tra điều kiện a <= x <= b
        result[mask] = 1 / (b - a)
        return result
    else:
        return 1 / (b - a) if a <= x <= b else 0

#2. Normal Distribution - PDF
def pmf_normal(mu, sigma, x):
    coefficient = 1 / (sigma * np.sqrt(2 * np.pi))
    exponent = -0.5 * ((x - mu) / sigma) ** 2
    return coefficient * np.exp(exponent)

def cdf_normal(mu, sigma, x):
    if isinstance(x, np.ndarray):
        return np.array([0.5 * (1 + math.erf((xi - mu) / (sigma * math.sqrt(2)))) for xi in x])
    else:
        return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))

#Vẽ đồ thị
def plot_all_exercises():
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
#1
    a, b = 4, 6
    X_uniform = generator_data(a, b, 100)
    Y_uniform = pmf_uniform_cont(a, b, X_uniform)
    
    axes[0].plot(X_uniform, Y_uniform, 'b-', linewidth=2, label='Uniform Distribution')
    axes[0].set_xlabel('X', fontsize=12)
    axes[0].set_ylabel('p(x)', fontsize=12)
    axes[0].set_title('1. Uniform Distribution on [4, 6]', fontsize=13, fontweight='bold')
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()
    axes[0].set_ylim([0, 0.6])
    
#2
    mu, sigma = 5, 0.5
    X_normal = generator_data(4, 6, 100)
    Y_pdf = pmf_normal(mu, sigma, X_normal)
    
    axes[1].plot(X_normal, Y_pdf, 'r-', linewidth=2, label=f'Normal PDF (μ={mu}, σ={sigma})')
    axes[1].set_xlabel('X', fontsize=12)
    axes[1].set_ylabel('p(x)', fontsize=12)
    axes[1].set_title('2. Normal Distribution - PDF', fontsize=13, fontweight='bold')
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()
    
#3
    Y_cdf = cdf_normal(mu, sigma, X_normal)
    
    axes[2].plot(X_normal, Y_cdf, 'g-', linewidth=2, label=f'Normal CDF (μ={mu}, σ={sigma})')
    axes[2].set_xlabel('X', fontsize=12)
    axes[2].set_ylabel('φ(x)', fontsize=12)
    axes[2].set_title('3. Exercise 1: Normal Distribution - CDF', fontsize=13, fontweight='bold')
    axes[2].grid(True, alpha=0.3)
    axes[2].legend()
    axes[2].set_ylim([0, 1])
    
    plt.tight_layout()
    plt.show()

print("\n" + "="*60)
print("="*60)
plot_all_exercises()

#Ex02
def calculate_production_probability():
    mu, sigma = 10, 1
    
    # P(X <= 12)
    prob_12 = cdf_normal(mu, sigma, 12)
    
    # P(X <= 9)
    prob_9 = cdf_normal(mu, sigma, 9)
    
    # P(9 <= X <= 12) = P(X <= 12) - P(X <= 9)
    probability = prob_12 - prob_9
    
    print("\n" + "="*60)
    print("Ex02")
    print("="*60)
    print(f"The standardization of time to produce a product of workshop N(μ={mu}, σ={sigma})")
    print(f"P(X <= 12) = {prob_12:.4f}")
    print(f"P(X <= 9) = {prob_9:.4f}")
    print(f"P(9 <= X <= 12) = {probability:.4f}")
    print(f"\n✓ Đáp án: {probability:.4f} (≈ 0.8185)")
    print("="*60)
    
    # Vẽ
    X_range = generator_data(7, 13, 200)
    Y_pdf = pmf_normal(mu, sigma, X_range)
    
    X_fill = X_range[(X_range >= 9) & (X_range <= 12)]
    Y_fill = pmf_normal(mu, sigma, X_fill)
    
    plt.figure(figsize=(10, 6))
    plt.plot(X_range, Y_pdf, 'b-', linewidth=2, label=f'N(μ={mu}, σ={sigma})')
    plt.fill_between(X_fill, Y_fill, alpha=0.3, color='green', 
                     label=f'P(9 ≤ X ≤ 12) = {probability:.4f}')
    plt.axvline(x=9, color='red', linestyle='--', alpha=0.5, label='x = 9 phút')
    plt.axvline(x=12, color='red', linestyle='--', alpha=0.5, label='x = 12 phút')
    plt.xlabel('Thời gian (phút)', fontsize=12)
    plt.ylabel('Mật độ xác suất', fontsize=12)
    plt.title('Exercise 2: The time to produce a product of workshop from 9mins to 12mins', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

calculate_production_probability()

print("\n" + "="*60)
print("="*60)
print("- Đồ thị 1: Uniform Distribution")
print("- Đồ thị 2: PDF")
print("- Đồ thị 3: CDF")
print("- Đồ thị 4: The time to produce a product of workshop from 9mins to 12mins")
print("="*60)