import dagster as dg

bluesky_weekly_refresh_job = dg.define_asset_job(
    "weekly_refresh", 
    selection=dg.AssetSelection.all()
)

weekly_schedule = dg.ScheduleDefinition(
    job=bluesky_weekly_refresh_job,
    name="bluesky_job",
    cron_schedule="0 8 * * 5",  # Runs every day at 6 PM
    execution_timezone="Australia/Melbourne",  
)

