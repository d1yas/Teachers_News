from rest_framework.pagination import PageNumberPagination

class TeacherPagination(PageNumberPagination):
    page_size = 10              # har bir sahifada nechta bo‘lsin
    page_size_query_param = 'page_size'  # ?page_size=5 ishlaydi
    max_page_size = 100         # eng ko‘pi bilan 100
