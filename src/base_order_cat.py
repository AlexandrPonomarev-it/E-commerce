from abc import ABC, abstractmethod


class BaseOrderCat(ABC):

    @abstractmethod
    def __str__(self):
        pass
