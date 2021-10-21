from django.shortcuts import render
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "c23575a576mshc2a1ab00487db9ap19f969jsn4c3d8826f138"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)
def home(request):
    noofresult =  int(response['results'])
    mylist=[]
    for i in range(0, noofresult):
        mylist.append(response['response'][i]['country'])
    
        
    if request.method =='POST':
      
        selectedcountry= request.POST['selectedcountry']
        noofresult =  int(response['results'])
        for i in range(0, noofresult):
            if selectedcountry == response['response'][i]['country']:
                new=response['response'][i]['cases']['new']
                active=response['response'][i]['cases']['active']
                critical=response['response'][i]['cases']['critical']
                recovered=response['response'][i]['cases']['recovered']
                total=response['response'][i]['cases']['total']
                deaths= int(total)- int(recovered)-int(active)
                print (response['response'][i]['cases'])
                
        context={'selectedcountry':selectedcountry,'mylist':mylist, 'new':new, 'active':active,  'critical':critical, 'recovered':recovered, 'total':total,'deaths':deaths}
        return render(request, 'covidapp/home.html',context)
    noofresult =  int(response['results'])
    mylist=[]
    for i in range(0, noofresult):
        mylist.append(response['response'][i]['country'])
    
  
  
    return render(request, 'covidapp/home.html', {'mylist': mylist})