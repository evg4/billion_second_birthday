# Billion second birthday

## Description 
Inspired by [billion birthday](https://billionbirthday.com/), [@markrshaw99 ](https://github.com/markrshaw99) and I wanted to see if we could create a version in Python. The user inputs their birthday and the programme calculates the date and time that they turn one billion seconds old.

## How to use

``` bash
# Clone the repo
; git clone https://github.com/evg4/billion_second_birthday.git

# Set up a venv and install the requirements
; cd billion_second_birthday
; python -m venv venv
; source venv/bin/activate
(venv); pip install -r requirements.txt

# Uncomment line 22 in lib/app.py:
# print(find_billion_birthday())

# Run the app
; python lib/app.py

```
You will be prompted to enter your birthday. You must enter at least a year, month and date, but the hours, seconds and minutes are optional, and will default to 0 if not entered.