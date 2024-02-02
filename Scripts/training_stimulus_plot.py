import matplotlib.pyplot as plt

# Sample data for a week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Random sample data for Training Stimulus (Intensity and Volume) for Lifting and Running
lifting_intensity = [20, 25, 30, 22, 27, 31, 26]
lifting_volume = [40, 45, 50, 42, 47, 55, 44]
running_intensity = [15, 18, 22, 16, 20, 25, 19]
running_volume = [35, 38, 45, 32, 40, 48, 36]

# Creating the plot
plt.figure(figsize=(12,8))

# Plotting Lifting data
plt.plot(days, lifting_intensity, label='Lifting Intensity', marker='o', color='darkred', linestyle='--')
plt.plot(days, lifting_volume, label='Lifting Volume', marker='o', color='navy', linestyle='-.')

# Plotting Running data
plt.plot(days, running_intensity, label='Running Intensity', marker='o', color='darkgreen', linestyle='--')
plt.plot(days, running_volume, label='Running Volume', marker='o', color='purple', linestyle='-.')

# Adding titles and labels
plt.title('Training Stimulus Over the Week', fontsize=16, fontweight='bold')
plt.xlabel('Days of the Week', fontsize=14)
plt.ylabel('Training Stimulus', fontsize=14)
plt.legend()

# Display the chart
plt.grid(True)
plt.show()
