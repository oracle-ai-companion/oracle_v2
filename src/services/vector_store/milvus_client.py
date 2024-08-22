from pymilvus import connections, Collection, utility
from src.config import MILVUS_HOST, MILVUS_PORT, MILVUS_USER, MILVUS_PASSWORD
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class MilvusClient:
    def __init__(self):
        self.connection = None
        self.alias = "default"

    def connect(self):
        try:
            self.connection = connections.connect(
                alias=self.alias,
                host=MILVUS_HOST,
                port=MILVUS_PORT,
                user=MILVUS_USER,
                password=MILVUS_PASSWORD
            )
            logger.info(f"Successfully connected to Milvus server at {MILVUS_HOST}:{MILVUS_PORT}")
        except Exception as e:
            logger.error(f"Failed to connect to Milvus server: {str(e)}")
            raise

    def disconnect(self):
        if self.connection:
            try:
                connections.disconnect(self.alias)
                logger.info("Successfully disconnected from Milvus server")
            except Exception as e:
                logger.error(f"Failed to disconnect from Milvus server: {str(e)}")

    def get_collection(self, collection_name):
        try:
            return Collection(collection_name)
        except Exception as e:
            logger.error(f"Failed to get collection {collection_name}: {str(e)}")
            raise

    def list_collections(self):
        try:
            return utility.list_collections()
        except Exception as e:
            logger.error(f"Failed to list collections: {str(e)}")
            raise

    def has_collection(self, collection_name):
        try:
            return utility.has_collection(collection_name)
        except Exception as e:
            logger.error(f"Failed to check if collection {collection_name} exists: {str(e)}")
            raise