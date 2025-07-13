# Dagster Training Project

A data orchestration system built with **Dagster** and **dlt** that collects fuel price data and social media posts and stores them in PostgreSQL.
This repository is prepared by  [Pipeline To Insights](https://pipeline2insights.substack.com/)  for tutorial purposes.
## Project Overview

This project demonstrates two main data ingestion pipelines:

1. **Bluesky Social Media Posts** - Collects posts about fuel prices
2. **Seven Eleven Fuel Price Data** - Gathers fuel price information from Australian fuel stations.

## Quick Start

### Prerequisites
- Python 3.9.11 or higher
- PostgreSQL database

### Installation

1. **Clone and setup environment**
   ```bash
   git clone <repository-url>
   cd dagster_training
   

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Start Dagster UI**
   ```bash
   make start
   # or: dagster dev -w workspace.yaml
   ```

4. **Access the UI**
   
   Open `http://localhost:3000` in your browser

## Project Structure

```
company_orchestrator/ 
├── bluesky_project/  
│   ├── assets.py          # Dagster assets for bluesky_project
│   ├── pipeline.py        # Jobs / Graph definitions for bluesky_project
│   ├── schedules.py       # Schedules for bluesky_project job
│   └── definitions.py     # Wraps assets, jobs, schedules into Dagster Definitions
│
├── seven_eleven_project/ 

│   ├── assets.py          # Dagster assets for seven_eleven_project
│   ├── pipeline.py        # Jobs / Graph definitions for seven_eleven_project
│   ├── schedules.py       # Schedules for seven_eleven_project job 
│   └── definitions.py     # Wraps assets, jobs, schedules into Dagster Definitions
│
├── definitions.py         # Central Dagster Definitions (aggregates all projects)
└── workspace.yaml         # Dagster workspace file
```

## Data Pipelines

### Bluesky Pipeline
- Collects social media posts about fuel prices
- Runs weekly on Fridays at 8 AM (AEST)
- Uses incremental loading to avoid re-processing data

### Seven Eleven Pipeline
- Collects actual fuel price data from Australian stations
- Includes geographic data (latitude/longitude)
- Overwrites existing data with latest prices

## Configuration

The project uses:
- **Dagster** for orchestration
- **dlt** for data loading
- **PostgreSQL** for data storage
- **dagster-embedded-elt** for integration

## Development

```bash
# Start development server
make start
# or 
dagster dev -w workspace.yaml

# Clean generated files
make clean
```

## Learning Resources

- [Dagster Documentation](https://docs.dagster.io/)
- [DLT Documentation](https://dlthub.com/docs)
- [Project Blog Post](dagster_training_blog_post.md) - Detailed walkthrough

---
