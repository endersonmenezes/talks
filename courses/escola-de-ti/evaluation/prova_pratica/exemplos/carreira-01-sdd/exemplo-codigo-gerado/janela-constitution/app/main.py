from fastapi import FastAPI

from app.routers import bookings, clients, courts

app = FastAPI(title="Court Booking API")
app.include_router(courts.router)
app.include_router(clients.router)
app.include_router(bookings.router)
