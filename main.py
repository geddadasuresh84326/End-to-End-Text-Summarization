from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"{'*'*10} {STAGE_NAME} started {'*'*10}")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{'*'*10} {STAGE_NAME} completed    {'*'*10}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"{'*'*10} {STAGE_NAME} started {'*'*10}")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{'*'*10} {STAGE_NAME} completed    {'*'*10}")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"{'*'*10} {STAGE_NAME} started {'*'*10}")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{'*'*10} {STAGE_NAME} completed    {'*'*10}")
except Exception as e:
    logger.exception(e)
    raise e