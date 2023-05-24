
from flask import Flask, render_template, request, jsonify, send_file
# import boto3
import json
# # import L4Emodule as L4E
# import re
from flask_cors import CORS
import config
# import awswrangler as wr
import pandas as pd
import joblib
import numpy as np


invalid_method_call_message = {'message': 'Invalid method called'}
success_message = config.success_message
failed_message = config.failed_message


# current_user = boto3.client('sts').get_caller_identity().get('Account')

app = Flask(__name__)
CORS(app)

app.secret_key = "super secret key"

model_training_success_message = "Training of the model started. Please wait while the model is training."

glue_database = config.glue_database
property_data_glue_table = config.property_data_glue_table
property_data_glue_table_for_inference = config.property_data_glue_table_for_inference
meta_data_glue_table = config.meta_data_glue_table

@app.route('/api/detectAnomalies', methods=['POST'])
def detectAnomalies():
    try: 
        json_data = '''[{"Time":"2023-01-02T03:30:26.500","1_PWMS(1ST_DM)":3.3,"1_PWMS(LST_DM)":3.3,"1_REF(1ST_DM)":43.8,"1_REF(LST_DM)":44.3,"HCR7(1ST_DM)":0.0,"HCR7(LST_DM)":1.0,"MS_ATO(1ST_DM)":0.0,"MS_ATO(LST_DM)":0.0,"MS_ATP(1ST_DM)":0.0,"MS_ATP(LST_DM)":0.0,"TCI1_IMC1(1ST_DM)":0.0,"TCI1_IMC1(LST_DM)":0.0,"TCI1_IMC2(1ST_DM)":0.0,"TCI1_IMC2(LST_DM)":0.0,"TCI1_PTR(1ST_DM)":0.0,"TCI1_PTR(LST_DM)":0.0,"TCI2_IMC1(1ST_DM)":0.0,"TCI2_IMC1(LST_DM)":0.0,"TCI2_IMC2(1ST_DM)":0.0,"TCI2_IMC2(LST_DM)":0.0,"TCI2_PTR(1ST_DM)":0.0,"TCI2_PTR(LST_DM)":0.0,"TL_BRK1(1ST_DM)":1.0,"TL_BRK1(LST_DM)":1.0,"TL_MTR1(1ST_DM)":0.0,"TL_MTR1(LST_DM)":0.0,"TPA_CS(1ST_DM)":0.0,"TPA_CS(LST_DM)":0.0,"TPA_NS(1ST_DM)":0.0,"TPA_NS(LST_DM)":0.0,"TVO_ACTUAL(1ST_DM)":0.0,"TVO_ACTUAL(LST_DM)":0.0}]'''
        content = request.json
        # modelName = content['modelName']
        # assetPropertyIdList = json.loads(content['assetPropertyIdList'])
        # print(assetPropertyIdList)
        # Convert JSON to DataFrame
        df_new = pd.read_json(json_data)
        df_new = df_new.set_index('Time')
        # Print the DataFrame
        print(df_new)
        #Load the saved model
        loaded_model = joblib.load('isolation_forest_model.joblib')
        # Predict on new data
        new_results = loaded_model.predict(df_new)
        print(new_results)
        new_anomalies = np.where(new_results == -1)[0]
        print("Number of anomalies detected in data:", len(new_anomalies))
        dictToReturn = {'status': 'SUCCESS',
                            'data': jsonify(content), 'message': ''}
        return jsonify(dictToReturn)
    except Exception as error:
        print('An exception occurred', str(error))
        dictToReturn = {'status': 'FAILED', 'message': str(error)}
        return jsonify(dictToReturn)


    
    
@app.route('/')
def home():
    return render_template('LforE.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('LforE.html')


if __name__ == '__main__':
    # app.run(host ='0.0.0.0', port = 5001, debug = True)
    app.run(host='0.0.0.0', port=5001, debug=False)
    # http_server = WSGIServer(("localhost", 5001), app)
    # http_server.serve_forever()
