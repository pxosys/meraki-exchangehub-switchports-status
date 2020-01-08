# Setup + Installation
    1. Download repository and move to desired directory
    2. Run `pip install -r requirements.txt` to install any potentially missing packages
    3. Go to the Meraki Dashboard and generate an API key for yourself
    4. Paste this value into the provided credentials.json file (if desired)
    5. Run script. For instructions on running the script, read below

# Instructions
The script obtains its credentials in two ways: 
- Imported from a JSON file using the --credentials argument
- Specifically designated using the --apiKey argument

To run the script, enter `python[3] main.py [arguments]` and the script will begin, requiring no further input


# Description
The script will output a dict that will list all the switches in your organisations, with each one having a "ports" entry which will have an "inUse" key against it, which will be true if a device is detected to be plugged in to it
