# Unit Testing Assignment: Color Mixer

## 📚 Introduction

This assignment focuses on unit testing using pytest. You'll implement a ColorMixer class that handles RGB color operations, and use unit tests to verify your implementation. Each RGB color is represented as a tuple of three integers (R, G, B), where each value ranges from 0 to 255.

## 🎯 Objectives

By the end of this assignment, you should be able to:

1. Explain the purpose of unit tests
2. Write unit tests using pytest
3. Run and interpret unit test results
4. Debug code based on test results
5. Understand and apply test-driven development principles

## 🛠️ Setup

1. Ensure you have Python installed in your environment
2. Install pytest by running: `pip install pytest` in your terminal
3. Verify pytest is installed by running: `pytest --version`
4. Open the `color_mixer.py` file in your preferred IDE or text editor

## 📝 Instructions

### Step 1: Understand the Requirements

1. Open and review `test_color_mixer.py`
2. Each test function shows example inputs and expected outputs:
   - `test_mix_colors`: Shows how two colors should be combined
   - `test_lighten_color`: Shows how colors should be made brighter
   - `test_darken_color`: Shows how colors should be made darker
   - `test_invalid_inputs`: Shows how invalid inputs should be handled

### Step 2: Implement the ColorMixer Class

Open `color_mixer.py` and implement these three methods:

1. `mix_colors(color1, color2)`:
   - Input: Two RGB color tuples, e.g., (255, 0, 0) for red
   - Output: A new RGB color tuple
   - Example: mix_colors((255, 0, 0), (0, 255, 0)) returns (255, 255, 0)
   - Must raise ValueError if any RGB value is outside 0-255 range

2. `lighten_color(color, amount)`:
   - Input: RGB color tuple and amount (float between 0 and 1)
   - Output: Lightened RGB color tuple
   - Example: lighten_color((100, 100, 100), 0.5) returns (178, 178, 178)
   - Must raise ValueError if amount is not between 0 and 1

3. `darken_color(color, amount)`:
   - Input: RGB color tuple and amount (float between 0 and 1)
   - Output: Darkened RGB color tuple
   - Example: darken_color((200, 200, 200), 0.5) returns (100, 100, 100)
   - Must raise ValueError if amount is not between 0 and 1

### Step 3: Test Your Implementation

1. Open a terminal in your project directory
2. Run the tests using: `pytest test_color_mixer.py`
3. If tests fail, you'll see:
   - Which test failed
   - Expected vs actual output
   - Location of the failure
4. Fix any failures and run tests again
5. Repeat until all tests pass

### Step 4: Add Your Own Test

1. Think of a new test case, for example:
   - Mixing two identical colors
   - Lightening a very dark color
   - Darkening a very light color
   
2. Add your test to `test_color_mixer.py`:

## 🧪 Testing

The `test_color_mixer.py` file contains tests for each method in the ColorMixer class. These tests check both the correctness of your implementation and handle invalid inputs.

To run the tests:
1. Open a terminal in your project directory
2. Run the command: `pytest test_color_mixer.py`
3. Review the test results in the terminal output

## 📈 Completion Criteria

You've completed the assignment when:

1. All methods in the ColorMixer class are correctly implemented.
2. All tests in `test_color_mixer.py` pass when you run `pytest test_color_mixer.py`.
3. You've added at least one new test and corresponding functionality using the Test-Driven Development approach.

## 💡 Tips

- Start by implementing the simplest functionality that could work.
- Use the test results to guide your implementation.
- Remember to handle edge cases and invalid inputs.
- Don't hesitate to add more tests if you think of additional scenarios to cover.

## 🆘 Getting Help

If you encounter any issues or have questions:

1. Review this README file and the comments in `color_mixer.py` carefully.
2. Check the pytest documentation for guidance on writing and running tests.

Good luck, and happy testing! 🧪🔬
