import numpy as np

class MockLightMixer:
    def __init__(self):
        # Define the light characteristics matrix
        # Each row represents how a light contributes to R, G, B components
        self.light_matrix = np.array([
            [0.8, 0.2, 0.1],  # Light 1: mainly red
            [0.1, 0.9, 0.2],  # Light 2: mainly green
            [0.1, 0.2, 0.8],  # Light 3: mainly blue
        ])

    def mix_lights(self, intensities):
        """
        Mix lights according to given intensities.
        
        Args:
            intensities: List or array of 3 values between 0 and 1
                       representing the intensity of each light
        
        Returns:
            Array of RGB values representing the mixed color
        """
        # Convert intensities to numpy array if needed
        intensities = np.array(intensities)
        
        # Ensure intensities are in valid range
        if not np.all((0 <= intensities) & (intensities <= 1)):
            raise ValueError("Light intensities must be between 0 and 1")
        
        # Calculate the resulting color
        mixed_color = np.dot(intensities, self.light_matrix)
        
        # Ensure no component exceeds 1
        mixed_color = np.clip(mixed_color, 0, 1)
        
        return mixed_color

    def get_mixed_color(self, intensities):
        """
        Get the RGB color values (0-255) for given light intensities.
        
        Args:
            intensities: List or array of 3 values between 0 and 1
        
        Returns:
            List of RGB values (0-255)
        """
        # Mix the lights
        mixed_color = self.mix_lights(intensities)
        
        # Convert to 0-255 range and round to integers
        rgb_color = np.round(mixed_color * 255).astype(int)
        
        return rgb_color.tolist()
