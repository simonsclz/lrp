r'''Interface for simplified access to Random Number Generators.'''


__author__ = 'Rodrigo Bermudez Schettino (TU Berlin)'
__credits__ = ['Rodrigo Bermudez Schettino (TU Berlin)']
__maintainer__ = 'Rodrigo Bermudez Schettino (TU Berlin)'
__email__ = 'r.bermudezschettino@campus.tu-berlin.de'
__status__ = 'Development'

from typing import Generator, Union, Tuple
from abc import ABC, abstractmethod
import numpy


class RandomNumberGenerator(ABC):
    r'''
    Base random number generator class. Acts as interface for number generator classes.
    '''

    def __init__(self,
                 seed: int = 42):
        '''
        Constructor

        :param seed: Seed for the random number generator.
        '''
        self.generator: Generator = numpy.random.default_rng(seed=seed)

    @abstractmethod
    def draw(self) -> float:
        r'''
        Draws a random number from the distribution.
        '''


class UniformRNG(RandomNumberGenerator):
    r'''
    Uniform random number generator class.
    '''

    def draw(self, low: float = 0.0, high: float = 1.0, size: Union[int, Tuple[int]] = 1) -> float:
        r'''
        Draws a random number from the distribution.

        The lower and upper bounds are inclusive.

        :param low: Lower bound of the distribution.
        :param high: Upper bound of the distribution.
        :param size: Number of random numbers to draw.

        :returns: A random number from the uniform distribution.
        '''
        return self.generator.uniform(low, high)