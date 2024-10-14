# Base Number Converter
### **Project has been deployed to production.**
### Site url -> https://multibase-number-converter-65c70b967fcd.herokuapp.com/
*IOS mobile version of application currently not working. Page loads but all request made to backend server are throwing errors*

## **Code Objective:** 
### Create a program that converts numbers between different numerical representations. The program should handle conversions between any bases from 2 to 16. The user will input a number, specify its base, and the base to which it should be converted.

## Code Explanation:
1. I created a string variable HEX_MAP to be used for mapping hexadecimal digits (base 16).
    ```
    HEX_MAP = "0123456789ABCDEF"
    ```
3. Add a dictionary for identifying number bases.
    ```
    BASE_REGEX = {
      2: re.compile(r'^[01]+$'),
      8: re.compile(r'^[0-7]+$'),
      10: re.compile(r'^[0-9]+$'),
      16: re.compile(r'^[0-9A-F]+$', re.IGNORECASE)
    }
    ```
4. Define function for converting decimal numbers to any base (2 - 16). This will be used later in another function *conver_number* so that I can have a middle value to convert all numbers from.
    ```
    def decimal_to_base(decimal_number: int, base: int) -> str:
        """Converts a decimal number to any base between 2 and 16."""
        if decimal_number == 0:
            return "0"
        result = ""
        while decimal_number > 0:
            result = HEX_MAP[decimal_number % base] + result
            decimal_number //= base
        return result
    ```
5. Create a funciton that will convert any num to a specific base to another given the to_base value, from_base value and our function for converting decimal numbers.
    ```
    def convert_number(number: str, from_base: int, to_base: int) -> str:
        """Converts a number from one base to another (from base 2 to 16)."""
        if not is_valid_for_base(number, from_base):
            raise ValueError(f"'{number}' is not a valid number in base {from_base}")
    
        try:
            decimal_number = int(number, from_base)
        except ValueError as e:
            raise ValueError(f"Invalid number '{number}' for base {from_base}. Error: {str(e)}")
    
        return decimal_to_base(decimal_number, to_base)
    ```
6. I was running into errors while attempting to convert a number from a base that was not valid for it's original state. Meaning I was attempting to convert 400 from base 2 to base 10, but int 400 is originally a base 10 number at not a base 2. To solve this error I create a function for checking if the from_base value was valid for the number given to convert.
    ```
    def is_valid_for_base(number: str, base: int) -> bool:
        """Checks if the number is valid for the given base."""
        if base in BASE_REGEX:
            return bool(BASE_REGEX[base].match(number))
        # Custom validation for bases between 2 and 16
        valid_chars = HEX_MAP[:base]
        return all(char in valid_chars for char in number.upper())
    ```
   


## Page Screenshot:
### Screenshot ------------> ![Screenshot 2024-10-13 at 6 58 11 PM](https://github.com/user-attachments/assets/620e337d-2d9a-48d7-9f16-ab499df256ea)
