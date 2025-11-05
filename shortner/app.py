from fastapi import FastAPI

from shortner.middleware.performance_check import PerformanceCheckMiddleware
from shortner.routers import router

app = FastAPI()

app.add_middleware(PerformanceCheckMiddleware)

app.include_router(router)
