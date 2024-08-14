# Room Temperature Control with Fuzzy Logic
This repository contains the implementation of a fuzzy logic-based temperature control system for a room. The system is designed to maintain a comfortable room temperature by controlling the operation of a heating and cooling system.

## Introduction
The goal of this project is to develop a fuzzy logic-based temperature control system that ensures a stable and comfortable environment in a room. Fuzzy logic is particularly well-suited for this application due to its ability to handle uncertainties and approximate reasoning, which are inherent in real-world control systems.

## System Overview
The temperature control system operates by adjusting the flow of warm or cool air through a pump. The fuzzy logic controller processes the temperature difference between the desired setpoint and the current room temperature to determine the appropriate control actions. The controller is capable of responding to temperature variations in a flexible and human-like manner, making it ideal for maintaining a comfortable room environment.

## Fuzzy Logic Controller Design
### Fuzzy Variables
The system uses the following fuzzy variables:

1. Input Variable: Temperature Difference (ΔT)

Describes the difference between the current room temperature and the desired setpoint.
Fuzzy Sets: Negative, Zero, Positive
2. Output Variable: Pump Control (PumpAction)

Determines the speed and direction of the pump to control the air flow.
Fuzzy Sets: Decrease, Hold, Increase

### Fuzzy Rules
The control decisions are made based on a set of fuzzy rules that relate the input variable to the output variable. The rules are designed to adjust the pump's action to decrease, hold, or increase the air flow depending on the temperature difference.

Example fuzzy rules:

If (ΔT is Negative) then (PumpAction is Decrease)
If (ΔT is Zero) then (PumpAction is Hold)
If (ΔT is Positive) then (PumpAction is Increase)

### Fuzzy Inference System
The fuzzy inference process involves:

Fuzzification: Converting the crisp input temperature difference into fuzzy values.
Rule Evaluation: Applying the fuzzy rules to generate fuzzy outputs.
Defuzzification: Converting the fuzzy output into a crisp value to control the pump.
Simulation and Results
The system's performance is simulated to demonstrate its ability to maintain a stable room temperature. The simulation results, including temperature trends and pump actions, are visualized using Matplotlib.

### Requirements
Python 3.x
NumPy
Matplotlib
scikit-fuzzy (skfuzzy)

## Installation

<ol>
  <li>
    Clone the repository:
    <pre><code>git clone https://github.com/yourusername/fuzzy-temperature-control.git
cd fuzzy-temperature-control</code></pre>
  </li>
  <li>
    Install the required Python libraries:
    <pre><code>pip install numpy matplotlib scikit-fuzzy</code></pre>
  </li>
</ol>

<h2>Usage</h2>
<ol>
  <li>
    Run the main script to simulate the temperature control system:
    <pre><code>python main.py</code></pre>
  </li>
  <li>
    Adjust the setpoint or modify the fuzzy rules in the <code>fuzzy_controller.py</code> file to customize the system's behavior.
  </li>
  <li>
    The simulation results will be displayed as graphs showing the room temperature and pump actions over time.
  </li>
</ol>


## Contributing
Contributions are welcome! If you have any ideas for improvements or find any issues, feel free to submit a pull request or open an issue in the repository.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
