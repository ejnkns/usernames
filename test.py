import requests

# for checking email addresses
import dns.resolver
import socket
import smtplib

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

def checkGoogle(username):
    # to do this we check if the gmail account exists using dns
    # every google account has a gmail

    records = dns.resolver.query('gmail.com', 'MX')
    mxRecord = str(records[0].exchange)

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(server.local_hostname)
    server.mail('findallusernames@gmail.com')
    code, message = server.rcpt(str(username + '@gmail.com'))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        return(True)
    else:
        return(False)
#these always time out ...
#print(checkGoogle('elliotjenkins3'))
#print(checkGoogle('apirgfjh'))

def checkInstagram(username):
    userPage = requests.head('http://instagram.com/' + username)
    if userPage.status_code == 200:
        return(True)
    else:
        return(False)

#print(checkInstagram('aldkfjthaf'))
#print(checkInstagram('johndoe'))


def 
