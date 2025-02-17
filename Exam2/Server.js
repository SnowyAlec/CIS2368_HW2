// npm init -y for json package
//npm install express ejs axios for node modules and rest of jason packages
const express = require("express"); // Load express and axios modules
const axios = require("axios");
const app = express();              // Create an Express application
app.set('view engine', 'ejs');

app.use(express.static("public")); //using the style 

//          Templet to start ejs


//          Home page route
app.get("/", (req,res)=>{
    res.render("index",{
        data: "Welcome to Todo List Apllication"
    });
});

app.get("/todos", async(req,res)=>{
    try{
        //fetching todo data
        const response = await axios.get("https://dummyjson.com/todos");
        const todos = response.data.todos;

        todos.sort((a,b)=> a.userId - b.userId);

        const todoTasks = todos.filter(task => !task.completed);
        const completedTasks = todos.filter(task => task.completed);

        res.render("todos",{
            todoTasks,
            completedTasks,
        });
    } catch (error){
        console.error("Error getting todos", error);
        res.status(500).send("Error fetching Todo data.")
    }
});

app.listen(8080,() => {
    console.log("Server is listening on port 8080")
});
