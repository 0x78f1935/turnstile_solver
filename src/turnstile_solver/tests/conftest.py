import logging
import pytest

from ..solver_console import SolverConsole
from ..utils import init_logger
from ..constants import PROJECT_HOME_DIR

_console = SolverConsole()

logger = logging.getLogger(__name__)


@pytest.fixture
def console() -> SolverConsole:
  return SolverConsole()


# noinspection PyUnusedLocal
@pytest.hookimpl
def pytest_configure(config: pytest.Config):
  print()

  if not PROJECT_HOME_DIR.exists():
    PROJECT_HOME_DIR.mkdir(parents=True)

  init_logger(
    console=_console,
    level=logging.DEBUG,
    handler_level=logging.DEBUG,
    force=True,
  )
  # Route hypercorn.error logs to __main__ logger
  logging.getLogger("hypercorn.error")._log = logger._log
  logging.getLogger('faker').setLevel(logging.WARNING)
  # logging.getLogger("werkzeug").setLevel(logging.WARNING) # flask
