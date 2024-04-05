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
    if item in player_inventory:
        raise HTTPException(status_code=400, detail="Item already in inventory")
    player_inventory.append(item)
    return {"inventory": player_inventory}


@app.post("/inventory/remove")
def remove_item_from_inventory(item: str):
    if item not in player_inventory:
        raise HTTPException(status_code=400, detail="Item not found in inventory")
    player_inventory.remove(item)
    return {"inventory": player_inventory}


@app.get("/explore/{location_name}")
def explore_location(location_name: str):
    if location_name not in game_locations:
        raise HTTPException(status_code=404, detail="Location not found")
    return game_locations[location_name]