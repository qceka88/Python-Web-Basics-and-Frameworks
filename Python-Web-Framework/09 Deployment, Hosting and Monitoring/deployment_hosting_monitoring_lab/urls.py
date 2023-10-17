"""
#For deoployment
1. Package application in Docker image
2. Push docker image into docker hub
3. pull dicker image inside the server
3. Start application using the new image ein the server
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('deployment_hosting_monitoring_lab.web_deployment.urls'))
]
