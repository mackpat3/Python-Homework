country_capitals={"USA" : "Washington D.C.", "France" : "Paris", "Germany" : "Berlin", "Japan" : "Tokyo", "UK" : "London"}

country=input("Enter a country from the following options- USA, France, Germany, Japan or UK: ")
capital=country_capitals.get(country)

if capital:
    print(f"The capital city of {country} is {capital}.")
else:
    print("Country not on the list.")
