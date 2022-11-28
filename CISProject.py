import pandas as pd

standings = pd.read_excel('sportsref_download.xlsx')
team = ''
open('Selected_Teams.txt', 'w').close()
print("Hi, enter a MLB team below to see their record during the 2022 season.")
print("When finished enter 'Done' to see the results.")
while team != 'Done':
    team = input('Team: ')
    for i in standings['Tm']:
        if i == team:
            with open("Selected_Teams.txt","a") as f:
                f.write(standings.iloc[i] + "\n")
        elif i == 'Done':
            break
          