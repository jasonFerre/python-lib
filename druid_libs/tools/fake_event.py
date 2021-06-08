
from typing import Optional


class FakeEvent:
    def __init__(self) -> None:
        pass

    def proxy_api_event(
        resource: str = "/",
        path: str = "/",
        method: str = "GET",
        body: Optional[str] = None,
        iam: Optional[str] = None,
        cognito: Optional[str] = None,
        path_params: Optional[dict] = None,
        query_params: Optional[dict] = None,
    ):
        return {
            "resource": resource,
            "path": path,
            "httpMethod": method,
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "CloudFront-Forwarded-Proto": "https",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-Mobile-Viewer": "false",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Tablet-Viewer": "false",
                "CloudFront-Viewer-Country": "BR",
                "Host": "qxdb8jvno4.execute-api.us-east-1.amazonaws.com",
                "Postman-Token": "e8531730-a73f-4c6a-ade2-e90a9151f78d",
                "User-Agent": "PostmanRuntime/7.26.8",
                "Via": "1.1 500f59fe7e67ec25b5c0692f11203995.cloudfront.net (CloudFront)",
                "X-Amz-Cf-Id": "nIeXAosYYVyqR_2-j1OfuAQW4W0Y8JjITxmXGe3XZ55AJwyy7fj8Vw==",
                "x-amz-date": "20210511T144925Z",
                "X-Amzn-Trace-Id": "Root=1-609a9974-39c9cddc0e4fe38d7334b081",
                "X-Forwarded-For": "201.95.56.60, 130.176.40.157",
                "X-Forwarded-Port": "443",
                "X-Forwarded-Proto": "https",
            },
            "multiValueHeaders": {
                "Accept": ["*/*"],
                "Accept-Encoding": ["gzip, deflate, br"],
                "CloudFront-Forwarded-Proto": ["https"],
                "CloudFront-Is-Desktop-Viewer": ["true"],
                "CloudFront-Is-Mobile-Viewer": ["false"],
                "CloudFront-Is-SmartTV-Viewer": ["false"],
                "CloudFront-Is-Tablet-Viewer": ["false"],
                "CloudFront-Viewer-Country": ["BR"],
                "Host": ["qxdb8jvno4.execute-api.us-east-1.amazonaws.com"],
                "Postman-Token": ["e8531730-a73f-4c6a-ade2-e90a9151f78d"],
                "User-Agent": ["PostmanRuntime/7.26.8"],
                "Via": ["1.1 500f59fe7e67ec25b5c0692f11203995.cloudfront.net (CloudFront)"],
                "X-Amz-Cf-Id": ["nIeXAosYYVyqR_2-j1OfuAQW4W0Y8JjITxmXGe3XZ55AJwyy7fj8Vw=="],
                "x-amz-date": ["20210511T144925Z"],
                "X-Amzn-Trace-Id": ["Root=1-609a9974-39c9cddc0e4fe38d7334b081"],
                "X-Forwarded-For": ["201.95.56.60, 130.176.40.157"],
                "X-Forwarded-Port": ["443"],
                "X-Forwarded-Proto": ["https"],
            },
            "queryStringParameters": query_params,
            "multiValueQueryStringParameters": None,
            "pathParameters": {"proxy": path_params},
            "stageVariables": None,
            "requestContext": {
                "resourceId": "bi0u94",
                "resourcePath": resource,
                "httpMethod": method,
                "extendedRequestId": "fKzqPEuOIAMFT0Q=",
                "requestTime": "11/May/2021:14:49:24 +0000",
                "path": path,
                "accountId": "653636420967",
                "protocol": "HTTP/1.1",
                "stage": "prod",
                "domainPrefix": "qxdb8jvno4",
                "requestTimeEpoch": 1620744564698,
                "requestId": "f50288c9-2111-4b6f-aca2-daef189c358d",
                "identity": {
                    "cognitoIdentityPoolId": cognito,
                    "accountId": "653636420967",
                    "cognitoIdentityId": cognito,
                    "caller": "AIDAZQL6EIVT7NTE4B6YP",
                    "sourceIp": "201.95.56.60",
                    "principalOrgId": "o-yuaj5cshgl",
                    "accessKey": "",
                    "cognitoAuthenticationType": None,
                    "cognitoAuthenticationProvider": None,
                    "userArn": None,
                    "userAgent": "PostmanRuntime/7.26.8",
                    "user": "AIDAZQL6EIVT7NTE4B6YP",
                },
                "domainName": "qxdb8jvno4.execute-api.us-east-1.amazonaws.com",
                "apiId": "qxdb8jvno4",
            },
            "body": body,
            "isBase64Encoded": False,
        }
