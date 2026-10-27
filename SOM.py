import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# FLOWCHART STEP 1: Load / Prepare Dataset & Normalize Input Data
# ============================================================

def load_and_normalize_data():
    np.random.seed(42)

    # Generate 3 distinct feature patterns (clusters) in 3D space
    cluster1 = np.random.normal(loc=[10, 2, 2], scale=1.0, size=(25, 3))
    cluster2 = np.random.normal(loc=[-2, 10, 2], scale=1.0, size=(25, 3))
    cluster3 = np.random.normal(loc=[2, 2, 10], scale=1.0, size=(25, 3))

    raw_data = np.vstack((cluster1, cluster2, cluster3))

    # Min-Max Normalization to scale features between 0 and 1
    min_vals = np.min(raw_data, axis=0)
    max_vals = np.max(raw_data, axis=0)

    normalized_data = (raw_data - min_vals) / (max_vals - min_vals)

    return normalized_data


# ============================================================
# KOHONEN SELF-ORGANIZING MAP (SOM) CLASS
# ============================================================

class KohonenSOM:

    def __init__(
        self,
        num_output_neurons=10,
        input_dim=3,
        initial_lr=0.5,
        total_epochs=100
    ):
        # Matching architecture: Input Layer -> Output Layer
        self.num_neurons = num_output_neurons
        self.input_dim = input_dim
        self.initial_lr = initial_lr
        self.total_epochs = total_epochs

        # FLOWCHART STEP 2: Initialize SOM Weights, Learning Rate, and Radius
        self.weights = np.random.rand(self.num_neurons, self.input_dim)
        self.initial_radius = self.num_neurons / 2.0
        self.time_constant = self.total_epochs / np.log(self.initial_radius)

    def euclidean_distance(self, x, w):
        """Calculate distance between input and neuron weight vectors."""
        return np.sqrt(np.sum((x - w) ** 2, axis=1))

    def find_bmu(self, x):
        """FLOWCHART STEP 5: Find Best Matching Unit (BMU)."""
        distances = self.euclidean_distance(x, self.weights)
        bmu_idx = np.argmin(distances)
        return bmu_idx

    def train(self, data):
        """Execute the training loop following the flowchart logic."""

        for epoch in range(self.total_epochs):

            # FLOWCHART STEPS 7 & 8: Update Learning Rate and Radius
            current_lr = self.initial_lr * np.exp(
                -epoch / self.total_epochs
            )

            current_radius = self.initial_radius * np.exp(
                -epoch / self.time_constant
            )

            # FLOWCHART STEP 3 & 9: Select an Input Pattern X
            for x in data:

                # FLOWCHART STEPS 4 & 5: Distance Calculation and BMU Identification
                bmu_idx = self.find_bmu(x)

                # FLOWCHART STEPS 6 & 7: Identify BMU's Neighbouring Neurons
                # and Update Weights
                for j in range(self.num_neurons):

                    # Lateral distance along the output layer chain
                    # (1D map topology)
                    grid_dist = np.abs(j - bmu_idx)

                    if grid_dist <= current_radius:

                        # Topological influence factor (Gaussian distribution)
                        influence = np.exp(
                            -(grid_dist ** 2) /
                            (2 * (current_radius ** 2))
                        )

                        # Weight Update Formula
                        # W_ij(new) = W_ij(old) + LR * Influence
                        #             * (X - W_ij(old))
                        self.weights[j] += (
                            current_lr
                            * influence
                            * (x - self.weights[j])
                        )

    def visualize_clusters(self, data):
        """FLOWCHART STEP 10: Visualize SOM Map and Form Clusters."""

        mapped_bmus = [self.find_bmu(x) for x in data]

        plt.figure(figsize=(12, 5))

        # Plot 1: Cluster Distribution
        plt.subplot(1, 2, 1)

        plt.hist(
            mapped_bmus,
            bins=np.arange(self.num_neurons + 1) - 0.5,
            rwidth=0.8,
            color="skyblue",
            edgecolor="black"
        )

        plt.title("Cluster Distribution across Output Neurons")
        plt.xlabel("Output Neuron Index")
        plt.ylabel("Number of Assigned Input Patterns")
        plt.xticks(range(self.num_neurons))
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Plot 2: Final Weight Matrix
        plt.subplot(1, 2, 2)

        plt.imshow(
            self.weights,
            aspect="auto",
            cmap="viridis"
        )

        plt.colorbar(label="Learned Weight Values")
        plt.title("Final Trained Weights (W_ij Matrix)")
        plt.xlabel("Input Features (X_1 to X_n)")
        plt.ylabel("Output Neurons (Y_1 to Y_m)")

        plt.tight_layout()
        plt.show()


# ============================================================
# MAIN EXECUTION
# ============================================================

if __name__ == "__main__":

    # 1. Load and Normalize Data
    data = load_and_normalize_data()

    # 2. Initialize SOM
    som = KohonenSOM(
        num_output_neurons=10,
        input_dim=3,
        initial_lr=0.6,
        total_epochs=200
    )

    # 3. Train SOM Network
    print("Training SOM according to flowchart steps...")
    som.train(data)
    print("Training finished.")

    # 4. Visualize Results
    som.visualize_clusters(data)