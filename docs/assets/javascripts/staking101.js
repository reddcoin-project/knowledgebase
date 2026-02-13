// ReddCoin Knowledgebase - Staking 101 (PoSV intuition tool)
// This is a teaching aid for ReddHeads. It is NOT a protocol calculator.
(function () {
  function $(sel, root) { return (root || document).querySelector(sel); }
  function $$ (sel, root) { return Array.prototype.slice.call((root||document).querySelectorAll(sel)); }

  function clamp(n, a, b) { return Math.max(a, Math.min(b, n)); }

  function init() {
    const wrap = document.getElementById("staking101");
    if (!wrap) return;

    const balance = $("#s101-balance", wrap);
    const activity = $("#s101-activity", wrap);
    const age = $("#s101-age", wrap);
    const out = $("#s101-output", wrap);

    const balanceV = $("#s101-balance-v", wrap);
    const activityV = $("#s101-activity-v", wrap);
    const ageV = $("#s101-age-v", wrap);

    const explainSimple = $("#s101-simple", wrap);
    const explainDeep = $("#s101-deep", wrap);

    function score() {
      // Intuition-only composite score: balance has diminishing returns, activity helps, age helps to a cap.
      const b = parseFloat(balance.value || "0");
      const a = parseFloat(activity.value || "0"); // tx/week proxy
      const d = parseFloat(age.value || "0");      // days since last movement

      const bScore = Math.log10(1 + b) / 6.0;      // ~0..1 for 1..1,000,000
      const aScore = clamp(a / 20.0, 0, 1);        // 0..1 for 0..20+ actions/week
      const dScore = clamp(d / 30.0, 0, 1);        // 0..1 for 0..30+ days

      // "Velocity" intuition: more activity helps, but not infinitely.
      const composite = (0.45*bScore + 0.35*aScore + 0.20*dScore);
      return clamp(composite, 0, 1);
    }

    function render() {
      balanceV.textContent = Number(balance.value).toLocaleString();
      activityV.textContent = Number(activity.value).toLocaleString();
      ageV.textContent = Number(age.value).toLocaleString();

      const s = score();
      const pct = Math.round(s*100);

      // Friendly labels
      let label = "Low";
      if (pct >= 70) label = "High";
      else if (pct >= 40) label = "Medium";

      out.innerHTML = `
        <div class="s101-meter" role="img" aria-label="Staking readiness meter">
          <div class="s101-meter-bar" style="width:${pct}%"></div>
        </div>
        <p class="s101-result"><strong>Staking readiness:</strong> ${label} (${pct}/100)</p>
      `;

      // Simple explanation
      explainSimple.innerHTML = `
        <ul>
          <li><strong>Balance</strong> helps (with diminishing returns).</li>
          <li><strong>Activity (“velocity”)</strong> helps — ReddCoin rewards a living social currency.</li>
          <li><strong>Age</strong> helps up to a point (leaving funds untouched for a while can help).</li>
        </ul>
      `;

      // Deep dive
      explainDeep.innerHTML = `
        <p><strong>Deep dive:</strong> This widget is not computing protocol rewards. It illustrates the PoSV idea that
        participation matters: a social currency should reward people who keep value moving responsibly, not just those who park it forever.</p>
        <p>For exact protocol behavior, see the PoSV v2 docs and the Core source.</p>
      `;
    }

    ["input","change"].forEach(ev=>{
      balance.addEventListener(ev, render);
      activity.addEventListener(ev, render);
      age.addEventListener(ev, render);
    });

    render();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
