import requests
import json
from .models import Block
from .tables_handler import BlockTableHandler


class ApiHandler(object):
    """
    Class for handling all operations with BCS API
    """

    def __init__(self):
        self.api_url = "https://bcschain.info/api/"  # main API url
        self.block_table_handler = BlockTableHandler()

    def get_block_info(self, height: int):
        """
        Gets info about one block by the block's height
        """

        #  URL for GET request (GET /block/:height):
        request_url = self.api_url + "block/" + str(height)

        # Gets response from API
        response = requests.get(request_url)  # response from API
        json_response = response.json()  # Parses to JSON

        #  Extracts different values from JSON:
        height = json_response["height"]
        block_hash = json_response["hash"]
        timestamp = json_response["timestamp"]
        miner = json_response["miner"]
        num_of_transactions = len(json_response["transactions"])

        # Adds Num of transaction key:
        json_response["transactionCount"] = num_of_transactions

        # Block is already in the database
        if not self.block_table_handler.check_by_height(height=height):

            #  Replaces values in JSON with values from the database:
            elem = self.block_table_handler.get_block_by_height(height=height)
            json_response["height"] = elem.height
            json_response["hash"] = elem.hash
            json_response["miner"] = elem.miner
            json_response["timestamp"] = elem.timestamp
            json_response["transactionCount"] = elem.number_of_transactions

        # Block is not in the database
        else:
            # Adds block to the database
            self.block_table_handler.add_block(height=height,
                                               hash=block_hash,
                                               timestamp=timestamp,
                                               miner=miner,
                                               num_of_transactions=num_of_transactions)
        return json_response

    def get_page(self, page_num: int, page_size: int):
        """
        Gets page with blocks from BCS API
        page_num, page_size: pagination params
        """
        #  URL for GET request (GET /blocks?page=...):
        request_url = self.api_url + "recent-blocks"
        params = {
            "count": page_num * page_size
        }

        response = requests.get(request_url, params=params)
        json_response = response.json()[-page_size:]  # Takes blocks from the last page

        for block in json_response:
            # Extracts block params from JSON
            height = block["height"]
            block_hash = block["hash"]
            timestamp = block["timestamp"]
            miner = block["miner"]
            num_of_transactions = block["transactionCount"]

            # Block is already in the database
            if not self.block_table_handler.check_by_height(height=height):

                #  Replaces values in JSON with values from the database:
                elem = self.block_table_handler.get_block_by_height(height=height)
                block["height"] = elem.height
                block["hash"] = elem.hash
                block["miner"] = elem.miner
                block["timestamp"] = elem.timestamp
                block["transactionCount"] = elem.number_of_transactions

            # Block is not in the database
            else:
                # Adds block to the database
                self.block_table_handler.add_block(height=height,
                                                   hash=block_hash,
                                                   timestamp=timestamp,
                                                   miner=miner,
                                                   num_of_transactions=num_of_transactions)

        return json_response







