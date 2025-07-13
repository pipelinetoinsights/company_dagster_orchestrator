from seven_eleven_project import assets
from dagster import Definitions, load_assets_from_modules, define_asset_job, AssetSelection
from dagster_embedded_elt.dlt import DagsterDltResource

#from im_open_jobs.schedules import daily_schedule
from seven_eleven_project.schedules import daily_schedule

dlt_resource = DagsterDltResource()
all_assets = load_assets_from_modules([assets])

seven_eleven_defs = Definitions(
    assets=all_assets,
    resources={
        "dlt": dlt_resource,
    },
    schedules=[daily_schedule],
)