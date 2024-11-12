import numpy as np
from src.mock_light_mixer import MockLightMixer

class ColorMixer:
    def __init__(self):
        """Initialize your variables here"""
        # TODO: Initialize the MockLightMixer and get the light matrix
        pass

    def match_color(self, target_color):
        """
        Match the target RGB color by finding appropriate light intensities.
        
        Args:
            target_color: List of 3 integers (0-255) representing RGB values
                         Example: [255, 128, 0] for orange
        
        Returns:
            List of 3 float values (0-1) representing the intensity of each light
            Example: [0.8, 0.4, 0.0]
        """
        # TODO: Implement your color matching algorithm here
        # 1. Convert target_color from 0-255 range to 0-1 range
        # 2. Use the light_matrix to find appropriate intensities
        # 3. Make sure intensities are between 0 and 1
        # 4. Return the intensities as a list
        pass

    @staticmethod
    def mix_colors(color1, color2):
        """
        Mix two colors and return the result.
        Colors should be in the format (R, G, B) where R, G, and B are integers from 0 to 255.
        """
        # TODO: Implement color mixing logic
        # 1. Mix the two colors (hint: try averaging their values)
        # 2. Make sure the result is in valid range (0-255)
        pass

    @staticmethod
    def lighten_color(color, amount):
        """
        Lighten a color by a certain amount.
        Color should be in the format (R, G, B) where R, G, and B are integers from 0 to 255.
        Amount should be a float between 0 and 1.
        """
        # TODO: Implement color lightening logic
        # 1. Check if amount is between 0 and 1
        # 2. Move the color towards white by the given amount
        # 3. Make sure the result is in valid range (0-255)
        pass

    @staticmethod
    def darken_color(color, amount):
        """
        Darken a color by a certain amount.
        Color should be in the format (R, G, B) where R, G, and B are integers from 0 to 255.
        Amount should be a float between 0 and 1.
        """
        # TODO: Implement color darkening logic
        # 1. Check if amount is between 0 and 1
        # 2. Move the color towards black by the given amount
        # 3. Make sure the result is in valid range (0-255)
        pass
