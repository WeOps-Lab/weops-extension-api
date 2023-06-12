from fastapi import Body
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from core.bk_api_utils.main import ApiManager
from core.blueking.component.shortcuts import get_client_by_admin
from core.http_schemas.common_response_schema import CommonResponseSchema
from server.apps.example.forms.test_api import FLowTicketModel, SearchBusinessModel

test_api = InferringRouter()


@cbv(test_api)
class Api:
    @test_api.post("/tickets_1", response_model=CommonResponseSchema, name="测试无参数获取单据")
    async def get_flow_tickets(self) -> CommonResponseSchema:
        resp = ApiManager.flow.over_get_tickets()
        return CommonResponseSchema(data=resp["data"], message="操作成功", success=True)

    @test_api.post("/tickets_2", response_model=CommonResponseSchema, name="测试带参数获取单据")
    async def get_flow_tickets_2(
        self,
        data: FLowTicketModel = Body(
            None,
            description="获取单据参数",
            example={
                "page": 1,
                "page_size": 10,
            },
        ),
    ) -> CommonResponseSchema:
        resp = ApiManager.flow.over_get_tickets(**data.dict())
        return CommonResponseSchema(data=resp["data"], message="操作成功", success=True)

    @test_api.post("/douban/tags", response_model=CommonResponseSchema, name="获取豆瓣标签")
    async def get_douban_tags(self) -> CommonResponseSchema:
        resp = ApiManager.douban.search_tags()
        return CommonResponseSchema(data=resp["tags"], message="操作成功", success=True)

    @test_api.post("/cc/search_business", response_model=CommonResponseSchema, name="获取蓝鲸业务列表(分页)")
    async def search_business(
        self,
        data: SearchBusinessModel = Body(
            None,
            description="获取业务的参数",
            example={
                "start": 0,
                "limit": 10,
            },
        ),
    ) -> CommonResponseSchema:
        client = get_client_by_admin()
        resp = client.cc.search_business({"page": data.dict()})
        return CommonResponseSchema(data=resp["data"], message="操作成功", success=True)
