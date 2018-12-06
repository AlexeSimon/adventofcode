# adventofcode

This repo contains my personnal answers to all of the problems proposed by [AdventOfCode](https://adventofcode.com/).
Most of it is missing and will be pushed as I complete them. You can check the commits or the list below to know which has been completed. I also propose to viewers to use init.py to copy this repo hierarchy and get down to coding themselves.

## Copying the template

You can use init.py if you want to copy this repo template and answer the problems by yourself. 
Its functionnalities include making directories, downloading statements, downloading inputs, making code templates and making url links.

### Prerequisites

You need python 3 and its module "requests" installed.
To install the module requests, use 
```shell
pip install requests
```
### Running init.py
To run init.py, follow these steps:
** Create a new folder.
** Download init.py and put it into the folder.
** Open init.py in a text editor and put your session into **USER_SESSION_ID** (see below).
** Change other user parameters in the init.py as desired (see below).
** Change the date of the last advent of code year and day if needed.
** Run init.py from within the folder with
```shell
python init.py
```
### Users Parameters
The init.py parameters come as follow:
```python
# USER SPECIFIC PARAMETERS
base_pos = "./"            # Folders will be created here. If you want to make a parent folder, change this to ex "./adventofcode/"
USER_SESSION_ID = ""       # Get your session by inspecting the session cookie content in your web browser while connected to adventofcode and paste it here as plain text in between the ". Leave at is to not download inputs.
DOWNLOAD_STATEMENTS = True # Set to false to not download statements. Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_INPUTS = True     # Set to false to not download inputs. Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
MAKE_CODE_TEMPLATE = True  # Set to false to not make code templates. Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_URL = True            # Set to false to not create a direct url link in the folder.
author = ""                # Name automatically put in the code templates.
OVERWRITE = False          # If you really need to download the whole thing again, set this to true. As the creator said, AoC is fragile; please be gentle. Statements and Inputs do not change. This will not overwrite codes.

# DATE SPECIFIC PARAMETERS
date = "December 2018"              # Date automatically put in the code templates.
starting_advent_of_code_year = 2017 # You can go as early as 2015.
last_advent_of_code_year = 2018     # The setup will download all advent of code data up until that date included
last_advent_of_code_day = 6         # If the year isn't finished, the setup will download days up until that day included for the last year
```
The only important parameter is **USER_SESSION_ID**, which has to be set correctly for the script to download your personnal problems input.
To recover your session:
** Got to [AdventOfCode](https://adventofcode.com/).
** Log in by any means (GitHub, Google, ...).
** Check for a cookie named **session**. This step depends on the browser used. It can be done through network inspection or, in advanced browser like Chrome, by simply clicking on the **View site information** button directly left of the url (shown as a padlock), then clicking **Cookies**.
** Copy this cookie content and paste it in init.py in between the ". It might be automatically formated upon being copied and look different, do not worry.
Other parameters are self explanatory.

## Running this repo code
Simply download the wanted solution folders.
Script can be run from a parent directory:
```shell
python 2018/2/code.py
```
Or set current directory to wanted solution folder:
```shell
cd 2018/2
python code.py
```
Note that copying the whole repo doesn't make much sense at the moment, since it is mostly empty.

## Advent of code problems solved
* 2015
    * /
* 2016
    * /
* 2017
    * Incoming. All done locally. Making the code beautiful before pushing it.
* 2018
    * Day 1
    * Day 2

## Contributing
Any constructive pull request directly correcting errors or improving the code is welcomed.
