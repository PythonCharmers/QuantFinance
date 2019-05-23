
# Question 1
class KalmanFilter:
    
    def __init__(self, original_estimate, estimated_measurement_error, original_estimated_error=0):
        self.current_estimate = original_estimate
        self.estimated_measurement_error = estimated_measurement_error
        self.current_error = original_estimated_error
        self.estimates = []
        
    def update(self, new_data):
        kalman_gain = 1e-6 + self.current_error / (1e-6 + self.current_error + self.estimated_measurement_error)
        # print(kalman_gain, self.current_error, self.current_estimate)
        # Update estimate
        self.current_estimate = self.current_estimate + kalman_gain * (new_data - self.current_estimate)
        self.current_error = (1 - kalman_gain) * self.current_error  # Update error
        self.estimates.append(self.current_estimate)
        return self.current_estimate
    
data = np.random.randn(1000) * 5 + 25
temperature_filter = KalmanFilter(30, 5, 2)

for measurement in data:
    estimated_temperature = temperature_filter.update(measurement)