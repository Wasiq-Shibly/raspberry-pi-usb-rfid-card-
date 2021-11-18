<?php
$host = 'localhost';
$user = 'root';
$pass = '1234';
$db = 'super_home';
$mysqli = new mysqli($host,$user,$pass,$db);

if($_POST['token'] !== 'raspberry_local_token'){
    echo 'unauthorized!';
    return;
}

$validate = mysqli_fetch_assoc($mysqli->query("SELECT id from members where card_number = '".$_POST['card_number']."'"));

if(!empty($validate)){
    $mysqli->query("UPDATE members set status = ".$_POST['status']." where card_number = '".$_POST['card_number']."'" );
    return;
}

$mysqli->query("INSERT INTO `members`(`card_number`, `status`, `name`, `branch`, `image_link`) VALUES ('".$_POST['card_number']."','".$_POST['status']."','".$_POST['name']."','".$_POST['branch']."','".$_POST['image_link']."')");
echo mysqli_error($mysqli);