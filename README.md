# Modular ETL Architecture

A flexible, configuration-driven ETL (Extract, Transform, Load) framework built in Python that allows you to create data pipelines through simple YAML configuration files.

The goal was to highlight key patterns (e.g., modularity, plugin-based ingestion, and configuration-driven design) under time constraints of 2-4h as per task specification.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Poetry (for dependency management)

### Installation

1. **Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd modular-etl-architecture
   ```

3. **Install dependencies:**
   ```bash
   poetry install
   ```

### Running the ETL

```bash
# Run with a configuration file
poetry run python main.py --config configurations/dummy_mongo/dummy_mongo_bulk.yml
```

## 🛠️ How the Template Works

### Core Architecture

The ETL framework consists of two main components:

1. **ComponentFactory**: Handles dynamic importing and instantiation of components
2. **ETL**: Main orchestrator that manages the entire pipeline

### Configuration Structure

ETL pipelines are defined using YAML configuration files with the following structure:

```yaml
etl_name: my_pipeline
components:
  extractor:
    location: plugins.extractors.mongo.MongoBatchExtractor
    parameters:
      uri: mongodb://localhost:27017/
      database: my_db
      collection: my_collection
    components:
      validator:
        location: plugins.validators.model_validator.ModelValidator
        parameters:
          model: entities.models.my_model.MyModel
  loader:
    location: plugins.loaders.s3_loader.S3Loader
    parameters:
      destination: s3://my-bucket/data/
      batch_size: 1000
      format: parquet
    components:
      error_handler:
        location: plugins.error_handlers.simple_handler.SimpleHandlerPlugin
```

### Component Hierarchy

- **Top-level components**: `extractor` and `loader` (`transformer` or others can be added on demand)
- **Sub-components**: Can be nested within any component (e.g., `validator` within `extractor`)
- **Parameters**: Passed to component constructors
- **Dynamic imports**: Components are imported at runtime based on the `location` string

### Key Features

- **Dynamic Component Loading**: Components are imported and instantiated at runtime
- **Nested Components**: Support for sub-components with automatic attribute assignment
- **Error Handling**: Comprehensive error handling and logging
- **Flexible Configuration**: Support for both YAML files and Python dictionaries

## 🔧 Adding New Flows

### 1. Create a New Configuration File

Create a new YAML file in the `configs/` directory:

```yaml
# configurations/my_new_flow/my_new_flow.yml
etl_name: my_new_flow
components:
  extractor:
    location: plugins.extractors.api.APIExtractor
    parameters:
      base_url: https://api.example.com
      endpoints: ["/users", "/orders"]
      headers:
        Authorization: "Bearer token123"
    components:
      rate_limiter:
        location: plugins.rate_limiters.token_bucket.TokenBucketLimiter
        parameters:
          requests_per_second: 10
  transformer:
    location: plugins.transformers.json_transformer.JSONTransformer
    parameters:
      transformations:
        - flatten_nested_objects
        - normalize_dates
  loader:
    location: plugins.loaders.postgres_loader.PostgresLoader
    parameters:
      connection_string: postgresql://user:pass@localhost/db
      table_name: processed_data
      batch_size: 500
```

### 2. Create Required Plugin Components

If your flow needs new components, create them in the appropriate plugin directory:

```python
# plugins/extractors/api.py
class APIExtractor:
    def __init__(self, base_url, endpoints, headers=None):
        self.base_url = base_url
        self.endpoints = endpoints
        self.headers = headers or {}
    
    def extract(self):
        # Implementation here
        pass
```

### 3. Run Your New Flow

```bash
poetry run python main.py --config configurations/my_new_flow/my_new_flow.yml
```
