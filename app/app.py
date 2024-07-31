from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sql = SQLHelper()

#################################################
# Flask Routes
#################################################


# SQL Queries
@app.route("/api/v1.0/get_dashboard/<min_attempts>/<region>")
def get_dashboard(min_attempts, region):
    bar_data = sql.get_bar(min_attempts, region)
    pie_data = sql.get_pie(min_attempts, region)
    table_data = sql.get_table(min_attempts, region)

    data = {
        "bar_data": bar_data,
        "pie_data": pie_data,
        "table_data": table_data
    }
    return(jsonify(data))

@app.route("/api/v1.0/get_map/<min_attempts>/<region>")
def get_map(min_attempts, region):
    map_data = sql.get_map(min_attempts, region)

    return(jsonify(map_data))



# Run the App
if __name__ == '__main__':
    app.run(debug=True)