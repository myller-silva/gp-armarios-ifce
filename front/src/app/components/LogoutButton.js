"use client"; 

// import { useRouter } from 'next/router';
import { useRouter } from 'next/navigation'; // Use 'next/navigation' no Next.js 13+

const LogoutButton = () => {
    const router = useRouter();

    const handleLogout = () => {
        localStorage.removeItem('token');
        router.push('/login'); // Redireciona para a página de login
    };

    return <button onClick={handleLogout}>Logout</button>;
};

export default LogoutButton;
