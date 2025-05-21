from django.urls import path
from .views import ProductListView,product_detail,SearchProductsView,ProductListByCategory,products_categories_partial


urlpatterns = [
        # path("products-function", product_list, name="products-fbv"),
        path("products",ProductListView.as_view(), name="products-cbv"),
        path("products/search", SearchProductsView.as_view(), name="search-products"),
        path("products/<int:productId>/<str:name>", product_detail, name="product-detail"),
        path("products/<str:category_name>",ProductListByCategory.as_view(), name="products-with-category"),
        path("products_categories_partial",products_categories_partial, name="products_categories_partial"),

]

