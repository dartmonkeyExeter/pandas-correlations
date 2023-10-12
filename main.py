import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', None)


def correlation_function():
    print('options: audi, bmw, cclass, focus, ford, hyundi, merc, skoda,'
          'toyota, unclean cclass, unclean focus, vauxhall, vw. '
          '(options are case sensitive!)')
    csv = ''
    df = ''
    while not csv:
        csv = input('what csv do you want to read?\n')
        try:
            df = pd.read_csv(f'data/{csv}.csv')
        except FileNotFoundError:
            print('no file with that name found, try again.')
            csv = ''
    cols_to_read = []

    allowed = ['year', 'price', 'mileage', 'tax', 'mpg', 'engineSize']
    print(f'options: {allowed}. (options are case sensitive!)')

    for i in range(2):
        choice = ''
        while not choice:
            choice = input(f'column {i+1}: ').strip()
            if choice in allowed:
                cols_to_read.append(choice)
            else:
                print('not a valid column, try again')
                choice = ''
    subset = df[cols_to_read]
    correlation = subset.corr()
    print(f'the correlation value between {cols_to_read[0]} '
          f'and {cols_to_read[1]} is \n{correlation}')
    sns.heatmap(correlation, cmap='coolwarm', annot=True)
    plt.show()


def main():
    correlation_function()


if __name__ == '__main__':
    main()
