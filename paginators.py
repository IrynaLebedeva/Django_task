from rest_framework.pagination import PageNumberPagination

class SubTasksPagination(PageNumberPagination):
    ordering = '-created_at'
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 10

class TasksPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page'
    max_page_size = 10
    ordering = '-created_at'