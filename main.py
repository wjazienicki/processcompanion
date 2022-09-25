# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass

# print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
