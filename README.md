# [Music Miner](https://musicminer.net)

The goal of Music Miner is to help people find new genres and underepresented artists. 

## Web Scraper and Crawler
It was written in python and is designed to collect links of other artists from an artists page while also collecting their data. It then collects genre data about the artists from the spotify API using [spotipy](https://spotipy.readthedocs.io/en/master/). It is done with the Datascraper.py file but incase it fails or gets stuck you can run Backup.py.

## Website
It has a simplistic UI and the artist data is displayed using javascript by making a call to my [API](http://yushyush17.pythonanywhere.com) for randomised artist data from the collected.
