
"""
# Hydrogen Bond Plotting Script

This script reads hydrogen bond data from `.xvg` files, generates individual plots for each genotype's hydrogen bonds, and creates a combined plot comparing the hydrogen bonds across multiple genotypes.

## Code
"""
```python
import matplotlib.pyplot as plt
import numpy as np

def read_hbond_data(file_path):
    """Reads hydrogen bond data from an .xvg file, skipping headers and comments."""
    time = []
    hbonds = []
    
    with open(file_path, 'r') as file:
        for line in file:
            # Skip comment lines starting with "@" or "#"
            if line.startswith("@") or line.startswith("#"):
                continue
            
            # Parse numerical data lines
            parts = line.split()
            if len(parts) >= 2:  # Ensure the line contains at least two columns
                time.append(float(parts[0]))
                hbonds.append(int(float(parts[1])))
    
    return np.array(time), np.array(hbonds)

def plot_individual_hbonds(file_path, genotype_label, color, output_prefix):
    """Creates an individual plot for a single genotype's H-bonds."""
    # Read data from the file
    time, hbonds = read_hbond_data(file_path)
    
    # Calculate average number of H-bonds
    avg_hbonds = np.mean(hbonds)
    
    # Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(time, hbonds, label=f"{genotype_label}", color=color)
    plt.axhline(y=avg_hbonds, color='r', linestyle='--', 
                label=f"Average: {avg_hbonds:.2f}")
    
    plt.title(f"Number of Hydrogen Bonds Over Time - {genotype_label}")
    plt.xlabel("Time (ns)")
    plt.ylabel("Number of Hydrogen Bonds")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot
    output_file = f"{output_prefix}_{genotype_label.replace(' ', '_')}.png"
    plt.savefig(output_file)
    plt.close()
    print(f"Individual H-bond plot saved as {output_file}")
    
    return avg_hbonds

def plot_combined_hbonds(file_paths, genotype_labels, colors, output_file):
    """Creates a combined plot with H-bonds from all genotypes."""
    plt.figure(figsize=(12, 7))
    averages = []
    
    # Plot each genotype
    for i, file_path in enumerate(file_paths):
        time, hbonds = read_hbond_data(file_path)
        avg_hbonds = np.mean(hbonds)
        averages.append(avg_hbonds)
        
        plt.plot(time, hbonds, label=f"{genotype_labels[i]} (Avg: {avg_hbonds:.2f})", 
                 color=colors[i], linewidth=1.5)
    
    plt.title("Comparison of Hydrogen Bonds Across Genotypes")
    plt.xlabel("Time (ns)")
    plt.ylabel("Number of Hydrogen Bonds")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # Save the plot
    plt.savefig(output_file)
    plt.close()
    print(f"Combined H-bond plot saved as {output_file}")
    
    return averages

if __name__ == "__main__":
    # Define input files for all genotypes
    hbond_files = [
        "g1_hb_all.xvg", 
        "g2_hb_all.xvg", 
        "g3_hb_all.xvg", 
        "g4_hb_all.xvg", 
        "g5_hb_all.xvg"
    ]
    
    labels = ["Genotype 1", "Genotype 2", "Genotype 3", "Genotype 4", "Genotype 5"]
    colors = ["blue", "red", "green", "orange", "purple"]
    
    # Create individual plots for each genotype
    print("\nGenerating individual H-bond plots...")
    all_averages = []
    for i, file_path in enumerate(hbond_files):
        avg = plot_individual_hbonds(file_path, labels[i], colors[i], "hbonds")
        all_averages.append(avg)
    
    # Create a combined plot with all genotypes
    print("\nGenerating combined H-bond plot...")
    combined_averages = plot_combined_hbonds(hbond_files, labels, colors, "hbonds_combined.png")
    
    # Print summary of average H-bonds for each genotype
    print("\nSummary of average hydrogen bonds:")
    for i, label in enumerate(labels):
        print(f"{label}: {all_averages[i]:.2f}")
    
    print("\nAll hydrogen bond plots generated successfully!")

-----
**Author**: Hariprasad T
-----
