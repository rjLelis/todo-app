import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

  state ={
    title: '',
    description: ''
  }

  componentDidMount() {
    
    fetch(`http://localhost:8080/api/todo/1`,
    {
      method: 'GET',
      headers: new Headers({'Content-type': 'application/json'})
    }).then(response => {
      if(response.status !== 200){
        return response.message
      }
      return response.json()
    }).then(data => this.setState({title: data.title, description: data.description})
    )
  }


  render() {
    const {title, description} = this.state
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            {title}
          </p>
          <p>
            {description}
          </p>
        </header>
      </div>
    );
  }
}

export default App;
