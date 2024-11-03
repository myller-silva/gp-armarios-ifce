'use client';

import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

const HomePage = () => {
    const router = useRouter();

    useEffect(() => {
        // Tenta recuperar o token armazenado no localStorage
        const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null;

        if (!token) {
        // Se não houver token, redireciona para a página de login
        router.push('/login');
        } else {
        // Se o token existir, redireciona para a página principal
        router.push('/dashboard');
        }
    }, [router]);

    return (
        <div>
        <p>Verificando autenticação...</p>
        </div>
    );
};

export default HomePage;
