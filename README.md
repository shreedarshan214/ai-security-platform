 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>AI Autonomous Security Platform — Project Showcase</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
  :root{
    --bg:#F5F0E4;
    --bg-panel:#FFFFFF;
    --bg-panel-2:#FBF7ED;
    --line:#E1D8C3;
    --cyan:#0E7D6E;
    --cyan-dim:#5C9A8F;
    --amber:#B8790F;
    --red:#C43B3B;
    --blue:#2A63C7;
    --text:#22292E;
    --text-dim:#6B6459;
    --mono: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
    --sans: -apple-system, BlinkMacSystemFont, 'Segoe UI', Inter, Roboto, sans-serif;
  }
  *{box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  body{
    margin:0;
    background:
      radial-gradient(circle at 15% 0%, rgba(14,125,110,0.06), transparent 40%),
      radial-gradient(circle at 85% 20%, rgba(42,99,199,0.05), transparent 45%),
      var(--bg);
    color:var(--text);
    font-family:var(--sans);
    -webkit-font-smoothing:antialiased;
    overflow-x:hidden;
  }
  .grid-overlay{
    position:fixed; inset:0; pointer-events:none; z-index:0; opacity:0.5;
    background-image:
      linear-gradient(rgba(34,41,46,0.045) 1px, transparent 1px),
      linear-gradient(90deg, rgba(34,41,46,0.045) 1px, transparent 1px);
    background-size: 42px 42px;
    mask-image: radial-gradient(ellipse 80% 60% at 50% 0%, black 40%, transparent 90%);
  }
  section{position:relative; z-index:1; padding:96px 8vw;}
  @media (max-width:720px){ section{padding:64px 6vw;} }

  /* ---------- HERO ---------- */
  .hero{
    min-height:100vh;
    display:flex; flex-direction:column; justify-content:center;
    padding-top:64px;
  }
  .kernel{
    font-family:var(--mono);
    font-size:12.5px;
    color:var(--cyan-dim);
    line-height:1.75;
    white-space:pre-wrap;
    border-left:2px solid var(--line);
    padding-left:18px;
    min-height:150px;
    max-width:640px;
  }
  .kernel .ok{color:var(--cyan);}
  .cursor{display:inline-block; width:8px; height:15px; background:var(--cyan); vertical-align:-2px; animation:blink 1s steps(1) infinite;}
  @keyframes blink{50%{opacity:0;}}

  h1.title{
    font-family:var(--sans);
    font-weight:800;
    font-size:clamp(34px, 6vw, 76px);
    line-height:1.02;
    letter-spacing:-0.02em;
    margin:28px 0 10px 0;
    max-width:920px;
    opacity:0;
  }
  h1.title span{color:var(--cyan);}
  .subtitle{
    font-family:var(--mono);
    font-size:clamp(13px,1.6vw,16px);
    color:var(--text-dim);
    max-width:640px;
    margin:0 0 34px 0;
    opacity:0;
  }
  .badge-row{display:flex; flex-wrap:wrap; gap:10px; opacity:0;}
  .badge{
    font-family:var(--mono); font-size:12px; padding:6px 12px;
    border:1px solid var(--line); border-radius:3px; color:var(--text-dim);
    background:rgba(34,41,46,0.02);
  }
  .badge b{color:var(--cyan); font-weight:600;}

  .fade-in-up{animation:fadeInUp 0.7s ease forwards;}
  @keyframes fadeInUp{from{opacity:0; transform:translateY(14px);} to{opacity:1; transform:translateY(0);}}

  .scroll-cue{
    position:absolute; bottom:34px; left:8vw; font-family:var(--mono); font-size:11px; color:var(--text-dim);
    display:flex; align-items:center; gap:8px; opacity:0;
  }
  .scroll-cue .line{width:28px; height:1px; background:var(--text-dim); animation:pulseline 2s ease-in-out infinite;}
  @keyframes pulseline{0%,100%{opacity:0.3;} 50%{opacity:1;}}

  /* ---------- SECTION HEADERS ---------- */
  .eyebrow{
    font-family:var(--mono); font-size:12px; color:var(--cyan); letter-spacing:0.04em; margin-bottom:10px;
  }
  h2.h{
    font-family:var(--sans); font-weight:700; font-size:clamp(24px,3.2vw,38px);
    letter-spacing:-0.01em; margin:0 0 14px 0; max-width:680px;
  }
  p.lead{color:var(--text-dim); max-width:600px; font-size:15.5px; line-height:1.65; margin:0 0 48px 0;}

  .reveal{opacity:0; transform:translateY(24px); transition:opacity 0.7s ease, transform 0.7s ease;}
  .reveal.in{opacity:1; transform:translateY(0);}

  /* ---------- PIPELINE ---------- */
  .pipeline-wrap{
    background:var(--bg-panel);
    border:1px solid var(--line);
    border-radius:8px;
    padding:34px 20px;
    overflow-x:auto;
  }
  svg.pipeline{display:block; min-width:900px; width:100%; height:auto;}
  .node-box{fill:var(--bg-panel-2); stroke:var(--line); stroke-width:1.2; rx:6;}
  .node-box.active{stroke:var(--cyan);}
  .node-label{font-family:var(--mono); font-size:12px; fill:var(--text);}
  .node-sub{font-family:var(--mono); font-size:9.5px; fill:var(--text-dim);}
  .flow-path{fill:none; stroke:var(--line); stroke-width:1.4;}
  .flow-pulse{fill:none; stroke:var(--cyan); stroke-width:2; stroke-dasharray:10 340; filter:drop-shadow(0 0 4px rgba(14,125,110,0.6));}

  /* ---------- STATS ---------- */
  .stat-grid{display:grid; grid-template-columns:repeat(5,1fr); gap:1px; background:var(--line); border:1px solid var(--line); border-radius:8px; overflow:hidden;}
  @media (max-width:820px){.stat-grid{grid-template-columns:repeat(2,1fr);}}
  .stat-cell{background:var(--bg-panel); padding:26px 20px; text-align:left;}
  .stat-num{font-family:var(--sans); font-weight:800; font-size:clamp(28px,3.4vw,42px); line-height:1;}
  .stat-num.crit{color:var(--red);} .stat-num.high{color:var(--amber);} .stat-num.med{color:var(--blue);} .stat-num.low{color:var(--cyan);}
  .stat-label{font-family:var(--mono); font-size:11px; color:var(--text-dim); margin-top:8px; letter-spacing:0.03em;}

  .split{display:grid; grid-template-columns:1.1fr 0.9fr; gap:28px; margin-top:28px;}
  @media (max-width:820px){.split{grid-template-columns:1fr;}}
  .panel{background:var(--bg-panel); border:1px solid var(--line); border-radius:8px; padding:22px;}
  .panel-title{font-family:var(--mono); font-size:12px; color:var(--text-dim); margin-bottom:16px; letter-spacing:0.03em;}

  .target-row{display:flex; align-items:center; gap:12px; padding:9px 0; border-bottom:1px solid var(--line); font-family:var(--mono); font-size:12.5px;}
  .target-row:last-child{border-bottom:none;}
  .target-bar{flex:1; height:7px; background:#EAE2CE; border-radius:3px; overflow:hidden;}
  .target-bar i{display:block; height:100%; background:linear-gradient(90deg, var(--red), #ff8080); width:0%; border-radius:3px; transition:width 1.2s cubic-bezier(.2,.8,.2,1);}

  .donut-wrap{display:flex; align-items:center; justify-content:center; gap:28px; flex-wrap:wrap;}
  .legend{font-family:var(--mono); font-size:12px; color:var(--text-dim); display:flex; flex-direction:column; gap:10px;}
  .legend .dot{display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:8px;}

  /* ---------- ALERT FEED ---------- */
  .feed{display:flex; flex-direction:column; gap:16px; max-width:640px;}
  .alert-card{
    background:var(--bg-panel); border:1px solid var(--line); border-left:3px solid var(--red);
    border-radius:6px; padding:18px 20px; font-family:var(--mono); font-size:12.5px; line-height:1.75;
  }
  .alert-card.high{border-left-color:var(--amber);}
  .alert-card.medium{border-left-color:var(--blue);}
  .a-top{display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;}
  .a-title{color:var(--text); font-weight:600; letter-spacing:0.02em;}
  .a-title.high{color:var(--amber);} .a-title.crit{color:var(--red);} .a-title.med{color:var(--blue);}
  .a-time{color:var(--text-dim); font-size:11px;}
  .a-row{color:var(--text-dim);}
  .a-row b{color:var(--text); font-weight:600;}
  .a-reason{margin-top:8px; color:#5A5347; border-top:1px dashed var(--line); padding-top:8px;}
  .typewrite{overflow:hidden; white-space:nowrap; width:0; display:inline-block; vertical-align:top;}

  /* ---------- STACK ---------- */
  .stack-grid{display:grid; grid-template-columns:repeat(auto-fit, minmax(150px,1fr)); gap:1px; background:var(--line); border:1px solid var(--line); border-radius:8px; overflow:hidden;}
  .stack-cell{background:var(--bg-panel); padding:20px; font-family:var(--mono); font-size:12.5px; color:var(--text-dim); text-align:center;}
  .stack-cell b{display:block; color:var(--text); font-size:14px; margin-bottom:3px;}

  footer{padding:40px 8vw 60px; font-family:var(--mono); font-size:11.5px; color:var(--text-dim); border-top:1px solid var(--line); display:flex; justify-content:space-between; flex-wrap:wrap; gap:10px;}
  footer .dotlive{display:inline-block; width:7px; height:7px; border-radius:50%; background:var(--cyan); margin-right:7px; box-shadow:0 0 6px var(--cyan); animation:blink 1.6s ease-in-out infinite;}
</style>
</head>
<body>

<div class="grid-overlay"></div>

<!-- ================= HERO ================= -->
<section class="hero">
  <div class="kernel" id="kernel"></div>
  <h1 class="title" id="titleEl">AI Autonomous <span>Security Platform</span></h1>
  <p class="subtitle" id="subEl">soc / threat-intelligence / attack-surface-management — automated detect → enrich → decide → respond pipeline</p>
  <div class="badge-row" id="badgeEl">
    <div class="badge"><b>Python</b> · Flask</div>
    <div class="badge"><b>n8n</b> · orchestration</div>
    <div class="badge"><b>Nmap</b> · ASM</div>
    <div class="badge"><b>VirusTotal API</b> · enrichment</div>
    <div class="badge"><b>Telegram</b> · alerting</div>
  </div>
  <div class="scroll-cue" id="scrollCue"><div class="line"></div>scroll to see the pipeline in action</div>
</section>

<!-- ================= PIPELINE ================= -->
<section id="pipeline-section">
  <div class="eyebrow reveal">01 — Architecture</div>
  <h2 class="h reveal">Every target flows through one automated decision pipeline</h2>
  <p class="lead reveal">A webhook triggers scans, an AI agent reasons over the findings, VirusTotal enriches indicators, and correlation logic decides whether to block, monitor, or allow — before dispatching alerts.</p>
  <div class="pipeline-wrap reveal">
    <svg class="pipeline" viewBox="0 0 920 220" xmlns="http://www.w3.org/2000/svg">
      <!-- connecting paths -->
      <path id="p1" class="flow-path" d="M 110 110 H 210"/>
      <path id="p2" class="flow-path" d="M 310 110 H 410"/>
      <path id="p3" class="flow-path" d="M 510 110 H 610"/>
      <path id="p4" class="flow-path" d="M 710 110 H 810"/>
      <path id="pulse1" class="flow-pulse" d="M 110 110 H 210"/>
      <path id="pulse2" class="flow-pulse" d="M 310 110 H 410"/>
      <path id="pulse3" class="flow-pulse" d="M 510 110 H 610"/>
      <path id="pulse4" class="flow-pulse" d="M 710 110 H 810"/>

      <!-- nodes -->
      <g>
        <rect class="node-box" x="10" y="80" width="100" height="60" rx="6"/>
        <text class="node-label" x="60" y="106" text-anchor="middle">Webhook</text>
        <text class="node-sub" x="60" y="122" text-anchor="middle">scan trigger</text>
      </g>
      <g>
        <rect class="node-box" x="210" y="80" width="100" height="60" rx="6"/>
        <text class="node-label" x="260" y="106" text-anchor="middle">AI Agent</text>
        <text class="node-sub" x="260" y="122" text-anchor="middle">LLM reasoning</text>
      </g>
      <g>
        <rect class="node-box" x="410" y="80" width="100" height="60" rx="6"/>
        <text class="node-label" x="460" y="106" text-anchor="middle">VT Enrich</text>
        <text class="node-sub" x="460" y="122" text-anchor="middle">reputation lookup</text>
      </g>
      <g>
        <rect class="node-box" x="610" y="80" width="100" height="60" rx="6"/>
        <text class="node-label" x="660" y="106" text-anchor="middle">Correlate</text>
        <text class="node-sub" x="660" y="122" text-anchor="middle">block / monitor</text>
      </g>
      <g>
        <rect class="node-box" x="810" y="80" width="100" height="60" rx="6"/>
        <text class="node-label" x="860" y="102" text-anchor="middle">Dispatch</text>
        <text class="node-sub" x="860" y="118" text-anchor="middle">Telegram +</text>
        <text class="node-sub" x="860" y="130" text-anchor="middle">Sheets log</text>
      </g>
    </svg>
  </div>
</section>

<!-- ================= DASHBOARD ================= -->
<section id="stats-section">
  <div class="eyebrow reveal">02 — Live SOC Dashboard</div>
  <h2 class="h reveal">Severity, targets, and risk — at a glance</h2>
  <p class="lead reveal">Every scan result lands in a running dashboard: record volume, severity breakdown, and the targets generating the most activity.</p>

  <div class="stat-grid reveal">
    <div class="stat-cell"><div class="stat-num" data-count="14">0</div><div class="stat-label">RECORD COUNT</div></div>
    <div class="stat-cell"><div class="stat-num crit" data-count="2">0</div><div class="stat-label">CRITICAL ALERTS</div></div>
    <div class="stat-cell"><div class="stat-num high" data-count="2">0</div><div class="stat-label">HIGH</div></div>
    <div class="stat-cell"><div class="stat-num med" data-count="2">0</div><div class="stat-label">MEDIUM</div></div>
    <div class="stat-cell"><div class="stat-num low" data-count="2">0</div><div class="stat-label">LOW</div></div>
  </div>

  <div class="split">
    <div class="panel reveal">
      <div class="panel-title">TOP TARGETS BY RECORD COUNT</div>
      <div class="target-row"><span>google.com</span><div class="target-bar"><i data-w="92" style="width:0"></i></div></div>
      <div class="target-row"><span>www.google.com</span><div class="target-bar"><i data-w="70" style="width:0"></i></div></div>
    </div>
    <div class="panel reveal">
      <div class="panel-title">SEVERITY DISTRIBUTION</div>
      <div class="donut-wrap">
        <svg width="150" height="150" viewBox="0 0 42 42">
          <circle cx="21" cy="21" r="15.9" fill="transparent" stroke="#EAE2CE" stroke-width="7"/>
          <circle id="donutHigh" cx="21" cy="21" r="15.9" fill="transparent" stroke="var(--blue)" stroke-width="7"
                  stroke-dasharray="0 100" stroke-dashoffset="25" transform="rotate(-90 21 21)"/>
          <circle id="donutCrit" cx="21" cy="21" r="15.9" fill="transparent" stroke="var(--red)" stroke-width="7"
                  stroke-dasharray="0 100" stroke-dashoffset="25" transform="rotate(-90 21 21)"/>
        </svg>
        <div class="legend">
          <div><span class="dot" style="background:var(--blue)"></span>high — 64.3%</div>
          <div><span class="dot" style="background:var(--red)"></span>critical — 35.7%</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= ALERT FEED ================= -->
<section id="feed-section">
  <div class="eyebrow reveal">03 — Automated Alerting</div>
  <h2 class="h reveal">Decisions reach the team the moment they're made</h2>
  <p class="lead reveal">Every verdict — block, monitor, or allow — is pushed straight to Telegram with the target, priority, risk score, and the model's reasoning, and logged to a sheet for audit.</p>

  <div class="feed">
    <div class="alert-card reveal" data-severity="crit">
      <div class="a-top"><span class="a-title crit">🚨 CRITICAL — BLOCK</span><span class="a-time">P1</span></div>
      <div class="a-row"><b>Target:</b> scanme.nmap.org</div>
      <div class="a-row"><b>Risk Score:</b> 100 &nbsp; <b>Threat:</b> port scanning</div>
      <div class="a-row"><b>Attack Stage:</b> reconnaissance</div>
      <div class="a-reason">reason: <span class="typewrite" data-text="critical risk score of 100 indicates immediate threat; blocking to prevent potential exploitation."></span></div>
    </div>
    <div class="alert-card high reveal" data-severity="high">
      <div class="a-top"><span class="a-title high">⚠ HIGH — MONITOR</span><span class="a-time">P2</span></div>
      <div class="a-row"><b>Target:</b> google.com</div>
      <div class="a-row"><b>VirusTotal:</b> malicious 0 / suspicious 0</div>
      <div class="a-reason">reason: <span class="typewrite" data-text="high ai score with a clean vt result; mapping rules require monitoring rather than a hard block."></span></div>
    </div>
    <div class="alert-card medium reveal" data-severity="med">
      <div class="a-top"><span class="a-title med">◉ MEDIUM — ALLOW</span><span class="a-time">P3</span></div>
      <div class="a-row"><b>Target:</b> 185.199.108.153</div>
      <div class="a-row"><b>VirusTotal:</b> clean across all engines</div>
      <div class="a-reason">reason: <span class="typewrite" data-text="no correlated indicators found; logged for audit trail only."></span></div>
    </div>
  </div>
</section>

<!-- ================= STACK ================= -->
<section id="stack-section">
  <div class="eyebrow reveal">04 — Built With</div>
  <h2 class="h reveal">Stack</h2>
  <div class="stack-grid reveal">
    <div class="stack-cell"><b>Python / Flask</b>APIs & scan logic</div>
    <div class="stack-cell"><b>n8n</b>workflow orchestration</div>
    <div class="stack-cell"><b>Nmap</b>attack surface mapping</div>
    <div class="stack-cell"><b>VirusTotal API</b>indicator enrichment</div>
    <div class="stack-cell"><b>Telegram Bot API</b>real-time alerting</div>
    <div class="stack-cell"><b>Google Sheets</b>alert logging</div>
  </div>
</section>

<footer>
  <div><span class="dotlive"></span>AI Autonomous Security Platform — SOC, Threat Intelligence &amp; ASM</div>
  <div>Shree · M.E. Cyber Security, KCT</div>
</footer>

<script>
// ---------- HERO KERNEL BOOT TYPE ----------
const kernelLines = [
  "$ init soc-pipeline --mode autonomous",
  "[ok] webhook listener attached",
  "[ok] ai agent loaded (decision engine)",
  "[ok] virustotal enrichment online",
  "[ok] correlation ruleset compiled",
  "[ok] telegram dispatch channel connected",
  "> ready."
];
const kernelEl = document.getElementById('kernel');
let li = 0, ci = 0, buffer = "";
function typeKernel(){
  if(li >= kernelLines.length){
    kernelEl.innerHTML = buffer + '<span class="cursor"></span>';
    revealHero();
    return;
  }
  const line = kernelLines[li];
  if(ci <= line.length){
    let shown = buffer + line.slice(0, ci);
    let cls = line.startsWith('[ok]') ? 'ok' : '';
    kernelEl.innerHTML = (cls ? buffer + '<span class="ok">'+line.slice(0,ci)+'</span>' : shown) + '<span class="cursor"></span>';
    ci++;
    setTimeout(typeKernel, line.startsWith('$') ? 38 : 14);
  } else {
    buffer += (line.startsWith('[ok]') ? '<span class="ok">'+line+'</span>' : line) + '\n';
    li++; ci = 0;
    setTimeout(typeKernel, 90);
  }
}
function revealHero(){
  document.getElementById('titleEl').classList.add('fade-in-up');
  setTimeout(()=>document.getElementById('subEl').classList.add('fade-in-up'), 200);
  setTimeout(()=>document.getElementById('badgeEl').classList.add('fade-in-up'), 380);
  setTimeout(()=>document.getElementById('scrollCue').classList.add('fade-in-up'), 560);
}
setTimeout(typeKernel, 300);

// ---------- SCROLL REVEALS ----------
const revealEls = document.querySelectorAll('.reveal');
const io = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.classList.add('in');
      io.unobserve(e.target);
    }
  });
}, {threshold:0.2});
revealEls.forEach(el=>io.observe(el));

// ---------- PIPELINE PULSE (looping) ----------
function loopPulse(id, delay){
  const el = document.getElementById(id);
  let offset = 350;
  function anim(){
    offset -= 6;
    if(offset < -20) offset = 350;
    el.style.strokeDashoffset = offset;
    requestAnimationFrame(anim);
  }
  setTimeout(()=>requestAnimationFrame(anim), delay);
}
['pulse1','pulse2','pulse3','pulse4'].forEach((id,i)=>loopPulse(id, i*260));

// ---------- STAT COUNTERS ----------
const statObserver = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      const target = +e.target.dataset.count;
      let cur = 0;
      const step = Math.max(1, Math.round(target/24));
      const t = setInterval(()=>{
        cur += step;
        if(cur >= target){ cur = target; clearInterval(t); }
        e.target.textContent = cur;
      }, 40);
      statObserver.unobserve(e.target);
    }
  });
}, {threshold:0.4});
document.querySelectorAll('.stat-num').forEach(el=>statObserver.observe(el));

// ---------- TARGET BARS ----------
const barObserver = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      e.target.querySelectorAll('.target-bar i').forEach(bar=>{
        bar.style.width = bar.dataset.w + '%';
      });
      barObserver.unobserve(e.target);
    }
  });
}, {threshold:0.3});
document.querySelectorAll('.panel').forEach(p=>barObserver.observe(p));

// ---------- DONUT ----------
const donutObserver = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      document.getElementById('donutHigh').style.transition = 'stroke-dasharray 1.4s ease';
      document.getElementById('donutHigh').setAttribute('stroke-dasharray','64.3 100');
      const crit = document.getElementById('donutCrit');
      crit.style.transition = 'stroke-dasharray 1.4s ease';
      crit.setAttribute('stroke-dashoffset', (25 - 64.3).toString());
      crit.setAttribute('stroke-dasharray','35.7 100');
      donutObserver.unobserve(e.target);
    }
  });
}, {threshold:0.4});
document.querySelectorAll('.donut-wrap').forEach(d=>donutObserver.observe(d));

// ---------- ALERT CARD TYPEWRITER ----------
const twObserver = new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      const spans = e.target.querySelectorAll('.typewrite');
      spans.forEach(span=>{
        const text = span.dataset.text;
        let i = 0;
        span.style.whiteSpace = 'normal';
        function type(){
          if(i <= text.length){
            span.textContent = text.slice(0,i);
            i++;
            setTimeout(type, 12);
          }
        }
        type();
      });
      twObserver.unobserve(e.target);
    }
  });
}, {threshold:0.5});
document.querySelectorAll('.alert-card').forEach(c=>twObserver.observe(c));
</script>

</body>
</html>
