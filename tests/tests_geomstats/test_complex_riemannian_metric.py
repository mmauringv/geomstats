"""Unit tests for the complex Riemannian metrics."""

import tests.conftest
from tests.conftest import Parametrizer
from tests.data.complex_riemannian_metric_data import ComplexRiemannianMetricTestData
from tests.tests_geomstats.test_riemannian_metric import TestRiemannianMetric


class TestComlexRiemannianMetric(TestRiemannianMetric, metaclass=Parametrizer):

    skip_test_log = True

    testing_data = ComplexRiemannianMetricTestData()

    def test_cometric_matrix(self, metric, base_point, expected):
        result = metric.cometric_matrix(base_point)
        self.assertAllClose(result, expected)

    def test_inner_coproduct(
        self, metric, cotangent_vec_a, cotangent_vec_b, base_point, expected
    ):
        result = metric.inner_coproduct(cotangent_vec_a, cotangent_vec_b, base_point)
        self.assertAllClose(result, expected)

    def test_hamiltonian(self, metric, state, expected):
        result = metric.hamiltonian(state)
        self.assertAllClose(result, expected)

    @tests.conftest.autograd_and_torch_only
    def test_inner_product_derivative_matrix(self, metric, base_point, expected):
        result = metric.inner_product_derivative_matrix(base_point)
        self.assertAllClose(result, expected)

    def test_inner_product(
        self, metric, tangent_vec_a, tangent_vec_b, base_point, expected
    ):
        result = metric.inner_product(tangent_vec_a, tangent_vec_b, base_point)
        self.assertAllClose(result, expected)

    def test_normalize(self, metric, tangent_vec, point, expected, atol):
        result = metric.norm(metric.normalize(tangent_vec, point), point)
        self.assertAllClose(result, expected, atol)

    def test_random_unit_tangent_vec(self, metric, point, n_vectors, expected, atol):
        result = metric.norm(metric.random_unit_tangent_vec(point, n_vectors), point)
        self.assertAllClose(result, expected, atol)

    @tests.conftest.torch_only
    def test_christoffels(self, metric, base_point, expected):
        result = metric.christoffels(base_point)
        self.assertAllClose(result, expected)

    @tests.conftest.torch_only
    def test_exp(self, metric, tangent_vec, base_point, expected):
        result = metric.exp(tangent_vec, base_point)
        self.assertAllClose(result, expected)
