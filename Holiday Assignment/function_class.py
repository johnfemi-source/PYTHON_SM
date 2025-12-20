import unittest


def temperature_advisory(temp, unit='C', threshold=30):
    """
    Convert temperature to opposite unit and check against threshold.
    
    Args:
        temp (float): Temperature value
        unit (str): 'C' for Celsius or 'F' for Fahrenheit (default: 'C')
        threshold (float): Threshold value for heat advisory (default: 30)
    
    Returns:
        str: "Cold advisory" if below threshold, "Heat alert" if at or above
    """
    
    if unit == 'C':
       
        converted_temp = (temp * 9/5) + 32
    elif unit == 'F':
        
        converted_temp = (temp - 32) * 5/9
    else:
        raise ValueError("Unit must be 'C' or 'F'")
    
 
    if converted_temp < threshold:
        return "Cold advisory"
    else:
        return "Heat alert"


class TestTemperatureAdvisory(unittest.TestCase):
    """Test suite for temperature_advisory function using TDD"""
    
    def test_celsius_to_fahrenheit_conversion_accuracy(self):
        """Test accurate conversion from Celsius to Fahrenheit"""
        
        result = temperature_advisory(0, 'C', threshold=32)
        self.assertEqual(result, "Heat alert")
       
        result = temperature_advisory(100, 'C', threshold=212)
        self.assertEqual(result, "Heat alert")
        
        result = temperature_advisory(-40, 'C', threshold=-40)
        self.assertEqual(result, "Heat alert")
    
    def test_fahrenheit_to_celsius_conversion_accuracy(self):
        """Test accurate conversion from Fahrenheit to Celsius"""
      
        result = temperature_advisory(32, 'F', threshold=0)
        self.assertEqual(result, "Heat alert")
     
        result = temperature_advisory(212, 'F', threshold=100)
        self.assertEqual(result, "Heat alert")
        
      
        result = temperature_advisory(-40, 'F', threshold=-40)
        self.assertEqual(result, "Heat alert")
    
    def test_cold_advisory_celsius_input(self):
        """Test cold advisory with Celsius input"""
       
        result = temperature_advisory(10, 'C', threshold=60)
        self.assertEqual(result, "Cold advisory")
        
     
        result = temperature_advisory(-10, 'C', threshold=32)
        self.assertEqual(result, "Cold advisory")
    
    def test_heat_alert_celsius_input(self):
        """Test heat alert with Celsius input"""
        
        result = temperature_advisory(30, 'C', threshold=80)
        self.assertEqual(result, "Heat alert")
        
       
        result = temperature_advisory(40, 'C', threshold=100)
        self.assertEqual(result, "Heat alert")
    
    def test_cold_advisory_fahrenheit_input(self):
        """Test cold advisory with Fahrenheit input"""
       
        result = temperature_advisory(50, 'F', threshold=15)
        self.assertEqual(result, "Cold advisory")
        
       
        result = temperature_advisory(32, 'F', threshold=5)
        self.assertEqual(result, "Cold advisory")
    
    def test_heat_alert_fahrenheit_input(self):
        """Test heat alert with Fahrenheit input"""
        
        result = temperature_advisory(86, 'F', threshold=25)
        self.assertEqual(result, "Heat alert")
        
        result = temperature_advisory(104, 'F', threshold=35)
        self.assertEqual(result, "Heat alert")
    
    def test_threshold_boundary_exactly_at_threshold(self):
        """Test behavior when converted temp equals threshold"""
       
        result = temperature_advisory(0, 'C', threshold=32)
        self.assertEqual(result, "Heat alert")
        
        
        result = temperature_advisory(68, 'F', threshold=20)
        self.assertEqual(result, "Heat alert")
    
    def test_default_unit_celsius(self):
        """Test that default unit is Celsius"""
       
        result = temperature_advisory(25, threshold=80)
       
        self.assertEqual(result, "Cold advisory")
    
    def test_default_threshold_value(self):
        """Test default threshold of 30"""
      
        result = temperature_advisory(10, 'C')
        self.assertEqual(result, "Heat alert")
        
     
        result = temperature_advisory(-1, 'C')
        self.assertEqual(result, "Heat alert")
        
        
        result = temperature_advisory(-2, 'C')
        self.assertEqual(result, "Cold advisory")
    
    def test_invalid_unit(self):
        """Test that invalid unit raises ValueError"""
        with self.assertRaises(ValueError):
            temperature_advisory(25, 'K', threshold=80)
        
        with self.assertRaises(ValueError):
            temperature_advisory(25, 'X', threshold=80)
    
    def test_decimal_temperatures(self):
        """Test with decimal temperature values"""

        result = temperature_advisory(25.5, 'C', threshold=78)
        self.assertEqual(result, "Cold advisory")
     
        result = temperature_advisory(98.6, 'F', threshold=37)
        self.assertEqual(result, "Heat alert")
    
    def test_negative_temperatures(self):
        """Test with negative temperature values"""
        
        result = temperature_advisory(-20, 'C', threshold=0)
        self.assertEqual(result, "Cold advisory")
        
        result = temperature_advisory(-4, 'F', threshold=-15)
        self.assertEqual(result, "Cold advisory")


if __name__ == '__main__':
    
    print("Running Temperature Advisory TDD Test Suite")
    print("=" * 60)
    unittest.main(verbosity=2)
