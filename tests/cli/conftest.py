from click.testing import CliRunner
from pytest import fixture


@fixture
def cli_runner():
    yield CliRunner()
