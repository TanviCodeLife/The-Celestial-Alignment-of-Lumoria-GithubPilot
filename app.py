# Make an array of planets with plant data shown below
# **Planetary Data:**

#| Planet Name | Distance (AU) | Size (km) |
#|-------------|---------------|----------|
#| Mercuria    | 0.4           | 4879     |
#| Earthia     | 1             | 12742    |
#| Marsia      | 1.5           | 6779     |
#| Venusia     | 0.7           | 12104    |
#The planets aren't sorted by their distance from the Lumorian Sun so you'll need to handle that.

#Light Dynamics:
#If a smaller planet is behind a larger planet (relative to the Lumorian Sun), it will be in the shadow and will receive no light (None).
#If a larger planet is behind a smaller planet (relative to the Lumorian Sun), it will have Partial light.
#If a planet is in the shadow of multiple planets, it will be marked as None (Multiple Shadows).
#If two planets are of similar size and are near each other in alignment, they might partially eclipse each other, but for simplicity, you can consider them both to receive full light.
#Output:
#Your system should output a list of planets and the light intensity they receive: Full, Partial, None, or None (Multiple Shadows).
#Constraints
#Use GitHub Copilot and write the simulation in any language you'd like.
#Focus on clear and concise code that handles planet checks efficiently. Ask GitHub Copilot/Chat, "How can I make this code more readable and maintainable?".
#Creating a visual SVG representation for the planets is optional but encouraged if you have time.
#Summary of High-Level Tasks to Perform
#Use a console application to render the output.
#Sort the list of planets based on their distance from the Lumorian Sun.
#Traverse the sorted list of planets.
#For each planet, check the planets that are closer to the Lumorian Sun to see if they cast a shadow on other planets.
#Output the light intensity each planet receives.
# Define the planetary data
planets = [
    {"name": "Mercuria", "distance": 0.4, "size": 4879},
    {"name": "Earthia", "distance": 1, "size": 12742},
    {"name": "Marsia", "distance": 1.5, "size": 6779},
    {"name": "Venusia", "distance": 0.7, "size": 12104}
]

# Sort the planets based on their distance from the Lumorian Sun
sorted_planets = sorted(planets, key=lambda p: p["distance"])

# Function to check if a planet is in shadow
def is_in_shadow(planet, other_planet):
    if planet["size"] < other_planet["size"] and planet["distance"] > other_planet["distance"]:
        return True
    return False

# Function to determine the light intensity received by a planet
def get_light_intensity(planet):
    for other_planet in sorted_planets:
        if other_planet == planet:
            continue
        if is_in_shadow(planet, other_planet):
            return "None"
    return "Full"

# Output the light intensity received by each planet
for planet in sorted_planets:
    light_intensity = get_light_intensity(planet)
    print(f"{planet['name']}: {light_intensity}")
