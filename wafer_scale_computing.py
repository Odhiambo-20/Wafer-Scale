# wafer_scale_computing.py

import numpy as np

class WaferScaleProcessor:
    def __init__(self, num_cores=64):
        self.num_cores = num_cores
        self.core_temps = np.zeros(num_cores)
        self.core_usage = np.zeros(num_cores)

    def assign_task(self, compute_units):
        # Find the core with the lowest temperature and assign task
        core_id = np.argmin(self.core_temps)
        added_heat = compute_units * 0.05  # Arbitrary heat addition factor
        self.core_temps[core_id] += added_heat
        self.core_usage[core_id] += compute_units
        print(f"Task assigned to core {core_id}. Core temperature: {self.core_temps[core_id]}")

    def manage_heat(self):
        # Cool down each core slightly
        self.core_temps -= 0.5
        self.core_temps = np.clip(self.core_temps, 0, None)
        print(f"Core temperatures after cooling: {self.core_temps}")

def run_wafer_scale_computing_simulation():
    processor = WaferScaleProcessor()
    for _ in range(10):  # Simulate 10 tasks
        processor.assign_task(compute_units=100)
        processor.manage_heat()
