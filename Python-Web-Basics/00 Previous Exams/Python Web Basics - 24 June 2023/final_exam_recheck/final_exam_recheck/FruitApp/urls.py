from django.urls import path, include
from final_exam_recheck.FruitApp.views import fruit_create, fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('create/', fruit_create, name='fruit create page'),
    path('<int:fruitID>/', include([
        path('details/', fruit_details, name='fruit details page'),
        path('edit/', fruit_edit, name='fruit edit page'),
        path('delete/', fruit_delete, name='fruit delete page'),
    ])),
]
