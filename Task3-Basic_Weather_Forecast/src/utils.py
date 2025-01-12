def convert_temperature(temp, to_unit="Celsius"):
    if to_unit == "Fahrenheit":
        return (temp * 9/5) + 32
    return temp  # Celsius by default
