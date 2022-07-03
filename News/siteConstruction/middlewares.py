from django.shortcuts import render


class underConstructionMiddleware :
    def __init__(self,get_response) :
        self.get_response  = get_response
    def __call__(self, request) :
        print("Call from Middleware Before View")
        # response = self.get_response(request)
        response = render(request,'siteConstruction.html')
        print("Call from Middleware After View")
        return response