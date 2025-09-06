import typing
from json import JSONDecodeError

import httpx
from httpx import Response
from httpx._client import USE_CLIENT_DEFAULT, UseClientDefault
from httpx._types import (
    AuthTypes,
    CookieTypes,
    HeaderTypes,
    QueryParamTypes,
    RequestContent,
    RequestData,
    RequestExtensions,
    RequestFiles,
    TimeoutTypes
)
from fastmcp.server.context import Context
from fastmcp.server.dependencies import get_context

from .utils import get_backend_session_id


class AsyncClient(httpx.AsyncClient):
    """
    重写 httpx.AsyncClient 的请求方法（GET、POST、PUT、DELETE、PATCH）

    以至于在发送请求时自动在请求头中添加 cookies 进行身份验证
    """

    def get_backend_session_id(self) -> str:
        context: Context = get_context()
        return get_backend_session_id(context)

    def construct_cookies(self, cookies: CookieTypes | None = None):
        session_id = self.get_backend_session_id()
        _cookies = cookies or {}
        _cookies["session_id"] = session_id
        return _cookies

    def parse_response(self, response: Response):
        if response.status_code != 200:
            return {}
        try:
            json_response = response.json()
        except JSONDecodeError:
            return {}
        if json_response["code"] != 200:
            return {}
        return json_response

    async def get(
        self,
        url: str,
        *,
        parse_response: bool = True,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault | None = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ):
        response = await super().get(
            url, 
            params=params, 
            headers=headers, 
            cookies=self.construct_cookies(cookies),
            auth=auth, 
            follow_redirects=follow_redirects, 
            timeout=timeout, 
            extensions=extensions
        )
        if parse_response:
            return self.parse_response(response)
        return response
    
    async def post(
        self,
        url: str,
        *,
        parse_response: bool = True,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: typing.Any | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ):
        response = await super().post(
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=self.construct_cookies(cookies),
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions
        )
        if parse_response:
            return self.parse_response(response)
        return response
    
    async def put(
        self,
        url: str,
        *,
        parse_response: bool = True,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: typing.Any | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ):
        response = await super().put(
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=self.construct_cookies(cookies),
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions,
        )
        if parse_response:
            return self.parse_response(response)
        return response
    
    async def delete(
        self,
        url: str,
        *,
        parse_response: bool = True,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ):
        response = await super().delete(
            url,
            params=params,
            headers=headers,
            cookies=self.construct_cookies(cookies),
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions,
        )
        if parse_response:
            return self.parse_response(response)
        return response
    
    async def patch(
        self,
        url: str,
        *,
        parse_response: bool = True,
        content: RequestContent | None = None,
        data: RequestData | None = None,
        files: RequestFiles | None = None,
        json: typing.Any | None = None,
        params: QueryParamTypes | None = None,
        headers: HeaderTypes | None = None,
        cookies: CookieTypes | None = None,
        auth: AuthTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        follow_redirects: bool | UseClientDefault = USE_CLIENT_DEFAULT,
        timeout: TimeoutTypes | UseClientDefault = USE_CLIENT_DEFAULT,
        extensions: RequestExtensions | None = None,
    ):
        response = await super().patch(
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=self.construct_cookies(cookies),
            auth=auth,
            follow_redirects=follow_redirects,
            timeout=timeout,
            extensions=extensions,
        )
        if parse_response:
            return self.parse_response(response)
        return response
