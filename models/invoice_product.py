from models.base import Base

from sqlalchemy import BigInteger, String, Column, TIMESTAMP, ForeignKey
from datetime import datetime, timezone
from sqlalchemy.orm import relationship


class Invoice_Product(Base):
    __tablename__ = "invoice_products"

    id = Column(BigInteger, primary_key=True,autoincrement=True)
    user_id = Column(BigInteger,ForeignKey("users.id"), nullable=False)
    product_id = Column(BigInteger,ForeignKey("products.id"), nullable=False)
    invoice_id = Column(BigInteger,ForeignKey("invoices.id"), nullable=False)
    qty = Column(String,nullable=False)
    sale_price = Column(String, nullable=False)
    create_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(TIMESTAMP, nullable=False, default=datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    # relationship

    user = relationship("User",back_populates="invoice_products")
    proudct =relationship("Product",back_populates="invoice_products")
    invoice = relationship("Invoice",back_populates="invoice_products")