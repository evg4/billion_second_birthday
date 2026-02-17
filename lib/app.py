from datetime import datetime, timedelta

def find_billion_birthday():
    print('Enter date of birth in this format: YYYY MM DD HH MM SS')
    birthday = input().split()
    birthday = datetime(*[int(num) for num in birthday])
    one_billion_birthday = birthday + timedelta(seconds=1000000000)
    if one_billion_birthday.day in range(11,14):
        suffix = 'th'
    else:
        match str(one_billion_birthday.day)[-1]:
            case '1':
                suffix = 'st'
            case '2':
                suffix = 'nd'
            case '3':
                suffix = 'rd'
            case _:
                suffix = 'th'
    return f"You will turn one billion seconds old on {one_billion_birthday.strftime(f'{one_billion_birthday.day}{suffix} %B %Y at %H:%M:%S!')}"

