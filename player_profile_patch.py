from pathlib import Path
f=Path("index.html")
html=f.read_text()

html=html.replace(
'onclick="showPlayerHistory(\'${row.player}\')"',
'onclick="showPlayerProfile(\'${row.player}\')"'
)

css='''
.profile-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px}
.stat-box{background:var(--surface);padding:12px;border-radius:10px;text-align:center}
.stat-box .v{font-size:24px;font-weight:700;color:var(--gold)}
.stat-box .l{font-size:11px;color:var(--muted)}
.profile-header{text-align:center;margin-bottom:20px}
.profile-name{font-size:28px;font-weight:800}
.profile-link{margin-top:15px}
'''

html=html.replace('</style>',css+'</style>')

modal='''
<div id="playerProfileModal" class="modal">
<div class="modal-card" style="width:min(1000px,95%)">
<div class="modal-head">
<h3 id="profileTitle">Player Profile</h3>
<button class="btn-sm red" onclick="closePlayerProfile()">Close</button>
</div>
<div class="modal-body" id="profileBody"></div>
</div>
</div>
'''

html=html.replace('</body>',modal+'''
<script>

function getPlayerStats(player){

 let stats={
 matches:0,wins:0,draws:0,losses:0,
 gf:0,ga:0
 };

 state.groupMatches.forEach(m=>{

   if(!m.played) return;

   const isHome=PLAYERS[m.homeIdx]===player;
   const isAway=PLAYERS[m.awayIdx]===player;

   if(!isHome && !isAway) return;

   stats.matches++;

   const gf=isHome?m.homeGoals:m.awayGoals;
   const ga=isHome?m.awayGoals:m.homeGoals;

   stats.gf+=gf;
   stats.ga+=ga;

   if(gf>ga) stats.wins++;
   else if(gf<ga) stats.losses++;
   else stats.draws++;
 });

 stats.gd=stats.gf-stats.ga;
 stats.winpct=stats.matches?Math.round((stats.wins/stats.matches)*100):0;

 let trophies=0;

 if(state.championsHistory){
   state.championsHistory.forEach(c=>{
      if(c.champion===player) trophies++;
   });
 }

 stats.trophies=trophies;

 return stats;
}

function showPlayerProfile(player){

 const pick=state.picks[player];
 const s=getPlayerStats(player);

 document.getElementById("profileTitle").innerHTML=
 pick.flag+" "+player+" Profile";

 document.getElementById("profileBody").innerHTML=`

 <div class="profile-header">
   <div class="profile-name">${player}</div>
   <div>${pick.country}</div>
 </div>

 <div class="profile-grid">

   <div class="stat-box">
      <div class="v">${s.matches}</div>
      <div class="l">Matches</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.wins}</div>
      <div class="l">Wins</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.draws}</div>
      <div class="l">Draws</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.losses}</div>
      <div class="l">Losses</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.gf}</div>
      <div class="l">Goals For</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.ga}</div>
      <div class="l">Goals Against</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.gd}</div>
      <div class="l">Goal Diff</div>
   </div>

   <div class="stat-box">
      <div class="v">${s.trophies}</div>
      <div class="l">World Cups</div>
   </div>

 </div>

 <div class="text-center">
    <button class="btn-sm green profile-link"
      onclick="closePlayerProfile();showPlayerHistory('${player}')">
      View Match History
    </button>
 </div>
 `;
 document.getElementById("playerProfileModal").classList.add("show");
}

function closePlayerProfile(){
 document.getElementById("playerProfileModal").classList.remove("show");
}

</script>
</body>
''')

f.write_text(html)
print("PATCH APPLIED")
