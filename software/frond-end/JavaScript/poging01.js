
// const API = "http://localhost:8000";
const API = "http://127.0.0.1:8000"
// Afvaltypes tonen in .afvaltypes
fetch(`${API}/type`)
.then(res => res.json())
.then(types => {
let html = '';
types.forEach(t => {
html += `<div class="typeblok"><div style="font-size:2rem">${t.type}</div><div><b id="type-${t.type}">0</b> kg</div></div>`;
});
document.getElementById('kg-per-type').innerHTML = html;
});

// Totaal afgegeven gewicht vandaag/maand tonen
fetch(`${API}/totaal/gewicht`)
.then(res => res.json())
.then(data => {
document.getElementById('today-kg').textContent = data.totaalgewicht ?? data;
});

// Populairst afvaltype vinden via overzicht
fetch(`${API}/totaal/overzicht`)
.then(res => res.json())
.then(items => {
const typeCounter = {};
items.forEach(i => typeCounter[i.type] = (typeCounter[i.type] ?? 0) + i.gewicht);
let topType = Object.entries(typeCounter).sort((a,b) => b[1]-a[1])[0] ?? ["n.v.t.", 0];
document.getElementById('top-afvaltype').textContent = `${topType[0]} (${topType[1]} kg)`;
// Vul per type totalen in:
Object.entries(typeCounter).forEach(([type,kg]) => {
const el = document.getElementById(`type-${type}`);
if(el) el.textContent = kg;
});
// Laatste afvalrecords in tabel
let html = '';
items.slice(-10).reverse().forEach(row => {
html += `<tr>
    <td>${row.tijd?.substring(0, 16) || ''}</td>
    <td>${row.userName || ''}</td>
    <td>${row.type}</td>
    <td>${row.gewicht} kg</td>
  </tr>`;
});
document.querySelector('#recent-afval tbody').innerHTML = html;
});

// Eventueel: Top gebruikers berekenen
fetch(`${API}/totaal/overzicht`)
.then(res => res.json())
.then(items => {
const userCounter = {};
items.forEach(i => userCounter[i.userName] = (userCounter[i.userName] ?? 0) + i.gewicht);
let topUsers = Object.entries(userCounter)
.sort((a,b)=>b[1]-a[1])
.slice(0,3)
.map(u => `${u[0]} (${u[1]}kg)`).join(', ');
document.getElementById('top-users').textContent = topUsers;
});

