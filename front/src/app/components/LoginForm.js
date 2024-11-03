
import { useState } from 'react';
// import { useAuth } from '../hooks/useAuth';
import ErrorMessage from './ErrorMessage';

const LoginForm = ({ onLoginSubmit }) => {
    // const { error, login } = useAuth();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!email || !password) {
            setError('Preencha todos os campos');
            return;
        }
        const response = await onLoginSubmit(email, password);
        
        if (response.error) {
            setError(response.error);
            return;
        }
        else {
            setError(null);
        }

    };

    return (
        <form onSubmit={handleSubmit}>
            <div>
                <label htmlFor="username">Email</label>
                <input
                    type="text"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
            </div>
            <div>
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
            </div>
            <button type="submit">Login</button>
            {error && <ErrorMessage message={error} />}
        </form>
    );
};

export default LoginForm;