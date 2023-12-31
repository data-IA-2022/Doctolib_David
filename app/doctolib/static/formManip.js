document.addEventListener('DOMContentLoaded', (event) => {
  // On récupère le conteneur du formulaire
  let formContainer = document.getElementById('formContainer');
  // On récupère tous les champs du formulaire (chaque champ est dans un élément <p>)
  let allFields = formContainer.querySelectorAll('p');

  // Une liste pour stocker nos groupes de champs
  let fieldGroups = [];
  // Une variable pour savoir dans quel groupe de champs on se trouve
  let currentGroup = 0;

  // On va diviser les champs en groupes de 3
  for (let i = 0; i < allFields.length; i += 3) {
      // On crée un nouveau div pour chaque groupe de champs
      let fieldGroup = document.createElement('div');
      // On lui donne une classe pour pouvoir le styliser plus tard si besoin
      fieldGroup.className = 'field-group';
      // On cache le groupe pour le moment
      fieldGroup.style.display = 'none';

      // On prend les 3 champs suivants et on les ajoute à ce groupe
      for (let j = 0; j < 3; j++) {
          // On vérifie qu'on n'a pas dépassé le nombre total de champs
          if (i + j < allFields.length) {
              fieldGroup.appendChild(allFields[i + j]);
          }
      }

      // On ajoute ce groupe à notre liste
      fieldGroups.push(fieldGroup);

      // On ajoute ce groupe au formulaire, juste avant le bouton "Suivant"
      formContainer.insertBefore(fieldGroup, document.getElementById("nextBtn"));
  }

  // On affiche le premier groupe de champs
  fieldGroups[currentGroup].style.display = 'block';

  // Quand on clique sur le bouton "Suivant"
  document.getElementById('nextBtn').addEventListener('click', () => {
      // On cache le groupe actuel
      fieldGroups[currentGroup].style.display = 'none';
      // On passe au groupe suivant
      currentGroup++;

      // On vérifie qu'on n'a pas dépassé le nombre total de groupes
      if (currentGroup < fieldGroups.length) {
          // On affiche le nouveau groupe
          fieldGroups[currentGroup].style.display = 'block';

          // Si c'est le dernier groupe, on cache le bouton "Suivant" et on affiche le bouton "Envoyer"
          if (currentGroup == fieldGroups.length - 1) {
              document.getElementById('nextBtn').style.display = 'none';
              document.getElementById('submitBtn').style.display = 'block';
          }
      }
  });
});