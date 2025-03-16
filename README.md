## Overview

Python program for Celsius <-> Fahrenheit conversion with single and range support using a specified step size.

## Features

- Convert a **single** temperature.
- Convert a **range** of temperatures with a step size.
- Supports **Celsius to Fahrenheit** and **Fahrenheit to Celsius** conversions.
- Includes **error handling** for non-numeric input and invalid choices.
- Allows the user to **continue converting** or exit the program.

## How to Use

1. **Run the script** in a Python environment.
2. Choose the conversion type:
   - `C` for Celsius to Fahrenheit
   - `F` for Fahrenheit to Celsius
   - `exit` to quit
3. Select whether to convert a **single temperature** or a **range**.
4. Enter the temperature value(s).
5. View the converted results.
6. Choose whether to continue or exit the program.

## Example Usage

```
Convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? (Type 'exit' to quit): C
Do you want to convert a single temperature or a range? (single/range): range
Enter the starting temperature: 0
Enter the ending temperature: 100
Enter the step size: 10

Temperature Conversions:
------------------------
Input Temp  |  Converted Temp
0.00°C  ->  32.00°F
10.00°C  ->  50.00°F
20.00°C  ->  68.00°F
...
Do you want to convert another temperature? (yes/no): no
Goodbye! Thanks for using the converter.
```


