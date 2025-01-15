# pygame-murdle-grid
Pygame Murdle Grid - (simple Pygame grid to track playing a basic Murdle puzzle game).

# Getting Started
For example on a current Mac installation in a terminal after cloning this repo.
- change into the cloned repo<br>
  `cd pygame-murdle-grid`
- create python virtual environment<br>
  `python3 -m venv venv`
- activate the new environment<br>
  `source venv/bin/activate`
- install the Pygame module using the [requirements.txt](requirements.txt) file and pip3<br>
  `pip3 install -r requirements.txt`
- start the program<br>
  `python3 ./pygame-murdle-grid-simple.py`

# Using
Reading the Murdle Puzzle page use the Pygame grid to record your guesses rather than using a paper, pen or pencil.<br>
On each square type either 'Y' or 'N' to change the colour to 'Green' or 'Red' accordingly to get to your culprit.<br>
The axis are labbelled S1-S3, L1-L3 and W1-W3 for Suspects, Locations and Weapons.<br>
Press the 'RESET' button to clear the grid.<br>

# Inspiration
This is a quick and simple program to start learning the Pygame module as I didn't want to use a pencil in my new [Murdle](https://www.waterstones.com/book/murdle/g-t-karber/9781800818026) game book or waste paper elsewhere.  There are other online versions of the game and more detailed puzzles not covered by the simple grid used here.  But something I might do once I get to those !

# License
GNU General Public License v3.0 or later

See [COPYING](COPYING) to see the full text.
