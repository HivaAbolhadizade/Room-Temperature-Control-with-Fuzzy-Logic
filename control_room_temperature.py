
#pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Define fuzzy variables
target_temp = ctrl.Antecedent(np.arange(0, 101, 1), 'target_temp')
voltage = ctrl.Consequent(np.arange(0, 11, 1), 'voltage', defuzzify_method='centroid')

# Define membership functions for target temperature (K) using sigmoid function
target_temp['low'] = fuzz.zmf(target_temp.universe, 15, 60)
target_temp['high'] = fuzz.smf(target_temp.universe, 15, 65)

# Plot membership functions for visualization
target_temp.view()
voltage.view()
plt.show()

# Define membership functions for voltage (V)
voltage['V1'] = fuzz.trimf(voltage.universe, [0, 0, 5])
voltage['V2'] = fuzz.trimf(voltage.universe, [5, 10, 10])

# Define the rules
rule1 = ctrl.Rule(target_temp['low'], voltage['V1'])
rule2 = ctrl.Rule(target_temp['high'], voltage['V2'])

# Create the control system
voltage_ctrl = ctrl.ControlSystem([rule1, rule2])
voltage_sim = ctrl.ControlSystemSimulation(voltage_ctrl)

# Function to simulate voltage based on target temperature and plot the steps
def simulate_voltage_and_plot(K):
    # Fuzzification
    voltage_sim.input['target_temp'] = K
    
    # Compute membership values for K
    mem_low = fuzz.interp_membership(target_temp.universe, target_temp['low'].mf, K)
    mem_high = fuzz.interp_membership(target_temp.universe, target_temp['high'].mf, K)
    
    # Visualize fuzzification
    target_temp.view(sim=voltage_sim)
    plt.axvline(x=K, color='r', linestyle='--', label=f'K={K}')
    plt.scatter([K], [mem_low], color='b', label=f'Membership Low={mem_low:.2f}')
    plt.scatter([K], [mem_high], color='g', label=f'Membership High={mem_high:.2f}')
    plt.title(f"Fuzzification of Target Temperature (K={K})")
    plt.xlabel('Temperature (K)')
    plt.ylabel('Membership')
    plt.legend()
    plt.show()
    
    # Compute the result to visualize the intermediate steps
    voltage_sim.compute()

    V = voltage_sim.output['voltage']
    
    # Visualize the fuzzy inference results
    voltage.view(sim=voltage_sim)
    plt.title(f"Fuzzy Inference of Voltage for Target Temperature (K={K})")
    plt.xlabel('Voltage (V)')
    plt.ylabel('Membership')
    
    # Annotate the plot with the V value
    plt.annotate(f'V = {V:.2f}', xy=(V, 0), xytext=(V, 0.5),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 horizontalalignment='center', verticalalignment='bottom')
    
    plt.show()
    
    # Output the defuzzified result
    print(f"Target Temperature: {K} -> Voltage: {V}")
    
    return V

# Example simulation and plots
K = 30  # Example target temperature
V = simulate_voltage_and_plot(K)
