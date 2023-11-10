from enum import Enum


class FriendshipStatus(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "REJECTED"
    REJECTED = "REJECTED"