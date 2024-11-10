# wafer_level_packaging.py

import numpy as np

class WaferPackage:
    def __init__(self, num_layers=5, interlayer_temp_limit=80):
        self.num_layers = num_layers
        self.interlayer_temp_limit = interlayer_temp_limit
        self.layer_temps = np.zeros(num_layers)
        self.heat_generation_rate = np.random.uniform(1, 5, size=num_layers)

    def simulate_heat(self, compute_units):
        for layer in range(self.num_layers):
            added_heat = self.heat_generation_rate[layer] * compute_units / 100
            self.layer_temps[layer] += added_heat
            if self.layer_temps[layer] > self.interlayer_temp_limit:
                print(f"Warning: Layer {layer} exceeds temperature limit! Current Temp: {self.layer_temps[layer]}")

    def dissipate_heat(self):
        # Assume passive heat dissipation that reduces temp by a fixed rate
        self.layer_temps -= 1
        self.layer_temps = np.clip(self.layer_temps, 0, None)  # No negative temperatures
        print(f"Heat levels after dissipation: {self.layer_temps}")

def run_wafer_packaging_simulation():
    package = WaferPackage()
    for _ in range(10):  # Simulate 10 compute tasks
        package.simulate_heat(compute_units=100)
        package.dissipate_heat()
