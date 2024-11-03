
const API_URL = 'http://localhost:5000'; // URL da API

import { saveToLocalStorage } from './localStorageService';
import { getUserInfo } from './userService';

export const loginUser = async (email, password) => {
    console.log('Tentando fazer login com:', email, password);
    
    const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.msg || 'Login failed');
    }

    const data = await response.json();
    
    // Salva o token no localStorage
    saveToLocalStorage('token', data.token);

    const user = await getUserInfo();
    saveToLocalStorage('user', user);

    return data.token; 
};


export const registerUser = async (username, email, password) => {
    console.log('Tentando fazer registro com:', username, email, password);
    
    const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.msg || 'Login failed');
    }

    const data = await response.json();

    // Salva o token no localStorage
    saveToLocalStorage('token', data.token);
    
    const user = await getUserInfo();
    saveToLocalStorage('user', user);
    
    return data.token; 
};
