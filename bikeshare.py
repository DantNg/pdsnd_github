import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'D:\\Udacity\\all-project-files\\chicago.csv',
              'new york city': 'D:\\Udacity\\all-project-files\\new_york_city.csv',
              'washington': 'D:\\Udacity\\all-project-files\\washington.csv' }
MONTH = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
DAYS_IN_WEEK = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
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
    while True:
        print('Please select a city name (chicago, new york city, washington): ')
        city = input().lower()
        citis_list = list(CITY_DATA.keys())
        if city not in citis_list:
            continue
        else:
            print('Selected {city} successfully'.format(city=city))
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        print('Please select a month (all, january, february, ... , june): ')
        month = input().lower()
        
        if month not in MONTH:
            continue
        else:
            print('Selected {month} successfully'.format(month=month))
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Please select a day in week (all, monday, tuesday, ... sunday): ')
        day = input().lower()
        days_list = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in days_list:
            continue
        else:
            print('Selected {day} successfully'.format(day=day))
            break

    print('-'*40)
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

    df['Start Time'] = pd.to_datetime(df['Start Time'],format="%Y-%m-%d %H:%M:%S")
    df['Month'] = df['Start Time'].dt.month
    df['Day In Week'] = df['Start Time'].dt.weekday
    df['Hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month = MONTH.index(month)
        print(month)
        df = df[df['Month'] == month]
    if day != 'all':
        day = DAYS_IN_WEEK.index(day) - 1 
        print(day)
        df = df[df['Day In Week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    print(df)
    # display the most common month
    popular_month = df['Month'].mode()[0]   
    print('Most Popular Month :', popular_month)

    # display the most common day of week
    popular_day = df['Day In Week'].mode()[0]   
    print('Most Popular Day :', DAYS_IN_WEEK[popular_day+1])

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]   
    print('Most Popular Hour :', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]   
    print('Most Popular Start Station :', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]   
    print('Most Popular End Station :', popular_end_station)

    # display most frequent combination of start station and end station trip
    df['Trips'] = df['Start Station'] + ' - ' + df['End Station']
    popular_trip = df['Trips'].mode()[0]
    print('Most Popular Trip :',popular_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df['Trip Duration'].sum()
    print('Total trip duration', total_trip_duration)
    # display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('Average trip duration', average_trip_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print('Counts of user types: ')
    print(user_type_counts)

    
    # Display counts of gender
    if hasattr(df, 'Gender'):
        gender_counts = df['Gender'].value_counts()
        print('Counts of each gender: ')
        print(gender_counts)

    # Display earliest, most recent, and most common year of birth
    if hasattr(df,'Birth Year'):
        df['Birth Year'] = pd.to_numeric(df['Birth Year'], errors='coerce')
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print("Earliest birth year: ",earliest_birth_year)
        print("Most recent birth year: ",most_recent_birth_year)
        print("Most common birth year: ", most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
