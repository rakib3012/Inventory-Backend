from models.base import Base

from sqlalchemy import BigInteger, String, Column, TIMESTAMP, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Customer(Base):
    __tablename__ = "customers"

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    user_id = Column(BigInteger,ForeignKey("users.id"), nullable=False)
    invoice_id = Column(BigInteger, ForeignKey("invoices.id"), nullable=False)
    name = Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True)
    mobile = Column(String,nullable=False,unique=True)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    # Relationship
    invoice = relationship("Invoice", back_populates="customers")
    user = relationship("User", back_populates="customers")
