from django.shortcuts import render
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from rgb_app.models import Chemical_Properties,Admin_login
from rgb_app.seriallizers import chemical_value_serializer
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

class view_chemical_class(viewsets.ModelViewSet):

    @csrf_exempt
    def UserReg(self,request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username, password)


        try:
            Users=Admin_login.objects.get(username=username,password=password)
            return JsonResponse({"success": 1})

        except Exception as e:
            print(e)
            return JsonResponse({"success": 0})


    @csrf_exempt
    def post_API_chemical_values(self,request):
        
        chemical_properties=Chemical_Properties()
        chemical_properties.chemical_category=request.POST.get('chemical_category')
        chemical_properties.chemical_name=request.POST.get('chemical_name')
        chemical_properties.value_b=request.POST.get('value_b')
        chemical_properties.value_m=request.POST.get('value_m')
        chemical_properties.parameter_y=request.POST.get('parameter_y')
        chemical_properties.save()
        return HttpResponse("Success")    


    @csrf_exempt
    def get_API_chemical_values(self,request):
        
        stored_chemical_values = Chemical_Properties.objects.all()
        seriallizer = chemical_value_serializer(stored_chemical_values,many=True)
        
        return JsonResponse({'values':json.loads(json.dumps(seriallizer.data)),'success':1})  

  

    @csrf_exempt
    def update_values(self, request):
        chemical_property = Chemical_Properties.objects.get(id=request.POST.get('id'))
        fields = {'chemical_category', 'chemical_name', 'value_b', 'value_m', 'parameter_y'}
        for field in fields:
            value = request.POST.get(field)
            if value is not None:
                # setattr(obj(chemical_property),stringer(field),value(the value to be set))
                setattr(chemical_property, field, value)  #chemical_Properties.chemical_category=request.POST.get('chemical_category') and so on
        chemical_property.save()
        return JsonResponse({"Success": True})



    @csrf_exempt
    def delate_values_by_id(self,request):
        Chemical_Properties.objects.get(id=request.POST.get('id')).delete()       
        return JsonResponse({'success':1})

    # @csrf_exempt
    # def deleteData(self,request):
    #     Chemical_Properties.objects.all().delete()       
    #     return JsonResponse({'success':1})    

        