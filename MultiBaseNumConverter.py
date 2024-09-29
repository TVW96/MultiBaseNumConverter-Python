def convert_number(number: str, from_base: int, to_base: int) -> str:
    """Converts a number from one base to another (from base 2 to 16)."""

    # Dictionary to handle digits beyond 9 in bases greater than 10
    hex_map = "0123456789ABCDEF"

    # Step 1: Convert the input number from the original base to base 10 (decimal)
    decimal_number = int(number, from_base)

    # Step 2: Convert the base 10 number to the desired target base
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


def main():
    # Input: number, the base of the input number, and the target base
    number = input("Enter the number to convert: ")
    from_base = int(input("Enter the base of the input number (2-16): "))
    to_base = int(input("Enter the base to convert to (2-16): "))

    # Validate base inputs
    if not (2 <= from_base <= 16) or not (2 <= to_base <= 16):
        print("Invalid base. Please enter a base between 2 and 16.")
        return

    # Perform conversion
    result = convert_number(number.upper(), from_base, to_base)

    # Output the result
    print(f"The number {number} in base {from_base} is {result} in base {to_base}.")


if __name__ == "__main__":
    main()
