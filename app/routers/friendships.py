from fastapi import APIRouter

router = APIRouter(prefix="/friendships", tags=["Friendship"])

@router.get("/")
def get_friendships(limit: int = 30, offset: int = 0):
    return []

@router.get("/{friendship_id}")
def get_friendships(friendship_id):
    return {}

@router.post("/{friendship_id}")
def create_friendship(friendship_id):
    return {}

@router.put("/{friendship_id}")
def update_friendship():
    return {}

@router.delete("/{friendship_id}")
def delete_friendship(friendship_id):
    return {}

@router.get("/requests/user/{user_id}")
def get_friendship_requests_by_user(user_id: int):
    return []

@router.get("/requests/detail/{friendship_request_id}")
def get_friendship_request(friendship_request_id: int):
    return {}

@router.put("/requests/update/{friendship_request_id}")
def update_friendship_request(friendship_request_id: int):
    return {}