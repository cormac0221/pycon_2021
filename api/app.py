from fastapi import APIRouter, FastAPI

from api.handlers import get_individ_info, get_readiness


def create_app() -> FastAPI:
    app = FastAPI()

    router = APIRouter()
    router.add_api_route('/readiness', get_readiness, methods=['GET'])
    app.include_router(router)

    individ_router = APIRouter()
    individ_router.add_api_route('/{inn}/info', get_individ_info, methods=['GET'])
    app.include_router(individ_router, prefix='/individ')

    return app


if __name__ == '__main__':
    import uvicorn

    from db import DBSettings

    DBSettings().setup_db()

    app = create_app()
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
