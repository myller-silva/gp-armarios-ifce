'use client';


import { useEffect, useState } from 'react';
import { getUser } from '../services/localStorageService';
// import {getUserInfo} from '../services/userService';
import Navbar from '../components/Navbar';

export default function Dashboard() {
  const [userInfo, setUserInfo] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    try {
      const user = getUser();
      setUserInfo(user);
    } catch (err) {
      setError(err.message);
    }
  }, []);

  if (error) {
    return <div>Error: {error}</div>;
  }

  if (!userInfo) {
    return <div>Loading...</div>; // Ou qualquer indicador de carregamento que você deseja usar
  }

  return (
    <div>
      <Navbar />
      <h1>Dashboard</h1>
      <p>Olá, {userInfo.username}!</p>
      
    </div>
  );
}
