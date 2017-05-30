"""
    Collection of functions that get information from steam
"""

import requests
from utils import ifnokey
import pandas as pd
from model import db, App, Price


def get_game(game_id):
    """
        request steam by game id

        Args:
        --------
            game_id: the game id

        Returns:
        --------
            response object from request
    """
    resp = requests.get('http://store.steampowered.com/api/appdetails/?appids='+\
                        str(game_id) + '&v=1')

    return resp.json()


def db_parse_price(game_info):
    if game_info['is_free']:
        return None
    else:
        price_info = game_info['price_overview']
        return Price(
            price=price_info['final']/100,
            price_original=price_info['initial']/100,
            discount=price_info['discount_percent']/100,
            currency=price_info['currency']
        )


def save_db(game_id):
    data = get_game(game_id)
    if data[game_id]['success']:
        game_info = data[game_id]['data']
        price_table = db_parse_price(game_info)
        game = App(
            app_id=game_id,
            name=game_info['name'],
            description=game_info['detailed_description'],
            price_info=price_table
        )

        db.session.add(game)
        db.session.commit()


class SteamAppList():
    def __init__(self):
        resp = requests.get('http://api.steampowered.com/ISteamApps/GetAppList/v0001')
        self.raw = resp.json()
        self.df = pd.DataFrame(self.raw['applist']['apps']['app'])

    # def search_for(self):


# class SteamGame():

#     def __init__(self, game_id):
#         self.game_id = game_id
#         game_detail_json = get_game(game_id)
#         self.json = game_detail_json if game_detail_json else {}
#         self.price_info = self.get_price()

#     def get_price(self):
#         if ifnokey(self.json, 'price_overview', False):
#             return None
#         return self.json[self.game_id]['data']['price_overview']

