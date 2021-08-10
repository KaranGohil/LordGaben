
""""This function takes item's name
    which the user wants to search
    
    improvement to make:
    change - 
    app id (CSGO item)
    currency (CDN only)

    Right now the market_hast_name needs to be perfect.
    """
def setlink(item_name):
  oglink = "http://steamcommunity.com/market/priceoverview/?appid=730&currency=20&market_hash_name="

  return oglink + item_name

