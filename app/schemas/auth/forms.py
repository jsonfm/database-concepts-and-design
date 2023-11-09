from pydantic import (BaseModel, EmailStr, Field, SecretStr, model_validator,
                      field_validator)

from app.utils.auth import hash_password

class LoginForm(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class SignupForm(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    confirm: str = Field(min_length=8)
    
    @model_validator(mode="after")
    def validate_and_hash_password(self, **kwargs) -> 'SignupForm':
        if self.password != self.confirm:
            raise ValueError("Password doesn't match.")
        hashed = hash_password(self.password)
        self.password = hashed
        delattr(self, "confirm")
        return self

