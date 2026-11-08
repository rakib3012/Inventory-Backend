from models.base import Base

from sqlalchemy import BigInteger, String, Column, TIMESTAMP, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    total = Column(String,nullable=False)
    discount = Column(String, nullable=False)
    vat = Column(String, nullable=False)
    payable = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))


    #relationship
    user = relationship("User", back_populates="invoices")
    invoice_product = relationship("Invoice_Product", back_populates="invoice")
    customer = relationship("Customer", back_populates="invoice")