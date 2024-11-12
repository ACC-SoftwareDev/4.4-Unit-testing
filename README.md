# Unit Testing Assignment: Color Mixer

## 📚 Introduction

This assignment focuses on unit testing using pytest. You'll implement a ColorMixer class that handles color mixing and matching operations. The class will work with a simulated light mixing system to achieve target colors.

## 🎯 Objectives

By the end of this assignment, you should be able to:

1. Understand color mixing and matching concepts
2. Implement algorithms to match target colors using light intensities
3. Write and use unit tests with pytest
4. Debug code based on test results

## 🛠️ Setup

1. Ensure you have Python installed in your environment
2. Install required packages: `pip install -r requirements.txt`
3. Verify pytest is installed: `pytest --version`

## 📝 Instructions

### Step 1: Understand the Requirements

1. Review `test_color_mixer.py` to understand the test requirements
2. The main tasks are:
   - Match basic colors (Red, Green, Blue)
   - Match mixed colors (Gray, Yellow, Purple)
   - Handle edge cases (Black, White)
   - Implement color manipulation functions

### Step 2: Implement the ColorMixer Class

Open `color_mixer.py` and implement these methods:

1. `match_color(target_color)`:
   - Input: List of 3 integers (0-255) representing RGB values
   - Output: List of 3 float values (0-1) representing light intensities
   - Example: match_color([255, 0, 0]) returns intensities for red
   - Must ensure all intensities are between 0 and 1

2. `mix_colors(color1, color2)`:
   - Input: Two RGB color tuples
   - Output: Mixed color as RGB tuple
   - Example: mix_colors((255, 0, 0), (0, 0, 255)) returns purple

3. `lighten_color(color, amount)`:
   - Input: RGB color tuple and amount (0-1)
   - Output: Lightened color
   - Must validate amount is between 0 and 1

4. `darken_color(color, amount)`:
   - Input: RGB color tuple and amount (0-1)
   - Output: Darkened color
   - Must validate amount is between 0 and 1

### Step 3: Test Your Implementation

1. Run the tests: `pytest test_color_mixer.py`
2. Tests will check:
   - Basic color matching (error < 70)
   - Mixed color matching (error < 105)
   - Edge case handling
   - Color manipulation functions
3. Fix any failures and rerun tests
4. Continue until all tests pass

## 🧪 Testing Criteria

Your implementation should:
1. Match basic colors with error < 70
2. Match mixed colors with error < 105
3. Handle edge cases appropriately
4. Implement color manipulation correctly
5. Keep all light intensities between 0 and 1

## 💡 Tips

- Start with the `match_color` method as it's the most important
- Use the MockLightMixer class to test your color matching
- Remember to handle edge cases
- Use numpy for efficient calculations
- Test incrementally as you implement each feature

## 🆘 Getting Help

If you encounter issues:

1. Review the test file to understand what's expected
2. Check the MockLightMixer implementation for hints
3. Look at the error messages from pytest
4. Ask for clarification if needed

Good luck! 🎨✨
