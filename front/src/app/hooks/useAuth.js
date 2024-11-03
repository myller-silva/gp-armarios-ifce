import { loginUser } from '../services/authService';
import { useState } from 'react';

export const useAuth = () => {
    const [error, setError] = useState(null);

    const login = async (email, password) => {
        setError(null);
        try {
            const token = await loginUser(email, password);
            localStorage.setItem('token', token);
            return token; // Retorna o token para uso posterior
        } catch (err) {
            setError(err.message);
            throw err; // Re-lança para que o componente que chamou possa tratar
        }
    };

    return { login, error };
};


