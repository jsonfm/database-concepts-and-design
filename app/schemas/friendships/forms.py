from pydantic import BaseModel

from app.schemas.friendships import FriendshipStatus


class CreateFriendShipForm(BaseModel):
    user_one_id: int
    user_two_id: int
    status: FriendshipStatus


