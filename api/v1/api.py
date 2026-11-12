from api.v1.endpoints import auth,customers,dashboard,invoice,users,produts,categories,invoice_item
from fastapi import APIRouter


router= APIRouter()


router.include_router(auth.router,tags=["Auth"]) # akhanay prefix (prefix="/auth")nam a akta property add kora jay . jata protita url er shurutay add boshay

router.include_router(users.router, tags=["users"])

router.include_router(produts.router, tags=["products"])

router.include_router(categories.router, tags=["categories"])

router.include_router(invoice.router, tags=["invoice"])

router.include_router(invoice_item.router, tags=["invoice_item"])

router.include_router(customers.router, tags=["customer"])

router.include_router(dashboard.router, tags=["dashboard"])