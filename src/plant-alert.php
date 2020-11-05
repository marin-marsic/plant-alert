<?php
$old_path = getcwd();
chdir('/home/marin/Documents/plant-alert/src/');
$output = shell_exec('python3 refresh.py');
chdir($old_path);
$output = str_replace("\n", "<br>", $output);
echo $output
?>

