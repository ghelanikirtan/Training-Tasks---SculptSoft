from typing import List, Dict, Optional

from src.app.pipelines.etl import ETLPipeline


pipeline = ETLPipeline()

pipeline.invoke(pagesize=5000)


