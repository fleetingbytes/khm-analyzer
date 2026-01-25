from __future__ import annotations

from textwrap import dedent
from typing import TYPE_CHECKING

from khm_cli.cli import cli
from khm_cli.return_code import ReturnCode
from pytest import mark, param

if TYPE_CHECKING:
    from click.testing import CliRunner, Result


@mark.parametrize(
    "maybe_xml, out_match, err_match, return_code",
    (
        param("this is not xml", "", "Start tag expected", ReturnCode.INVALID_XML, id="no-start-tag"),
        param("<this>", "", "Premature", ReturnCode.INVALID_XML, id="premature-end"),
        param("", "", "Document is empty", ReturnCode.INVALID_XML, id="empty-file"),
        param(
            dedent("""\
                       <?xml version="1.0" encoding="UTF-8"?>
                       <root>
                           <child>ok</child>
                       </root>
                   """),
            "",
            "",
            ReturnCode.OK,
            id="xml-ok",
        ),
    ),
)
def test_validate_xml(
    capfd, cli_runner: CliRunner, maybe_xml: str, out_match: str, err_match: str, return_code: ReturnCode
):
    result: Result = cli_runner.invoke(cli, ("validate", "-"), input=maybe_xml)

    stdout, stderr = capfd.readouterr()

    assert out_match in stdout
    assert err_match in stderr
    assert result.return_value is None
    assert result.exit_code == return_code
