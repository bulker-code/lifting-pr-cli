#LIFTING PR TRACKER
CLI that can track and display PRs. All units are currently in kilograms. 


## Commands
The CLI can process the following commands. 
### add
Allows a PR to be added to the PR database. 
An example use of this command is as follows:

~ python Lifting_CLI.py add bench 120

This will initiate or update the bench pr to 120kg and output:

BENCH: 120kg

### show
Shows the entire collection of PRs that have currently been tracked. A
An example use is as follows:

~ python Lifting_CLI.py show

This will display all PRs that have been added up to this point. 
Eg.
BENCH: 120kg
SQUAT: 160kg
DEADLIFT: 180kg



