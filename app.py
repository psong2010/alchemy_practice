import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    twelve_months = dt.date(2017, 8 ,23) - dt.timedelta(days=365)
    precip_data = dict(session.query(measurement.date, measurement.tobs).\
                       filter(measurement.date >= twelve_months).all()
    return jsonify(precip_data)

@app.route("/api/v1.0/station")
def station():
    station_data = session.query(station.station).all()
    stations = list(np.ravel(station_data))
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs()
    tobs_data = session.query(measurement.tobs).\
                filter(measurement.date >= twelve_months).all()
    tobs = list(np.ravel(tobs_data))
    return jsonify(tobs)

@app.route("/api/v1.0/temp/<start>")
def start(start):
    data = engine.execute("select max(tobs), min(tobs), avg(tobs).\ 
                            from measurement.\ 
                            where date >= {start}")
    titles = ('TMAX', 'TMIN', 'TAVG')
    dic = {}
    for i in x:
        tup = i
        break
    for a,b in zip(y,tup):
        dic[a]=b
    
    return jsonify(dic)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    x = engine.execute("select max(tobs), min(tobs), avg(tobs) from measurement where date >= '{0}' and date <= '{1}'".format(start,end))
    y = ('TMAX','TMIN','TAVG')
    dic = {}
    for i in x:
        tup = i
        break
    for a,b in zip(y,tup):
        dic[a]=b
    
    return jsonify(dic)


if __name__ == '__main__':
    app.run(debug=True)