# -*- coding: utf-8 -*-

# Copyright (c) 2013 Ole Krause-Sparmann

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import numpy
import unittest

from nearpy.filters import NearestFilter, DistanceThresholdFilter


class TestVectorFilters(unittest.TestCase):

    def setUp(self):
        self.V = []
        self.V.append((numpy.array([0]), 'data', 0.4))
        self.V.append((numpy.array([1]), 'data', 0.9))
        self.V.append((numpy.array([2]), 'data', 1.4))
        self.V.append((numpy.array([3]), 'data', 2.1))
        self.V.append((numpy.array([4]), 'data', 0.1))
        self.V.append((numpy.array([5]), 'data', 8.7))
        self.V.append((numpy.array([6]), 'data', 3.4))
        self.V.append((numpy.array([7]), 'data', 2.8))

        self.threshold_filter = DistanceThresholdFilter(1.0)
        self.nearest_filter = NearestFilter(5)

    def test_thresholding(self):
        result = self.threshold_filter.filter_vectors(self.V)
        self.assertEqual(len(result), 3)
        self.assertTrue(self.V[0] in result)
        self.assertTrue(self.V[1] in result)
        self.assertTrue(self.V[4] in result)

    def test_nearest(self):
        result = self.nearest_filter.filter_vectors(self.V)
        self.assertEqual(len(result), 5)
        self.assertTrue(self.V[0] in result)
        self.assertTrue(self.V[1] in result)
        self.assertTrue(self.V[4] in result)
        self.assertTrue(self.V[2] in result)
        self.assertTrue(self.V[3] in result)


if __name__ == '__main__':
    unittest.main()