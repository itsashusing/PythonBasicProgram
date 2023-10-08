ch = input('Enter any of a week day: ')
print('*' * 50)
match (ch).lower():
    case 'monday' | 'tuesday' | 'wednesday'| 'thursday'|'friday':
        print('{} is a working day  '.format(ch))
    case 'saturday':
        print('{} is a weekend enjoy it. '.format(ch))
    case 'sunday' :
        print('{} is a holiday. booooyahhh'.format(ch))
    case _:
        print('This is not a week day . Check your input')
print('*' * 50)
