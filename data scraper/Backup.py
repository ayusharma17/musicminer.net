import urllib
import urllib.request
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# How To Backup
# 1. Copy  last link in final_backup.txt 
# 2. Look for it in artists.txt. the line number will be the fail number
# 3. Set the fail number as starting point
# 4. Filtered artists are saved in final_backup.txt and all collected artists are backed up in artists.txt
# ------------------------------------------------------------------------------------------------------------------------#
artist_links = []#make theses list comprehensions
final_artists = []


with open('artists.txt') as txt_file:
    for i in txt_file:
        artist_links.append(i.strip())
        pass
print('d')

final_back =open('final_backup.txt', encoding='utf-8')
for i in final_back.readlines():
    final_artists.append(i.rstrip())
final_back.close()
print(len(artist_links))
# ------------------------------------------------------------------------------------------------------------------------#

# Web Crawling and Filtering out the Artist fitting criteria
count = len(artist_links) + 200000
start_point = 680000 #link no where code failed 
for url in artist_links[start_point::]:
    print('processing', artist_links.index(url), url)
    for step in range(5):
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
    

    # find Listeners and Name
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
        listeners = soup.find(
        class_="Type__TypeElement-goli3j-0 cPwEdQ fjP8GyQyM5IWQvTxWk6W")
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
