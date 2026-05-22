# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import linear_sum_assignment

class InterceptManager:
    def __init__(self, num_interceptors=10):
        self.num_interceptors = num_interceptors
        # Наша база ПВО находится в точке [0, 0, 0]
        self.positions = np.zeros((num_interceptors, 3)) 
        self.active_assignments = {} # Словарь: {цель_id: перехватчик_id}
        self.interceptor_speed = 50.0  # Скорость перехватчиков 180 км/ч
        
    def allocate_targets(self, targets_positions):
        """
        Использует Венгерский алгоритм для минимизации общего расстояния (времени) до целей.
        """
        N = len(self.positions)
        M = len(targets_positions)
        
        if M == 0:
            return {}

        # Матрица расстояний (Стоимость)
        cost_matrix = np.zeros((N, M))
        for i in range(N):
            for j in range(M):
                cost_matrix[i, j] = np.linalg.norm(self.positions[i] - targets_positions[j])

        # Решение задачи оптимизации
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        
        assignments = {}
        for r, c in zip(row_ind, col_ind):
            assignments[c] = r  # Назначаем цели (c) конкретный перехватчик (r)
            
        return assignments