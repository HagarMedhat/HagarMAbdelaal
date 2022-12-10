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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input('Which city you are interested in? Chicago, New york city or Washington.')).lower().strip()
    allowed_cities = ['chicago', 'new york city', 'washington']
    while city not in allowed_cities:
        if city not in allowed_cities:
            print("Oh oh! did you make a typo? Please try again.")
            city = str(input('Which city you are interested in? Chicago, New york city or Washington.')).strip().lower()

    print(f"You chose {city.capitalize()}, let's go.")

    # get user input for month (all, january, february, ... , june)
    month = str(input('What about months?, specify the month or just type all for all months brief.')).lower().strip()
    allowed_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in allowed_months:
        if month not in allowed_months:
            print("Oh oh! did you make a typo? Please try again.")
            month = str(input('What about months?, specify the month or type all for allover brief.')).lower().strip()

    print(f"You chose {month.capitalize()}, let's go.")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = str(input('You know the deal,which day of week? or type all to have a brief for all days.')).lower().strip()
    allowed_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in allowed_days:
        if day not in allowed_days:
            print("Oh oh! did you make a typo? Please try again.")
            day = str(input('Which day of the week? or type all to have a brief for all.')).lower().strip()
    print(f"You chose {day.capitalize()}, let's go.")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    # Loads data for the specified city and filters by month and day if applicable.
    #
    # Args:
    #     (str) city - name of the city to analyze
    #     (str) month - name of the month to filter by, or "all" to apply no month filter
    #     (str) day - name of the day of week to filter by, or "all" to apply no day filter
    # Returns:
    #     df - Pandas DataFrame containing city data filtered by month and day
    # """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def raw_data(df):
    # Shows 5 rows of raw data upon request.
    # If it is still needed 5 more rows will be shown until input starts with n
    n = 0
    print(df[n:n + 5])
    while True:
        yes_no = str(input('Would you like to see some raw data? Enter yes or no.')).lower().strip()
        if yes_no[0] != "y":
            break
        n += 5
        print(df[n:n + 5])


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print(f"Most Popular month: {popular_month}")

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print(f"Most Popular day: {popular_day}")

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f"Most Popular Start Hour: {popular_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    popular_start_station = df['Start Station'].mode()[0]
    print(f"Most Popular start station: {popular_start_station}")

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f"Most Popular end station: {popular_end_station}")

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print(f"The most frequent combination of start and end stations trip is : {frequent_combination}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df["Trip Duration"].sum()
    print(f"Total travel time: {total_time}")

    # display mean travel time
    mean_time = df["Trip Duration"].mode()[0]
    print(f"Mean travel time: {mean_time}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):

    if city == "washington":
        """If city is washington print sorry."""
        print("Sorry that's the end we don't have more information.")

    else:
        """Displays statistics on bikeshare users."""
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_types = df["User Type"].value_counts().to_frame()
        print(f"Counts of user types: {user_types}")

        # Display counts of gender
        gender = df["Gender"].value_counts().to_frame()
        print(f"Counts of gender: {gender}")

        # Display earliest, most recent, and most common year of birth
        earliest = df["Birth Year"].min()
        print(f"Earliest year of birth: {earliest}")

        most_recent = df["Birth Year"].max()
        print(f"Most recent year of birth: {most_recent}")

        common_year_birth = df["Birth Year"].mode()[0]
        print(f"Most common year of birth: {common_year_birth}")

        print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while True:
            yes_no = str(input('Would you like to see some raw data? Enter yes or no.')).lower().strip()
            if yes_no[0] != "y":
                break
            raw_data(df)
            break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
