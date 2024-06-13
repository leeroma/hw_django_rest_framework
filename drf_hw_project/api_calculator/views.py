from rest_framework.response import Response
from rest_framework.views import APIView


class AddView(APIView):
    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number", "returns": "sum"})

    def post(self, request):
        a, b = request.data['a'], request.data['b']
        if isinstance(a, int) and isinstance(b, int):
            answer = {"answer": a + b}
        else:
            answer = {"error": "incorrect input"}

        return Response(answer)


class MultiplyView(APIView):
    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number", "returns": "product"})

    def post(self, request):
        a, b = request.data['a'], request.data['b']
        if isinstance(a, int) and isinstance(b, int):
            answer = {"answer": a * b}
        else:
            answer = {"error": "incorrect input"}

        return Response(answer)
