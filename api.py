import requests
import constants


def get_puuid(summoner_name, region):
    """
    Queries the API and returns the PUUID for given summoner ID in given region.
    :param summoner_name: str
    :param region: str - region ALL CAPS
    :return: str - PUUID
    """
    response = requests.get(
        'https://{}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}'.format(constants.REGION_CODES[region],
                                                                                   summoner_name.replace(' ', '%20')),
        headers=constants.headers)
    puuid = response.json()['puuid']
    return puuid


def get_last_x_matches(puuid, x_matches=20):
    """
    returns list of match ID for given player by puuid
    :param puuid: str unique player id
    :param x_matches: int number of matches you want returned (0-100) default 20
    :return: list of match IDs (str)
    """
    response = requests.get(
        "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?queue={}&start=0&count={}".format(
            puuid, constants.QUEUE_ID['SOLOQ'], x_matches),
        headers=constants.headers)

    matchid_list = response.json()
    return matchid_list
