# Slave Engine
Very simple Python game engine with a component system. Currently the backend is powered by pygame, but it should be easily ported to any library or language if needed.

## Repository structure
- *ecs:* component system, pure Python.
- *engine:* game engine, built on top of the ecs and pygame.
- *pong_test:* example project.

## Requirements
- Python 3
- pygame 1.9

A requirements.txt file is included for convenience, just run *pip install -r requirements.txt* with your virtualenv active.