
import numpy as np
import matplotlib.pyplot as plt


# ==========================================
# 1. MEMBERSHIP FUNCTION DEFINITIONS
# ==========================================
class FuzzyMembership:

    @staticmethod
    def triangular(x, a, b, c):
        """Triangular MF: a = left foot, b = peak, c = right foot"""
        x = np.asarray(x, dtype=float)

        left_slope = (x - a) / (b - a) if b != a else np.where(x >= b, 1.0, 0.0)
        right_slope = (c - x) / (c - b) if c != b else np.where(x <= b, 1.0, 0.0)

        mu = np.minimum(left_slope, right_slope)
        return np.maximum(0.0, np.minimum(1.0, mu))

    @staticmethod
    def trapezoidal(x, a, b, c, d):
        """Trapezoidal MF: a = left foot, b = left peak, c = right peak, d = right foot"""
        x = np.asarray(x, dtype=float)

        left_slope = (x - a) / (b - a) if b != a else np.where(x >= b, 1.0, 0.0)
        right_slope = (d - x) / (d - c) if d != c else np.where(x <= c, 1.0, 0.0)

        mu = np.minimum(left_slope, right_slope)
        return np.maximum(0.0, np.minimum(1.0, mu))

    @staticmethod
    def gaussian(x, mean, sigma):
        """Gaussian MF: center = mean, width = sigma"""
        x = np.asarray(x, dtype=float)
        return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

    @staticmethod
    def sigmoidal(x, c, a):
        """Sigmoidal MF: center = c, slope = a"""
        x = np.asarray(x, dtype=float)
        return 1.0 / (1.0 + np.exp(-a * (x - c)))


# ==========================================
# 2. FUZZY SET OPERATIONS
# ==========================================
class FuzzyOperations:

    @staticmethod
    def fuzzy_and(mu1, mu2):
        """Fuzzy Intersection (Min operator)"""
        return np.minimum(mu1, mu2)

    @staticmethod
    def fuzzy_or(mu1, mu2):
        """Fuzzy Union (Max operator)"""
        return np.maximum(mu1, mu2)

    @staticmethod
    def fuzzy_not(mu):
        """Fuzzy Complement (1 - mu)"""
        return 1.0 - mu


# ==========================================
# 3. EXECUTION AND VISUALIZATION
# ==========================================
if __name__ == "__main__":

    # Define Universe of Discourse (Temperature Range: 0°C to 40°C)
    x = np.linspace(0, 40, 401)

    # 1. Generate Individual Fuzzy Sets
    mu_cold = FuzzyMembership.trapezoidal(x, a=0, b=0, c=10, d=18)
    mu_comfortable = FuzzyMembership.triangular(x, a=15, b=22, c=28)
    mu_warm = FuzzyMembership.gaussian(x, mean=30, sigma=4)
    mu_hot = FuzzyMembership.sigmoidal(x, c=32, a=0.8)

    # 2. Evaluate single point (e.g., T = 20°C)
    test_temp = 20.0

    print(f"--- Degrees of Membership at {test_temp}°C ---")
    print(f"Cold:        {FuzzyMembership.trapezoidal(test_temp, 0, 0, 10, 18):.2f}")
    print(f"Comfortable: {FuzzyMembership.triangular(test_temp, 15, 22, 28):.2f}")
    print(f"Warm:        {FuzzyMembership.gaussian(test_temp, 30, 4):.2f}")
    print(f"Hot:         {FuzzyMembership.sigmoidal(test_temp, 32, 0.8):.2f}")

    # 3. Compute Fuzzy Set Operations
    mu_not_cold = FuzzyOperations.fuzzy_not(mu_cold)                # NOT Cold
    mu_cool_or_warm = FuzzyOperations.fuzzy_or(mu_cold, mu_warm)   # Cold OR Warm
    mu_overlap = FuzzyOperations.fuzzy_and(mu_cold, mu_comfortable)  # Cold AND Comfortable

    # 4. Plot Results
    plt.figure(figsize=(12, 8))

    # Subplot 1: Base Membership Functions
    plt.subplot(2, 1, 1)
    plt.plot(x, mu_cold, label="Cold (Trapezoidal)", color="blue", linewidth=2)
    plt.plot(x, mu_comfortable, label="Comfortable (Triangular)", color="green", linewidth=2)
    plt.plot(x, mu_warm, label="Warm (Gaussian)", color="orange", linewidth=2)
    plt.plot(x, mu_hot, label="Hot (Sigmoidal)", color="red", linewidth=2)

    plt.title("Base Fuzzy Sets (Temperature)")
    plt.ylabel("Membership Degree (μ)")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper right")

    # Subplot 2: Fuzzy Set Operations
    plt.subplot(2, 1, 2)
    plt.plot(x, mu_not_cold, label="NOT Cold (1 - μ)", color="purple", linestyle="--", linewidth=1.5)
    plt.plot(x, mu_cool_or_warm, label="Cold OR Warm (MAX)", color="darkgreen", linewidth=2)
    plt.plot(x, mu_overlap, label="Cold AND Comfortable (MIN)", color="brown", linewidth=2)

    plt.fill_between(x, 0, mu_overlap, color="brown", alpha=0.3)  # Highlight overlap area

    plt.title("Fuzzy Set Operations")
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Membership Degree (μ)")
    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper right")

    plt.tight_layout()
    plt.show()
