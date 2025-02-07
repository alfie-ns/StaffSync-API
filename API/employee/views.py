from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import status

'''
    'comp2000' API ENDPOINTS; these were originally created
    by Plymouth University; this is my own copy of the API
    so the app continues to work.
'''

@api_view(['GET'])
def health_check(request):
    return Response({'status': 'API is working'})

@api_view(['GET'])
def get_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True) # multiple objects
    return Response(serializer.data)

@api_view(['GET'])
def get_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee added successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Employee updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_employee(request, id):
    try:
        employee = Employee.objects.get(id=id)
        employee.delete()
        return Response({'message': 'Employee deleted successfully'})
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)