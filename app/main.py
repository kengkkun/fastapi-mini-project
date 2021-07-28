from fastapi import FastAPI
import uvicorn
from configs.db import Base, engine
from routers import carrier_router


# -------- Create DB --------------
# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, checkfirst=True)


app = FastAPI(title='Mini Project')

# ------------- All Router -----------------
# app.include_router(price_router.price_router, tags=['price'])
# app.include_router(price_truck_load_router.price_truck_router, tags=['price truck'])
app.include_router(carrier_router.carrier_router, tags=['Carrier'])

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8000,
        reload=True,
        access_log=False,
        workers=2,
    )
