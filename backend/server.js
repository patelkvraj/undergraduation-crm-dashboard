const express = require('express');
const cors = require('cors');
const admin = require('firebase-admin');

// Initialize the Express app
const app = express();
// Enable CORS for all routes
app.use(cors());
// Parse incoming JSON requests
app.use(express.json());

// Path to your Firebase service account key file
const serviceAccount = require("./serviceAccountKey.json");

// Initialize the Firebase app
admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

// Get a reference to the Firestore database
const db = admin.firestore();
// Get a reference to the 'students' collection
const studentsRef = db.collection('students');

// Endpoint to get all students
app.get('/api/students', async (req, res) => {
    try {
        const snapshot = await studentsRef.get();
        const students = [];
        snapshot.forEach(doc => {
            students.push({ id: doc.id, ...doc.data() });
        });
        // Return the data as a JSON response
        res.status(200).json(students);
    } catch (error) {
        // Handle any errors
        res.status(500).send(error);
    }
});

// Endpoint to get a single student profile
app.get('/api/students/:id', async (req, res) => {
    try {
        const doc = await studentsRef.doc(req.params.id).get();
        if (!doc.exists) {
            // Return a 404 error if the student is not found
            res.status(404).json({ error: "Student not found" });
        } else {
            // Return the student profile
            res.status(200).json({ id: doc.id, ...doc.data() });
        }
    } catch (error) {
        res.status(500).send(error);
    }
});

// Placeholder for creating a student
app.post('/api/students', async (req, res) => {
    try {
        const data = req.body;
        // Add a new document with an auto-generated ID
        const docRef = await studentsRef.add(data);
        res.status(201).json({ success: "Student added", id: docRef.id });
    } catch (error) {
        res.status(500).send(error);
    }
});

const PORT = process.env.PORT || 8000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});