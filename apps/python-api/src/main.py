from fastapi import FastAPI, HTTPException
from typing import List, Dict, Any
import os

app = FastAPI(
    title="python-api",
    description="Reference FastAPI service using platform-images/python-base",
)

ITEMS: List[Dict[str, Any]] = [
    {"id": 1, "name": "item-1", "description": "First item"},
    {"id": 2, "name": "item-2", "description": "Second item"},
]


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok", "service": "python-api"}


@app.get("/api/items")
def list_items() -> List[Dict[str, Any]]:
    return ITEMS


@app.get("/api/items/{item_id}")
def get_item(item_id: int) -> Dict[str, Any]:
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8000")))
