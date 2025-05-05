"""
# Genotype Plotting Script

This script reads `.xvg` files and generates both individual and combined plots for RMSD and RMSF data of multiple genotypes using `matplotlib`.

## Features
- Parses `.xvg` files while skipping comments and headers.
- Creates individual RMSD plots for each genotype
- Creates individual RMSF plots for each genotype
- Creates one combined plot with all 5 genotypes' RMSD data
- Creates one combined plot with all 5 genotypes' RMSF data
- Saves plots as PNG files.

## Dependencies
```bash
pip install matplotlib numpy
```

## File Structure
Assumes the following input files are present in the working directory:
```
g1_rmsd.xvg
...
g5_rmsd.xvg
g1_rmsf.xvg
...
g5_rmsf.xvg
```

## Usage
Run the script directly:
```bash
python plot_genotypes.py
```

## Output
- Individual RMSD plots:
  - `rmsd_Genotype_1.png`, ..., `rmsd_Genotype_5.png`
- Individual RMSF plots:
  - `rmsf_Genotype_1.png`, ..., `rmsf_Genotype_5.png`
- Combined plots:
  - `rmsd_combined.png`
  - `rmsf_combined.png`
"""
## Python Code
```python
import matplotlib.pyplot as plt
import numpy as np

def read_xvg_data(file_path):
    x_values, y_values = [], []
    with open(file_path, 'r') as f:
        for line in f:
            if line.startswith("#") or line.startswith("@"):  
                continue
            data = line.split()
            x_values.append(float(data[0]))
            y_values.append(float(data[1]))
    return np.array(x_values), np.array(y_values)

def plot_combined_data(genotype_files, labels, title, xlabel, ylabel, output_file, colors):
    plt.figure(figsize=(10, 6))
    for i, file in enumerate(genotype_files):
        x, y = read_xvg_data(file)
        plt.plot(x, y, label=labels[i], color=colors[i], linewidth=1.5)

    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)
    plt.grid(True)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()
    print(f"Combined plot saved as {output_file}")

def plot_individual_genotypes(files, labels, title_prefix, xlabel, ylabel, output_prefix, colors):
    for i, file in enumerate(files):
        x, y = read_xvg_data(file)
        plt.figure(figsize=(8, 5))
        plt.plot(x, y, color=colors[i], linewidth=1.5)
        plt.title(f"{title_prefix} - {labels[i]}", fontsize=14)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.grid(True)
        plt.tight_layout()
        output_file = f"{output_prefix}_{labels[i].replace(' ', '_')}.png"
        plt.savefig(output_file)
        plt.close()
        print(f"Individual plot saved as {output_file}")

if __name__ == "__main__":
    rmsd_files = ["g1_rmsd.xvg", "g2_rmsd.xvg", "g3_rmsd.xvg", "g4_rmsd.xvg", "g5_rmsd.xvg"]
    rmsf_files = ["g1_rmsf.xvg", "g2_rmsf.xvg", "g3_rmsf.xvg", "g4_rmsf.xvg", "g5_rmsf.xvg"]
    labels = ["Genotype 1", "Genotype 2", "Genotype 3", "Genotype 4", "Genotype 5"]
    colors = ["blue", "red", "green", "orange", "purple"]

    print("Generating individual RMSD plots...")
    plot_individual_genotypes(rmsd_files, labels, "RMSD vs Time", 
                              "Time (ns)", "RMSD (nm)", "rmsd", colors)

    print("Generating individual RMSF plots...")
    plot_individual_genotypes(rmsf_files, labels, "RMSF vs Residue", 
                              "Residue", "RMSF (nm)", "rmsf", colors)

    print("Generating combined RMSD plot...")
    plot_combined_data(rmsd_files, labels, "RMSD vs Time for Different Genotypes", 
                       "Time (ns)", "RMSD (nm)", "rmsd_combined.png", colors)

    print("Generating combined RMSF plot...")
    plot_combined_data(rmsf_files, labels, "RMSF vs Residue for Different Genotypes", 
                       "Residue", "RMSF (nm)", "rmsf_combined.png", colors)

    print("All plotting completed successfully!")
```

---

 
**Author**: Hariprasad T
---

