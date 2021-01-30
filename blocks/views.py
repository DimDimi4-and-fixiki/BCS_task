from django.shortcuts import render
from django.http import HttpResponse
from .api_handler import ApiHandler
# Create your views here.


api_handler = ApiHandler()


def show_block_by_height(request, height: int):
    response = api_handler.get_block_info(height=height)
    return render(request, 'blocks/block_page.html', context={"content": response})


def index(request, page_num: int):
    response = api_handler.get_page(page_num=page_num, page_size=50)
    prev_page = 0
    if page_num == 1:
        prev_page = "#"
    else:
        prev_page = page_num - 1
    context = {
        "data": response,
        "page_num": page_num,
        "next_page_num": page_num + 1,
        "prev_page_num": prev_page

    }
    return render(request, 'blocks/index.html', context=context)
