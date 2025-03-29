#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from plants_researcher.crew import PlantsResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with a specific plant name as input.
    """
    plant_name = sys.argv[1] if len(sys.argv) > 1 else "Tomato"
    inputs = {
        'plant_name': plant_name,
        'current_year': str(datetime.now().year)
    }
    
    try:
        PlantsResearcher().crew().kickoff(inputs=inputs)
        print(f"Research and blog for {plant_name} completed. Check blog.md for details.")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "plant_name": "Tomato"
    }
    try:
        PlantsResearcher().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        PlantsResearcher().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and return the results.
    """
    plant_name = sys.argv[1] if len(sys.argv) > 1 else "Tomato"
    inputs = {
        "plant_name": plant_name,
        "current_year": str(datetime.now().year)
    }
    try:
        PlantsResearcher().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()
