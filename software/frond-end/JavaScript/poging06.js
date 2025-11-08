const API = "http://127.0.0.1:8000";

function updateKgPerType() {
    fetch(`${API}/type`)
        .then(res => res.json())
        .then(data => {
            console.log('updateKgPerType data:', data);
            // data.types is de array met items volgens backend response
            let html = '';
            (data.types || []).forEach(t => {
                html += `<div class="typeblok">
                    <div style="font-size:2rem">${t.afvaltype || t.type || 'Onbekend'}</div>
                    <div><b id="type-${t.afvaltype || t.type || 'Onbekend'}">0</b> kg</div>
                </div>`;
            });
            const container = document.getElementById('kg-per-type');
            if (container) container.innerHTML = html;
        })
        .catch(err => console.error("Fetch error updateKgPerType:", err));
}

function updateTodayKg() {
    fetch(`${API}/totaal/gewicht`)
        .then(res => res.json())
        .then(data => {
            console.log('updateTodayKg data:', data);
            const gewichten = data.gewicht || [];
            let totaal = 0;
            gewichten.forEach(item => {
                totaal += item.totaal_gewicht || 0;
            });
            const container = document.getElementById('today-kg');
            if (container) container.textContent = totaal.toFixed(2);
        })
        .catch(err => console.error("Fetch error updateTodayKg:", err));
}

function updateTopAfvalTypeAndTable() {
    fetch(`${API}/totaal/overzicht`)
        .then(res => res.json())
        .then(data => {
            console.log('updateTopAfvalTypeAndTable data:', data);
            const items = data.overzicht || [];

            const typeCounter = {};
            items.forEach(i => {
                if(i.type && i.gewicht) {
                    typeCounter[i.type] = (typeCounter[i.type] || 0) + i.gewicht;
                }
            });

            let topTypeEntry = ["N.v.t.", 0];
            if (Object.keys(typeCounter).length > 0) {
                topTypeEntry = Object.entries(typeCounter).sort((a, b) => b[1] - a[1])[0];
            }

            const topAfvalEl = document.getElementById('top-afvaltype');
            if(topAfvalEl) topAfvalEl.textContent = `${topTypeEntry[0]} (${topTypeEntry[1].toFixed(2)} kg)`;

            Object.entries(typeCounter).forEach(([type, kg]) => {
                const el = document.getElementById(`type-${type}`);
                if(el) el.textContent = kg.toFixed(2);
            });

            let html = '';
            // Laatste 10 items tonen in tabel
            items.slice(-10).reverse().forEach(row => {
                html += `<tr>
                    <td>${row.maand || (row.tijd ? row.tijd.substring(0, 16) : '')}</td>
                    <td>${row.userName || ''}</td>
                    <td>${row.type || ''}</td>
                    <td>${row.gewicht != null ? row.gewicht.toFixed(2) : 0} kg</td>
                </tr>`;
            });
            const tbody = document.querySelector('#recent-afval tbody');
            if (tbody) tbody.innerHTML = html;
        })
        .catch(err => console.error("Fetch error updateTopAfvalTypeAndTable:", err));
}

function updateTopUsers() {
    fetch(`${API}/totaal/overzicht`)
        .then(res => res.json())
        .then(data => {
            console.log('updateTopUsers data:', data);
            const items = data.overzicht || [];
            const userCounter = {};
            items.forEach(i => {
                if(i.userName && i.gewicht) {
                    userCounter[i.userName] = (userCounter[i.userName] || 0) + i.gewicht;
                }
            });

            const topUsers = Object.entries(userCounter)
                .sort((a,b) => b[1] - a[1])
                .slice(0, 3)
                .map(([u, kg]) => `${u} (${kg.toFixed(2)}kg)`)
                .join(', ');

            const el = document.getElementById('top-users');
            if(el) el.textContent = topUsers || "Geen gebruikers data";
        })
        .catch(err => console.error("Fetch error updateTopUsers:", err));
}

document.addEventListener("DOMContentLoaded", () => {
    updateKgPerType();
    updateTodayKg();
    updateTopAfvalTypeAndTable();
    updateTopUsers();

    const btnUsers = document.getElementById('btn-refresh-users');
    if (btnUsers) {
        btnUsers.addEventListener('click', () => {
            updateTopUsers();
            alert("Top gebruikers geüpdatet!");
        });
    }

    const btnStats = document.getElementById('btn-refresh-stats');
    if (btnStats) {
        btnStats.addEventListener('click', () => {
            updateTopAfvalTypeAndTable();
            updateTodayKg();
            updateKgPerType();
            alert("Statistieken geüpdatet!");
        });
    }
});
