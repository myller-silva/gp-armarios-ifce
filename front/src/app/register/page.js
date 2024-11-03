"use client";
import { useRouter } from 'next/navigation';
import { registerUser } from '../services/authService';
import RegisterForm from '../components/RegisterForm';

const RegisterPage = () => {
    const router = useRouter();

    const onRegisterSubmit = async (username, email, password) => {
        try {
            const token = await registerUser(username, email, password);
            console.log('Token:', token);
            router.push('/dashboard');
        } catch (error) {
            console.error('Erro ao fazer registro:', error);
            return { error: 'Erro ao fazer registro' };
        }
        return { success: 'Registro bem-sucedido' };
    }

    return (
        
        <div>
            <h1>Register</h1>
            <RegisterForm onRegisterSubmit={onRegisterSubmit} />
            <p>Already have an account? <a href="/login">Login</a></p>
        </div>
    );
};

export default RegisterPage;
