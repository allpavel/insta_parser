from bs4 import BeautifulSoup
import sys

with open("..\\following.html", 'r') as following_file:
    soup = BeautifulSoup(following_file, 'html.parser')
    list_of_following = soup.find_all('a')

    sys.stdout = open("../following.xlsx", "w")

    for following in list_of_following:
        print(following.get_text())

    sys.stdout.close()

with open("..\\followers.html", 'r') as followers_file:
    soup = BeautifulSoup(followers_file, 'html.parser')
    list_of_followers = soup.find_all('a')

    sys.stdout = open("../followers.xlsx", "w")

    for follower in list_of_followers:
        print(follower.get_text())

    sys.stdout.close()
