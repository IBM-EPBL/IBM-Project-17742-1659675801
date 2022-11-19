@import url(https://fonts.googleapis.com/css?family=Open+Sans);
.btn { 
	display: inline-block; 
	*display: inline; 
	*zoom: 1; padding: 
	4px 10px 4px; 
	margin-bottom: 0; 
	font-size: 13px; 
	line-height: 18px; 
	color: #333333; 
	text-align: center;
	text-shadow: 0 1px 1px rgba(255, 255, 255, 0.75); 
	vertical-align: middle; 
	background-color: #d70c0c; 
	background-image: -moz-linear-gradient(top, #ffffff, #e6e6e6); 
	background-image: -ms-linear-gradient(top, #ffffff, #e6e6e6); 
	background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#ffffff), to(#e6e6e6)); 
	background-image: -webkit-linear-gradient(top, #ffffff, #e6e6e6); 
	background-image: -o-linear-gradient(top, #ffffff, #e6e6e6); 
	background-image: linear-gradient(top, #ffffff, #e6e6e6); 
	background-repeat: repeat-x; 
	filter: progid:dximagetransform.microsoft.gradient(startColorstr=#ffffff, endColorstr=#e6e6e6, GradientType=0); 
	border-color: #e6e6e6 #e6e6e6 #e6e6e6; 
	border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25); 
	border: 1px solid #e6e6e6; 
	-webkit-border-radius: 4px; 
	-moz-border-radius: 4px; 
	border-radius: 4px; 
	-webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); 
	-moz-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); 
	box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.05); 
	cursor: pointer; *margin-left: .3em; 
	}
	
.btn:hover, .btn:active, .btn.active, .btn.disabled, .btn[disabled] { background-color: #e6e6e6; }

.btn-large { 
	padding: 9px 14px; 
	font-size: 15px; 
	line-height: normal; 
	-webkit-border-radius: 5px; 
	-moz-border-radius: 5px; 
	border-radius: 5px; 
	}
	
.btn:hover { 
	color: #333333; 
	text-decoration: none; 
	background-color: #e6e6e6; 
	background-position: 0 -15px; 
	-webkit-transition: background-position 0.1s linear; 
	-moz-transition: background-position 0.1s linear; 
	-ms-transition: background-position 0.1s linear; 
	-o-transition: background-position 0.1s linear; 
	transition: background-position 0.1s linear; 
	}
	
.btn-primary, .btn-primary:hover { 
	text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.25); 
	color: #ffffff; 
	}
	
.btn-primary.active { color: rgba(255, 255, 255, 0.75); }

.btn-primary { 
	background-color: #d70c0c; 
	background-image: -moz-linear-gradient(top, #6eb6de, #4a77d4); 
	background-image: -ms-linear-gradient(top, #6eb6de, #4a77d4); 
	background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#6eb6de), to(#4a77d4)); 
	background-image: -webkit-linear-gradient(top, #6eb6de, #4a77d4); 
	background-image: -o-linear-gradient(top, #6eb6de, #4a77d4); 
	background-image: linear-gradient(top, #6eb6de, #4a77d4); 
	background-repeat: repeat-x; 
	filter: progid:dximagetransform.microsoft.gradient(startColorstr=#6eb6de, endColorstr=#4a77d4, GradientType=0);  
	border: 1px solid #3762bc; 
	text-shadow: 1px 1px 1px rgba(0,0,0,0.4); 
	box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.2), 0 1px 2px rgba(0, 0, 0, 0.5); 
	}
	
.btn-primary:hover, .btn-primary:active, .btn-primary.active, .btn-primary.disabled, .btn-primary[disabled] { 
	filter: none; 
	background-color: #d70c0c 
	}
	
.btn-block { width: 100%; display:block; }

* { -webkit-box-sizing:border-box; -moz-box-sizing:border-box; -ms-box-sizing:border-box; -o-box-sizing:border-box; box-sizing:border-box; }

html { width: 100%; height:100%; overflow:hidden; }

body { 
	width: 100%;
	height:100%;
	font-family: 'Open Sans', sans-serif;
	color: #000000;
	font-size: 18px;
	text-align:center;
	letter-spacing:1.2px;
	

}
.header {	
			top:0;	
			margin:0px;
			left: 0px;
			right: 0px;
			position: fixed;
			background: #d44a4a;
			color: black;
			box-shadow: 0px 8px 4px grey;
			overflow: hidden;
			padding: 15px;
			font-size: 1.5vw;
			width: 100%;
			text-align: center;
		}
.login { 
	position: absolute;
	top: 70%;
	left: 50%;
	margin: -25px 0 0 -150px;
	width:400px;
	height:400px;
}

.header div { color: #fff; text-shadow: 0 0 10px rgba(0,0,0,0.3); letter-spacing:1px; text-align:center; float:left; padding-left:150px;}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  padding-right:150px;
  overflow: hidden;
 }


li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 0px 15px;
  text-decoration: none;
}


input { 
	width: 100%; 
	margin-bottom: 10px; 
	background: rgba(255,255,255,255);
	border: none;
	outline: none;
	padding: 10px;
	font-size: 13px;
	color: black;
	text-shadow: black;
	border: 1px solid rgba(0,0,0,0.3);
	border-radius: 4px;
	box-shadow: inset 0 -5px 45px rgba(100,100,100,0.2), 0 1px 1px rgba(255,255,255,0.2);
	-webkit-transition: box-shadow .5s ease;
	-moz-transition: box-shadow .5s ease;
	-o-transition: box-shadow .5s ease;
	-ms-transition: box-shadow .5s ease;
	transition: box-shadow .5s ease;
}
input:focus { box-shadow: inset 0 -5px 45px rgba(100,100,100,0.4), 0 1px 1px rgba(255,255,255,0.2); }


textarea { 
	width: 100%; 
	margin-bottom: 10px; 
	background: rgba(255,255,255,255);
	border: none;
	outline: none;
	padding: 10px;
	font-size: 13px;
	color: black;
	text-shadow: black;
	border: 1px solid rgba(0,0,0,0.3);
	border-radius: 4px;
	box-shadow: inset 0 -5px 45px rgba(100,100,100,0.2), 0 1px 1px rgba(255,255,255,0.2);
	-webkit-transition: box-shadow .5s ease;
	-moz-transition: box-shadow .5s ease;
	-o-transition: box-shadow .5s ease;
	-ms-transition: box-shadow .5s ease;
	transition: box-shadow .5s ease;
}
textarea:focus { box-shadow: inset 0 -5px 45px rgba(100,100,100,0.4), 0 1px 1px rgba(255,255,255,0.2); }

select { 
	width: 100%; 
	margin-bottom: 10px; 
	background: rgba(255,255,255,255);
	border: none;
	outline: none;
	padding: 10px;
	font-size: 13px;
	color: #000000;
	text-shadow: 1px 1px 1px rgba(0,0,0,0.3);
	border: 1px solid rgba(0,0,0,0.3);
	border-radius: 4px;
	box-shadow: inset 0 -5px 45px rgba(100,100,100,0.2), 0 1px 1px rgba(255,255,255,0.2);
	-webkit-transition: box-shadow .5s ease;
	-moz-transition: box-shadow .5s ease;
	-o-transition: box-shadow .5s ease;
	-ms-transition: box-shadow .5s ease;
	transition: box-shadow .5s ease;
}