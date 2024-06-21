from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if b == 0:
            raise ValueError
        return a / b


class CalculatorView(APIView):
    _calculator = Calculator()

    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number", "method": "add/multiply/subtract/divide"})

    def post(self, request):
        a, b, method = request.data['a'], request.data['b'], request.data['method']

        if not isinstance(a, int) or not isinstance(b, int):
            error = {"error": "Incorrect input!"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        try:
            answer = getattr(self._calculator, method)(a, b)
        except AttributeError:
            error = {"error": "No such method"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            error = {"error": "Division by zero!"}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response({"answer": answer})
