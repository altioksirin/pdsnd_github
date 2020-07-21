import time
import pandas as pd
import numpy as np

city_data = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

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
   
    city = str(input("Please input city name as: Chicago, New York, or Washington...\n"))    
    while city.lower() not in city_data.keys():
        try:
            city = str(input("That is not a valid city. Please input city name as: Chicago, New York, or Washington...\n")) 
        except Exception as e:
            print("Exception occurred: {}".format(e))
        
      
            
    # TO DO: get user input for month (all, january, february, ... , june) 
        
    month = input("\nWhich month would you like to analyze? \
                       \n Enter a month as: January, February, March, April, May, June \n OR enter all for no month filter: ").lower()
    
    while month not in months:
           month = input("Month is invalid. \n Enter a month as: January, February, March, April, May, June \n OR enter all for no month filter: ").lower()
            
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nWhich day would you like to analyze? \
                       \n Enter a day as : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n OR enter all for no day filter: ").lower()
    
    while day not in days:
           day = input("Day is invalid. \n Enter a day as : Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday \n OR enter all for no day filter: ").lower()

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
    print("Loading data.  Please wait.")
    
    df = pd.read_csv(city_data[city])
       
    """ parse datetime """
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    """ Extract month and hour from the Start Time column to create month, day, hour columns """
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour 

    """ Filter by month if "all" is not selected"""
    if month != 'all':
        df = df[df['month'] == months.index(month) + 1]

    """ Filter by day if "all" is not selected"""
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df
   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)
    
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', most_common_day)
    
    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)
    
    # TO DO: display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start End'] = " from " + df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    most_frequent_combination = df['Start End'].value_counts().idxmax()
    print('Most popular trip is:' ,most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def time_calculation(total_travel_time,calculation_type):
    time = total_travel_time
    day = total_travel_time // (24 * 3600)
    time = time % (24 * 3600)
    hour = time // 3600
    time %= 3600
    minutes = time // 60
    time %= 60
    seconds = time
    
    print('{} Travel Time is {} days {} hours {} minutes {} seconds'.format(calculation_type, day, hour, minutes, seconds))
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    time_calculation(total_travel_time,str('Total'))
   
    
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    time_calculation(mean_travel_time,str('Mean'))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print('Count of User Types:\n',user_types)
    
    if city=='new york' or city=='chicago':
    # TO DO: Display counts of gender
        gender_counts = df.groupby(['Gender'])['Gender'].count()
        print('Count of Gender Types:\n',gender_counts)
        
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_birth = int(df['Birth Year'].min())
        print('Earliest Year of Birth: ',earliest_year_birth)
        most_recent_year_birth =int(df['Birth Year'].max())
        print('Most Recent Year of Birth: ',most_recent_year_birth)
        most_common_year_birth = int(df['Birth Year'].mode()[0])
        print('Most common Year of Birth: ',most_common_year_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
     Ask if the user wants to see 5 lines of raw data, 
     display that data if the answer is 'yes', and continue these prompts and displays until the user says 'no'.
    """
    #index initialization
    sample_count = 5
    sample_start = 0
    sample_end = sample_count - 1    

    print('\nWould you like to see some sample from the raw data?')
    while True:
        try:
            answer = input(" Please input (y or n):  ")
        except Exception as e:
            print("Exception occurred: {}".format(e))
        if answer.lower() == 'y':
            # print which rows are displayed to the user
            print('\nDisplaying rows from {} to {}:'.format(sample_start + 1, sample_end + 1))
            print('\n', df.iloc[sample_start : sample_end + 1])
            sample_start += sample_count
            sample_end += sample_count

            print('\nWould you like to see {} more rows?'.format(sample_count))
        elif answer.lower() == 'n':
            break
        else:
            print("It's not a valid answer!!!")
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        #print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
