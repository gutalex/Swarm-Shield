# -*- coding: utf-8 -*-
import numpy as np

class TargetSwarm:
    def __init__(self, num_targets=15, target_center=[0, 0, 100]):
        self.num_targets = num_targets
        self.target_center = np.array(target_center)
        
        # Спавним дроны на расстоянии 500-700 метров от базы по случайным азимутам
        angles = np.random.uniform(0, 2 * np.pi, num_targets)
        distances = np.random.uniform(500, 700, num_targets)
        altitudes = np.random.uniform(20, 80, num_targets)
        
        self.positions = np.zeros((num_targets, 3))
        self.positions[:, 0] = distances * np.cos(angles)
        self.positions[:, 1] = distances * np.sin(angles)
        self.positions[:, 2] = altitudes
        
        # Скорость целей (векторы, направленные к центру базы)
        self.velocities = np.zeros((num_targets, 3))
        self.speeds = np.random.uniform(20, 30, num_targets)  # м/с (72-108 км/ч)
        
        for i in range(num_targets):
            direction = self.target_center - self.positions[i]
            direction = direction / np.linalg.norm(direction)
            self.velocities[i] = direction * self.speeds[i]

    def update(self, dt=0.1):
        # Добавляем случайный шум "рыскания" для симуляции реального полета
        wind_noise = np.random.normal(0, 0.5, self.positions.shape)
        self.positions += (self.velocities * dt) + wind_noise