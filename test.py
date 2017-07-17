import requests

def checkReddit(username):
    # Reddit has an api request limit so might need to change this to just
    # parse the regular html page at www.reddit.com/user/[username]
    isTaken = requests.get("http://www.reddit.com/api/username_available.json?user=" + username)

    return(isTaken.json())
#print(checkReddit('ejnkns'))


def checkHackerNews(username):
    site = requests.get("http://news.ycombinator.com/user?id=" + username)

    if site.text == "No such user.":
        return(False)
    return(True)
#print(checkHackerNews('ejnkns'))

def checkTwitter(username):
    site = requests.get("https://twitter.com/users/username_available?username=" + username)

    return(site.json()['valid'])
#print(checkTwitter('ejnkns'))


