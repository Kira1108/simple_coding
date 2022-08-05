from typing import Protocol


class DataPlotting(Protocol):
    
    def draw(self, hours:list, temperatures:list) -> None:
        """draw line plot of hours and temperaturs list"""