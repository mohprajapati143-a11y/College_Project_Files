<?php
function checkEvenOdd($num) {
 if ($num % 2 == 0) {
 return "$num is Even";
 } else {
 return "$num is Odd";
 }
}
echo checkEvenOdd(7);
?>