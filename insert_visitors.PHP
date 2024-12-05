<?php
// Database configuration
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "visitors_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve form data
$serial_number = $_POST['serial_number'];
$name = $_POST['name'];
$id_no = $_POST['id_no'];
$phone_number = $_POST['phone_number'];
$tag_number = $_POST['tag_number'];
$office = $_POST['office'];
$time_in = $_POST['time_in'];
$time_out = $_POST['time_out'];
$vehicle_reg = $_POST['vehicle_reg'];
$signature = $_POST['signature'];

// Insert data into the database
$sql = "INSERT INTO visitors (serial_number, name, id_no, phone_number, tag_number, office, time_in, time_out, vehicle_reg, signature)
        VALUES ('$serial_number', '$name', '$id_no', '$phone_number', '$tag_number', '$office', '$time_in', '$time_out', '$vehicle_reg', '$signature')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

// Close connection
$conn->close();
?>
