# Room Temperature Control with Fuzzy Logic
This project was developed as part of the course Soft Computing under the supervision of Dr.Bahrololoum at Shahid Bahonar University of Kerman. The aim of the project is to implement a fuzzy logic-based temperature control system that ensures a stable and comfortable environment in a room. Fuzzy logic is particularly well-suited for this application due to its ability to handle uncertainties and approximate reasoning, which are inherent in real-world control systems.

## Introduction
The goal of this project is to develop a fuzzy logic-based temperature control system that ensures a stable and comfortable environment in a room. Fuzzy logic is particularly well-suited for this application due to its ability to handle uncertainties and approximate reasoning, which are inherent in real-world control systems.

<img src="https://github.com/user-attachments/assets/96e4a0b9-5e41-4c8a-8b76-ecfb3fcd7139" alt="description" width="400"/>

## System Overview
The temperature control system operates by adjusting the flow of warm or cool air through a pump. The fuzzy logic controller processes the temperature difference between the desired setpoint and the current room temperature to determine the appropriate control actions. The controller is capable of responding to temperature variations in a flexible and human-like manner, making it ideal for maintaining a comfortable room environment.

<img src="https://github.com/user-attachments/assets/eeb4d89c-94dd-49f3-a587-da64685ef62e" alt="description" width="300"/>
<img src="https://github.com/user-attachments/assets/3e39f407-e7d0-48ec-adb5-3dcd5db3bbb5" alt="description" width="300"/>

## Fuzzy Logic Controller Design

<img src="https://github.com/user-attachments/assets/39c51032-8863-43a4-947d-2864793f0198" alt="description" width="300"/>

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

### example of the result 

<img src="https://github.com/user-attachments/assets/625bdf40-128a-46cf-8b66-7162429a9fa6" alt="description" width="300"/>
<img src="https://github.com/user-attachments/assets/6d8270df-11f5-4980-8b2c-10a95c23c931" alt="description" width="300"/>

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
