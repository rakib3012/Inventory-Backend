from models.base import Base
from sqlalchemy import Column,BigInteger, TIMESTAMP,String
from datetime import datetime, timezone
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True,autoincrement=True,nullable=False)
    fastName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    mobile = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    otp = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=lambda:datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=lambda:datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))

    # relationship
    category = relationship("Category", back_populates="users")
    product = relationship("Product", back_populates="users")
    invoice = relationship("Invoice", back_populates="users")
    invoice_product = relationship("Invoice_Proudcts", back_populates="users")
