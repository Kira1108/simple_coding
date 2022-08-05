from typing import Protocol


class DataReader(Protocol):
    def read(self,**kwargs) -> dict:
        """read data from file"""