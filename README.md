# Doctolib_David

### Plan 
#### Les utilisateurs
- Administrateur
  - CRUD comptes patient et médecin
  - attribution des patients
  - il peut consulter les informations sur les patients
- Medecin
  - Peut créer des comptes patients et crud les patients attribués
- Patient
  - Accèder aux formulaires disponibles de la plateforme
  - Consulter l'historique de ces informations

#### Le système d'authentification
- tout les utilisateurs doivent s'identifier
- 1er connexion = mot de passe (8 caractères dont chiffres, lettres minuscules et majuscules ainsi qu’un ou plusieurs symboles)
- 1 id = 1 utilisateur
### La base de données
- Schéma fonctionnel
- SQLite

### Setup
- clone repos
```bash
git clone git@github.com:data-IA-2022/Doctolib_David.git <folder_path>
```
- create env
```bash
python -m venv env 
```
- install requirements
```bash
pip install -r requiements.txt
```
- start tailwind
```bash
cd app && python manage.py tailwind start
```
- start the server
```bash
cd app && python manage.py runserver
```