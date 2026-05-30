from controller import Robot

# Khởi tạo robot từ Webots
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Cấu hình động cơ bánh xe TurtleBot3
left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# Các mốc tọa độ Waypoint từ thuật toán DAP để robot di chuyển mượt mà
dap_waypoints = [
    [0.0, 0.0],
    [0.3, 0.1],
    [0.6, -0.1],
    [1.0, 0.3]
]
current_wp_idx = 0

# Vòng lặp điều khiển thời gian thực
while robot.step(timestep) != -1:
    if current_wp_idx < len(dap_waypoints):
        left_motor.setVelocity(3.0)
        right_motor.setVelocity(3.0)
        if robot.getTime() > (current_wp_idx + 1) * 2.5: 
            current_wp_idx += 1
    else:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
