import requests
import json
from .models import Block
from .tables_handler import BlockTableHandler


class ApiHandler(object):

    def __init__(self):
        self.api_url = "https://bcschain.info/api/"
        self.block_table_handler = BlockTableHandler()

    def get_block_info(self, height: int):


        #  URL for GET request (GET /block/:height):
        request_url = self.api_url + "block/" + str(height)

        response = requests.get(request_url)  # response from API
        json_response = response.json()
        return json_response["hash"]

    def get_page(self, page_num: int, page_size: int):

        #  URL for GET request (GET /blocks?page=...):
        request_url = self.api_url + "recent-blocks"
        params = {
            "count": page_num * page_size
        }

        response = requests.get(request_url, params=params)
        json_response = response.json()[-page_size:]
        for block in json_response:
            height = block["height"]
            block_hash = block["hash"]
            timestamp = block["timestamp"]
            miner = block["miner"]
            num_of_transactions = block["transactionCount"]
            if not self.block_table_handler.check_by_height(height=height):
                elem = self.block_table_handler.get_block_by_height(height=height)
                block["height"] = elem.height
                block["hash"] = elem.hash
                block["miner"] = elem.miner
                block["timestamp"] = elem.timestamp
                block["transactionCount"] = elem.number_of_transactions
            else:
                self.block_table_handler.add_block(height=height,
                                                   hash=block_hash,
                                                   timestamp=timestamp,
                                                   miner=miner,
                                                   num_of_transactions=num_of_transactions)

        return json_response







