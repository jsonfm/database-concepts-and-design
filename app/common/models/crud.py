from app.db import db


class CRUD:
    """Common CRUD operations."""

    @classmethod
    def get_items(cls, limit: int = 20, offset: int = 0):
        """Returns a list of items"""
        with db.session() as session:
            result = session.query(cls).limit(limit).offset(offset).all()
            return result

    @classmethod
    def get_item(cls, item_id: int):
        """Returns an item given its ID."""
        with db.session() as session:
            result = session.query(cls).filter_by(id=item_id).first()
            return result

    @classmethod
    def update(cls, item_id: int, data: dict):
        """Updates an item."""
        with db.session() as session:
            item = session.query(cls).filter_by(id=item_id).first()
            if item is not None:
                for key, value in data.items():
                    if getattr(item, key, None) is not None:
                        setattr(item, key, value)
                session.commit()
                session.refresh(item)
                return item

    @classmethod
    def delete(cls, item_id: int):
        with db.session() as session:
            item = session.query(cls).filter_by(id=item_id).first()
            if item is not None:
                session.delete(item)
                session.commit()
                return item.id

    def delete_instance(self):
        """Deletes current instance from database."""
        with db.session() as session:
            session.delete(self)
            session.commit()

    @classmethod
    def create(cls, data: dict):
        with db.session() as session:
            instance = cls(**data)
            session.add(instance)
            session.commit()
            return instance

    def create_instance(self):
        """Saves current instance to database."""
        with db.session() as session:
            session.add(self)
            session.commit()
            session.refresh(self)
            return self
