import pytest
from click.testing import CliRunner
import freebilly.endpoint.ClickEndPoint as ClickEndPoint

# check that asking for help is helpful :)
@pytest.mark.parametrize(
    "subcmd",
    [
        None,
        "record-session",
        "produce-bill",
    ],
)
def test_record_session_helpflags(subcmd):

    runner = CliRunner()

    # Setup CLI args
    cli_args = ["--help"]
    if subcmd is not None:
        cli_args = [subcmd, "--help"]

    result = runner.invoke(ClickEndPoint.freebilly_cli, cli_args)
    assert "Error:" not in result.output
