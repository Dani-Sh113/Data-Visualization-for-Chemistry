import matplotlib.pyplot as plt
import numpy as np
import math
from sklearn.datasets import load_wine



def plot_3s_wave_function():
    
    print("Generating Plot 1: 3s Radial Wave Function...")

    def orbital_3s_psi(r):
        # The mathematical function for the 3s orbital radial wave function
        
        psi = (2 / 27) * np.sqrt(3) * (2 * r**2 / 9 - 2 * r + 3) * np.exp(-r / 3)
        return psi

    # Generate data to plot using NumPy for better performance
    r_values = np.linspace(0, 40, 200)
    psi_3s_values = orbital_3s_psi(r_values)

    # Create the plot
    plt.figure(figsize=(8, 5))
    plt.plot(r_values, psi_3s_values, "g-", label='$\Psi$') # Solid green line
    plt.axhline(0, color='black', linewidth=0.5) # Add a line at y=0
    plt.xlabel("Radius, $a_0$ (Bohr radii)")
    plt.ylabel('Wave Function, $\Psi$')
    plt.title('3s Radial Wave Function')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Save the figure
    plt.savefig("3s_wave_function.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_molar_mass_bar_chart():
    
    print("Generating Plot 2: Molar Mass Bar Chart...")
    
    atomic_numbers = list(range(1, 11))
    element_names = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne']
    molar_masses = [1.01, 4.04, 6.94, 9.01, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18]
    error = 0.1 # A single error value for all bars

    plt.figure(figsize=(10, 6))
    plt.bar(atomic_numbers, molar_masses, yerr=error, capsize=5, color='skyblue', ecolor='darkred', label='Molar Mass')
    
    plt.xlabel('Element')
    plt.ylabel('Molar Mass (g/mol)')
    plt.title('Molar Mass of the First 10 Elements')
    plt.xticks(atomic_numbers, element_names) # Use element symbols as labels
    plt.legend()

    plt.savefig("molar_mass_plot.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_wine_data_scatter():
   
    print("Generating Plot 3: Wine Dataset Scatter Plot...")
    
    wine_data = load_wine().data

    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(wine_data[:, 0], wine_data[:, 5], c=wine_data[:, 12], cmap='viridis')
    
    plt.xlabel("Alcohol Content")
    plt.ylabel("Alkalinity of Ash")
    plt.title("Wine Dataset: Alcohol Content vs. Ash Alkalinity")
    
    cbar = plt.colorbar(scatter)
    cbar.set_label("Proline Content")

    plt.savefig("wine_scatter_plot.png", dpi=300, bbox_inches='tight')
    plt.show()


def plot_halogen_properties_scatter():
    
    print("Generating Plot 4: Halogen Properties Scatter Plot...")

    # Halogen data
    elements = ['Fluorine', 'Chlorine', 'Bromine', 'Iodine', 'Astatine']
    atomic_numbers = [9, 17, 35, 53, 85]
    electronegativities = [3.98, 3.16, 2.96, 2.66, 2.2]
    atomic_radii = np.array([64, 99, 114, 133, 202])  # in pm

    # Normalize atomic radii for marker size to make them look good on the plot
    marker_sizes = atomic_radii * 3

    # Create the plot
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(atomic_numbers, electronegativities, s=marker_sizes, alpha=0.7, c=atomic_radii, cmap='plasma')

    # Adding color bar for atomic radius
    cbar = plt.colorbar(scatter)
    cbar.set_label('Atomic Radius (pm)')

    # Adding titles and labels
    plt.title('Electronegativity vs. Atomic Number for Halogens')
    plt.xlabel('Atomic Number')
    plt.ylabel('Electronegativity (Pauling Scale)')
    plt.xticks(atomic_numbers, elements)
    plt.grid(True, linestyle='--', alpha=0.6)

    plt.savefig("halogen_properties_plot.png", dpi=300, bbox_inches='tight')
    plt.show()



if __name__ == '__main__':
    
    plot_3s_wave_function()
    plot_molar_mass_bar_chart()
    plot_wine_data_scatter()
    plot_halogen_properties_scatter()