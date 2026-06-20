#LIFTING PR CLI

import sys
import json
"""
class PR_database(dict): 

    #class to hold information pertaining to lift PRs

    def __init__(self, lift_dict:dict):
        self.lift_prs = lift_dict
        

    def add_pr(self, lift_name: str, lift_weight):
        self.lift_prs.update({lift_name:lift_weight})
        print(f"{lift_name}: {lift_weight}kg")

    def show(self):
        for lift in self.lift_prs:
            print(f"{lift.upper()}: {self.lift_prs[lift]}kg")
        
        
    
prs = PR_database({"Bench": 0, "Squat": 0, "Deadlift": 0})
#prs.add_pr("Bench", 115)
#prs.add_pr("Squat", 160)
#prs.show()
"""
try:
    with open('output.json', 'r') as file:
        current_prs = json.load(file)
except FileNotFoundError:
    with open('output.json', 'w') as file:
        current_prs = {}

script_name = sys.argv[0]
cmd1 = sys.argv[1]

if cmd1 == "add":
    lift_name = sys.argv[2].upper()
    weight_lifted = sys.argv[3]
    current_prs.update({lift_name: weight_lifted})
    print(f"{lift_name}: {weight_lifted}kg")

if cmd1 == "show":
    for lift in current_prs:
        print(f"{lift.upper()}: {current_prs[lift]}kg")

with open('output.json', 'w') as file:
    json.dump(current_prs, file, indent=4)


    

    


