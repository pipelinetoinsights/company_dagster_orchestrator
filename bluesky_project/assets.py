import dlt
from dagster import AssetExecutionContext, asset, get_dagster_logger
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from .bluesky_pipeline import bluesky_posts_source

@dlt_assets(
    dlt_source=bluesky_posts_source(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="bluesky_api",
        dataset_name="bluesky_data",
        destination="postgres",
        progress="log"
    ),
    name="bluesky_data_ingestion",
    group_name="bluesky",
)
def bluesky_data_asset(context: AssetExecutionContext, dlt: DagsterDltResource):
    logger = get_dagster_logger()
    logger.info("Starting dlt pipeline execution")