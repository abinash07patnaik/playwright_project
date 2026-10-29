from playwright.sync_api import Playwright

ordersPayload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}

class APIUtils:
    def getToken(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail":"patnaikabinash07@gmail.com","userPassword":"Abichinu@#12345"},
                                            )
        assert response.ok
        return response.json()["token"]


    def createOrder(self, playwright:Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com", ignore_https_errors=True)
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Authorization":token,
                                          "Content-Type":"application/json"},
                                 )
        return response.json()