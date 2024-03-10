import tkinter as tk
import math
import threading
import pygame
from pygame.locals import QUIT

# Initialize Pygame for the simulation
pygame.init()

# Function to perform the space orbit simulation
def simulate_orbit():
    # Get user input from entry widgets
    eccentricity = float(e_entry.get())
    perigee_radius = float(a_entry.get())
    true_anomaly = float(theta_entry.get())
    inclination = float(i_entry.get())
    argument_of_perigee = float(omega_entry.get())
    right_ascension = float(omega_entry.get())

    # Calculate orbital characteristics (you can add the equations here)
    initial_radius = perigee_radius * (1 + eccentricity)
    current_time = 0
    mean_anomaly = true_anomaly
    initial_velocity = (math.sqrt((6.67430 * 10 ** -11) * 5.972 * 10 ** 24 / initial_radius))/2
    eccentric_anomaly = mean_anomaly
    angular_momentum = 0
    flight_path_angle = 0
    energy = 0

    # Display the calculated characteristics in the text widget
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Orbital Characteristics:\n")
    result_text.insert(tk.END, f"Initial radius: {initial_radius} km\n")
    result_text.insert(tk.END, f"Current time (from perigee): {current_time} s\n")
    result_text.insert(tk.END, f"Mean anomaly: {mean_anomaly} deg\n")
    result_text.insert(tk.END, f"Initial velocity: {initial_velocity} m/s\n")
    result_text.insert(tk.END, f"Eccentric anomaly: {eccentric_anomaly} deg\n")
    result_text.insert(tk.END, f"Perigee radius: {perigee_radius} km\n")
    result_text.insert(tk.END, f"Angular momentum: {angular_momentum} (units)\n")
    result_text.insert(tk.END, f"Flight path angle: {flight_path_angle} deg\n")
    result_text.insert(tk.END, f"Energy: {energy} (units)\n")

    # Pygame setup
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    orbit_center = (WIDTH // 2, HEIGHT // 2)
    orbit_radius = perigee_radius
    angle = math.radians(true_anomaly)  # Convert to radians

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Set background color to black

        x = orbit_center[0] + orbit_radius * math.cos(angle)
        y = orbit_center[1] + orbit_radius * math.sin(angle)

        pygame.draw.circle(screen, (0, 0, 255), orbit_center, 20)  # Earth (a simple circle)
        pygame.draw.circle(screen, (255, 255, 255), orbit_center, int(orbit_radius), 1)  # Orbit
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 5)  # Spacecraft (a small circle)

        pygame.display.flip()

        angle += 0.01  # Adjust this for the desired speed

        clock.tick(60)  # Control the frame rate

    pygame.quit()

# Create a Tkinter window
window = tk.Tk()
window.title("Integrated Space Simulator")
window.configure(bg="#000000")  # Set the background color to black

# Create labels and entry widgets for input parameters
label_e = tk.Label(window, text="Eccentricity (e):", bg="#000000", fg="#FFFFFF")
e_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")
label_a = tk.Label(window, text="Perigee Radius (km) (a):", bg="#000000", fg="#FFFFFF")
a_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")
label_theta = tk.Label(window, text="True Anomaly (deg) (θ):", bg="#000000", fg="#FFFFFF")
theta_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")
label_i = tk.Label(window, text="Inclination (deg) (i):", bg="#000000", fg="#FFFFFF")
i_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")
label_omega = tk.Label(window, text="Argument of Perigee (deg) (ω):", bg="#000000", fg="#FFFFFF")
omega_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")
label_omega = tk.Label(window, text="Right Ascension (deg) (Ω):", bg="#000000", fg="#FFFFFF")
omega_entry = tk.Entry(window, bg="#333333", fg="#FFFFFF")

# Create a "Simulate" button with a custom color
simulate_button = tk.Button(window, text="Simulate", command=lambda: threading.Thread(target=simulate_orbit).start(), bg="#2F77B2", fg="#FFFFFF")

# Create a text widget with a white background
result_text = tk.Text(window, width=40, height=15, bg="#FFFFFF")

# Pack the widgets
label_e.pack()
e_entry.pack()
label_a.pack()
a_entry.pack()
label_theta.pack()
theta_entry.pack()
label_i.pack()
i_entry.pack()
label_omega.pack()
omega_entry.pack()
label_omega.pack()
omega_entry.pack()
simulate_button.pack()
result_text.pack()

# Start the Tkinter main loop
window.mainloop()

# Create a Pygame window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a spacecraft (represented as a rectangle)
spacecraft_color = (255, 0, 0)  # Red
spacecraft_rect = pygame.Rect(0, 0, 20, 20)  # Initial position and size

spacecraft_speed = 2

# Create spacecraft information
spacecraft_info = {
    "Remaining Fuel": 1000,  # Example value
    "Crew Info": "Narendra Modi, Prime Minister",  # Example crew info
    "Satellite Name": "Chandrayan - II",  # Example satellite name
}

# Create a font for displaying information
font = pygame.font.Font(None, 36)

# Add a variable to track whether to display spacecraft information
display_spacecraft_info_flag = False

# Function to display spacecraft information
def display_spacecraft_info():
    for i, (key, value) in enumerate(spacecraft_info.items()):
        text = font.render(f"{key}: {value}", True, (255, 255, 255))
        screen.blit(text, (10, 10 + i * 30))

# Set up the main loop
running = True
clock = pygame.time.Clock()

# Define ellipse parameters
ellipse_center = (WIDTH // 2, HEIGHT // 2)
ellipse_semimajor = 150  # Adjust as needed
ellipse_semiminor = 100  # Adjust as needed
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if spacecraft_rect.collidepoint(event.pos):
                # Toggle the flag to display/hide spacecraft information
                display_spacecraft_info_flag = not display_spacecraft_info_flag

    # Calculate spacecraft position based on the equation of an ellipse
    spacecraft_x = ellipse_center[0] + ellipse_semimajor * math.cos(angle)
    spacecraft_y = ellipse_center[1] + ellipse_semiminor * math.sin(angle)

    # Update the angle to make the spacecraft move along the ellipse
    angle += 0.01  # Adjust this value to control the speed and direction

    # Draw the background
    screen.fill((0, 0, 0))

    # Draw Earth (for reference)
    earth = pygame.draw.circle(screen, (0, 0, 255), ellipse_center, 20)

    # Draw the spacecraft (red rectangle)
    spacecraft_rect.topleft = (spacecraft_x - spacecraft_rect.width / 2, spacecraft_y - spacecraft_rect.height / 2)
    pygame.draw.rect(screen, spacecraft_color, spacecraft_rect)

    # Display the spacecraft information when the flag is set
    if display_spacecraft_info_flag:
        display_spacecraft_info()

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
