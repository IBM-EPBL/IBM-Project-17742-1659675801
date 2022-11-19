<!DOCTYPE html>
<html >
<!--From https://codepen.io/frytyler/pen/EGdtg-->
<head>
  <meta charset="UTF-8">
  <title>IBM Plasma Donor App</title>
	<link href='https://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>
	<link href='https://fonts.googleapis.com/css?family=Arimo' rel='stylesheet' type='text/css'>
	<link href='https://fonts.googleapis.com/css?family=Hind:300' rel='stylesheet' type='text/css'>
	<link href='https://fonts.googleapis.com/css?family=Open+Sans+Condensed:300' rel='stylesheet' type='text/css'>
	<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">

<style>
.login{
top: 20%;
}
</style>
</head>

<body>
<div class="header">
<div>Plasma Donor App</div>
	<ul>
		
		
		<li><a href="/requester">Request</a></li>
		<li><a href="/registration">Register</a></li>
		<li><a class="active" href="/dashboard">Home</a></li>
	</ul>
</div>
 <div class="login">
		<div>
		</div>

     <!-- Main Input For Receiving Query to our ML -->
    <form action="{{ url_for('requested')}}"method="post">
    	<input type="text" name="name" placeholder="Enter Name" required="required" style="color:black" />
        <input type="email" name="email" placeholder="Enter Email" required="required" style="color:black"/>
		<input type="text" name="phone" placeholder="Enter 10-digit mobile number" required="required" style="color:black"/>
		<select name="bloodgrp">
					  <option value="select" selected>Choose your blood group</option>
					  <option value="O Positive">O Positive</option>
					  <option value="A Positive">A Positive</option>
					  <option value="B Positive">B Positive</option>
					  <option value="AB Positive">AB Positive</option>
					  <option value="O Negative">O Negative</option>
					  <option value="A Negative">A Negative</option>
					  <option value="B Negative">B Negative</option>
					  <option value="AB Negative">AB Negative</option>
		</select>
		<textarea rows="4" placeholder="Enter the address" required="required" style="color:black" name="address"></textarea>
        <button type="submit" class="btn btn-primary btn-block btn-large">Submit the request</button>
    
    </form>


 <br><br>
<div style="color:black">
 {{ pred }}</div>

 </div>


</body>
</html>
