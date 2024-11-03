// userService.js

'use client';

import { saveToLocalStorage, getFromLocalStorage } from "./localStorageService";

const API_URL = 'http://localhost:5000';

export const getUserInfo = async () => {
    const token = getFromLocalStorage('token');
    
    if (!token) {
        throw new Error('Token não encontrado');
    }
    
    const response = await fetch(`${API_URL}/user`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json',
        },
    });
    
    if (!response.ok) {
        // Aqui pode verificar o status e lançar um erro mais informativo
        const errorResponse = await response.json(); // Pega a resposta de erro como JSON
        throw new Error(`Erro ao obter informações do usuário: ${errorResponse.msg}`);
    }
    const userData = await response.json();
    saveToLocalStorage('user', userData);
    
    return userData;
};

