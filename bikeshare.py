import time

import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Enter the name of the city (chicago, new york city, washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please enter a valid city.')

    while True:
        month = input('Enter the name of the month to filter by (all, january, february, ..., june): ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid month. Please enter a valid month.')

    while True:
        day = input('Enter the name of the day of the week to filter by (all, monday, tuesday, ..., sunday): ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid day of the week. Please enter a valid day.')

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of the week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower()

    # Filter by month
    if month != 'all':
        month_number = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_number]

    # Filter by day of the week
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most common month: {common_month}')

    # Display the most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most common day of the week: {common_day}')

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f'Most common start hour: {common_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

########################################################## 
 #Define the remaining statistical functions (station_stats, trip_duration_stats, user_stats) here...
####################################################################

def times_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Display the most common month
    common_month = df['month'].mode()[0]
    print(f'Most common month: {common_month}')
    
    # Display the most common day of the week
    common_day = df['day_of_week'].mode()[0]
    print(f'Most common day of the week: {common_day}')
    
    # Display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print(f'Most common start hour: {common_start_hour}:00')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f'Most commonly used start station: {common_start_station}')
    
    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f'Most commonly used end station: {common_end_station}')
    
    # Display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'Most frequent combination of start and end station: {common_trip[0]} to {common_trip[1]}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total travel time: {total_travel_time} seconds')
    
    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Mean travel time: {mean_travel_time} seconds')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('Counts of user types:')
    for user_type, count in user_counts.items():
        print(f'{user_type}: {count}')
    
    # Check if 'Gender' column exists in the dataframe
    if 'Gender' in df:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of gender:')
        for gender, count in gender_counts.items():
            print(f'{gender}: {count}')
    else:
        print('\n\033[91mGender data not available for this city.\033[0m')  
    
    # Check if 'Birth Year' column exists in the dataframe
    if 'Birth Year' in df:
        # Display earliest, most recent, and most common year of birth
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
    
        print(f'\nEarliest year of birth: {earliest_birth_year}')
        print(f'Most recent year of birth: {most_recent_birth_year}')
        print(f'Most common year of birth: {common_birth_year}')
    else:
        print('\n\033[91mBirth Year data not available for this city.\033[0m')  
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

import matplotlib.pyplot as plt
import seaborn as sns


def plot_trip_duration_distribution(df):
    plt.figure(figsize=(8, 6))
    plt.hist(df['Trip Duration'], bins=20, edgecolor='k')
    plt.title('Trip Duration Distribution')
    plt.xlabel('Trip Duration (seconds)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
    
def plot_user_types(df):
    user_type_counts = df['User Type'].value_counts()
    plt.figure(figsize=(8, 6))
    plt.bar(user_type_counts.index, user_type_counts.values)
    plt.title('User Types Distribution')
    plt.xlabel('User Type')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

def plot_trip_counts_over_months(df):
    monthly_counts = df.groupby('month')['Trip Duration'].count()
    plt.figure(figsize=(10, 6))
    plt.plot(monthly_counts.index, monthly_counts.values, marker='o')
    plt.title('Trip Counts Over Months')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()

    
def plot_boxplot_trip_durations_by_user_type(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='User Type', y='Trip Duration', data=df)
    plt.title('Trip Durations by User Type')
    plt.xlabel('User Type')
    plt.ylabel('Trip Duration (seconds)')
    plt.show()



def plot_violin_trip_durations_by_user_type(df):
    plt.figure(figsize=(8, 6))
    sns.violinplot(x='User Type', y='Trip Duration', data=df, inner='quart', palette='Set3')
    plt.title('Trip Durations by User Type (Violin Plot)')
    plt.xlabel('User Type')
    plt.ylabel('Trip Duration (seconds)')
    plt.show()


def plot_gender_pie_chart(df):
    
    # Check if 'Gender' column exists in the dataframe
    if 'Gender' in df:
        # Calculate gender counts
        gender_counts = df['Gender'].value_counts()

        # Plot a pie chart for gender distribution
        labels = gender_counts.index
        sizes = gender_counts.values
        colors = ['lightblue', 'lightcoral', 'lightgreen']  # You can change the colors as needed
        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
        plt.title('Gender Distribution')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.show()
    else:
        print('\n\033[91mGender data not available for this city.\033[0m')  # Red color for warning message

        

def display_data(df):
    """
    Displays raw data in 5-row increments based on user input.

    Args:
        df - Pandas DataFrame containing the data
    """
    start_loc = 0
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    
    while view_data == 'yes':
        end_loc = start_loc + 5
        print(df.iloc[start_loc:end_loc])
        start_loc = end_loc
        view_data = input("Do you wish to continue? Enter yes or no: ").lower()
        if view_data != 'yes':
            break




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        times_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        plot_trip_duration_distribution(df)
        plot_user_types(df)
        plot_trip_counts_over_months(df)
        plot_boxplot_trip_durations_by_user_type(df)
        plot_violin_trip_durations_by_user_type(df)
        plot_gender_pie_chart(df)
        
        
        display_data(df)

        # Call the other statistical functions here...

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

    