from rest_framework.response import Response
from rest_framework.views import APIView


class AddView(APIView):
    def get(self, request):
        return Response({"a": "enter a number", "b": "enter a number"})

    def post(self, request):
        a, b = request.data['a'], request.data['b']
        answer = {"answer": a + b}
        return Response(answer)

