# Bridging Linear Algebra (Eigenvalues) and AI (Dimension Reduction)

import numpy as np

def simple_pca_logic():
    # 1. Create a 2D Dataset (e.g., Height and Weight of students)
    # This data is highly correlated (as one grows, usually the other does too)
    data = np.array([[150, 50], 
                     [160, 60], 
                     [170, 70], 
                     [180, 80]])

    print("---  AI Math: PCA & Eigenvectors ---")
    print(f"Original 2D Data (Height, Weight):\n{data}")

    # 2. Center the data (Subtract the mean)
    mean_vec = np.mean(data, axis=0)
    centered_data = data - mean_vec

    # 3. Calculate Covariance Matrix (Linear Algebra Concept)
    cov_matrix = np.cov(centered_data.T)

    # 4. Find Eigenvalues and Eigenvectors
    # These tell us the "Principal Components" (directions of max variance)
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    print(f"\nEigenvalues (Importance of each component):")
    print(eigenvalues)
    
    print(f"\nEigenvectors (The new 'Directions' for our data):")
    print(eigenvectors)

if __name__ == "__main__":
    simple_pca_logic()