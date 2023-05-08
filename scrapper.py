# Import selenium webdriver
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Create a driver object
driver = webdriver.Chrome()

# Go to the website
driver.get("https://www.livesport.com/en/cricket/india/ipl/results/")

# Wait for the page to load
driver.implicitly_wait(4)

# Find the table element that contains the results
table = driver.find_elements(
    by=By.CLASS_NAME, value="event__match")


# Loop through each row and get the text of each cell
for table in table:
    homeTeams = table.find_elements(
        by=By.CLASS_NAME, value="event__participant--home")
    awayTeams = table.find_elements(
        by=By.CLASS_NAME, value="event__participant--away")
    Outcomes = table.find_elements(
        by=By.CLASS_NAME, value="extraInfo")

    home_team = homeTeams[0].text
    away_team = awayTeams[0].text
    outcome = Outcomes[0].text

    if "won" in outcome:
        # Split the string into an array of words
        result_array = outcome.split()

        # Find the index of the word "won"
        won_index = result_array.index("won")

        # Get the substring before the word "won" to get the name of the winner
        result = " ".join(result_array[:won_index])
    else:
        result = ("No winner in this match")

    print("IPL match: " + home_team + " vs " +
          away_team + "- " + "Winner " + result)


# Close the driver
driver.close()
