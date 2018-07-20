from flask import Flask,jsonify, request

app = Flask(__name__)

#route getting every entries
@app.route('/api/v1/entries', methods=['GET'])
def get_entries():
    return jsonify({'Entries': Entries})

if __name__ == '__main__':
    app.run(debug=True)
