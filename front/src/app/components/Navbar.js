// components/Navbar.js
import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { ClearLocalStorage } from '../services/localStorageService';

const Navbar = () => {
  const [isDarkTheme, setIsDarkTheme] = useState(false);
  const router = useRouter();

  // Verifica a preferência de tema no localStorage ao carregar o componente
  useEffect(() => {
    const theme = localStorage.getItem('theme');
    if (theme === 'dark') {
      setIsDarkTheme(true);
      document.body.classList.add('dark-theme');
    } else {
      document.body.classList.remove('dark-theme');
    }
  }, []);

  // Função para alternar o tema
  const toggleTheme = () => {
    const newTheme = isDarkTheme ? 'light' : 'dark';
    setIsDarkTheme(!isDarkTheme);
    localStorage.setItem('theme', newTheme);

    if (newTheme === 'dark') {
      document.body.classList.add('dark-theme');
    } else {
      document.body.classList.remove('dark-theme');
    }
  };

  // Função para fazer logout
  const handleLogout = () => {
    // Remova o token do localStorage ou qualquer outra informação do usuário
    // localStorage.removeItem('token');
    // localStorage.removeItem('user');
    ClearLocalStorage();
    router.push('/login'); // Redireciona para a página de login
  };

  return (
    <nav>
      <h1>Meu App</h1>
      <button onClick={toggleTheme}>
        {isDarkTheme ? 'Tema Claro' : 'Tema Escuro'}
      </button>
      <button onClick={handleLogout}>Logout</button>
    </nav>
  );
};

export default Navbar;
