import apis

my_puuid = "7X5uHYPv5LVZDlMNriPw1oKRI0zTxPW8UzSA0hLNOxRRsboZ6oEGTDG5pyMRZAo4CIki30-HWbBFNw"

REGION_CODES = {
    'EUNE': 'EUN1',
    'BR': 'BR1',
    'EUW': 'EUW1',
    'JP': 'JP1',
    'KR': 'KR',
    'LA1': 'LA1',
    'LA2': 'LA2',
    'NA': 'NA1',
    'OCE': 'OC1',
    'RU': 'RU',
    'TR': 'TR1'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": apis.riot_api,
}
