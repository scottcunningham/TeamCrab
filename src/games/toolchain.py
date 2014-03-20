from engine.Project import Project
from engine.Location import Location
from engine.Module import Module
from engine.Team import Team
from engine.RevenueTier import MediumRevenueTier

def get_name():
    return "7 sites - Worldwide toolchain development"

def load_game():
    ''' Project is a toolchain for a microprocessor architecture with a purpose-built
    high level programming language made up of 7 modules:
    Compiler frontend, compiler backend, assembler, disassembler, linker, debugger and virtual machine.
    Each module in its entirity has been assigned to a single team.
    '''
    project = Project('Tool Chain', 'Agile', 250000, MediumRevenueTier())

    # Setup a team in Rio de Janeiro
    rio_de_janeiro = Location('Rio de Janeiro', -3, "Brazilian", 20, 25, (285,337))
    rio_de_janeiro_team = Team('Rio de Janeiro', 30, 10)
    rio_de_janeiro.add_team(rio_de_janeiro_team)
    project.locations.append(rio_de_janeiro)

    # Setup a team in Florida
    florida = Location('Florida', -8, "American", 30, 5, (192,207))
    florida_team = Team('Florida', 35, 25)
    florida.add_team(florida_team)
    project.locations.append(florida)

    # Setup a team in Toronto
    toronto = Location('Toronto', -5, "Canadian", 30, 35, (206,179))
    toronto_team = Team('Toronto', 15, 15)
    toronto.add_team(toronto_team)
    project.locations.append(toronto)

    # Setup a team in Dublin
    dublin = Location('Dublin', 0, "Irish", 20, 25, (375,148))
    dublin_team = Team('Dublin', 30, 10)
    dublin.add_team(dublin_team)
    project.locations.append(dublin)
    project.home_site = dublin

    # Setup a team in Canberra
    canberra = Location('Canberra', +11, "Australian", 30, 35, (733,369))
    canberra_team = Team('Canberra', 15, 25)
    canberra.add_team(canberra_team)
    project.locations.append(canberra)

    # Setup a team in Tokyo
    tokyo = Location('Tokyo', +9, "Japanese", 20, 25, (704,201))
    tokyo_team = Team('Tokyo', 15, 20)
    tokyo.add_team(tokyo_team)
    project.locations.append(tokyo)

    # Setup a team in Nuuk
    nuuk = Location('Nuuk', -3, "Canadian", 25, 30, (273,68))
    nuuk_team = Team('Nuuk', 20, 25)
    nuuk.add_team(nuuk_team)
    project.locations.append(nuuk)

    # Create modules and assign tasks to appropriate teams
    comp_fe = Module('Frontend', 600)
    project.modules.append(comp_fe)
    comp_be = Module('Backend', 1200)
    project.modules.append(comp_be)
    asm = Module('Assembler', 600)
    project.modules.append(asm)
    disasm = Module('Disassembler', 800)
    project.modules.append(disasm)
    linker = Module('Linker', 600)
    project.modules.append(linker)
    debugger = Module('Debugger', 1000)
    project.modules.append(debugger)
    vm = Module('VM', 600)
    project.modules.append(vm)

    project.locations[0].teams[0].modules.append(comp_fe)
    project.locations[1].teams[0].modules.append(comp_be)
    project.locations[2].teams[0].modules.append(asm)
    project.locations[3].teams[0].modules.append(disasm)
    project.locations[4].teams[0].modules.append(linker)
    project.locations[5].teams[0].modules.append(debugger)
    project.locations[6].teams[0].modules.append(vm)

    return project
