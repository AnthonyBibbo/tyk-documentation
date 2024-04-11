from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/authenticated', methods=['GET'])
def authenticated():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header == 'Basic am9obkBzbWl0aC5jb206MTIzNDU2Nw==':  # Replace 
        return Response('Authenticated', status=200)
    else:
        return Response('Unauthorized', status=401)

if __name__ == '__main__':
    app.run(debug=True)
