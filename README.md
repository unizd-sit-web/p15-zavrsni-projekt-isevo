# Zavrsni projekt
Projekt se sastoji od stranice index.html na kojoj se nalaze tri kviza. Klikom na sliku otvara se kviz.Nakon sto se odgovori na pitanja i
klikne na button u dnu stranice, prikazuje se poruka. Na vrhu index.html se nalazi padajuci izbornik na kojem se korisnik moze ulogirati 
kako bi dobivao obavijesti na mail. Podaci se spremaju u bazu. Ulogirani korisnik moze vidjeti ostale koji su ulogirani i pretraziti 
korisnike u tablici. Skripta CreateDateBase.py omogucuje stvaranje SQLite baze.
(employee.db je baza koju sam ja napravila pa nije potrebno pokreteti CreateDataBase.py)

## Pokretanje
<ol>
<li>instalacija virtualnog okruzenja:python -m venv venv </li>
<li>venv\Scripts\activate</li>
<li> instalirati sve sa requirements.txt : pip install -r requirements.txt</li>
<li>set FLASK_APP=app.py</li>
<li>set FLASK_DEBUG=1</li>
<li>flask run</li>
<li> u browser upisati:  http://127.0.0.1:5000/ .</li>
</ol>

