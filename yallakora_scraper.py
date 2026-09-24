import requests
from bs4 import BeautifulSoup
import pandas as pd


def main():
  date = input("Please enter the date of matches you want to scrap in the format MM/DD/YYYY")

  url = f"https://www.yallakora.com/match-center?date={date}"

  page = requests.get(url)

  soup = BeautifulSoup(page.content, "lxml")

  championships = soup.find_all("div", {"class" : "matchCard"})

  all_matches_list = []

  for championship in championships:

    championship_name = championship.find("h2").text.strip()

    all_finished_match = championship.find_all("div", {"class" : "item finish liItem"})

    for match in all_finished_match:

      team_A = match.find("div", {"class" : "teams teamA"}).find("p").text.strip()
      team_B = match.find("div", {"class" : "teams teamB"}).find("p").text.strip()

      match_result = match.find("div", {"class" : "MResult"})

      # score_a = match_result.find("span", {"class" : "score"}).text.strip()
      # score_b = match_result.find_all("span", {"class" : "score"})[1].text.strip()

      scores = match_result.find_all("span", {"class" : "score"})

      score_a = scores[0].text.strip()

      score_b = scores[1].text.strip()

      match_time = match_result.find("span", {"class" : "time"}).text.strip()

      all_matches_list.append({"Championship Name" : championship_name
                               ,"Team A" : team_A
                               , "Team B" : team_B
                               , "Score" : f"{score_a} - {score_b}"
                               , "Time" : match_time})

    return all_matches_list

all_matches_df = pd.DataFrame(main())

print(all_matches_df)

all_matches_df.to_excel("matches1.xlsx",index=False)
