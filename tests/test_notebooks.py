"""Unit tests for the notebooks."""

import subprocess
import tempfile

import geomstats.tests


def _exec_notebook(path):

    file_name = tempfile.NamedTemporaryFile(suffix='.ipynb').name
    args = ['jupyter', 'nbconvert', '--to', 'notebook', '--execute',
            '--ExecutePreprocessor.timeout=1000',
            '--ExecutePreprocessor.kernel_name=python3',
            '--output', file_name, path]
    subprocess.check_call(args)


class TestNotebooks(geomstats.tests.TestCase):
    @staticmethod
    @geomstats.tests.np_only
    def test_tangent_pca_s2():
        _exec_notebook('notebooks/tangent_pca_s2.ipynb')

    @staticmethod
    def test_01_data_on_manifolds():
        _exec_notebook('notebooks/01_data_on_manifolds.ipynb')

    @staticmethod
    def test_02_from_vector_spaces_to_manifolds():
        _exec_notebook('notebooks/02_from_vector_spaces_to_manifolds.ipynb')

    @staticmethod
    @geomstats.tests.np_and_pytorch_only
    def test_03_embedding_graph_structured_data_h2():
        _exec_notebook('notebooks/03_embedding_graph_structured_data_h2.ipynb')

    @staticmethod
    def test_04_simple_machine_learning_tangent_spaces():
        _exec_notebook(
            'notebooks/04_simple_machine_learning_tangent_spaces.ipynb')
