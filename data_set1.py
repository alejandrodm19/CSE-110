# Author: Alejandro Malvacias
# File: Data_set1.py

lowest_expectancy = 10000000000000
highest_expectancy = -1
max_country = ''
max_year = ''
total_expectancy = 0
num_countries = 0
max_percentage = -1
min_percentage = 101
min_country = ''
max_percentage_country = ''
# Variables with an empty string
choose_year = input("Enter the year of interest: ")
# Main section
with open("life-expectancy.csv") as life_file:
    for i, line in enumerate(life_file): #For loop iteration
        if i == 0:
            continue
        else:
            line = line.strip()
            parts = line.split(",")
            country_name = parts[0]
            letter_country = parts[1]
            year = parts[2]
            life_expectancy = float(parts[3])
            percentage = float(parts[3])
            if choose_year.lower() == year.lower():
                if life_expectancy > highest_expectancy:
                    highest_expectancy = life_expectancy
                    max_country = country_name
                    max_year = year
                if life_expectancy < lowest_expectancy:
                    lowest_expectancy = life_expectancy
                    min_country = country_name
                if life_expectancy > max_percentage:
                    max_percentage = percentage
                    max_percentage_country = country_name
                    expectancy_with_max_percentage = life_expectancy
                if life_expectancy < min_percentage:
                    min_percentage = percentage
                    min_country = country_name
                    expectancy_with_min_percentage = life_expectancy
                total_expectancy += life_expectancy
                num_countries += 1

avg_expectancy = total_expectancy / num_countries
print(f"For the year: {max_year}")
print(f"The overall max life expectancy is: {highest_expectancy} from: {country_name} in {year}")
print(f"The overall min life expectancy is: {lowest_expectancy} from: {country_name} in {year}")   
print()
print(f"The max life expectancy was in {max_country} with {highest_expectancy:.2f}")
print(f"The min life expectancy was in {min_country} with {lowest_expectancy:.2f}")
print()
print(f"The average life expectancy for all countries in {choose_year} was {avg_expectancy:.2f}")
# End of the loop