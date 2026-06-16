from pathlib import Path

f=Path("index.html")
html=f.read_text()

old='''
<button class="btn-sm red" onclick="closeHistory()">Close</button>
'''

new='''
<div style="display:flex;gap:10px">
<button class="btn-sm" onclick="closeHistory();showPlayerProfile(document.getElementById('historyTitle').textContent.replace(' Match History',''))">← Back</button>
<button class="btn-sm red" onclick="closeHistory()">Close</button>
</div>
'''

html=html.replace(old,new)

marker='''
<div class="text-center">
     <button class="btn-sm green profile-link"
'''

insert='''
<hr style="margin:25px 0;border-color:#24304d">

<h3 style="margin-bottom:15px">Season Statistics</h3>

<div class="profile-grid">

<div class="stat-box">
<div class="v">${s.matches}</div>
<div class="l">Season 2 Matches</div>
</div>

<div class="stat-box">
<div class="v">${s.wins+s.draws*0}</div>
<div class="l">Points Earned</div>
</div>

<div class="stat-box">
<div class="v">${s.winpct}%</div>
<div class="l">Win Rate</div>
</div>

<div class="stat-box">
<div class="v">${s.trophies}</div>
<div class="l">Career Titles</div>
</div>

</div>

<div style="margin-top:20px;background:var(--surface);padding:15px;border-radius:10px">
<b>Current Season:</b> Season 2<br>
<b>Nation:</b> ${pick.flag} ${pick.country}<br>
<b>Career World Cups:</b> ${s.trophies}
</div>

<div class="text-center">
<button class="btn-sm green profile-link"
'''

html=html.replace(marker,insert)

f.write_text(html)

print("SEASON PROFILE UPGRADE APPLIED")
