from http import HTTPStatus
from typing import Union

from starlette.responses import Response

from api import individ_info


def get_readiness() -> Response:
    return Response(content='Ok', status_code=HTTPStatus.OK)


def get_individ_info(inn: int) -> Union[Response, individ_info.IndividInfo]:
    try:
        return individ_info.get_individ_info(inn=inn)
    except individ_info.UserNotFoundError:
        return Response(status_code=HTTPStatus.NOT_FOUND)
