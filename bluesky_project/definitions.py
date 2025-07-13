from bluesky_project import assets
from dagster import Definitions, load_assets_from_modules
from dagster_embedded_elt.dlt import DagsterDltResource

#from im_open_jobs.schedules import daily_schedule
from bluesky_project.schedules import weekly_schedule

dlt_resource = DagsterDltResource()
all_assets = load_assets_from_modules([assets])

blusky_defs = Definitions(
    assets=all_assets,
    resources={
        "dlt": dlt_resource,
    },
    schedules=[weekly_schedule],
)