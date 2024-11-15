<?php
//phpinfo();
session_start();

$servername = "localhost";
$username = "root";
$password = "Md-3308333";
$dbname = "smart_home_aki";
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
else {      
  //echo "Connected successfully";
}

$user = $_POST['username'];
$pass = $_POST['password'];

$sql = "SELECT * FROM user WHERE username = '$user' AND password = '$pass'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $_SESSION['login_attempts'] = 0;
    header("Location: /ha/pages/home-4.html");
    exit();
} else {
    if (!isset($_SESSION['login_attempts'])) {
        $_SESSION['login_attempts'] = 0;
    }
    $_SESSION['login_attempts']++;

    $remaining_attempts = 3 - $_SESSION['login_attempts'];
    if ($_SESSION['login_attempts'] >= 3) {
        echo 
        "<script>
            alert('登入失敗次數過多，請稍後再試');
            window.location.href = '/ha/pages/login-4.html';
        </script>";

    } else {
        echo 
        "<script>
            alert('輸入錯誤，您還有 $remaining_attempts 次機會');
            window.location.href = '/ha/pages/login-4.html';
        </script>";

    }
}

$conn->close();
?>
