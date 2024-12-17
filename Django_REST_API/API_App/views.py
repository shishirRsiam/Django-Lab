from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    print('()' * 50)
    print(request)
    print('()' * 50)
    my_data = {
        "message": "Welcome to the API Home!",
        "status": "success",
        "data": {
            "user": "shishirRsiam",
            "role": "programmer",
            "projects": ["Django Blog", "Meal Search Application", "Library Management System"]
        }
    }
    return Response(my_data)
