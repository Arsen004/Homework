import React, { useState } from 'react';

// Компонент Greeting для отображения приветствия
function Greeting(props) {
  return <h1>Привет, {props.name}!</h1>;
}

// Компонент Counter для увеличения значения счетчика
function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Вы нажали {count} раз</p>
      <button onClick={() => setCount(count + 1)}>Увеличить счетчик</button>
    </div>
  );
}

// Главный компонент App
function App() {
  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <Greeting name="Артем" />
      <Counter />
      <button onClick={() => alert('Кнопка нажата!')} style={{ marginTop: '20px' }}>
        Нажми меня
      </button>
    </div>
  );
}

export default App;
