import pytest
from src.mock_light_mixer import MockLightMixer
from color_mixer import ColorMixer

@pytest.fixture
def setup():
    mixer = MockLightMixer()
    color_mixer = ColorMixer()
    return mixer, color_mixer

def test_basic_colors(setup):
    """Test if basic colors (RGB) are matched correctly"""
    mixer, color_mixer = setup
    test_colors = [
        [255, 0, 0],    # Red
        [0, 255, 0],    # Green
        [0, 0, 255],    # Blue
    ]
    
    for target_color in test_colors:
        intensities = color_mixer.match_color(target_color)
        result = mixer.get_mixed_color(intensities)
        error = max(abs(target_color[i] - result[i]) for i in range(3))
        assert error < 70, f"Color matching error too large for {target_color}"

def test_mixed_colors(setup):
    """Test if mixed colors are matched correctly"""
    mixer, color_mixer = setup
    test_colors = [
        [128, 128, 128],  # Gray
        [255, 255, 0],    # Yellow
        [255, 0, 255],    # Purple
    ]
    
    for target_color in test_colors:
        intensities = color_mixer.match_color(target_color)
        result = mixer.get_mixed_color(intensities)
        error = max(abs(target_color[i] - result[i]) for i in range(3))
        assert error < 105, f"Mixed color matching failed for {target_color}"

def test_edge_cases(setup):
    """Test edge cases like black, white, and near-black colors"""
    mixer, color_mixer = setup
    edge_cases = [
        [0, 0, 0],        # Black
        [255, 255, 255],  # White
        [1, 1, 1],        # Near black
    ]
    
    for target_color in edge_cases:
        intensities = color_mixer.match_color(target_color)
        result = mixer.get_mixed_color(intensities)
        error = max(abs(target_color[i] - result[i]) for i in range(3))
        assert error < 70, f"Edge case handling failed for {target_color}"

def test_intensity_range(setup):
    """Test if output intensities are within valid range [0, 1]"""
    _, color_mixer = setup
    test_colors = [
        [128, 128, 128],
        [255, 0, 0],
        [0, 255, 255]
    ]
    
    for target_color in test_colors:
        intensities = color_mixer.match_color(target_color)
        for intensity in intensities:
            assert 0 <= intensity <= 1, f"Invalid intensity value: {intensity}"

def test_mix_colors():
    """Test color mixing functionality"""
    mixer = ColorMixer()
    
    # Test basic color mixing
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = mixer.mix_colors(red, blue)
    assert purple == (127, 0, 127), "Red + Blue should make Purple"
    
    # Test mixing with white
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = mixer.mix_colors(black, white)
    assert gray == (127, 127, 127), "Black + White should make Gray"

def test_lighten_color():
    """Test color lightening functionality"""
    mixer = ColorMixer()
    
    # Test lightening red
    red = (255, 0, 0)
    pink = mixer.lighten_color(red, 0.5)
    assert pink[0] == 255 and pink[1] > 0 and pink[2] > 0, "Lightened red should be pink"
    
    # Test full lightening
    black = (0, 0, 0)
    white = mixer.lighten_color(black, 1.0)
    assert white == (255, 255, 255), "Fully lightened black should be white"

def test_darken_color():
    """Test color darkening functionality"""
    mixer = ColorMixer()
    
    # Test darkening yellow
    yellow = (255, 255, 0)
    dark_yellow = mixer.darken_color(yellow, 0.5)
    assert all(x < 255 for x in dark_yellow), "Darkened yellow should have lower values"
    
    # Test full darkening
    white = (255, 255, 255)
    black = mixer.darken_color(white, 1.0)
    assert black == (0, 0, 0), "Fully darkened white should be black"

def test_invalid_amounts():
    """Test error handling for invalid amounts"""
    mixer = ColorMixer()
    color = (100, 100, 100)
    
    with pytest.raises(ValueError):
        mixer.lighten_color(color, 1.5)
    
    with pytest.raises(ValueError):
        mixer.darken_color(color, -0.1)
