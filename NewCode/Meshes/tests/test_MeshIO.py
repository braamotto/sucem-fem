from __future__ import division

import numpy as N
from numpy.testing import NumpyTestCase, assert_array_equal, assert_almost_equal, assert_equal

from NewCode.Utilities import Struct
from NewCode.tests.TetMeshes import SixPyramConverted

# class test_FemmeshWriter(NumpyTestCase):
#     TestMesh = SixPyramConverted
#     def test_output(self):
#         mesh = Struct(elements=TestMest.listmesh[