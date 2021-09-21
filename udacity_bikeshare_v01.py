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
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = input("would you like to see chicago, new york city or washington?: ").lower()

    while city not in CITY_DATA:
        print("Input is invalid, Cities can be only chicago, new york or washington")
        city = input("would you like to see chicago, new york city or washington?: ").lower()

        # TO DO: get user input for month (all, january, february, ... , june)
    months = ["January", "February", "March", "April", "May", "June"]
    month = input("Which month would you like to select?: ").title()

    while (month not in months) and (month != "All"):
        print("Input is invalid, Please select from jan till June!")
        month = input("Which month would you like to select?: ").title()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day = input("Please enter the day you want: ").title()

    while (day not in days) and (day != "All"):
        print("Input is invalid, Please select from saturday till friday!")
        day = input("Please enter the day you want: ").title()

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

    df["Start Time"] = pd.to_datetime(df["Start Time"])

    df["month"] = df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.day_name()

    if month != "All":
        df = df[df["month"] == month]

    if day != "All":
        df = df[df["day"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df["month"].mode()[0]
    print("The most common month: ", most_month)

    # TO DO: display the most common day of week
    most_day = df["day"].mode()[0]
    print("The most common day: ", most_day)

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    most_hour = df["hour"].mode()[0]
    print("The most common day: ", most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_st = df["Start Station"].mode()[0]
    print("The most commonly used start station: ", most_start_st)

    # TO DO: display most commonly used end station
    most_end_st = df["End Station"].mode()[0]
    print("The most commonly used end station: ", most_end_st)

    # TO DO: display most frequent combination of start station and end station trip
    freq_start_end = (df["Start Station"] + " " + df["End Station"]).mode()[0]
    print("The most frequent combination of start station and end station trip: ", freq_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df["Trip Duration"].sum()
    print("Total Travel : ", total_travel, "sec | ", total_travel/60, " min")

    # TO DO: display mean travel time
    avg_travel = df["Trip Duration"].mean()
    print("Total Travel : ", avg_travel, "sec | ", avg_travel/60, " min")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    if "Gender" not in df:
        print("Gender stats cannot be calculated because Gender does not appear in the dataframe")
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # TO DO: Display counts of user types
        user_types = df["User Type"].value_counts()
        print("User Types : ", user_types)

        # TO DO: Display counts of gender
        gender = df["Gender"].value_counts()
        print("Gender : ", gender)

        # TO DO: Display earliest, most recent, and most common year of birth
        eariest_birth = df.sort_values('Birth Year', ascending=True)["Birth Year"].head(1)
        most_recent = df.sort_values('Birth Year', ascending=False)["Birth Year"].head(1)
        most_common = df["Birth Year"].mode()[0]

        print("The Earliest year of birth : ", eariest_birth)
        print("The Most Recent year of birth : ", most_recent)
        print("The Most Common year of birth : ", most_common)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40)


def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while view_data == "yes":
        print(df.iloc[start_loc:start_loc+5])
        view_data = input("Do you wish to display 5 rows more? Enter yes or no?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
