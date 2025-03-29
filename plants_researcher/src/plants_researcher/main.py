import warnings
from datetime import datetime
from plants_researcher.crew import PlantsResearcher

warnings.filterwarnings("ignore")

def run():
    """Run the research crew for a specific plant."""
    plant_name = "Rose"
    inputs = {'plant_name': plant_name, 'current_year': str(datetime.now().year)}
    
    try:
        PlantsResearcher().crew().kickoff(inputs=inputs)
        print(f"Research completed for {plant_name}. Check blog.md for details.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run()
