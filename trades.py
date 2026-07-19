from fastapi import APIRouter

router = APIRouter()

@router.get("/trades")
def trades():

    return []

@router.post("/trade")
def place_trade():

    return {
        "status":
        "submitted"
    }
