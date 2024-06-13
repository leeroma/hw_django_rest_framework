from rest_framework import status
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


class SubtractView(APIView):
    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number", "returns": "difference"})

    def post(self, request):
        a, b = request.data['a'], request.data['b']
        if isinstance(a, int) and isinstance(b, int):
            answer = {"answer": a - b}
        else:
            answer = {"error": "incorrect input"}

        return Response(answer)


class DivideView(APIView):
    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number", "returns": "quotient"})

    def post(self, request):
        a, b = request.data['a'], request.data['b']

        if b == 0:
            error = {"error": "Division by zero!"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST, )

        if isinstance(a, int) and isinstance(b, int):
            answer = {"answer": a / b}
        else:
            answer = {"error": "incorrect input"}

        return Response(answer)
