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

## Future development
This is just a backend project at the moment so it would be nice to create a front-end to go with it, like the website that was our inspiration.<br>We also discussed the possibility of including user input for how much further in to the future they would like to see, i.e. rather than defaulting to one billion, they could choose the number themself.


## Licence
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
 