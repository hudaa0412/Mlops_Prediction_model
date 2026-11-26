from src.logger import logger
from src.data_ingestion import data_ingestion


def main():
    #Step 1 : Data Ingestion
    df = data_ingestion()
    

main()
