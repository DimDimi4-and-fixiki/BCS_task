from .models import Block


class BlockTableHandler(object):
    """
    Class for different operations with Block model
    """

    #  Checks if block is in the table by its height:
    def check_by_height(self, height: int) -> bool:
        # returns True if block is not in the table:
        res = Block.objects.filter(height=height).exists()
        return not res

    def add_block(self, **kwargs):
        height = kwargs.get("height")
        block_hash = kwargs.get("hash")
        timestamp = kwargs.get("timestamp")
        miner = kwargs.get("miner")
        num_of_transactions = kwargs.get("num_of_transactions")
        if self.check_by_height(height=height):
            block = Block(height=height,
                          hash=block_hash,
                          timestamp=timestamp,
                          miner=miner,
                          number_of_transactions=num_of_transactions)
            block.save()

    def get_block_by_height(self, height: int):
        res = {}
        block = Block.objects.get(height=height)
        return block



