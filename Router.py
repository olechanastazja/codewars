class Router:

    def __init__(self):
        self.routes= {}

    def bind(self, route, method, func):
        self.routes[route, method] = func

    def runRequest(self, route, method):
        return self.routes.get((route, method), lambda: "Error 404: Not Found")()
