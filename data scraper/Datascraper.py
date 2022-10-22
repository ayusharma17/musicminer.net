import urllib
import urllib.request
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# ------------------------------------------------------------------------------------------------------------------------#

# Base Artist links Collecting
playlists = [
    "https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd",
    "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U",
    "https://open.spotify.com/playlist/37i9dQZF1DX9GRpeH4CL0S",
    "https://open.spotify.com/playlist/0kz78XchNmM9aKwDHQhi0t",
    "https://open.spotify.com/playlist/37i9dQZF1DX7HOk71GPfSw",
    "https://open.spotify.com/playlist/3EyB7nH0Gt1CSLtgeT1cNw",
    "https://open.spotify.com/playlist/1Vtq5pePI2g6p0MpAB2gDt",
    "https://open.spotify.com/playlist/6TxuoHMx9qLTePZGS1CasY",
    "https://open.spotify.com/playlist/37i9dQZEVXbJiZcmkrIHGU",
    "https://open.spotify.com/playlist/44zrIqtaK4EIwyrE62yQ6o",
    "https://open.spotify.com/playlist/5zZDVkuWyO3hdjckJHHv40",
    "https://open.spotify.com/playlist/37i9dQZF1DX0XUfTFmNBRM",
    "https://open.spotify.com/playlist/08VCxXZsk7jkzqfHupsL61",
    "https://open.spotify.com/playlist/5TDtuKDbOhrfW7C58XnriZ",
    "https://open.spotify.com/playlist/1h0CEZCm6IbFTbxThn6Xcs",
    "https://open.spotify.com/playlist/7m1C1eHUC2kJQL69dGMjaz",
    "https://open.spotify.com/playlist/1LD6W0yUGghEu193n2OOJy",
    "https://open.spotify.com/playlist/0rh4JRWo3tSRBYNM3i4XXa",
    "https://open.spotify.com/playlist/2YE8ziv26B6ZIon7iSTrcQ",
    "https://open.spotify.com/playlist/0xev9Iu5toHJc1L1PthrpW",
    "https://open.spotify.com/playlist/3AfMvO7Ha5m06dJl51eeEy",
    "https://open.spotify.com/playlist/65M0woJ8PIdm5KmAesnZhr",
    "https://open.spotify.com/playlist/2otQLmbi8QWHjDfq3eL0DC",
    "https://open.spotify.com/playlist/37i9dQZF1EQqkOPvHGajmW",
    "https://open.spotify.com/playlist/37i9dQZF1DXd8cOUiye1o2",
    "https://open.spotify.com/playlist/37i9dQZF1DX5cZuAHLNjGz",
    "https://open.spotify.com/playlist/37i9dQZF1DWVo4cdnikh7Z",
    "https://open.spotify.com/playlist/37i9dQZF1DWU8quswnFt3c",
    "https://open.spotify.com/playlist/37i9dQZF1DWY0DyDKedRYY",
    "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO",
    "https://open.spotify.com/playlist/37i9dQZF1DX10zKzsJ2jva",
    "https://open.spotify.com/playlist/69fEt9DN5r4JQATi52sRtq",
    'https://open.spotify.com/playlist/4ibx3N0OdTyTFZTRX1zEQQ',
    "https://open.spotify.com/playlist/7eybPwcFDYDzw1KYGqHiQo",
    "https://open.spotify.com/playlist/5d6HDkkTouObGKeQOg39gk",
    "https://open.spotify.com/playlist/2HUpNZLoYHe0Sa9dglqQOg",
    "https://open.spotify.com/playlist/4jr1tvvMa8bYtXGQZPFn3T",
    "https://open.spotify.com/playlist/7kDOjv4aQuo4lFBDq9F6Rw"
]


artist_links = []
for url in playlists:
    try:
        html = urllib.request.urlopen(url).read()
    except:
        continue
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")

    for tag in tags:
        x = tag.get("href", None)
        if "artist" in x:
            y = "https://open.spotify.com" + x
            if y not in artist_links:
                print(y)
                artist_links.append(y)
print(len(artist_links))
print("Done collecting initial artists")
print("Starting Web Crawling")

# ------------------------------------------------------------------------------------------------------------------------#

# Web Crawling and Filtering out the Artist fitting criteria
count = len(artist_links)
final_artists = []
for url in artist_links:
    print('processing', artist_links.index(url), url)
    for step in range(6):
        if count % (10000+step) == 0:
            backup = open(r"artists.txt", "w", encoding="utf-8")
            final_backup = open(r"final_backup.txt", "w", encoding="utf-8")
            print("backing up")
            for url in artist_links:
                backup.write(url + '\n')
            for final_url in final_artists:
                final_backup.write(final_url + '\n')
            count += 6 - step 
            backup.close()
            final_backup.close()

    try:
        html = urllib.request.urlopen(url).read()
    except:
        print("opening this link failed")
        continue
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("a")

    # find Listeners and Name
    listeners = soup.find(
        class_="Type__TypeElement-goli3j-0 cPwEdQ fjP8GyQyM5IWQvTxWk6W"
    )
    
    try:

        m = listeners.get_text().split()[0]
        mlisteners = ""
        if "," in m:
            l = m.split(",")
            for i in l:
                mlisteners += i
        else:
            mlisteners = m

        

        if int(mlisteners) < 100000 and int(mlisteners) > 1000:
            name = soup.find(
                class_="Type__TypeElement-goli3j-0 qgdOC gj6rSoF7K4FohS2DJDEm"
            )
            print(len(final_artists), url + "[" + mlisteners + "[" + name.get_text())
            final_artists.append(mlisteners + "[" + name.get_text() + "[" + url)

    except:
        print("getting monthly listeners failed for this link")
        pass

    # find new links
    if count < 1000000:
        for tag in tags:
            x = tag.get("href", None)
            if "artist" in x:
                y = "https://open.spotify.com" + x
                if y not in artist_links:
                    artist_links.append(y)
                    count += 1
                    print(len(artist_links), y)

print("Done Web Crawling and Filtering out the Artist fitting criteria")
print("Starting Data Collection")
#print(final_artists)
# ------------------------------------------------------------------------------------------------------------------------#
#backing up final artists before API calls
backup = open(r"artists.txt", "w", encoding="utf-8")
final_backup = open(r"final_backup.txt", "w", encoding="utf-8")

print("backing up final artists before API calls")
for i in artist_links:
    backup.write(i + '\n')
for i in final_artists:
    final_backup.write(i + '\n')
backup.close()
final_backup.close()
# ------------------------------------------------------------------------------------------------------------------------#

# Collecting genre data from the API
client_credentials_manager = SpotifyClientCredentials(client_id='', client_secret='')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
artist_lst = []
artist_lst_id = []

final_backup = open('final_backup.txt', encoding='utf-8')
for i in final_backup.readlines():
    artist_lst_id.append('spotify:artist:' + i.split("[")[2][32::].strip())
    artist_lst.append(i)
final_backup.close()
save_data = open('data.txt', 'a', encoding='utf-8')
count = 0
for num in range(5000):
    # print(artist_lst_id[50*num: 50*num + 50])
    try:
        artist = sp.artists(artist_lst_id[50*num: 50*num + 50])
    except:
        continue
    for i in artist['artists']:
        try:
            data = artist_lst[count].strip() + '['
        except:
            break
        for j in i['genres']:
            if j != i['genres'][-1]:
                data += j + ", "
            else:
                data += j
        if len(i['genres']) > 0:
            save_data.write(data + '\n' )
            print(data)
        count+=1

print("Done Collecting Data")
print("Data ready to display on website")

# ------------------------------------------------------------------------------------------------------------------------#
