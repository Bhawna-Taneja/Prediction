<?php

$hostName = "localhost";
$dbUser = "root";
$dbPassword = "";
$dbName = "login_regis";
$conn = mysqli_connect($hostName, $dbUser, $dbPassword, $dbName);
if (!$conn) {
    die("Something went wrong;");
}

?>