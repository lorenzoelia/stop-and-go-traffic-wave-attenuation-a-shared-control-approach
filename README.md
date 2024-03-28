# Stop and Go Traffic Wave Attenuation: A Shared Control Approach

## Introduction

This project focuses on simulating a shared control approach for attenuating traffic waves in stop-and-go traffic scenarios. It employs a combination of human driving behavior models and autonomous control algorithms to optimize traffic flow and reduce congestion.

## Features

- Shared control parameters customization
- Simulation setup configuration
- Results logging and visualization

## Installation

1. Clone the repository:

```
git clone github.com/lorenzoelia/stop-and-go-traffic-wave-attenuation-a-shared-control-approach
```

2. Install SUMO (Simulation of Urban MObility) if not already installed. Refer to the [SUMO documentation](https://sumo.dlr.de/docs/) for installation instructions.

3. Set up the SUMO_HOME environment variable to point to the SUMO installation directory.

4. Install any required Python dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Configure the parameters in the config file (`config.py`) according to your simulation requirements.

2. Run the simulation script:

```
python stop_and_go_traffic_wave_attenuation_a_shared_control_approach\main.py
```

3. Monitor the simulation progress and view the results in the designated output directory.


## Contributing

Contributions to the project are welcome!

## License

This project is licensed under the [MIT License](LICENSE).

## Project Structure

```
stop_and_go_traffic_wave_attenuation_a_shared_control_approach/
    config.py
    main.py
    __init__.py
    data_prep/
        demand_generator.py      # Script to generate demand for simulation
        XML_file_editor.py      # Script to edit XML files for simulation
        __init__.py
        __pycache__/
            demand_generator.cpython-310.pyc
            XML_file_editor.cpython-310.pyc
            __init__.cpython-310.pyc
    post_processing/
        __init__.py
    preprocessing/
        XML_to_CSV_converter.py # Script to convert XML data to CSV format
        __init__.py
        __pycache__/
            XML_to_CSV_converter.cpython-310.pyc
            __init__.cpython-310.pyc
    processing/
        sensitivity_analysis.py # Script for sensitivity analysis
        __init__.py
        __pycache__/
            sensitivity_analysis.cpython-310.pyc
            __init__.cpython-310.pyc
    simulation/
        simulation_handler.py  # Script to handle simulation process
        __init__.py
        simulation_engine/
            arbitration.py     # Script for arbitration in simulation
            data_saver.py      # Script to save simulation data
            simulator.py       # Script for simulation logic
            vehicle.py         # Script defining vehicle behavior
            __init__.py
            sumo_config/
                circle.add.xml # SUMO configuration files
                circle.net.xml
                circle.rou.xml
                circle.sumocfg
                ring1.add.xml
                ring1.net.xml
                ring1.rou.xml
                ring1.sumocfg
                ring2.add.xml
                ring2.net.xml
                ring2.rou.xml
                ring2.sumocfg
    utils/
        constants.py            # File containing project constants
        __init__.py
    visualization/
        __init__.py
```

## Project Explanation

- **data_prep/**: Contains scripts for generating and editing data files used in simulation.
- **post_processing/**: Placeholder directory for post-processing scripts.
- **preprocessing/**: Contains scripts for preprocessing data before simulation.
- **processing/**: Scripts for processing simulation data, including sensitivity analysis.
- **simulation/**: Main directory for simulation-related scripts and configurations.
  - **simulation_engine/**: Scripts defining simulation logic and behavior.
  - **sumo_config/**: Configuration files for SUMO simulation engine.
- **utils/**: Utility scripts and files, including constants used across the project.
- **visualization/**: Placeholder directory for visualization scripts.
