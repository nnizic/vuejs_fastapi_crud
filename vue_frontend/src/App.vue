<template>
  <div id="app" class="bg-image">

    <app-header />
    <h2>Zadatci</h2>
    <h3>Dodaj zadatak</h3>
    <div class="todo-container center-content">
    <div>
      <label>Naziv: </label>
      <input type="text" v-model="newTodo.title">
    </div>
    <div class="move">
      <label>Opis: </label>
      <input type="text" v-model="newTodo.description">
    </div>
      <button @click="createTodo" class="btn-primary">Dodaj</button>
    </div>
    <div v-if="todos.length > 0"> 
      <h2>Zadatci u tijeku:</h2>
      <ul>
        <li v-for="todo in todos" :key="todo.id" class="todo"> 
          <div>{{ todo.title }}</div>
          <div>{{ todo.description }}</div>
          <button @click="deleteTodo(todo.id)" class="btn-primary">Ukloni</button>
        </li>
      </ul>
    </div>
    <app-footer />
  </div>
</template>

<script>
import axios from 'axios'
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'

export default {
  name: 'App',
  data() {
    return {
      todos: [],
      newTodo: {
        title: '',
        description: ''
      }
    }
  },
  created() {
    this.fetchTodos();
      
  },
    components: {
        AppHeader,
        AppFooter
    },
  methods: {
    fetchTodos() {
      axios.get('http://localhost:8000/todos/')
        .then(response => {
          this.todos = response.data;
        })
        .catch(error => {
          console.error('Error fetching todos:', error);
        });
    },
    createTodo() {
      this.newTodo.id = Math.floor(Math.random() * 1000); // Generate random number
      axios.post('http://localhost:8000/todos/', this.newTodo)
        .then(response => {
          this.todos.push(response.data);
          this.newTodo.title = '';
          this.newTodo.description = '';
        })
        .catch(error => {
          console.error('Error creating todo:', error);
        });
    },
    deleteTodo(todoId) {
      axios.delete(`http://localhost:8000/todos/${todoId}`)
        .then(()=> {
          this.todos = this.todos.filter(todo => todo.id !== todoId);
        })
        .catch(error => {
          console.error('Error deleting todo:', error);
        });
    }
  }
}
</script>

<style>
/* Custom Bootstrap theme */
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');

body {
  font-family: 'Roboto', sans-serif;
  background-color: #f8f9fa; /* Light gray background */
  ul {
      list-style: none;
  }
}


.card {
  background-color: #ffffff; /* White card background */
  border-radius: 0.5rem;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* Soft shadow */
}

.move {
    margin-left: 10px;
    margin-right: 10px;
}
.btn-primary {
  background-color: #007bff; /* Blue button */
  border-color: #007bff; /* Blue border */
}

.btn-primary:hover {
  background-color: #0056b3; /* Darker blue on hover */
  border-color: #0056b3; /* Darker blue border on hover */
}/* Background image */
.bg-image {
  background-image: url('assets/001-scaled.jpg');
  background-size: cover;
  background-position: center;
  height: 100vh; /* Set height to fill the viewport */
}

/* Overlay for background image */
.overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent black overlay */
}

/* Center content vertically */
.center-content {
  display: flex;
  align-items: center;
  justify-content: center;
}
/* Container for displayed todos */
.todo-container {
  margin-top: 25px; /* Adjust margin as needed */
}

/* Individual todo */
.todo {
  background-color: rgba(255, 255, 255, 0.5); /* Semi-transparent white background */
  padding: 10px;
  margin-top: 10px;
  margin-bottom: 10px;
  width: 95%;
}
</style>

