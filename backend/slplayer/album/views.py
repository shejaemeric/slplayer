from flask import jsonify
import requests
from . import album
from models import Albums,Track
from .. import db

@album.route('top',methods=['GET'])
def getTopAlbum():

    """retrieves top album at the moment"""
    albums = Albums.query.all()
    print(albums)
    return jsonify({"albums":albums}),200

@album.route('<album_id>/tracks',methods=['GET'])
def getAlbumTracks(album_id):

    """retrieves album tracks based on id

    Args:
        album_id (string): album id
    """
    import requests

    url = "https://spotify-data.p.rapidapi.com/album_tracks/"

    querystring = {"id":album_id,"offset":"0","limit":"10"}

    headers = {
        "X-RapidAPI-Key": "e4a1eb10e9msh95c4d1adb18cd60p1be7c2jsnfe7e3cf2dc60",
        "X-RapidAPI-Host": "spotify-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    response = (response.json())['data']['album']['tracks']['items']
    tracks = []

    album = Albums.query.filter_by(album_id=album_id).first()

    cover = album.cover
    album_name = album.name

    for item in response:

        item = item['track']
        id = (item['uri']).split(':')[2]
        print(id)
        name = item['name']
        artists = item['artists']['items']
        artist = ' ft '.join(artist["profile"]["name"] for artist in artists)
        duration = item['duration']['totalMilliseconds']
        track = Track(id, name, artist, cover, album_name, duration)
        tracks.append(track.__dict__)

    return jsonify({"tracks":tracks}),200


