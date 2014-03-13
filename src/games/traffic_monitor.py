from engine.Project import Project
from engine.Location import Location
from engine.Module import Module
from engine.Team import Team
from engine.RevenueTier import HighRevenueTier

def get_name():
    return "3 sites - Worldwide traffic monitoring system"

def load_game():
    ''' Project is a Traffic Monitoring system made up of 3 modules:
    Traffic camera API, backend infrastructure and UI.
    Each module has been assigned in its entirity to a single location.
    '''
    project = Project('Traffic Monitor', 'Agile', 230000, HighRevenueTier())

    # Setup a team in Dublin
    dublin = Location('Dublin', 0, "Irish", 20, 25, (375,148))
    dublin_team = Team('Dublin Team', 30, 10)
    dublin.add_team(dublin_team)
    project.locations.append(dublin)
    project.home_site = dublin

    # Setup a team in Florida
    florida = Location('Florida', -8, "American", 30, 5, (192,207))
    florida_team = Team('Florida Team', 35, 25)
    florida.add_team(florida_team)
    project.locations.append(florida)

    # Setup a team in New Dehli
    new_dehli = Location('New Dehli', -11, "Indian", 30, 35, (570,264))
    new_dehli_team = Team('New Dehli Team', 15, 5)
    new_dehli.add_team(new_dehli_team)
    project.locations.append(new_dehli)

    # Create three modules and assign each one to a single location
    cam_api = Module('Traffic cam', 600)
    project.locations[0].teams[0].modules.append(cam_api)


    project.modules.append(cam_api)

    infra = Module('Backend infra', 1200)
    project.locations[1].teams[0].modules.append(infra)


    project.modules.append(infra)

    ui = Module('UI', 800)
    project.locations[2].teams[0].modules.append(ui)


    project.modules.append(ui)

    return project
