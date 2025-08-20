const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());

app.post("/login", (req, res) => {
	// Simulate a login endpoint
	res.json({ message: "Login successful" });
});

app.post("/profile", (req, res) => {
	// Simulate a profile endpoint
	res.json({ message: "Profile data retrieved successfully" });
});

app.listen(3000, () => {
	console.log("API server is running on http://localhost:3000");
});
