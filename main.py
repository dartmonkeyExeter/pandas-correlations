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
    model_choice = ''
    while not model_choice:
        model_choice = input('would you like to use a specific model? Y for yes, N for no.\n').lower().strip()
        if model_choice == 'y':
            df['model'] = df['model'].str.strip()
            models = df['model'].to_list()
            while True:
                model_name = ''
                while not model_name:
                    model_name = input('what model would you like?\n')
                    if model_name in models:
                        print('model found!')
                    else:
                        print('model not found!')
                        model_name = ''
                year = ''
                while not year:
                    year = input('from what year?\n').strip()
                    try:
                        year = int(year)
                    except ValueError:
                        continue
                df = df[(df == f'{model_name}').any(axis=1) & (df == year).any(axis=1)]
                df = df.reset_index(drop=True)
                break
        elif model_choice == 'n':
            pass
        else:
            print('invalid input, please try again')
            model_choice = ''
    calculation(df, csv)


def calculation(df, csv):
    cols_to_read = []

    allowed = ['year', 'price', 'mileage', 'tax', 'mpg', 'engineSize']
    print(f'options: {allowed}. (options are case sensitive!)')

    for i in range(2):
        choice = ''
        while not choice:
            choice = input(f'column {i + 1}: ').strip()
            if choice in allowed:
                cols_to_read.append(choice)
            else:
                print('not a valid column, try again')
                choice = ''
    subset = df[cols_to_read]
    correlation = subset.corr()
    print(f'the correlation value between {cols_to_read[0]} '
          f'and {cols_to_read[1]} for {csv} is \n{correlation}')
    sns.heatmap(correlation, cmap='vlag', annot=True)
    plt.show()


def main():
    correlation_function()


if __name__ == '__main__':
    main()
