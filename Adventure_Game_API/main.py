from fastapi import FastAPI, HTTPException

app = FastAPI()

player_inventory = []
game_locations = {
    "forest": {
        "description": "You are in a dense forest.",
        "items": ["sword", "shield"]
    },
    "cave": {
        "description": "You are in a dark cave.",
        "items": ["torch", "key"]
    }
}

@app.post("/inventory/add")
def add_item_to_inventory(item: str):
    """
    Add an item to the player's inventory.

    Args:
        item (str): The name of the item to add.

    Raises:
        HTTPException: If the item is already in the inventory.

    Returns:
        dict: Dictionary containing the updated inventory.
    """
    if item in player_inventory:
        raise HTTPException(status_code=400, detail="Item already in inventory")
    player_inventory.append(item)
    return {"inventory": player_inventory}


@app.post("/inventory/remove")
def remove_item_from_inventory(item: str):
    """
    Remove an item from the player's inventory.

    Args:
        item (str): The name of the item to remove.

    Raises:
        HTTPException: If the item is not found in the inventory.

    Returns:
        dict: Dictionary containing the updated inventory.
    """
    if item not in player_inventory:
        raise HTTPException(status_code=400, detail="Item not found in inventory")
    player_inventory.remove(item)
    return {"inventory": player_inventory}


@app.get("/explore/{location_name}")
def explore_location(location_name: str):
    """
    Explore a game location.

    Args:
        location_name (str): The name of the location to explore.

    Raises:
        HTTPException: If the specified location is not found.

    Returns:
        dict: Dictionary containing the description and items of the location.
    """
    if location_name not in game_locations:
        raise HTTPException(status_code=404, detail="Location not found")
    return game_locations[location_name]