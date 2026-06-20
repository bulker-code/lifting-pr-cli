#LIFTING PR CLI

class PR_database(object): 

    #class to hold information pertaining to lift PRs

    def __init__(self, lift_name, lift_weight):
        self.lift_prs = {lift_name: lift_weight}

    def add_pr(self, lift_name, lift_weight):
        self.lift_prs