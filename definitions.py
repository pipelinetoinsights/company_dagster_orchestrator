
from dagster import Definitions
from bluesky_project.definitions
from seven_eleven_project.definitions

defs = Definitions.merge(
    bluesky_project.definitions.blusky_defs,
    seven_eleven_defs.definitions.seven_eleven_defs
)