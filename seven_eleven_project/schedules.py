import dagster as dg

seveneleven_daily_refresh_job = dg.define_asset_job(
    "daily_refresh", 
    selection=dg.AssetSelection.all()
)

daily_schedule = dg.ScheduleDefinition(
    job=seveneleven_daily_refresh_job,
    name="seveneleven_job",
    cron_schedule="0 8 * * 4",  # Runs every day at 6 PM
    execution_timezone="Australia/Melbourne",  
)

