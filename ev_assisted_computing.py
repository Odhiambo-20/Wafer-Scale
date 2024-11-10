# ev_assisted_computing.py

import simpy
import numpy as np

class EV:
    def __init__(self, env, ev_id, charge_level=200, cost_per_unit=0.5):
        self.env = env
        self.ev_id = ev_id
        self.charge_level = charge_level
        self.cost_per_unit = cost_per_unit
        self.available = True

    def provide_service(self, compute_units):
        if self.charge_level >= compute_units:
            self.charge_level -= compute_units
            print(f"[{self.env.now}] EV-{self.ev_id} provided {compute_units} units of compute")
            return compute_units * self.cost_per_unit
        else:
            print(f"[{self.env.now}] EV-{self.ev_id} has insufficient charge.")
            return float('inf')

class EdgeDataCenter:
    def __init__(self, env, peak_cost_multiplier=1.5, base_cost=1.0):
        self.env = env
        self.peak_cost_multiplier = peak_cost_multiplier
        self.base_cost = base_cost
        self.energy_cost = 0

    def compute(self, units, peak_hour):
        cost_multiplier = self.peak_cost_multiplier if peak_hour else 1
        compute_cost = units * self.base_cost * cost_multiplier
        self.energy_cost += compute_cost
        print(f"[{self.env.now}] EDC computed {units} units at cost {compute_cost}")
        return compute_cost

# ev_assisted_computing.py

class EVAssistedSimulation:
    def __init__(self, env, ev_count=10, tasks=50, task_compute=100, time_peak=20):
        self.env = env
        self.time_peak = time_peak
        self.evs = [EV(env, ev_id=i) for i in range(ev_count)]
        self.edc = EdgeDataCenter(env)
        self.tasks = [{'compute_units': task_compute} for _ in range(tasks)]

    def offload_tasks(self):
        for task in self.tasks:
            self.env.process(self.process_task(task))
            yield self.env.timeout(1)  # Add a 1-time-unit delay between each task

    def process_task(self, task):
        peak_hour = self.env.now >= self.time_peak
        best_ev = min(self.evs, key=lambda ev: ev.charge_level if ev.available else float('inf'))
        if best_ev.charge_level >= task['compute_units']:
            best_ev.provide_service(task['compute_units'])
        else:
            self.edc.compute(task['compute_units'], peak_hour)
        yield self.env.timeout(1)  # Simulate time delay for processing task

def run_ev_assisted_computing(env):
    sim = EVAssistedSimulation(env)
    sim.offload_tasks()
    yield env.timeout(30)
