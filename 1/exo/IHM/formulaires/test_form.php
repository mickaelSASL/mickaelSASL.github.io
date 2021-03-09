<html>
	<head>
		<title>TEST Formulaire</title>
		<meta charset="utf-8">
	</head>

	<body>


<form method="post" action="https://nsi-sasl.alwaysdata.net/exo/IHM/formulaires/test_form.php" style="background-color:#ADD8E6;">
 
   <fieldset>
       <legend>Vos coordonnées</legend> <!-- Titre du fieldset --> 

       <label for="nom">Quel est votre nom ?</label><span style="background-color:yellow;"><? echo $_POST['nom'] ;?><? echo $_GET['nom'] ;?></span></br>
       <label for="prenom">Quel est votre prénom ?</label><span style="background-color:yellow;"><? echo $_POST['prenom'] ;?><? echo $_GET['prenom'] ;?></span></br> 
       <label for="email">Quel est votre e-mail ?</label><span style="background-color:yellow;"><? echo $_POST['email'] ;?><? echo $_GET['email'] ;?></span>

   </fieldset>
 
   <fieldset>
       <legend>Votre souhait</legend> <!-- Titre du fieldset -->
 
       <p>
           Faites un souhait que vous voudriez voir exaucé :<span style="background-color:yellow;"><? echo $_POST['souhait'] ;?><? echo $_GET['souhait'] ;?></p></span>
 
       <p>
           <label for="precisions">Si "Autre", veuillez préciser :</label><span style="background-color:yellow;"><? echo $_POST['precisions'] ;?><? echo $_GET['precisions'] ;?></textarea></span>
       </p>
   </fieldset>
</form>

</body>
</html>