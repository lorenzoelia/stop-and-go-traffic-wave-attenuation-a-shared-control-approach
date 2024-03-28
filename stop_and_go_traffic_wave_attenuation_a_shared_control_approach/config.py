import os

# Project root
PROJECT_ROOT = 'stop_and_go_traffic_wave_attenuation_a_shared_control_approach'

# Shared control parameters
TIME_TO_COLLISION = 1.0
DELTA = 0.25

# Simulation setup
NUM_VEHICLES_PER_ROUTE = 20
NUM_ROUTES = 4
ROUTE_LENGTH = 224.56
TIME_STEP = 0.1
STOP_AND_GO_GENERATION_TIME = 500.0    # Time-steps, not seconds
SIMULATION_END = 10000
MONTECARLO_ITERATIONS = 1
ACC_PENETRATION_PERCENTAGE_SPLITS = 1
IDM_PENETRATION_PERCENTAGE_SPLITS = 10
SHC_PENETRATION_PERCENTAGE_SPLITS = 10

LEADER_STARTING_SPEED = 6
LEADER_ENDING_SPEED = 4

# Results
SIMULATIONS_ROOT = 'results'

# SUMO simulation
SUMO_HOME = os.environ['SUMO_HOME']
# SUMO_BINARY = os.path.join('bin', 'sumo-gui')  # Uncomment for gui display
SUMO_BINARY = os.path.join('bin', 'sumo')
SUMO_CONFIG_ROOT = os.path.join(PROJECT_ROOT, 'simulation', 'simulation_engine', 'sumo_config')
SUMO_CFG_FILE = 'circle.sumocfg'
SUMO_ROUTE_FILE = 'circle.rou.xml'
SUMO_OPTIONS = {
    '--step-length': TIME_STEP,
    '--xml-validation': 'never',
    '--time-to-teleport': -1,
    '--random': None,
    '--ignore-route-errors': None
}


