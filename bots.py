from fastapi import APIRouter

router = APIRouter()

@router.post("/bots/start")
def start_bot():

    return {
        "status":
        "started"
    }

@router.post("/bots/stop")
def stop_bot():

    return {
        "status":
        "stopped"
    }
