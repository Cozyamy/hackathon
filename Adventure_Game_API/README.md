```markdown
# FastAPI Game Inventory System

This is a simple FastAPI application for managing a player's inventory and exploring game locations.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-game-inventory.git
   ```

2. Install dependencies:
   ```bash
   poetry shell
   poetry install
   ```

## Usage

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. The API will be available at `http://localhost:8000`.

## Endpoints

### Add Item to Inventory

- **URL:** `/inventory/add`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "item": "item_name"
  }
  ```
- **Response:**
  ```json
  {
    "inventory": ["item1", "item2", ...]
  }
  ```

### Remove Item from Inventory

- **URL:** `/inventory/remove`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "item": "item_name"
  }
  ```
- **Response:**
  ```json
  {
    "inventory": ["remaining_item1", "remaining_item2", ...]
  }
  ```

### Explore Location

- **URL:** `/explore/{location_name}`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "description": "Location description",
    "items": ["item1", "item2", ...]
  }
  ```
