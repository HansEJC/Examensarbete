<!DOCTYPE HTML>
<html>

<head>
	<title>Newtons andra Vagn</title>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<meta name="description" content="" />
	<meta name="keywords" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
	<script src="dygraph-combined.js"></script>
	<link rel="stylesheet" href="css/skel.css" />
	<link rel="stylesheet" href="css/style.css" />
	<link rel="stylesheet" href="css/style-desktop.css" />
	<link rel="stylesheet" href="css/style-mobile.css" />
	<script Language="Javascript">
		function send() {
			document.getElementById("exp1").value = document.getElementById("exp").value;
			document.location = "cgi-bin/test.cgi";
			setTimeout('Redirect()', 1000);
		}
		function Redirect() {
			document.location = "index.php";
		}
		function forward() {
			document.location = "cgi-bin/forward.cgi";
		}
		function rev() {
			document.location = "cgi-bin/reverse.cgi";
		}
		function brake(event) {
			document.location = "cgi-bin/brake.cgi";
		}
		function ball(event) {
			document.location = "cgi-bin/ball.cgi";
		}
	</script>
</head>

<body class="left-sidebar">

	<!-- Header -->
	<div id="header-wrapper" class="wrapper">
		<div id="header">
			<!-- Logo -->
			<div id="logo">
				<h1><a href="#">Newtons andra Vagn</a></h1>
				<p>Välkommen till Högskolan i Halmstads fysikdemo för Newtons andra lag</p>
			</div>
		</div>
	</div>

	<!-- Main -->
	<div class="wrapper style2">
		<div class="title">Kontrolpanel </div>
		<div id="main" class="container">
			<div class="row 150%">
				<div class="4u">

					<!-- Sidebar -->
					<div id="sidebar">
						<section class="box">
							<header>
								<h2>Live Stream</h2>
							</header>
							<div><img width="256" height="144" id="mjpeg_dest" onclick="toggle_fullscreen(this);">
							</div>
							<a href="indexpicam.php" class="button style1">Kamera Inställningar</a>
						</section>
						<br><br><br><br><br><br><br><br><br><br><br><br><a href="graf.csv" class="button style1">Ladda
							ner som csv</a><br>
						<br><br><br><br><br><br><br><br><br><br><br><br><a href="graf2.csv" class="button style1">Ladda
							ner som csv</a><br>
					</div>

				</div>
				<div class="8u important(collapse)">

					<!-- Content -->
					<div id="content">

						<div class="row 150%">
							<div class="6u">
								<section class="box">
									<form>
										<input type="radio" name="drive" value="Automatiserad körning"
											checked>Automatiserad körning
										<br>
										<input type="radio" name="drive" value="Manuellt körning">Manuellt körning<br>
										<div id="manhast" hidden><br>
											Vagnen kommer nu köra på max hastighet som är ungefär 42cm/s.<br>
										</div>
										<div id="autoslap">
											Starta experiment [s]:<br>
											<input type="text" name="experiment" value="3" id=exp><br>
										</div>

									</form>
								</section>
								<script type="text/javascript">
									const hide = (div) => document.querySelector(div).style = 'display: none'; // hide
									const show = (div) => document.querySelector(div).style = 'display: block'; // show

									let rad = document.querySelectorAll("input[type=radio]");
									rad.forEach(ra => {ra.addEventListener('change', function () {
										if (rad[0].checked) {
											show("#auto");
											hide("#manhast");
											show("#autoslap");
											hide("#manuellt");
										}
										else {
											hide("#auto");
											show("#manhast");
											hide("#autoslap");
											show("#manuellt");
										}
									})});
								</script>
							</div>

							<div hidden class="6u" id="manuellt">
								<section class="box">
									<p>Tryck på pilarna på skärmen eller "w","s" för fram och bakkörning.
										Tryck på kulan eller "d" på tangentbordet för att skjuta/släppa kulan
									<p>
										<img src="images/forward.png" id="f" onmousedown="forward()"
											onmouseup="brake()">
										<br>
										<img align="right" src="images/ball.png" id="l" onmousedown="ball()">
										<!--	<img src="/right.jpg" id="r" onmousedown="set1()" onmouseup="clear01()"> -->
										<br>
										<img src="images/reverse.png" id="s" onmousedown="rev()" onmouseup="brake()">
										<script type="text/javascript">

											document.onkeydown = function (evt) {
												evt = evt || window.event;
												switch (evt.keyCode) {
													case 87:
														forward();
														break;
													case 83:
														rev();
														break;
													case 68:
														ball();
														break;
												}
											};
											document.onkeyup = function (evt) {
												evt = evt || window.event;
												switch (evt.keyCode) {
													case 87:
														brake();
														break;
													case 83:
														brake();
														break;
												}
											};
										</script>
								</section>
							</div>

							<div class="6u" id="auto">
								<section class="box">
									<form>
										<input type="radio" name="drivetype" value="Hastighet" checked>Hastighet [cm/s]
										<br>
										<input type="radio" name="drivetype" value="Acceleration">Acceleration [m/s²]
										<input type="text" name="accehast" value="35"><br>Avstånd [cm]
										<input type="text" name="avstond" value="500"><br>
										<div hidden> <input type="text" name="experiment1" id=exp1><br></div>
										<input name="ok" type="submit" value="Kör">

									</form>
								</section>

							</div>

							<article class="box post">
								<header class="style1">
									<h2>Grafer</h2>
								</header>
								<center>
									<h3>Konstant Hastighet</h3>
								</center>
								cm
								<div id="graphdiv2" style="width:700px; height:400px;"></div>
								<center>sec</center>
								<p><b>Visa: </b>
									<input type=checkbox id=0 onClick="change(this)" checked>
									<label for="0"> cm</label>
									<input type=checkbox id=1 onClick="change(this)">
									<label for="1"> cm/s</label>
								</p>
								<script type="text/javascript">
									g2 = new Dygraph(
										document.getElementById("graphdiv2"),
										"graf.csv", // path to CSV file
										{}          // options
									);
								</script>
								</header><br>
								<center>
									<h3>Konstant Acceleration</h3>
								</center>
								m
								<div id="graphdiv3" style="width:700px; height:400px;"></div>
								<center>sec</center>
								<p><b>Visa: </b>
									<input type=checkbox id=0 onClick="change(this)" checked>
									<label for="0"> m</label>
									<input type=checkbox id=1 onClick="change(this)">
									<label for="1"> m/s</label>
									<input type=checkbox id=2 onClick="change(this)">
									<label for="2"> m/s²</label>
								</p>
								<script type="text/javascript">
									g3 = new Dygraph(
										document.getElementById("graphdiv3"),
										"graf2.csv", // path to CSV file
										{}          // options
									);
									function change(el) {
										g2.setVisibility(el.id, el.checked);
										g3.setVisibility(el.id, el.checked);
									}
								</script>
							</article>
						</div>
					</div>

				</div>
			</div>
		</div>
		<div id="copyright">
			<ul>
				<li>&copy; Newtons andra Vagn.</li>
				<li>Design: <a href="http://html5up.net">HTML5 UP & Hans Juneby</a></li>
			</ul>
		</div>
	</div>
</body>

</html>
<?php      
	if(isset($_GET['ok'])){		
		echo '<script type="text/javascript">'
	   , 'send();'
	   , '</script>'
		;
		$selected_radio = $_GET['drivetype'];
		if($selected_radio=='Hastighet') {	
			$myfile = fopen("newfile.sh", "w") or die("Unable to open file!");
			$txt = $_GET['accehast'];
			$dst = $_GET['avstond'];
			$exp = $_GET['experiment1'];
			fwrite($myfile, "#!/bin/bash ". PHP_EOL);											
			fwrite($myfile, "sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/hastighet.py ");				         				fwrite($myfile, $txt);fwrite($myfile, " ");
			fwrite($myfile, $dst);											
			fwrite($myfile, " & sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/csvwriter.py ");
			fwrite($myfile, $txt);fwrite($myfile, " ");
			fwrite($myfile, $dst);										
			fwrite($myfile, " & sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/experiment.py ");
			fwrite($myfile, $exp);	
			fclose($myfile);
		}					
		else if($selected_radio=='Acceleration') {
			$myfile1 = fopen("newfile.sh", "w") or die("Unable to open file!");
			$txt = $_GET['accehast'];
			$dst = $_GET['avstond'];
			fwrite($myfile1, "#!/bin/bash". PHP_EOL);											
			fwrite($myfile1, "sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/acceleration.py ");	
			fwrite($myfile1, $txt);fwrite($myfile1, " ");
			fwrite($myfile1, $dst);											
			fwrite($myfile1, " & sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/csvwriteracc.py ");
			fwrite($myfile1, $txt);fwrite($myfile1, " ");
			fwrite($myfile1, $dst);										
			fwrite($myfile, " & sudo python /home/pi/wiringPi/WiringPi2-Python/drv8835-motor-driver-rpi/experiment.py ");
			fwrite($myfile, $exp);									
			fclose($myfile1);
		}
	}else   
?>