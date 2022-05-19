<?php
require ('config.php');
	$folder_path='uploads/';
	$file_path=$folder_path.$_FILES['upload_file']['name'];

	$flag_ok=true;
	if(file_exists($file_path)){
		echo 'File name exists<br>';

		$flag_ok=false;
	}


	$ex= array('jpg','png','jpeg');
	$file_type = strtolower(pathinfo($file_path,PATHINFO_EXTENSION));
	if(!in_array($file_type,$ex)){
		echo 'File type not allowed<br>';
		$flag_ok = false;
	}

	if($flag_ok){
		move_uploaded_file($_FILES['upload_file']['tmp_name'],$file_path);
		$id= $_SESSION['id'];
		$username=$_SESSION['username'];
		$name = $_FILES['upload_file']['name'];
		echo $name;
		mysqli_query($mydb,"DELETE FROM img where user_id='$id'");
		mysqli_query($mydb,"INSERT INTO img value(null,'$id','$name')");
		header("location:profile.php?username=$username");
	}else{
		echo 'upload error<br>';
	}

?>
