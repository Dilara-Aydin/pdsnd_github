import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        city = input("Select a city name to filter by: Chicago, New York City or Washington").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid input. Try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "Select a month to filter by: January, February, March, April, May, June or choose option 'all' if you have no preference").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Invalid input. Try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(
            "Select a day to filter by: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or choose option 'all' if you have no preference").lower()

        if day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
            print("Invalid input. Try again.")
            continue
        else:
            break

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print("The most common month:", df['month'].mode()[0], "\n")

    # TO DO: display the most common day of week

    print("The most common day of the week:", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print("The most commonly used start station:", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station

    print("The most commonly used end station:", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip

    df['combination'] = df['Start Station'] + " and " + df['End Station']
    print("The most frequent combination of start station and end station trip:", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    print("The total travel time:", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time

    print("The mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    count_of_user_types = df['User Type'].value_counts()
    print("Counts of user types:", count_of_user_types, "\n")

    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        counts_of_gender = df['Gender'].value_counts()
        print("Counts of gender:", counts_of_gender, "\n")
    else:
        print("There is no information regarding the counts of gender")

    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode())
        print("Earliest year of birth:", earliest_birth_year)
        print("Most recent year of birth:", most_recent_birth_year)
        print("Most common year of birth:", most_common_birth_year)
    else:
        print('There is no information regarding user birth year')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    continue_asking = True
    while (continue_asking):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == "no":
            continue_asking = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()