"use client";

import LoginForm from '../components/LoginForm';
import { useRouter } from 'next/navigation';
import { loginUser } from '../services/authService';

const LoginPage = () => {
    const router = useRouter();

    const onLoginSubmit = async (email, password) => {
        try {
            const token = await loginUser(email, password);
            console.log('Token:', token);
            router.push('/dashboard');
        } catch (error) {
            console.error('Erro ao fazer login:', error);
            return { error: 'Erro ao fazer login' };
        }
        return { success: 'Login bem-sucedido' };
    }

    return (
        <div>
            <h1>Login</h1>
            <LoginForm onLoginSubmit ={onLoginSubmit} />
            <p>Don&apos;t have an account? <a href="/register">Register</a></p>
        </div>
    );
};

export default LoginPage;
