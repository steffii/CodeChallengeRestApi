from flask import Flask, jsonify, abort
from resources.ComplaintsScrapper import ComplaintsScrapper

app=Flask(__name__)

cs=ComplaintsScrapper()
complaints=ComplaintsScrapper.all_complaints(cs)

@app.route('/',methods=['GET'])
def get_complaints():
    return jsonify({'complaints':complaints})

@app.route('/<int:areacode>',methods=['GET'])
def get_area_complaints(areacode):
    area_complaints=[complaint for complaint in complaints if complaint['area code']==areacode]
    if len(area_complaints)==0:
        abort(404)
    return jsonify({'complaints':area_complaints})


if __name__=='__main__':
    app.run()
