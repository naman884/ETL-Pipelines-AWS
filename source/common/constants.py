## File to store constants ##

from enum import Enum

# supported file types for S3BucketConnector
class S3FileTypes(Enum):
    CSV = 'csv'
    PARQUET = 'parquet'

# formation for MetaProcess class
class MetaProcessFormat(Enum):
    META_DATE_FORMAT = '%Y-%m-%d'
    META_PROCESS_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'
    META_SOURCE_DATE_COL = 'source_date'
    META_PROCESS_COL = 'datetime_of_processing'
    META_FILE_FORMAT = 'csv'