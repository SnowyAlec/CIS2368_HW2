const express = require("express"); // Load express and axios modules
const axios = require("axios");
const app = express();              // Create an Express application

//                              Set up EJS as the template engine
app.set("view engine", "ejs");

//                              Checking if the home page is working
app.get("/", (req, res) => {
    res.render("index", { 
        data: "Welcome to the Product Store" 
    });
});


//                              Route to get and display random products from Fake Store API
app.get("/random-products", async (req, res) => {
    try {
        //                      Fetch products from the Fake Store API
        const response = await axios.get("https://fakestoreapi.com/products");
        const products = response.data;

        //                      Randomly select 3 products
        const randomProducts = products
            .sort(() => 0.5 - Math.random())  // Randomize the selection
            .slice(0, 3);


        //                      If the sort checkbox is active --> sorts the products alphabetically
        if (req.query.sort === "true") {
            randomProducts.sort((a, b) => a.title.localeCompare(b.title));  // Sort alphabetically by title
        }
        const tagline = req.query.sort === "true"
            ? "Here are 3 random products sorted alphabetically"
            : "Here are 3 random products";

        //                      Render the products on the 'products.ejs' page
        res.render("products", { 
            data: randomProducts, 
            tagline: tagline 
        });
    } catch (error) {
        console.error("Error fetching products:", error);
        res.status(500).send("Error fetching product data.");
    }
});



// Start the server on port 8080
app.listen(8080, () => {
    console.log("Server is listening on on port 8080");
});