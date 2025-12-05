from rest_framework.pagination import PageNumberPagination

class SubTasksPagination(PageNumberPagination):
    ordering = '-created_at'
    page_size = 5
    page_size_quer_param = 'page'
    max_page_size = 10
