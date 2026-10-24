
import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # 1. Number of people of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(
        df.loc[df["sex"] == "Male", "age"].mean(), 1
    )

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round(
        (df["education"] == "Bachelors").mean() * 100, 1
    )

    # 4. Percentage of people with advanced education earning >50K
    higher_education = df["education"].isin(
        ["Bachelors", "Masters", "Doctorate"]
    )
    higher_education_rich = round(
        (df.loc[higher_education, "salary"] == ">50K").mean() * 100, 1
    )

    # 5. Percentage of people without advanced education earning >50K
    lower_education = ~higher_education
    lower_education_rich = round(
        (df.loc[lower_education, "salary"] == ">50K").mean() * 100, 1
    )

    # 6. Minimum number of hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 7. Percentage of people working minimum hours who earn >50K
    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round(
        (num_min_workers["salary"] == ">50K").mean() * 100, 1
    )

    # 8. Country with the highest percentage of people earning >50K
    country_rich = df[df["salary"] == ">50K"]["native-country"].value_counts()
    country_total = df["native-country"].value_counts()

    country_percentage = (
        country_rich / country_total * 100
    ).dropna()

    highest_earning_country = country_percentage.idxmax()
    highest_earning_country_percentage = round(
        country_percentage.max(), 1
    )

    # 9. Most popular occupation among people in India earning >50K
    top_IN_occupation = (
        df[
            (df["native-country"] == "India")
            & (df["salary"] == ">50K")
        ]["occupation"]
        .value_counts()
        .idxmax()
    )

    # Print results
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degrees:", percentage_bachelors)
        print("Percentage with higher education that earn >50K:",
              higher_education_rich)
        print("Percentage without higher education that earn >50K:",
              lower_education_rich)
        print("Minimum work hours:", min_work_hours)
        print("Percentage of rich among minimum-hours workers:",
              rich_percentage)
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print("Highest percentage of rich country:",
              highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
