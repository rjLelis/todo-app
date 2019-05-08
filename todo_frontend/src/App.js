import React from 'react';
import conf from './api.config'
import Table from './components/Table';
import './App.css';

class App extends React.Component {

  state ={
    todos: [],
    loading: true,
    message: 'Loading...'
  }

  componentDidMount() {
    
    fetch(`http://localhost:8080/api/todo/`, conf.GET).then(response => {
        if(response.status !== 200){
          return this.setState({message: response.message});
        }
        return response.json()
      }).then(data => this.setState({todos: data, loading: false})
    );
  }

  handleClick(todoId) {
    fetch(`http://localhost:8080/api/todo/${todoId}/finish`, conf.PUT).then(response => {
      if(response.status !== 200) {
          return this.setState({loading: false, message:'Something went wrong with the server'});
      }
      return (fetch('http://localhost:8080/api/todo/', conf.GET).then(response => {
        if(response.status !== 200){
          return this.setState({loading: false, message: 'Something went wrong with the server'});
        }
        return response.json();
      })
        ).then(data => {
          this.setState({todos:data});
        }
      );
    })
  }

  render() {
    return this.state.loading ? (<p>{this.state.message}</p>) :
      (<Table data={this.state.todos} onClick={i => this.handleClick(i)}/>);
  }
}

export default App;
