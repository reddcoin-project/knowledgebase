---
title: Staking 101 (PoSV & PoSV v2)
---

ReddCoin uses **Proof-of-Stake Velocity (PoSV)** — a design that rewards both:

- **Stake** (ownership / long-term alignment)
- **Velocity** (activity / circulation as a real currency)

This is part of our values: PoSV is designed to support a *social* currency without the waste of energy-intensive proof-of-work.

Official PoSV v2 FAQ (PDF): https://redd.love/assets/doc/PoSV-v2-FAQ.pdf

---

## Quick intuition (jargon-free)

- If you keep RDD in your wallet and stake, you help secure the network.
- **Velocity** is about the *movement* of RDD through real use — it’s a signal of a healthy social currency.
- PoSV v2 improves how rewards are distributed over time (and is aligned with sustainable, community-first network security).

---

## Mini “Staking Planner” (interactive)

<div class="redd-calculator" markdown>

<label><strong>Your RDD (estimate):</strong> <input id="rddAmount" type="number" min="0" step="1" value="100000"></label>

<label><strong>Days between stakes (guess):</strong> <input id="stakeDays" type="number" min="1" step="1" value="14"></label>

<label><strong>Activity level:</strong>
<select id="activity">
  <option value="low">Low (mostly holding)</option>
  <option value="med" selected>Medium (occasional use)</option>
  <option value="high">High (frequent tipping/spending)</option>
</select>
</label>

<p id="plannerOut"><em>Adjust the values to see an intuition-based estimate.</em></p>
</div>

<script>
(function(){
  function fmt(n){ return new Intl.NumberFormat().format(Math.round(n)); }
  function run(){
    const amt = Number(document.getElementById('rddAmount').value||0);
    const days = Math.max(1, Number(document.getElementById('stakeDays').value||1));
    const act = document.getElementById('activity').value;
    const actMult = act==='high'?1.15:(act==='low'?0.92:1.0);

    // This is NOT protocol math. It's a teaching tool to show relationships.
    const yearlyBase = 0.05; // 5% target intuition baseline
    const freqMult = Math.min(1.18, Math.max(0.85, 30/days)); // more frequent staking helps, capped
    const est = amt * yearlyBase * freqMult * actMult;

    document.getElementById('plannerOut').innerHTML =
      `<strong>Teaching estimate:</strong> ~${fmt(est)} RDD/year (intuition tool).<br>` +
      `For protocol specifics, see the PoSV v2 spec and FAQ.`;
  }
  ['rddAmount','stakeDays','activity'].forEach(id => document.getElementById(id).addEventListener('input', run));
  run();
})();
</script>

<details>
<summary><strong>Deep dive: the “why” behind PoSV</strong></summary>

PoSV was designed to support ReddCoin as both:
- a store of value (stake)
- a medium of exchange (velocity)

That’s a social equity design choice: we want real usage to matter, not just passive accumulation.
</details>
