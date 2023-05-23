# Update the name of the bucket you want to use
# to store the intermediate results of this getting
# started:

BUCKET                   = 'lookout4equipment32334'

# You can leave these other parameters to these
# default values:

PREFIX_TRAINING          = 'model/training-data/'
PREFIX_LABEL             = 'model/label-data/'
PREFIX_INFERENCE         = 'model/inference-data'
DATASET_NAME             = 'l4etest'#'demonstration'
MODEL_NAME               = f'{DATASET_NAME}-testmodel'
INFERENCE_SCHEDULER_NAME = f'{DATASET_NAME}-testscheduler'
MIN_TRAINING_DAY         = 130
MINUTES_IN_A_DAY         = 1440
PARAMETER_STORE_ROLE_NAME= 'execute-lookout-for-equipment-role'
MODEL_TRAINING_LOG_GROUP_NAME           = 'TrainModelLogs'

glue_database = 'meghaai_firehose_glue_database'
property_data_glue_table = 'meghaai_firehose_glue_table'
property_data_glue_table_for_inference = 'meghaai_firehose_glue_tableasset_property_updates'
meta_data_glue_table = 'meghaai_firehose_glue_table_metadata'

success_message = "SUCCESS"
failed_message = "FAILED"
LOG_TAG = {
    "Error": 'Error:',
    "ShowInUI": 'ShowInUI:',
    "Info": 'Info:'
}