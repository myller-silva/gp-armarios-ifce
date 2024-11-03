import { useState } from 'react';
import ErrorMessage from './ErrorMessage';

const RegisterForm = ({ onRegisterSubmit }) => {

    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (!email || !password) {
            setError('All fields must be filled');
            return;
        }
        const response = await onRegisterSubmit(username, email, password);
        
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
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
            </div>

            <div>
                <label htmlFor="email">Email</label>
                <input
                    type="email"
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
            <button type="submit">Sign in</button>
            {error && <ErrorMessage message={error} />}
        </form>
    );
};

export default RegisterForm;