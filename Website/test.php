<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
</head>

<style>
	/* table tr:last-child td{
		padding: 1%
	} */
</style>

<body>
	<table border="1" style="border-collapse: collapse">
		<?php
		for($i=1;$i<=10;$i++) {
			echo "<tr>";
			for($j=1;$j<=10;$j++) {
				echo "<td style='text-align: center; padding:5px;'>$i * $j = ". $i*$j."</td>";
			}
			echo "</tr>\n";
		}
		?>
	</table>
	</body>
</html>
