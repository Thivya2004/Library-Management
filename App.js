import React from 'react';
import Login from './Login';
import BookList from './BookList';
import AddBook from './AddBook';

const App = () => {
  return (
    <div>
      <h1>Library Management System</h1>
      <Login />
      <BookList />
      <AddBook />
    </div>
  );
};

export default App;
