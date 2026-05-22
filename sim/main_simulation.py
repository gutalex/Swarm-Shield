# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from target_swarm import TargetSwarm
from intercept_manager import InterceptManager

def run_simulation():
    swarm = TargetSwarm(num_targets=8)
    manager = InterceptManager(num_interceptors=8)
    
    dt = 0.2
    steps = 150
    
    plt.ion()
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    for step in range(steps):
        swarm.update(dt)
        assignments = manager.allocate_targets(swarm.positions)
        
        # Движение перехватчиков к назначенным целям
        for target_idx, interceptor_idx in assignments.items():
            target_pos = swarm.positions[target_idx]
            interceptor_pos = manager.positions[interceptor_idx]
            
            direction = target_pos - interceptor_pos
            distance = np.linalg.norm(direction)
            
            if distance > 2.0:  # Если еще не долетел
                step_dist = min(manager.interceptor_speed * dt, distance)
                manager.positions[interceptor_idx] += (direction / distance) * step_dist

        ax.clear()
        
        # Отрисовка
        ax.scatter(0, 0, 0, color='red', s=200, label='Наша База (Защита)')
        ax.scatter(swarm.positions[:, 0], swarm.positions[:, 1], swarm.positions[:, 2], 
                   color='black', s=50, label='Рой дронов врага')
        ax.scatter(manager.positions[:, 0], manager.positions[:, 1], manager.positions[:, 2], 
                   color='green', s=40, marker='^', label='Наши перехватчики')
        
        # Отрисовка линий наведения (назначений)
        for target_idx, intercept_idx in assignments.items():
            ax.plot([swarm.positions[target_idx, 0], manager.positions[intercept_idx, 0]],
                    [swarm.positions[target_idx, 1], manager.positions[intercept_idx, 1]],
                    [swarm.positions[target_idx, 2], manager.positions[intercept_idx, 2]], 'r--', alpha=0.5)

        ax.set_xlim([-400, 400])
        ax.set_ylim([-400, 400])
        ax.set_zlim([0, 150])
        ax.set_title(f"Симуляция Swarm-Shield. Кадр {step}")
        ax.legend()
        plt.draw()
        plt.pause(0.05)
        
    plt.ioff()
    plt.show()

if __name__ == "__main__":
    run_simulation()