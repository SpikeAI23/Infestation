from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/obfuscate', methods=['POST'])
def obfuscate():
    lua_code = request.form['code']
    obfuscated_code = run_lua_obfuscator(lua_code)
    return jsonify({'obfuscated': obfuscated_code})

def run_lua_obfuscator(code):
    # Example: Running an external Lua script for obfuscation
    with open("temp.lua", "w") as temp_file:
        temp_file.write(code)
    result = subprocess.run(
        ["lua", "obfuscator/obfuscate.lua", "temp.lua"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        return f"Error: {result.stderr}"
    return result.stdout.strip()

if __name__ == '__main__':
    app.run(port=8080, debug=True)
