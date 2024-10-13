from multiprocessing.managers import Value
import re
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='build')
CORS(app)

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

# Serve static files from build directory
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory(app.static_folder, path)




HEX_MAP = "0123456789ABCDEF"
BASE_REGEX = {
    2: re.compile(r'^[01]+$'),
    8: re.compile(r'^[0-7]+$'),
    10: re.compile(r'^[0-9]+$'),
    16: re.compile(r'^[0-9A-F]+$', re.IGNORECASE)
}

def decimal_to_base(decimal_number: int, base: int) -> str:
    """Converts a decimal number to any base between 2 and 16."""
    if decimal_number == 0:
        return "0"
    result = ""
    while decimal_number > 0:
        result = HEX_MAP[decimal_number % base] + result
        decimal_number //= base
    return result


def is_valid_for_base(number: str, base: int) -> bool:
    """Checks if the number is valid for the given base."""
    if base in BASE_REGEX:
        return bool(BASE_REGEX[base].match(number))
    # Custom validation for bases between 2 and 16
    valid_chars = HEX_MAP[:base]
    return all(char in valid_chars for char in number.upper())


def convert_number(number: str, from_base: int, to_base: int) -> str:
    """Converts a number from one base to another (from base 2 to 16)."""
    if not is_valid_for_base(number, from_base):
        raise ValueError(f"'{number}' is not a valid number in base {from_base}")

    try:
        decimal_number = int(number, from_base)
    except ValueError as e:
        raise ValueError(f"Invalid number '{number}' for base {from_base}. Error: {str(e)}")

    return decimal_to_base(decimal_number, to_base)


@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    number = data.get('number')
    from_base = data.get('from_base')
    to_base = data.get('to_base')

    try:
        # Validate base inputs
        if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):
            return jsonify({"error": "Invalid base. Please enter a base between 2 and 16."}), 400

        # Perform conversion
        result = convert_number(number.upper(), from_base, to_base)

        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred: {}".format(error), 500


if __name__ == "__main__":
    app.run(debug=True)
