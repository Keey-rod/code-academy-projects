# Time Traveler's Toolkit
 
 A Python based interactive program built as part of the Codecademy course. The Time Travel's Toolkit randomly generates a travel destination and year and calculates the cost of time travel based on the year difference. The program outputs a personalized message with all the time travel details a future adventurer needs to know. 

 ## Table of Contents
 * [Overview](#overview)
 * [Features](#features)
 * [Skills Practiced](#skills-practiced)
 * [Sample Output](#sample-output)
 * [How To Run](#how-to-run)
 * [What's Next](#whats-next)
 
 
 ## Overview
 
 This project simulates a time travel agency experience. When run, it:
 * Picks a random year and destination
 * Calculates the cost of travel using a custom formula
 * Displays a fun and personalized message to the traveler

 ## Features

* **Current Year Detection:** Uses `datetime` to get the current year and time 
 * **Random Destination & Year:** Uses `randint` and `random.choice()` to select a year and location
 * **Cost Calculator:** A function calculates the cost based on the number of years traveled and a multiplier
 * **Interactive Output:** Presents a final message with the destination, year, and total cost

 ## Skills Practiced

 * Importing and using Pyton libraries (`datetime`, `random`)
 * Writing and calling functions
 * Mathematical operations and type conversion
 * String formatting and user-friendly output

 ## Sample Output

 Pack your bags! You're traveling to Costa Rica in the year 2332. The cost of this trip will be $921.00

## How to Run

1. Clone this repository or download using the `.py` file 
2. Run the script in a Python environment 
```bash
python time_travelers_toolkit.py
```

## What's Next
In the future, I plan to:
* Add user input to let travelers choose their destination or era
* Store travel logs using file handling
* Integrate visuals or a GUI using Tkinter