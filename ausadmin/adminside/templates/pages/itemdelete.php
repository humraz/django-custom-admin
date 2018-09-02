
<?php
include("connect.php");
$itemid=$_GET['id'];
mysqli_query($con,"delete from item where itemid='$itemid'");
?>
<script>
alert("data deleted successfully");
window.location="viewitem.php";
</script>