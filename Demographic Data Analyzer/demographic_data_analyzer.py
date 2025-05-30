import pandas as pd
from io import StringIO

def calculate_demographic_data():
    data_string = """
age,workclass,fnlwgt,education,education-num,marital-status,occupation,relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary
39,State-gov,77516,Bachelors,13,Never-married,Adm-clerical,Not-in-family,White,Male,2174,0,40,United-States,<=50K
50,Self-emp-not-inc,83311,Bachelors,13,Married-civ-spouse,Exec-managerial,Husband,White,Male,0,0,13,United-States,<=50K
38,Private,215646,HS-grad,9,Divorced,Handlers-cleaners,Not-in-family,White,Male,0,0,40,United-States,<=50K
53,Private,234721,11th,7,Married-civ-spouse,Handlers-cleaners,Husband,Black,Male,0,0,40,United-States,<=50K
28,Private,338409,Bachelors,13,Married-civ-spouse,Prof-specialty,Wife,Black,Female,0,0,40,Cuba,<=50K
37,Private,284582,Masters,14,Married-civ-spouse,Exec-managerial,Wife,White,Female,0,0,40,United-States,>50K
"""
    data = pd.read_csv(StringIO(data_string))

    race_counts = data['race'].value_counts()
    avg_age_men = round(data[data['sex'] == 'Male']['age'].mean(), 1)
    percent_bachelors = round((data['education'] == 'Bachelors').mean() * 100, 1)

    advanced = data['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_edu = data[advanced]
    lower_edu = data[~advanced]

    higher_edu_rich = round((higher_edu['salary'] == '>50K').mean() * 100, 1)
    lower_edu_rich = round((lower_edu['salary'] == '>50K').mean() * 100, 1)

    min_hours = data['hours-per-week'].min()
    min_workers = data[data['hours-per-week'] == min_hours]
    rich_min_workers = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    country_total = data['native-country'].value_counts()
    country_rich = data[data['salary'] == '>50K']['native-country'].value_counts()
    country_percent = (country_rich / country_total * 100).dropna()
    top_country = country_percent.idxmax()
    top_country_percent = round(country_percent.max(), 1)

    india_rich = data[(data['native-country'] == 'India') & (data['salary'] == '>50K')]
    top_occupation_india = india_rich['occupation'].value_counts().idxmax() if not india_rich.empty else None

    return {
        'race_count': race_counts,
        'average_age_men': avg_age_men,
        'percentage_bachelors': percent_bachelors,
        'higher_education_rich': higher_edu_rich,
        'lower_education_rich': lower_edu_rich,
        'min_work_hours': min_hours,
        'rich_percentage': rich_min_workers,
        'highest_earning_country': top_country,
        'highest_earning_country_percentage': top_country_percent,
        'top_IN_occupation': top_occupation_india
    }

if __name__ == "__main__":
    result = calculate_demographic_data()
    for key, value in result.items():
        print(f"{key}:\n{value}\n")
