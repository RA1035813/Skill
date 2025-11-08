const API = "http://127.0.0.1:8000";

function updateKgPerType() {
    fetch(`${API}/type`)
        .then(res => res.json())
        .then(types => {
            let html = '';
            types.forEach(t => {
                html += `<div class="typeblok"><div style="font-size:2rem">${t.type}</div><div><b id="type-${t.type}">0</b> kg</div></div>`;
            });
            const container = document.getElementById('kg-per-type');
            if(container) {
                container.innerHTML = html; // CORRECT: gebruik container die juist is gedefinieerd
            }
        })
        .catch(err => console.error("Fetch error in updateKgPerType:", err));
}

function updateTodayKg() {
    fetch(`${API}/totaal/gewicht`)
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById('today-kg');
            if(container) {
                container.textContent = data.gewicht ?? data; // CORRECT
            }
        })
        .catch(err => console.error("Fetch error in updateTodayKg:", err));
}

function updateTopAfvalTypeAndTable() {
    fetch(`${API}/totaal/overzicht`)
        .then(res => res.json())
        .then(items => {
            const typeCounter = {};
            items.forEach(i => {
                if(i.type && i.gewicht) {
                    typeCounter[i.type] = (typeCounter[i.type] ?? 0) + i.gewicht;
                }
            });
            const topType = Object.entries(typeCounter).sort((a,b) => b[1]-a[1])[0] || ["n.v.t.", 0];
            const topAfvalEl = document.getElementById('top-afvaltype');
            if(topAfvalEl) topAfvalEl.textContent = `${topType[0]} (${topType[1]} kg)`;

            Object.entries(typeCounter).forEach(([type, kg]) => {
                const el = document.getElementById(`type-${type}`);
                if(el) el.textContent = kg;
            });

            let html = '';
            items.slice(-10).reverse().forEach(row => {
                html += `<tr>
                    <td>${row.tijd ? row.tijd.substring(0, 16) : ''}</td>
                    <td>${row.userName || ''}</td>
                    <td>${row.type || ''}</td>
                    <td>${row.gewicht || 0} kg</td>
                </tr>`;
            });
            const tbody = document.querySelector('#recent-afval tbody');
            if(tbody) tbody.innerHTML = html;
        })
        .catch(err => console.error("Fetch error in updateTopAfvalTypeAndTable:", err));
}

function updateTopUsers() {
    fetch(`${API}/totaal/overzicht`)
        .then(res => res.json())
        .then(items => {
            const userCounter = {};
            items.forEach(i => {
                if(i.userName && i.gewicht) {
                    userCounter[i.userName] = (userCounter[i.userName] ?? 0) + i.gewicht;
                }
            });
            const topUsers = Object.entries(userCounter)
                .sort((a,b) => b[1] - a[1])
                .slice(0, 3)
                .map(u => `${u[0]} (${u[1]}kg)`)
                .join(', ');
            const el = document.getElementById('top-users');
            if(el) el.textContent = topUsers;
        })
        .catch(err => console.error("Fetch error in updateTopUsers:", err));
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
