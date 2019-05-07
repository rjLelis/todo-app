import React from 'react';
import logo from './logo.svg';
import Table from './components/Table';
import './App.css';

class App extends React.Component {

  state ={
    todos: [],
    loading: true,
    message: 'Loading...'
  }

  componentDidMount() {
    
    fetch(`http://localhost:8080/api/todo/`,
    {
      method: 'GET',
      headers: new Headers({'Content-type': 'application/json'})
    }).then(response => {
        if(response.status !== 200){
          return this.setState({message: response.message});
        }
        return response.json()
      }).then(data => this.setState({todos: data, loading: false})
    );
  }


  render() {
    const {todos, loading, message} = this.state;
    return loading ? (<p>{message}</p>) :
      (todos.map(todo => 
        <Table key={todo.id} data={todo}/>
      )
    );
  }
}

export default App;
