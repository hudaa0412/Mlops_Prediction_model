import pandas as pd

from src.logger import logger

def data_ingestion():
    try:
        logger.info('Data Ingestion Started........')
        '''
        * Problem statement
        * Independent columns(X):'record_id', 'timestamp', 'mine_id', 'conveyor_id', 'idler_id',
       'vibration_rms', 'vibration_peak', 'vibration_kurtosis',
       'vibration_crest_factor', 'bpfo_amplitude', 'bpfi_amplitude',
       'bsf_amplitude', 'ftf_amplitude', 'bearing_temperature',
       'acoustic_level', 'rotational_speed', 'ambient_temperature', 'humidity',
       'dust_concentration', 'moisture_level', 'operating_hours',
       'conveyor_load', 'belt_speed', 'motor_current', 'lubrication_age_hours',
       'last_maintenance_hours', 'previous_failure_count',
       'seal_condition_score', 'bearing_age_months',
        * Target column (y): 'failure_within_7_days'
        '''
        df = pd.read_csv(r'C:\Mlops_Prediction_model\data\raw\preventative_maintainance_dataset.csv')
        logger.info(f'Data Ingestion Completed Successfully with {df.shape}')
        logger.info(f'Dataset Coulumns ... {df.columns}')
        return df
    
    except FileNotFoundError as e:
        logger.exception('Execption Occurs ....{e}')
        raise

