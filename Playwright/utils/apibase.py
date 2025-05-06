from playwright.sync_api import Playwright

ordersPayload= {"orders":[{"country":"India","productOrderedId":"67a8dde5c0d3e6622a297cc8"}]}

class APIBase:

    def gettoken(self, playwright:Playwright):
        apirequestcontext = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response= apirequestcontext.post("api/ecom/auth/login",
                               data={"userEmail":"rahul.m.lokurte@gmail.com","userPassword":"Wipro@123"})
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody


    def createorder(self,playwright:Playwright):
        token_data = self.gettoken(playwright)
        token = token_data["token"]
        apirequestcontext=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response2= apirequestcontext.post("api/ecom/order/create-order",
                               data=ordersPayload,
                               headers={"Authorization" : token,
                                        "Content-Type" : "application/json"})

        print(response2.json())
        response_body = response2.json()
        orderId= response_body["orders"][0]
        return orderId





