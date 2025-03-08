import React, { useState, ChangeEvent, FormEvent } from 'react';
import { Container, Box, TextField, Button, Typography, Paper } from '@mui/material';
import { RegisterData } from '../../services/type';

const SignUp: React.FC = () => {
  const [formData, setFormData] = useState<RegisterData>({
    email: '',
    password: '',
    password_confirmation: '',
    first_name: '',
    last_name: '',
    age: 0,
    user_id: 'qwe123',
  });

  const [message, setMessage] = useState<string>('');

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: name === 'age' ? Number(value) : value,
    }));
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Submitted data:', formData);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      if (response.ok) {
        setMessage('Реєстрація пройшла успішно!');
      } else {
        const errorData = await response.json();
        setMessage(`Помилка: ${errorData.error}`);
      }
    } catch (error) {
      setMessage('Сталася помилка при відправці даних.');
      console.error('Помилка:', error);
    }
  };

  return (
    <Container
      maxWidth="sm"
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <Paper elevation={8} sx={{ p: 4, borderRadius: 3, width: '100%' }}>
        <Typography variant="h4" component="h1" align="center" gutterBottom>
          Реєстрація
        </Typography>
        <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="first_name"
            name="first_name"
            label="Ім'я"
            value={formData.first_name}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="last_name"
            name="last_name"
            label="Прізвище"
            value={formData.last_name}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            name="email"
            label="Email"
            value={formData.email}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="password"
            name="password"
            label="Пароль"
            type="password"
            value={formData.password}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="password_confirmation"
            name="password_confirmation"
            label="Повторіть пароль"
            type="password"
            value={formData.password_confirmation}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            id="age"
            name="age"
            label="Вік"
            type="number"
            value={formData.age}
            onChange={handleChange}
            variant="outlined"
            sx={{ backgroundColor: '#fff', borderRadius: 1 }}
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            color="primary"
            size="large"
            sx={{ mt: 3, py: 1.5 }}
          >
            Зареєструватися
          </Button>
          {message && (
            <Typography variant="subtitle1" color="success.main" align="center" sx={{ mt: 2 }}>
              {message}
            </Typography>
          )}
        </Box>
      </Paper>
    </Container>
  );
};

export default SignUp;
