from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

hex_map = "0123456789ABCDEF"

def convert_number(number: str, from_base: int, to_base: int) -> str:
    """Converts a number from one base to another (from base 2 to 16)."""
    decimal_number = int(number, from_base)

    def decimal_to_base(n, base):
        """Helper function to convert a decimal number to any base between 2 and 16."""
        if n == 0:
            return "0"
        result = ""
        while n > 0:
            result = hex_map[n % base] + result
            n //= base
        return result

    return decimal_to_base(decimal_number, to_base)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    number = data.get('number')
    from_base = data.get('from_base')
    to_base = data.get('to_base')

    # Validate base inputs
    if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):
        return jsonify({"error": "Invalid base. Please enter a base between 2 and 16."}), 400

    # Perform conversion
    result = convert_number(number.upper(), from_base, to_base)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
