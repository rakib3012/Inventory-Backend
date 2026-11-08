from models.base import Base
from sqlalchemy import Column,BigInteger, TIMESTAMP,String, ForeignKey, Numeric
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class Proudct(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, autoincrement=True, nullable=False)
    user_id = Column(BigInteger,ForeignKey("users.id"), nullable=False)
    category_id = Column(BigInteger,ForeignKey("categories.id"),nullable=False)
    title = Column(String, nullable=False,)
    units = Column(String, nullable=False,)
    price = Column(String, nullable=False)
    img_url =  Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))


    # Relationship
    user = relationship("User", back_populates="proudcts")
    category = relationship("Category", back_populates="products")
    invoice_product = relationship("Invoice_Product", back_populates="products")
    