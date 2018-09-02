
<?php
include("connect.php");
$categoryid=$_GET['id'];
mysqli_query($con,"delete from category where categoryid='$categoryid'");
?>
<script>
alert("data deleted successfully");
window.location="viewcategory.php";
</script>