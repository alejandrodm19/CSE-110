def wind_chill(temp, wind_speed):
    """
    Calculate the wind chill based on the given temperature and wind speed.
    The formula used here is the one recommended by the National Weather Service.
    """
    if temp > 50 or wind_speed < 3:
        # The formula is only valid for temperatures below 50°F and wind speeds above 3 mph
        return 0
    else:
        wind_chill = 35.74 + (0.6215 * temp) - (35.75 * wind_speed ** 0.16) + (0.4275 * temp * wind_speed ** 0.16)
        return wind_chill

def celsius_to_fahrenheit(temp_celsius):
    """
    Convert the temperature from Celsius to Fahrenheit.
    """
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit

# Ask the user for the temperature and the unit of measure
temp_str = input("Enter the temperature: ")
unit_str = input("Enter the unit of measure (Celsius or Fahrenheit): ")

# Convert the temperature to Celsius or Fahrenheit as needed
if unit_str.lower() == "celsius":
    temp_celsius = float(temp_str)
    temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
else:
    temp_fahrenheit = float(temp_str)

# Loop through wind speeds from 5 to 60 mph and calculate the wind chill for each
for wind_speed in range(5, 61, 5):
    # Convert wind speed to meters per second, as required by the wind chill formula
    wind_speed_ms = wind_speed * 0.44704

    # Calculate wind chill using the current temperature and wind speed
    wind_chill_val = wind_chill(temp_fahrenheit, wind_speed_ms)

    # Display the result to two decimal places
    print(f"At a temperature of {temp_fahrenheit:.2f}°F and a wind speed of {wind_speed} mph, the wind chill is {wind_chill_val:.2f}°F.")
