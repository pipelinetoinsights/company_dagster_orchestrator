from datetime import datetime
import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

# Define the Bluesky posts resource
@dlt.source
def bluesky_posts_source():
    # Define RESTAPIConfig for Bluesky API
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.bsky.app/xrpc/"},
        "resources": [
            {
                "name": "posts",
                "endpoint": {
                    "path": "app.bsky.feed.searchPosts",
                    "params": {
                        "q": "petrol price australia",  # Search term
                        "sort": "latest",
                        "since": {
                            "type": "incremental",
                            "cursor_path": "created_at",
                            "initial_value": datetime.utcnow().isoformat() + "Z",
                        },
                        "until": datetime.utcnow().isoformat() + "Z",
                        "tag": ["PetrolPrice", "FuelPrice"],
                        "limit": 100,
                    },
                },
            },
        ],
    }

    # Generate resources using RESTAPIConfig
    yield from rest_api_resources(config)

# Create and configure the pipeline
#pipeline = dlt.pipeline(
      #  pipeline_name="bluesky_api",
      #  destination="postgres",
      #  dataset_name="bluesky_data" )

# Run the pipeline
#load_info = pipeline.run(blusky_source())
#print(load_info)