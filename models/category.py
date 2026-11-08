
from models.base import Base

from sqlalchemy import BigInteger, String, Column, TIMESTAMP, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    user_id = Column(BigInteger,ForeignKey("users.id"), nullable=False)
    product_id = Column(BigInteger,ForeignKey("products.id"), nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    # Relationship
    proudct = relationship("Product",back_populates="categories")
    user = relationship("User", back_populates="categories")