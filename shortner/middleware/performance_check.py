from time import perf_counter

from starlette.middleware.base import BaseHTTPMiddleware


class PerformanceCheckMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):  # noqa: PLR6301
        start = perf_counter()
        response = await call_next(request)
        duration_ms = (perf_counter() - start) * 1000

        print(f'{request.method} {request.url.path} took {duration_ms:.2f}ms')
        response.headers['X-Process-Time-ms'] = f'{duration_ms:.2f}'

        return response
