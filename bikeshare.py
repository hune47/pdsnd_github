import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['new york city','chicago','washington'];
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june'];
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
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
    city = input('Please enter the desired city (new york city, chicago or washington): ').lower()
    while True:
        if city in cities :
            break;
        city = input('Please enter VALID city name (new york, chicago or washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input('Please enter the desired month or all (from january to june):').lower()
    while True:
        if month in months :
            break;
        month = input('Please enter VALID month name or all (from january to june):').lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input('Please enter the desired day or all :').lower()
    while True:
        if day in days :
            break;
        day = input('Please enter VALID day name or all :').lower()
       
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, hour and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] =df['Start Time'].dt.hour
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


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
  
    # find the most common month (from 0 to 11
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    

    # find the most common day
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day of The Week:', popular_day)

    # TO DO: display the most common start hour

    
    
    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    # print value counts for most common start station
    df['mcss'] =df['Start Station'].value_counts().idxmax()
    popular_start_station = df['mcss'].mode()[0]
    print('Most Frequent Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    
    # print value counts for most common end station
    df['mces'] =df['End Station'].value_counts().idxmax()
    popular_end_station = df['mces'].mode()[0]    
    print('Most Frequent End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    
    # print size for most common combination of end and start station
    popular_station_combination =df.groupby(['Start Station','End Station']).size().idxmax()
    print('Most Frequent Trip from Start to End:', popular_station_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    # print sum for total travel time
    total =df['Trip Duration'].sum()
    print('Total Travel Time:', total)

    # TO DO: display mean travel time
    
    # print mean for travel time
    avg =df['Trip Duration'].mean()
    print('Average Travel Time:', avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types.to_string())
    
    # TO DO: Display counts of gender
    if city != 'washington':  

        # print value counts for each gender
        gender = df['Gender'].value_counts()
        print(gender.to_string())
        # TO DO: Display earliest, most recent, and most common year of birth

        # print maximum for birth year
       
        most_recent_birthyear = df['Birth Year'].max()
        print('Recent Birth Year:',most_recent_birthyear) 

        # print value counts for most common birth year
        df['yofr1'] = df['Birth Year'].value_counts().idxmax()
        most_common_birth_year = df['yofr1'].mode()[0]
        print('Most Common Birth Year:',most_common_birth_year)

        # print minimum for birth year
        earlist_birthyear=df['Birth Year'].min()
        print('Earlist Birth Year:',earlist_birthyear) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    counter = 5
    while True:
        city, month, day = get_filters()

        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
                   
        answer = input("\nDo you want to see five raw data? Enter yes or no.\n")
        while answer=='yes':
            print(df.head(counter))
            counter+=5;
            answer= input('\nFive more? Enter yes or stop.\n')
            if answer=='stop':
                break
  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
