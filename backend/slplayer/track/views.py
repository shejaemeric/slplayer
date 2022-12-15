from flask import jsonify
from . import track
import requests
from models import Track
import json

headers_option1 = {
	"X-RapidAPI-Key": "ef656a6955msh4387e4cdaf5996cp1dbe36jsn3c9918cf9fc9",
	"X-RapidAPI-Host": "spotify-data.p.rapidapi.com"
}


@track.route('/search/<string:keyword>',methods=['GET'])
def search(keyword):

    """search for track
        track-format: (id:int,name:str,artist:str,cover:str,album:str,duration:str)

    Args:
        keyword (string): keyword to search

    Returns:
        json: result of search
    """

    url = "https://spotify-data.p.rapidapi.com/search/"
    querystring = {"q":keyword,"type":"tracks","offset":"0","limit":"10","numberOfTopResults":"6"}
    response = requests.request("GET", url, headers=headers_option1, params=querystring)
    res  = (response.json())['tracks']['items']
    tracks = []
    for item in res:
        item = item['data']
        id = item['id']
        name = item['name']
        artists = item['artists']['items']
        artist = ' ft '.join(artist["profile"]["name"] for artist in artists)
        cover = item['albumOfTrack']['coverArt']['sources'][0]['url']
        album = item['albumOfTrack']['name']
        duration = item['duration']['totalMilliseconds']
        track = Track(id, name, artist, cover, album, duration)
        tracks.append(track.__dict__)
    return jsonify({"tracks":tracks})


@track.route('play/<string:track_id>',methods=['GET'])
def play_url(track_id):

    url = "https://spotify-data.p.rapidapi.com/tracks/"
    querystring = {"ids":track_id}
    response = requests.request("GET", url, headers=headers_option1, params=querystring)
    url = (response.json())['tracks'][0]['preview_url']
    return jsonify({"url":url})




@track.route('download/<string:track_id>',methods=['GET'])
def download_url(track_id):
    url = "https://spotify-downloader.p.rapidapi.com/SpotifyDownloader"
    spotify_link = "https://open.spotify.com/track/"+track_id+"?si=bf18bba46a474513"

    querystring = {"url":spotify_link}

    headers = {
        "X-RapidAPI-Key": "ef656a6955msh4387e4cdaf5996cp1dbe36jsn3c9918cf9fc9",
        "X-RapidAPI-Host": "spotify-downloader.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    url = (response.json())['audio']['url']
    size = (response.json())['audio']['size']
    return jsonify({
        "url":url,
        "size":size
    })

