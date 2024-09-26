
# Question 1
# Updated the Kalman Filter class to allow for multiple attributes to be recorded and measured.
# The calculation for the kalman gain also needed to be updated as the kalman gain over time should be approaching 0
# so the estimate reaches an equilibirum. The previous model didn't allow for this and didn't reach an equilibrium.
class KalmanFilter:

    def __init__(self, original_estimate,
                 estimated_measurement_error,
                 original_estimated_error=0,
                 process_variance_error=0.1):
        self.current_estimate = original_estimate
        self.all_estimates = [original_estimate]
        self.estimated_measurement_error = estimated_measurement_error
        self.current_error = original_estimated_error
        self.process_variance_error = process_variance_error
        self.cum_error = estimated_measurement_error

    def update(self, new_data):
        try:
            all_estimates = []
            for i in range(len(self.current_estimate)):
                kalman_gain = 1e-6 + self.current_error[i] / (1e-6 + self.current_error[i] + self.estimated_measurement_error[i] + self.cum_error[i])
                # print(kalman_gain, self.current_error, self.current_estimate)
                # Update estimate
                self.current_estimate[i] = self.current_estimate[i] + kalman_gain * (new_data[i] - self.current_estimate[i])
                self.current_error[i] = self.process_variance_error[i] + (1 - kalman_gain) * self.current_error[i]  # Update error
                self.cum_error[i] += self.current_error[i]  # A cumulative error term will fix this issue and allow for the estimate value to approach an equilibrium
                all_estimates.append(self.current_estimate[i])
            self.all_estimates.append(all_estimates)
            return self.current_estimate
        except:
            kalman_gain = 1e-6 + self.current_error / (1e-6 + self.current_error + self.estimated_measurement_error + self.cum_error)
            # print(kalman_gain, self.current_error, self.current_estimate)
            # Update estimate
            self.current_estimate = self.current_estimate + kalman_gain * (new_data - self.current_estimate)
            self.current_error = self.process_variance_error + (1 - kalman_gain) * self.current_error
            self.cum_error += self.current_error
            self.all_estimates.append(self.current_estimate)
            return self.current_estimate
