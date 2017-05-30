#!steam_env/Scripts/python
import requests


def get_game(game_id):
    resp = requests.get('http://store.steampowered.com/api/appdetails/?appids='+ str(game_id) +'&v=1')
    return resp


