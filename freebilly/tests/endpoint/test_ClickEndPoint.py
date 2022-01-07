from click.testing import CliRunner
from freebilly.endpoint.ClickEndPoint import ClickEndPoint

# check that asking for help is helpful :)
def test_record_session_helpflags():

    runner = CliRunner()
    result = runner.invoke(ClickEndPoint.freebilly_cli, ["record-session", "--help"])
    assert "Error:" not in result.output