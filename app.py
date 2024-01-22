from flask import Flask , request , render_template , jsonify
import socket

app = Flask(__name__)

@app.route('/')
def displayformpage():
    return render_template('portscanner.html')

def scanport(addresstoscan, portnumber):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((addresstoscan, portnumber))
        return f"<li> Port {portnumber} open. </li>"
    except:
        return f"<li> Port {portnumber} not open. </li>"
    finally:
        sock.close()

@app.route('/scantheaddress', methods=['POST'])
def theportscanner():
    if request.method == 'POST':
        address = request.json.get('address')  
        ports = [11 , 20 , 21 , 22 , 23 , 24 , 27 , 29 , 31 , 35 , 39 , 48 , 49 , 50 , 53 , 56 , 57 , 59 , 65 , 66 , 67 , 69 , 71 , 72 , 74 , 75 , 80 , 93 , 115 , 110 , 143 , 443 , 8080 , 3306]
        results = []

        for port in ports:
            result = scanport(address, port)
            results.append(result)

        return jsonify(results)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


























