import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
    
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
        if city not in cities:
            print("\nInvalid Input\n")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? Please type one of the following options: All, January, February, March, April, May, June.\n').lower()
        if month not in months :
            print("\nInvalid Input\n")
            continue
        else:
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Please type one of the following options: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n').lower()
        if day not in days :
            print("\nInvalid Input\n")
            continue
        else:
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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        df = df[df['day'] == day]
              

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    month = df['Start Time'].dt.month
    day_of_week = df['Start Time'].dt.day
    hour = df['Start Time'].dt.hour


    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    most_common_month = calendar.month_name[most_common_month]
    print('The most common month is ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day'].mode()[0]
    most_common_day = calendar.day_name[most_common_day]
    print('The most common day of week is ',most_common_day)

    
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour is ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('The most common start station is : ', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('The most common end station is : ', most_common_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + df['End Station']
    most_frequent_combo = df['combination'].mode()[0]
    print('The most frequent combination of start station and end station trip is : ', most_frequent_combo)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def convert(seconds): 
    """ Convert seconds into hours, minutes and seconds """
    
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is: ', convert(total_travel_time))
    
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is: ', convert(mean_travel_time))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Counts of user types:\n', user_type)
   
    
    # Leave a space in between 
    print('\n')
    
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        
        gender = df['Gender'].value_counts()
        print('Counts of gender:\n', gender)
        
    else:
        
        print("Gender column does not exists")
    
    # Leave a space in between
    print('\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        
        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth is ', earliest_year)
        
        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth is ', most_recent_year)
    
        most_common_year = df['Birth Year'].mode()
        print('The most common year of birth is ', most_common_year)
        
    else:
        
        print("Birth Year column does not exists")
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """display five lines of raw data if the user indicates that they want to see raw data"""
    i = 0
    view_data = input('\nWould you like to view 5 rows of raw data? Enter yes or no\n').lower()
    while True:
        if view_data == 'yes':
            print(df.iloc[i:i+5])
            i += 5
            view_data = input('\nWould you like to view more raw data? Enter yes or no\n').lower()  
            continue
        else:
            break
         
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
