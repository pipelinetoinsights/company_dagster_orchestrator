import dlt
from dagster import AssetExecutionContext, asset, get_dagster_logger
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from .seveneleven_pipeline import fuel_price_source

@dlt_assets(
    dlt_source=fuel_price_source(),
    dlt_pipeline=dlt.pipeline(
        pipeline_name="seven_eleven",
        dataset_name="seven_eleven_data",
        destination="postgres",
        progress="log"
    ),
    name="seven_eleven_data_ingestion",
    group_name="seven_eleven",
)
def seven_eleven_data_asset(context: AssetExecutionContext, dlt: DagsterDltResource):
    logger = get_dagster_logger()
    logger.info("Starting DLT pipeline execution")