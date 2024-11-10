# main_program.py

import simpy
from ev_assisted_computing import run_ev_assisted_computing
from wafer_level_packaging import run_wafer_packaging_simulation
from wafer_scale_computing import run_wafer_scale_computing_simulation

def main():
    # Environment for EV-Assisted Computing
    env = simpy.Environment()
    print("Running EV-Assisted Computing Simulation")
    env.process(run_ev_assisted_computing(env))
    env.run()

    # Run Wafer-Level Packaging Simulation
    print("\nRunning Wafer-Level Packaging Simulation")
    run_wafer_packaging_simulation()

    # Run Wafer-Scale Computing Simulation
    print("\nRunning Wafer-Scale Computing Simulation")
    run_wafer_scale_computing_simulation()

if __name__ == "__main__":
    main()
