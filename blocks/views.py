from django.shortcuts import render
from django.http import HttpResponse
from .api_handler import ApiHandler
# Create your views here.


api_handler = ApiHandler()


def show_block_by_height(request, height: int):
    """
    Shows info about one block by its height
    """
    response = api_handler.get_block_info(height=height)
    return render(request, 'blocks/block_page.html', context={"content": response})


def index(request, page_num: int):
    """
    Shows page of blocks
    """
    response = api_handler.get_page(page_num=page_num, page_size=50)
    prev_page = 0  # previous page number
    if page_num == 1:  # First page
        prev_page = "#"  # No previous page
    else:
        prev_page = page_num - 1
    context = {  # Params for the template
        "data": response,
        "page_num": page_num,
        "next_page_num": page_num + 1,
        "prev_page_num": prev_page

    }
    return render(request, 'blocks/index.html', context=context)
