#!/usr/bin/env python3
"""
build_merged.py
Merges Pharma_Complete_Guide.html (prose) + pharma_visual_new.html (SVGs)
into a single interactive book: Deepak Kumar - Pharma & MedTech Consultant

Update: Enhanced book-like HTML formatting with:
  - Typographic drop caps, decorative chapter openers
  - Sticky reading-controls bar (font size, dark/sepia/light theme)
  - Full-bleed cover with animated particle background
  - Improved sidebar TOC with progress indicators
  - Polished callout boxes, timelines, role cards
  - Ornamental section dividers
  - Robust print CSS (page breaks, running heads)
  - Chapter prev/next navigation footer
"""
import re, os, sys

# ── Paths ─────────────────────────────────────────────────────────────────────
# Update these two lines if your session mount paths change.
UPLOADS = '/sessions/vigilant-determined-cori/mnt/Xenon Pharmaceuticals'
OUT     = '/sessions/vigilant-determined-cori/mnt/Xenon Pharmaceuticals/Pharma_Complete_Visual_Guide.html'


CH2_EXTRA = """

<!-- ═══════════════════════════════════════════════════════════════════════
     CHAPTER 2 EXPANSION — DETAILED R&D PROCESS
     ═══════════════════════════════════════════════════════════════════════ -->

<!-- ── FULL PIPELINE DIAGRAM ── -->
<div class="vis-embed" id="ch2-pipeline-diagram" style="margin:40px 0 48px;">
  <div class="vis-label"><span class="vis-icon">◈</span> Drug Development Pipeline — Discovery to Launch &amp; Beyond</div>
  <div class="vis-inner">
<svg viewBox="0 0 1060 310" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;display:block;">
  <defs>
    <linearGradient id="rdBg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#1a0a30"/>
      <stop offset="100%" stop-color="#0a1e10"/>
    </linearGradient>
    <marker id="rdArr" markerWidth="8" markerHeight="8" refX="7" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#4a6080"/>
    </marker>
  </defs>
  <rect width="1060" height="310" rx="12" fill="url(#rdBg)"/>
  <!-- title -->
  <text x="530" y="24" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700" letter-spacing="2" font-family="sans-serif">DRUG DEVELOPMENT PIPELINE</text>

  <!-- Phase blocks -->
  <!-- Discovery -->
  <rect x="14" y="38" width="118" height="180" rx="8" fill="#2a1050" stroke="#7040C0" stroke-width="1.5"/>
  <text x="73" y="58" text-anchor="middle" fill="#9060E0" font-size="9.5" font-weight="800" font-family="sans-serif">DISCOVERY</text>
  <text x="73" y="71" text-anchor="middle" fill="#6a4090" font-size="8" font-family="sans-serif">Yrs 1–4</text>
  <line x1="73" y1="77" x2="73" y2="79" stroke="#7040C0" stroke-width="1"/>
  <text x="73" y="93"  text-anchor="middle" fill="#b090d0" font-size="8" font-family="sans-serif">Target ID</text>
  <text x="73" y="106" text-anchor="middle" fill="#b090d0" font-size="8" font-family="sans-serif">Hit Screening</text>
  <text x="73" y="119" text-anchor="middle" fill="#b090d0" font-size="8" font-family="sans-serif">Lead Optimisation</text>
  <text x="73" y="132" text-anchor="middle" fill="#b090d0" font-size="8" font-family="sans-serif">ADMET Profiling</text>
  <text x="73" y="145" text-anchor="middle" fill="#b090d0" font-size="8" font-family="sans-serif">Candidate Selection</text>
  <rect x="30" y="155" width="86" height="18" rx="4" fill="#3a1870"/>
  <text x="73" y="168" text-anchor="middle" fill="#d0b0ff" font-size="7.5" font-weight="700" font-family="sans-serif">IND Filing →</text>
  <!-- Pre-clinical -->
  <rect x="142" y="38" width="108" height="180" rx="8" fill="#1a1845" stroke="#3040A0" stroke-width="1.5"/>
  <text x="196" y="58" text-anchor="middle" fill="#6070C0" font-size="9.5" font-weight="800" font-family="sans-serif">PRE-CLINICAL</text>
  <text x="196" y="71" text-anchor="middle" fill="#4050A0" font-size="8" font-family="sans-serif">Yrs 2–5</text>
  <text x="196" y="93"  text-anchor="middle" fill="#9098C8" font-size="8" font-family="sans-serif">In-vitro studies</text>
  <text x="196" y="106" text-anchor="middle" fill="#9098C8" font-size="8" font-family="sans-serif">Animal tox studies</text>
  <text x="196" y="119" text-anchor="middle" fill="#9098C8" font-size="8" font-family="sans-serif">GLP safety studies</text>
  <text x="196" y="132" text-anchor="middle" fill="#9098C8" font-size="8" font-family="sans-serif">CMC development</text>
  <text x="196" y="145" text-anchor="middle" fill="#9098C8" font-size="8" font-family="sans-serif">Formulation</text>
  <rect x="152" y="155" width="88" height="18" rx="4" fill="#20205A"/>
  <text x="196" y="168" text-anchor="middle" fill="#b0b8e8" font-size="7.5" font-weight="700" font-family="sans-serif">IND Accepted ✓</text>
  <!-- Phase I -->
  <rect x="260" y="38" width="108" height="180" rx="8" fill="#0a2030" stroke="#1A7080" stroke-width="1.5"/>
  <text x="314" y="58" text-anchor="middle" fill="#2AACBC" font-size="9.5" font-weight="800" font-family="sans-serif">PHASE I</text>
  <text x="314" y="71" text-anchor="middle" fill="#186070" font-size="8" font-family="sans-serif">Yrs 4–6 · 20–100 pts</text>
  <text x="314" y="93"  text-anchor="middle" fill="#70C0C8" font-size="8" font-family="sans-serif">First-in-human</text>
  <text x="314" y="106" text-anchor="middle" fill="#70C0C8" font-size="8" font-family="sans-serif">SAD / MAD design</text>
  <text x="314" y="119" text-anchor="middle" fill="#70C0C8" font-size="8" font-family="sans-serif">PK/PD profiling</text>
  <text x="314" y="132" text-anchor="middle" fill="#70C0C8" font-size="8" font-family="sans-serif">MTD / RP2D dose</text>
  <text x="314" y="145" text-anchor="middle" fill="#70C0C8" font-size="8" font-family="sans-serif">Safety endpoints</text>
  <rect x="270" y="155" width="88" height="18" rx="4" fill="#0a2838"/>
  <text x="314" y="168" text-anchor="middle" fill="#7ECCC8" font-size="7.5" font-weight="700" font-family="sans-serif">~70% advance</text>
  <!-- Phase II -->
  <rect x="378" y="38" width="118" height="180" rx="8" fill="#0a2018" stroke="#1A7040" stroke-width="1.5"/>
  <text x="437" y="58" text-anchor="middle" fill="#3AC870" font-size="9.5" font-weight="800" font-family="sans-serif">PHASE II</text>
  <text x="437" y="71" text-anchor="middle" fill="#186030" font-size="8" font-family="sans-serif">Yrs 6–9 · 100–500 pts</text>
  <text x="437" y="93"  text-anchor="middle" fill="#80C898" font-size="8" font-family="sans-serif">IIa: Proof-of-concept</text>
  <text x="437" y="106" text-anchor="middle" fill="#80C898" font-size="8" font-family="sans-serif">IIb: Dose-ranging</text>
  <text x="437" y="119" text-anchor="middle" fill="#80C898" font-size="8" font-family="sans-serif">Efficacy signal</text>
  <text x="437" y="132" text-anchor="middle" fill="#80C898" font-size="8" font-family="sans-serif">Biomarker ID</text>
  <text x="437" y="145" text-anchor="middle" fill="#F0B040" font-size="8" font-weight="700" font-family="sans-serif">★ TPP issued</text>
  <rect x="388" y="155" width="98" height="18" rx="4" fill="#0a2818"/>
  <text x="437" y="168" text-anchor="middle" fill="#80D898" font-size="7.5" font-weight="700" font-family="sans-serif">EoP2 FDA Meeting</text>
  <!-- Commercial Engagement Arrow -->
  <path d="M437,222 L437,245" stroke="#F0B040" stroke-width="1.5" stroke-dasharray="4,3" marker-end="url(#rdArr)"/>
  <text x="437" y="258" text-anchor="middle" fill="#F0B040" font-size="7.5" font-weight="700" font-family="sans-serif">Commercial</text>
  <text x="437" y="269" text-anchor="middle" fill="#F0B040" font-size="7.5" font-family="sans-serif">Engagement Starts</text>
  <!-- Phase III -->
  <rect x="506" y="38" width="128" height="180" rx="8" fill="#1a1408" stroke="#907020" stroke-width="1.5"/>
  <text x="570" y="58" text-anchor="middle" fill="#C8A030" font-size="9.5" font-weight="800" font-family="sans-serif">PHASE III</text>
  <text x="570" y="71" text-anchor="middle" fill="#806010" font-size="8" font-family="sans-serif">Yrs 9–13 · 1,000–5,000</text>
  <text x="570" y="93"  text-anchor="middle" fill="#C8B060" font-size="8" font-family="sans-serif">Pivotal RCT(s)</text>
  <text x="570" y="106" text-anchor="middle" fill="#C8B060" font-size="8" font-family="sans-serif">Primary endpoint</text>
  <text x="570" y="119" text-anchor="middle" fill="#C8B060" font-size="8" font-family="sans-serif">SPA agreement</text>
  <text x="570" y="132" text-anchor="middle" fill="#C8B060" font-size="8" font-family="sans-serif">HEOR sub-studies</text>
  <text x="570" y="145" text-anchor="middle" fill="#C8B060" font-size="8" font-family="sans-serif">Rolling review opt.</text>
  <rect x="516" y="155" width="108" height="18" rx="4" fill="#201808"/>
  <text x="570" y="168" text-anchor="middle" fill="#E0C060" font-size="7.5" font-weight="700" font-family="sans-serif">~25% reach NDA</text>
  <!-- NDA/BLA -->
  <rect x="644" y="38" width="108" height="180" rx="8" fill="#1e0808" stroke="#802020" stroke-width="1.5"/>
  <text x="698" y="56" text-anchor="middle" fill="#C03030" font-size="9.5" font-weight="800" font-family="sans-serif">NDA / BLA</text>
  <text x="698" y="69" text-anchor="middle" fill="#803020" font-size="8" font-family="sans-serif">Yrs 12–14</text>
  <text x="698" y="90"  text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">eCTD compilation</text>
  <text x="698" y="103" text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">5 CTD Modules</text>
  <text x="698" y="116" text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">60-day filing review</text>
  <text x="698" y="129" text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">PDUFA date set</text>
  <text x="698" y="142" text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">Priority / Std review</text>
  <text x="698" y="155" text-anchor="middle" fill="#C07080" font-size="8" font-family="sans-serif">AdCom if needed</text>
  <rect x="654" y="162" width="88" height="18" rx="4" fill="#280808"/>
  <text x="698" y="175" text-anchor="middle" fill="#E08080" font-size="7.5" font-weight="700" font-family="sans-serif">Labelling negot.</text>
  <!-- FDA Approval -->
  <rect x="762" y="38" width="108" height="180" rx="8" fill="#061e08" stroke="#1A8030" stroke-width="2"/>
  <text x="816" y="58" text-anchor="middle" fill="#30C050" font-size="9.5" font-weight="800" font-family="sans-serif">FDA APPROVAL</text>
  <text x="816" y="71" text-anchor="middle" fill="#186030" font-size="8" font-family="sans-serif">Yr 13–15</text>
  <text x="816" y="93"  text-anchor="middle" fill="#70C880" font-size="8" font-family="sans-serif">Approval letter</text>
  <text x="816" y="106" text-anchor="middle" fill="#70C880" font-size="8" font-family="sans-serif">Final label</text>
  <text x="816" y="119" text-anchor="middle" fill="#70C880" font-size="8" font-family="sans-serif">REMS if required</text>
  <text x="816" y="132" text-anchor="middle" fill="#F0B040" font-size="8" font-weight="700" font-family="sans-serif">★ LAUNCH</text>
  <text x="816" y="145" text-anchor="middle" fill="#70C880" font-size="8" font-family="sans-serif">within 24–48 hrs</text>
  <rect x="772" y="155" width="88" height="18" rx="4" fill="#062010"/>
  <text x="816" y="168" text-anchor="middle" fill="#90E8A0" font-size="7.5" font-weight="700" font-family="sans-serif">Phase 4 begins</text>
  <!-- Phase 4 -->
  <rect x="880" y="38" width="166" height="180" rx="8" fill="#04100e" stroke="#107040" stroke-width="1.5"/>
  <text x="963" y="58" text-anchor="middle" fill="#20A060" font-size="9.5" font-weight="800" font-family="sans-serif">PHASE 4 / POST-MARKET</text>
  <text x="963" y="71" text-anchor="middle" fill="#106040" font-size="8" font-family="sans-serif">Yr 15+ (patent life ~10 yrs)</text>
  <text x="963" y="93"  text-anchor="middle" fill="#60A878" font-size="8" font-family="sans-serif">Post-marketing studies</text>
  <text x="963" y="106" text-anchor="middle" fill="#60A878" font-size="8" font-family="sans-serif">REMS monitoring</text>
  <text x="963" y="119" text-anchor="middle" fill="#60A878" font-size="8" font-family="sans-serif">Label expansions</text>
  <text x="963" y="132" text-anchor="middle" fill="#60A878" font-size="8" font-family="sans-serif">sNDA new indications</text>
  <text x="963" y="145" text-anchor="middle" fill="#60A878" font-size="8" font-family="sans-serif">Pharmacovigilance</text>
  <rect x="890" y="155" width="146" height="18" rx="4" fill="#062010"/>
  <text x="963" y="168" text-anchor="middle" fill="#80D898" font-size="7.5" font-weight="700" font-family="sans-serif">MedAffairs runs evidence</text>
  <!-- Connecting arrows -->
  <line x1="132" y1="128" x2="142" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="250" y1="128" x2="260" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="368" y1="128" x2="378" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="496" y1="128" x2="506" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="634" y1="128" x2="644" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="752" y1="128" x2="762" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <line x1="870" y1="128" x2="880" y2="128" stroke="#4a6080" stroke-width="1.5" marker-end="url(#rdArr)"/>
  <!-- Commercial bar at bottom -->
  <rect x="388" y="280" width="658" height="20" rx="4" fill="#3a2800" stroke="#F0B040" stroke-width="1"/>
  <text x="717" y="294" text-anchor="middle" fill="#F0D060" font-size="8" font-weight="700" font-family="sans-serif">COMMERCIAL &amp; MEDICAL AFFAIRS ENGAGEMENT ZONE → Phase IIb onward</text>
  <path d="M388,270 L388,280" stroke="#F0B040" stroke-width="1.5"/>
  <path d="M1046,270 L1046,280" stroke="#F0B040" stroke-width="1.5"/>
  <!-- Attrition label -->
  <text x="530" y="302" text-anchor="middle" fill="#4a6080" font-size="7.5" font-family="sans-serif">~10,000 compounds screened → 1 approved medicine (avg. 10–15 years · $1–2.6 billion)</text>
</svg>
  </div>
</div>

<!-- ── DRUG DISCOVERY ── -->
<h2 id="ch2-discovery">Stage 1 — Drug Discovery: From Target to Candidate</h2>
<p>Drug discovery is the science of finding a molecule that can safely and effectively treat a disease. It is a process of extreme attrition: for every 10,000 compounds screened, roughly one reaches the market. Understanding what happens at each sub-stage explains why drug development takes so long and costs so much.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#3a1870">🎯</div>
      <div>
        <div class="crm-obj-name">Target Identification &amp; Validation</div>
        <div class="crm-obj-api">Years 1–2 · Biology / Genomics teams</div>
      </div>
    </div>
    <div class="crm-obj-desc">Scientists identify a <strong>biological target</strong> — typically a protein, enzyme, receptor, or gene — whose activity is linked to disease pathology. Sources include: genomic data (GWAS studies), patient biobanks, disease pathway analysis, academic literature, and competitor intelligence. Validation means proving the target is <em>druggable</em> (can be modulated by a small molecule or biologic) and <em>disease-relevant</em> (modulating it actually changes disease progression). Target validation is the most common failure point — many programmes collapse here when early animal data doesn't translate to humans.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1845">🔬</div>
      <div>
        <div class="crm-obj-name">Hit Identification — High-Throughput Screening (HTS)</div>
        <div class="crm-obj-api">Years 1–3 · Chemistry / HTS labs</div>
      </div>
    </div>
    <div class="crm-obj-desc">Compound libraries of 500,000–2 million molecules are screened against the target using automated robotic assays. Hits are compounds that show activity at the target above a predefined threshold. HTS typically returns 0.1–1% of screened compounds as hits — thousands of starting points. Alternative approaches include <strong>fragment-based drug discovery</strong> (smaller, lower-affinity fragments that are elaborated into leads), <strong>DNA-encoded chemical libraries</strong> (billions of compounds in a single tube), and <strong>structure-based drug design</strong> (using X-ray crystallography or cryo-EM of the target protein to design molecules computationally).</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a2815">⚗️</div>
      <div>
        <div class="crm-obj-name">Lead Optimisation</div>
        <div class="crm-obj-api">Years 2–4 · Medicinal Chemistry · DMPK teams</div>
      </div>
    </div>
    <div class="crm-obj-desc">Hits are refined into <strong>leads</strong> — molecules with improved potency, selectivity, and preliminary drug-like properties. Medicinal chemists make hundreds of analogues, systematically improving: <strong>Potency</strong> (IC50 / EC50 against target), <strong>Selectivity</strong> (does it hit only the intended target?), <strong>ADMET profile</strong> (Absorption, Distribution, Metabolism, Excretion, Toxicity), <strong>Physicochemical properties</strong> (solubility, permeability, lipophilicity — governed by Lipinski's Rule of Five for oral drugs). DMPK (Drug Metabolism and Pharmacokinetics) teams run in-vitro microsomal stability assays, CYP inhibition panels, plasma protein binding, and hERG channel toxicity screens (cardiac safety).</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e1408">🧪</div>
      <div>
        <div class="crm-obj-name">Candidate Selection &amp; Development Nomination</div>
        <div class="crm-obj-api">Years 3–4 · Cross-functional go/no-go decision</div>
      </div>
    </div>
    <div class="crm-obj-desc">One or a small number of compounds are nominated as <strong>Development Candidates (DC)</strong> — the molecule(s) that will advance into formal pre-clinical development. The DC selection review is a major governance milestone attended by R&amp;D, Regulatory, CMC (Chemistry, Manufacturing &amp; Controls), and increasingly Commercial. Selection criteria include: potency and selectivity profile, ADMET data, intellectual property position (is the compound patentable?), manufacturability (can it be synthesised at scale?), and competitive differentiation (does it have an advantage over existing drugs?). At this stage, a preliminary <strong>Target Product Profile (TPP)</strong> is drafted — the first document that bridges R&amp;D and Commercial strategy.</div>
  </div>
</div>

<!-- ── PRE-CLINICAL ── -->
<h2 id="ch2-preclinical">Stage 2 — Pre-Clinical Development: Proving Safety Before Human Testing</h2>
<p>Before any drug can be tested in humans, it must pass a rigorous battery of pre-clinical studies conducted under <strong>Good Laboratory Practice (GLP)</strong> regulations (21 CFR Part 58). These studies are required by the FDA and generate the safety data package that supports the IND application. Pre-clinical development runs in parallel with late-stage lead optimisation and typically takes 2–3 years.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1845">🐭</div>
      <div>
        <div class="crm-obj-name">In-Vivo Toxicology Studies (GLP)</div>
        <div class="crm-obj-api">Required for IND · 21 CFR Part 58</div>
      </div>
    </div>
    <div class="crm-obj-desc">GLP toxicology studies are conducted in at least two species (rodent + non-rodent) across escalating durations: <strong>Acute toxicity</strong> (single dose), <strong>Sub-acute</strong> (2–4 weeks), <strong>Sub-chronic</strong> (13 weeks), and eventually <strong>Chronic</strong> studies (6–24 months, running in parallel with clinical trials). Key endpoints: NOAEL (No Observed Adverse Effect Level), target organ toxicity, reversibility of toxicity. Genotoxicity (Ames test, in-vitro micronucleus, in-vivo bone marrow) and safety pharmacology (cardiovascular, CNS, respiratory) are also required. GLP study findings directly determine the <strong>starting human dose</strong> and dosing restrictions in the IND.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a2815">🏭</div>
      <div>
        <div class="crm-obj-name">Chemistry, Manufacturing &amp; Controls (CMC)</div>
        <div class="crm-obj-api">Ongoing through all phases · CDER/CBER review</div>
      </div>
    </div>
    <div class="crm-obj-desc">CMC covers everything about how the drug is made and tested. For the IND: <strong>Drug Substance</strong> (synthesis route, impurity profile, stability data), <strong>Drug Product</strong> (formulation, dosage form, container closure), and <strong>Analytical methods</strong> (how purity, potency, and identity are tested). CMC is not a one-time activity — it evolves through all phases. The commercial manufacturing process is usually significantly different from the Phase I process, requiring comparability studies and potentially new clinical data to bridge the manufacturing change.</div>
  </div>
</div>

<!-- ── IND ── -->
<h2 id="ch2-ind">Stage 3 — The IND Application: Opening the Door to Human Testing</h2>
<p>The <strong>Investigational New Drug (IND) application</strong> (21 CFR Part 312) is the regulatory filing that permits a sponsor to ship an investigational drug to clinical investigators and begin testing in humans. It is not an approval — it is a permission to proceed. The FDA has <strong>30 days to place a clinical hold</strong>; if no hold is issued within 30 days, the sponsor may proceed.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">📋</div>
      <div>
        <div class="crm-obj-name">IND Content Requirements</div>
        <div class="crm-obj-api">21 CFR 312.23 · Submitted electronically via eCTD</div>
      </div>
    </div>
    <div class="crm-obj-desc"><strong>Section A — Cover Sheet (Form FDA 1571):</strong> Sponsor identity, drug identity, study type (Phase I/II/III), commitments to regulations. <strong>Section B — Table of Contents.</strong> <strong>Section C — Introductory Statement:</strong> Brief description of drug and rationale for testing. <strong>Section D — General Investigational Plan:</strong> Phases and studies planned for the coming year. <strong>Section E — Investigator's Brochure (IB):</strong> Comprehensive summary of pre-clinical data and (if any) prior human data. Updated annually. <strong>Section F — Protocols:</strong> Detailed clinical study protocol for Phase I. <strong>Section G — Chemistry, Manufacturing &amp; Controls.</strong> <strong>Section H — Pharmacology &amp; Toxicology:</strong> Pre-clinical GLP study reports. <strong>Section I — Previous Human Experience:</strong> Any foreign clinical data. <strong>Section J — Additional Information.</strong></div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#062010">⚖️</div>
      <div>
        <div class="crm-obj-name">Clinical Hold — When the FDA Says Stop</div>
        <div class="crm-obj-api">21 CFR 312.42 · Full Hold vs. Partial Hold</div>
      </div>
    </div>
    <div class="crm-obj-desc">The FDA can place a <strong>Full Clinical Hold</strong> (no studies may begin or continue) or a <strong>Partial Hold</strong> (restrictions on specific studies or patient populations). Grounds for a full hold: unreasonable risk to subjects, insufficient pre-clinical data to justify the proposed first dose, protocol deficiencies that create unreasonable risk, IRB has not reviewed the protocol. The sponsor receives written notice with the specific deficiencies. The hold is lifted only when the deficiencies are resolved to the FDA's satisfaction. Clinical holds cause significant programme delays — typically 3–12 months — and are a major risk in early development.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1845">📝</div>
      <div>
        <div class="crm-obj-name">IND Maintenance &amp; Annual Reports</div>
        <div class="crm-obj-api">21 CFR 312.33 · Due within 60 days of IND anniversary</div>
      </div>
    </div>
    <div class="crm-obj-desc">An IND is a living regulatory dossier. Sponsors must submit: <strong>Protocol amendments</strong> before initiating any new study or significant protocol change; <strong>Information amendments</strong> for new pre-clinical data that affects the benefit-risk profile; <strong>IND Safety Reports</strong> (15-day expedited reports for unexpected serious adverse reactions; 7-day reports for fatal or life-threatening events); <strong>Annual Reports</strong> summarising all studies conducted, subjects enrolled, safety experience, and plans for the coming year. Failure to maintain IND compliance can result in the FDA placing the IND on clinical hold.</div>
  </div>
</div>

<!-- ── PHASE I ── -->
<h2 id="ch2-phase1">Stage 4 — Phase I: First in Human</h2>
<p>Phase I trials are the first time the investigational drug is given to a human. The primary question is <strong>safety</strong>, not efficacy. Phase I typically involves 20–100 subjects (usually healthy volunteers for non-oncology drugs; patients for oncology where toxicity at therapeutic doses is expected). Approximately <strong>70% of drugs that enter Phase I advance to Phase II</strong>.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2030">💉</div>
      <div>
        <div class="crm-obj-name">SAD / MAD Study Design</div>
        <div class="crm-obj-api">Single Ascending Dose · Multiple Ascending Dose</div>
      </div>
    </div>
    <div class="crm-obj-desc">Most Phase I programmes begin with a <strong>Single Ascending Dose (SAD)</strong> study: cohorts of 6–10 subjects receive escalating single doses (e.g., 1mg → 5mg → 25mg → 100mg), with a dose escalation committee reviewing safety data before each step up. This establishes the <strong>Maximum Tolerated Dose (MTD)</strong> and <strong>Dose-Limiting Toxicities (DLTs)</strong>. The SAD is followed by a <strong>Multiple Ascending Dose (MAD)</strong> study where subjects receive multiple doses over 7–14 days, establishing steady-state PK, accumulation ratio, and tolerability at repeat doses. The PK data from SAD/MAD directly informs Phase II dose selection.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2030">📊</div>
      <div>
        <div class="crm-obj-name">PK/PD Profiling</div>
        <div class="crm-obj-api">Pharmacokinetics · Pharmacodynamics · Biomarkers</div>
      </div>
    </div>
    <div class="crm-obj-desc"><strong>Pharmacokinetics (PK)</strong> describes what the body does to the drug: Absorption (Cmax, Tmax, bioavailability), Distribution (volume of distribution, plasma protein binding), Metabolism (CYP enzymes involved, metabolite profile), Excretion (renal clearance, fecal excretion, half-life). <strong>Pharmacodynamics (PD)</strong> describes what the drug does to the body: the relationship between drug concentration and biological effect. Early biomarker data (target engagement, pathway modulation) is critical — it provides the first human evidence that the drug is hitting the intended target, which de-risks Phase II decisions. Drug-drug interaction potential (DDI studies) is also characterized in Phase I for drugs likely to be co-administered with other medications.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a2815">👥</div>
      <div>
        <div class="crm-obj-name">Special Population Studies</div>
        <div class="crm-obj-api">Hepatic impairment · Renal impairment · Elderly · Pediatric</div>
      </div>
    </div>
    <div class="crm-obj-desc">Regulatory guidance requires characterisation of drug behaviour in special populations likely to receive it in clinical practice. <strong>Hepatic impairment studies</strong> (21 CFR guidance): required if drug is hepatically metabolised; uses Child-Pugh classification (Mild/Moderate/Severe). <strong>Renal impairment studies</strong>: required if drug is renally excreted; uses GFR categories. These studies directly inform labelling — the Dosage and Administration section of the approved label must provide specific dosing guidance for special populations. Paediatric studies are governed by the Pediatric Research Equity Act (PREA) and may be deferred post-approval with an agreed Pediatric Study Plan (PSP).</div>
  </div>
</div>

<!-- ── PHASE II ── -->
<h2 id="ch2-phase2">Stage 5 — Phase II: Proof of Concept &amp; Dose Finding</h2>
<p>Phase II is where the drug is tested for the first time in the <em>target patient population</em> — people who actually have the disease. Phase II has two distinct sub-stages with different questions. Only approximately <strong>33% of drugs that enter Phase II proceed to Phase III</strong> — the highest attrition point in the development pipeline.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2018">🔍</div>
      <div>
        <div class="crm-obj-name">Phase IIa — Proof of Concept (PoC)</div>
        <div class="crm-obj-api">50–200 patients · Signal-finding · Go/No-Go decision</div>
      </div>
    </div>
    <div class="crm-obj-desc">Phase IIa asks: <em>does this drug have any biological effect in patients?</em> Trials are often exploratory and relatively small (50–200 patients), using biomarker or surrogate endpoints rather than clinical endpoints. The PoC read-out is the most important decision point in the entire development programme — a positive PoC study can trigger massive investment increases; a negative PoC study typically kills the programme. This is also where the first <strong>patient segmentation</strong> data emerges: which subpopulation responds best? This data will eventually define the approved indication and the commercial target population.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2018">📐</div>
      <div>
        <div class="crm-obj-name">Phase IIb — Dose Ranging</div>
        <div class="crm-obj-api">200–500 patients · Dose-response · Phase III design input</div>
      </div>
    </div>
    <div class="crm-obj-desc">Phase IIb characterises the dose-response relationship — which dose gives the best balance of efficacy and safety. Trial designs often use multiple dose arms (e.g., 5mg / 10mg / 25mg / 50mg vs. placebo) with a parallel group or crossover design. The Phase IIb data directly determines: (1) which dose(s) advance to Phase III; (2) the primary endpoint that will power the Phase III trial; (3) the patient population definition (inclusion/exclusion criteria) for Phase III. End of Phase IIb is typically when the <strong>formal End-of-Phase 2 (EoP2) meeting</strong> with the FDA is held — a critical alignment meeting on Phase III design.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#3a2800">⭐</div>
      <div>
        <div class="crm-obj-name">End-of-Phase 2 (EoP2) FDA Meeting</div>
        <div class="crm-obj-api">21 CFR 312.47 · Type B Meeting · Critical alignment</div>
      </div>
    </div>
    <div class="crm-obj-desc">The EoP2 meeting is the most strategically important interaction with the FDA during development. The sponsor presents the Phase II results and the proposed Phase III programme; the FDA provides binding guidance on: <strong>Phase III study design</strong> (endpoints, patient population, comparator arm), <strong>Statistical analysis plan</strong> (the primary analysis that will support approval), <strong>Number of studies required</strong> (usually two adequate and well-controlled studies, or one very large study with corroborating evidence), <strong>Regulatory pathway</strong> (standard vs. priority review; eligibility for expedited programmes), <strong>Special issues</strong> (REMS requirements, labelling commitments, post-marketing study requirements). FDA responses to EoP2 questions are not legally binding but carry enormous weight in subsequent review decisions.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a2815">💼</div>
      <div>
        <div class="crm-obj-name">★ Commercial Engagement Begins Here</div>
        <div class="crm-obj-api">Phase IIb PoC → TPP issued → Commercial teams activated</div>
      </div>
    </div>
    <div class="crm-obj-desc">A positive Phase IIb proof-of-concept is the formal trigger for sustained Commercial and Medical Affairs engagement. The R&amp;D team issues the first substantive <strong>Target Product Profile (TPP)</strong> document describing the anticipated drug profile — indication, efficacy claims, safety profile, dosing regimen, and target patient population. Commercial receives the TPP and begins: <strong>market sizing</strong> (how many patients? how often treated? what price can the market bear?), <strong>competitive landscape analysis</strong> (what is already approved or in development?), <strong>payer and access strategy</strong> (what evidence will payers require for formulary placement?), <strong>KOL identification</strong> (which physicians will be early adopters and scientific advisors?). Medical Affairs begins the <strong>Integrated Evidence Plan (IEP)</strong> — mapping what evidence is needed to support clinical use beyond the label claims.</div>
  </div>
</div>

<!-- ── PHASE III ── -->
<h2 id="ch2-phase3">Stage 6 — Phase III: The Pivotal Trials</h2>
<p>Phase III is the definitive proof that the drug works. These trials are large (1,000–10,000+ patients), long (1–5 years), multi-centre, randomised, and typically double-blind. They are designed to generate the evidence package that will support an NDA/BLA and, ultimately, the approved label. Phase III represents the largest single investment in drug development — a single pivotal trial can cost $100–500 million. Only about <strong>25–30% of drugs entering Phase III reach approval</strong>.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1408">📈</div>
      <div>
        <div class="crm-obj-name">Pivotal Trial Design — Statistical Framework</div>
        <div class="crm-obj-api">Pre-specified primary endpoint · 80–90% power · α = 0.05</div>
      </div>
    </div>
    <div class="crm-obj-desc">A pivotal trial must be designed to meet a pre-specified, clinically meaningful <strong>primary endpoint</strong> with adequate statistical power. The <strong>Special Protocol Assessment (SPA)</strong> process (21 CFR 312.45) allows sponsors to get the FDA to agree in writing that the trial design and analysis plan are acceptable for approval — this provides significant regulatory certainty. Key design elements: <strong>Primary endpoint</strong> (must be clinically meaningful — OS in oncology, MACE in cardiovascular, validated PRO instruments in other indications), <strong>Sample size</strong> (calculated to achieve 80–90% power to detect a clinically meaningful difference), <strong>Randomisation and blinding</strong> (double-blind RDBPCT is gold standard), <strong>Comparator</strong> (placebo or active comparator depending on standard of care), <strong>Analysis populations</strong> (ITT as primary, per-protocol as sensitivity), <strong>Pre-specified subgroup analyses</strong> (regulatory and commercial interest in whether the effect is consistent across age, gender, race, disease severity).</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2018">🌍</div>
      <div>
        <div class="crm-obj-name">Global Trial Operations</div>
        <div class="crm-obj-api">ICH E6 GCP · CRO management · Site monitoring</div>
      </div>
    </div>
    <div class="crm-obj-desc">Phase III trials are conducted at hundreds of sites across multiple countries under <strong>ICH E6 Good Clinical Practice (GCP)</strong>. Sponsors typically engage a <strong>Contract Research Organisation (CRO)</strong> to manage trial operations — site selection, IRB/IEC submissions, investigator training, clinical monitoring, data management, and biostatistics. Every site must have an approved <strong>Institutional Review Board (IRB)</strong> or Independent Ethics Committee (IEC) approval. <strong>Data Safety Monitoring Boards (DSMB)</strong> — independent experts — review unblinded interim data at pre-specified points and can recommend early stopping for efficacy, futility, or safety. Serious Adverse Events (SAEs) are reported to the FDA within 15 days (7 days if fatal or life-threatening).</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1408">💰</div>
      <div>
        <div class="crm-obj-name">HEOR &amp; Real-World Evidence Sub-Studies</div>
        <div class="crm-obj-api">Health Economics · Payer evidence generation</div>
      </div>
    </div>
    <div class="crm-obj-desc"><strong>Health Economics and Outcomes Research (HEOR)</strong> sub-studies are embedded within Phase III trials by Commercial and Medical Affairs. These capture data that clinical endpoints alone do not provide but that payers (insurance companies, PBMs, national health systems) require for formulary access decisions: <strong>Quality-adjusted life years (QALYs)</strong>, <strong>Patient-reported outcomes (PROs)</strong> — validated instruments measuring how patients feel and function, <strong>Healthcare resource utilisation (HCRU)</strong> — hospitalizations, ER visits, physician visits, <strong>Productivity loss</strong>, <strong>Caregiver burden</strong>. HEOR data feeds directly into the health technology assessment (HTA) submissions made to payers at launch. Without this data, even an approved drug may be denied formulary coverage.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">⚡</div>
      <div>
        <div class="crm-obj-name">Expedited Development Programs</div>
        <div class="crm-obj-api">FDA CDER Expedited Programs · PDUFA VII</div>
      </div>
    </div>
    <div class="crm-obj-desc">For drugs addressing serious unmet medical needs, the FDA offers four expedited programs that can significantly shorten development timelines: <strong>Fast Track Designation</strong> — facilitates development and expedites review; allows rolling NDA submission (modules submitted as completed rather than all at once); available if drug treats a serious condition AND may fill an unmet need. <strong>Breakthrough Therapy Designation (BTD)</strong> — intensive FDA guidance across all aspects of development; preliminary clinical evidence shows substantial improvement over available therapy on a clinically significant endpoint; most impactful of the four designations in terms of FDA engagement. <strong>Priority Review</strong> — FDA review clock shortened from 12 months to 6 months; granted automatically with BTD or separately for drugs offering major advance over available treatment. <strong>Accelerated Approval</strong> (21 CFR 601.41/314.510) — approval based on a surrogate endpoint (biomarker or intermediate clinical endpoint) reasonably likely to predict clinical benefit; requires a post-marketing confirmatory trial. Common in oncology — tumour response rate used as surrogate for survival.</div>
  </div>
</div>

<!-- ── NDA/BLA ── -->
<h2 id="ch2-nda">Stage 7 — NDA/BLA Submission: Building the Case for Approval</h2>
<p>When Phase III trials are complete and the data shows the drug works, the sponsor compiles everything into the <strong>New Drug Application (NDA)</strong> — or Biologics License Application (BLA) for biological products. This is the largest and most complex document in pharmaceutical development. A typical NDA contains hundreds of thousands of pages across five structured modules, submitted electronically in the <strong>eCTD (electronic Common Technical Document)</strong> format. The FDA charges a <strong>PDUFA user fee</strong> ($4.3 million in FY2025 for standard applications) upon submission.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">📚</div>
      <div>
        <div class="crm-obj-name">The Five CTD Modules</div>
        <div class="crm-obj-api">ICH M4 format · eCTD submission · Modular structure</div>
      </div>
    </div>
    <div class="crm-obj-desc"><strong>Module 1 — Administrative &amp; Prescribing Information (US-Specific):</strong> Cover letter, Form FDA 356h, proposed labelling (prescribing information, medication guide), patent information (Form FDA 3542), debarment certification. <strong>Module 2 — Common Technical Document Summaries:</strong> Quality Overall Summary (QOS), Nonclinical Overview, Nonclinical Written Summary, Clinical Overview, Clinical Summary — these are the reviewer-facing narratives that synthesise the full data package. <strong>Module 3 — Quality (CMC):</strong> Complete drug substance and drug product manufacturing, characterisation, specifications, and stability data. <strong>Module 4 — Nonclinical Study Reports:</strong> All GLP pharmacology and toxicology study reports. <strong>Module 5 — Clinical Study Reports:</strong> All clinical study reports from Phase I through Phase III, including integrated safety and efficacy summaries (ISS/ISE). The ISS and ISE are the central documents FDA reviewers use to evaluate the benefit-risk profile.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">📅</div>
      <div>
        <div class="crm-obj-name">Rolling NDA &amp; Filing Review (Day 60)</div>
        <div class="crm-obj-api">21 CFR 314.101 · Refuse to File (RTF)</div>
      </div>
    </div>
    <div class="crm-obj-desc">With <strong>Fast Track Designation</strong>, sponsors may submit a <strong>Rolling NDA</strong> — completed modules are submitted as they are ready rather than waiting for the entire application to be assembled. This can reduce the time from study completion to FDA action by 6–12 months. Upon receiving the complete NDA, the FDA conducts a <strong>Filing Review</strong> within 60 days. This is a completeness check — not a scientific review. The FDA can issue a <strong>Refuse to File (RTF)</strong> letter if the application is incomplete or significantly deficient. RTF restarts the clock and is a significant setback. If the application is accepted, the FDA sets the <strong>PDUFA date</strong> — the target action date — either 6 months (Priority Review) or 12 months (Standard Review) from the date of submission.</div>
  </div>
</div>

<!-- ── FDA REVIEW ── -->
<h2 id="ch2-fda-review">Stage 8 — FDA Review: The 12-Month Clock</h2>
<p>Once an NDA is accepted for review, a multi-disciplinary FDA review team undertakes the most rigorous scientific evaluation in any regulated industry. The review team includes medical officers, clinical pharmacologists, statisticians, chemists, and microbiologists — each reviewing their specific module. The process follows a structured timeline governed by PDUFA performance goals.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">⚖️</div>
      <div>
        <div class="crm-obj-name">FDA Review Process — Key Milestones</div>
        <div class="crm-obj-api">CDER / CBER · Multi-disciplinary review team</div>
      </div>
    </div>
    <div class="crm-obj-desc"><strong>Month 1–2:</strong> Mid-cycle review meeting — FDA reviewers discuss early findings with sponsors if issues are identified (PDUFA VII commitment). <strong>Month 3–4:</strong> Discipline reviews are drafted; FDA may issue <strong>Information Requests (IRs)</strong> asking for clarifications or additional analyses. Response time matters — delays responding to IRs extend the review clock. <strong>Month 5–8:</strong> Pre-submission facility inspections by FDA (for clinical sites and manufacturing facilities); Advisory Committee (AdCom) meeting if scheduled. <strong>Month 9–11:</strong> Labelling negotiations begin — the most commercially critical phase of review because the final label determines what the company can and cannot say about the drug. <strong>PDUFA date:</strong> FDA issues action letter — either an <strong>Approval letter</strong>, a <strong>Complete Response Letter (CRL)</strong>, or (rarely) a <strong>Not Approvable letter</strong>.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#062010">🎤</div>
      <div>
        <div class="crm-obj-name">Advisory Committee (AdCom) Meetings</div>
        <div class="crm-obj-api">Public meeting · External expert panel · Non-binding vote</div>
      </div>
    </div>
    <div class="crm-obj-desc">For drugs with novel mechanisms, complex benefit-risk profiles, or significant public health implications, the FDA convenes an <strong>Advisory Committee (AdCom)</strong> — a panel of external experts (physicians, scientists, statisticians, patient advocates) who review the NDA data in a public meeting and vote on specific questions: typically "Is the drug safe?", "Is the drug effective?", and "Does the benefit outweigh the risk?" The vote is <strong>non-binding</strong> but carries enormous weight — the FDA follows AdCom recommendations approximately 75–80% of the time. AdCom meetings are public events attended by investors, media, and competitor companies. A negative AdCom vote typically causes the sponsor's stock to fall sharply and may precede a CRL.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1408">🏷️</div>
      <div>
        <div class="crm-obj-name">Labelling Negotiation — The Commercial Battleground</div>
        <div class="crm-obj-api">Prescribing Information (PI) · Indications · Boxed Warnings</div>
      </div>
    </div>
    <div class="crm-obj-desc">The drug label (Prescribing Information, or PI) is the most commercially important document produced during development. It defines precisely what the company can say about the drug to physicians and patients. Key label sections the sponsor negotiates with the FDA: <strong>Indications and Usage</strong> — the FDA-approved indication(s); a narrow indication limits the addressable patient population; a broad indication maximises commercial opportunity. <strong>Dosage and Administration</strong> — approved dose, titration schedule, special population dosing. <strong>Contraindications</strong> — absolute restrictions on use. <strong>Warnings and Precautions</strong> — risks that require monitoring or disclosure. <strong>Boxed Warning (Black Box)</strong> — the most serious FDA warning; requires specific language in promotional materials and can significantly restrict commercial uptake. <strong>Clinical Studies</strong> — summary of pivotal trial results; the specific numbers used in this section become the foundation of all medical education and promotional materials.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1e0808">📩</div>
      <div>
        <div class="crm-obj-name">Complete Response Letter (CRL)</div>
        <div class="crm-obj-api">21 CFR 314.110 · Programme delay of 12–24+ months</div>
      </div>
    </div>
    <div class="crm-obj-desc">A <strong>Complete Response Letter (CRL)</strong> is the FDA's formal notification that the application cannot be approved in its current form. The CRL specifies the deficiencies that must be addressed. CRL categories: <strong>Clinical deficiency</strong> — FDA does not accept the primary endpoint as clinically meaningful, or results are not sufficiently robust; may require an additional clinical trial. <strong>CMC deficiency</strong> — manufacturing facility failed inspection or process validation is insufficient. <strong>Safety signal</strong> — new safety information emerging during review changes the benefit-risk assessment. <strong>Labelling</strong> — sponsor and FDA cannot agree on label language. Responding to a CRL typically takes 12–24 months and requires resubmission as a Class 1 (minor; 2-month review) or Class 2 (major; 6-month review) resubmission. CRLs are catastrophic for commercial timelines — revenue projections, hiring plans, and manufacturing commitments all built around the PDUFA date must be torn up and rebuilt.</div>
  </div>
</div>

<!-- ── REMS ── -->
<div class="callout warning" style="margin:32px 0;">
  <div class="callout-title">⚠️ Risk Evaluation and Mitigation Strategies (REMS)</div>
  <p style="margin:0 0 10px">Under the <strong>Food and Drug Administration Amendments Act (FDAAA 2007)</strong>, the FDA can require a <strong>REMS</strong> — a drug safety programme that goes beyond standard labelling to ensure benefits outweigh risks. REMS are required when the drug has a serious risk that standard prescribing information alone cannot adequately communicate or mitigate.</p>
  <p style="margin:0 0 10px"><strong>REMS components can include:</strong> Medication Guide (patient-facing safety document), Communication Plan (targeted outreach to healthcare providers), and/or <strong>Elements to Assure Safe Use (ETASU)</strong> — the most restrictive tier, which can require: prescriber certification (only certified physicians can prescribe), pharmacy certification (only certified pharmacies can dispense), patient enrolment in a registry, monitoring before each prescription, proof of negative pregnancy test.</p>
  <p style="margin:0 0 0"><strong>Commercial impact:</strong> REMS with ETASU significantly restrict the prescribing universe and add friction to every prescription — fewer prescribers, slower access, higher administrative burden on practices. Drugs with REMS require specialised Commercial and Medical Affairs strategies including targeted REMS education, certified prescriber programmes, and patient support services.</p>
</div>

<!-- ── R&D–COMMERCIAL INTERACTION ── -->
<h2 id="ch2-commercial-start">Stage 9 — When Commercial Engagement Starts: The Integrated Timeline</h2>
<p>Commercial and Medical Affairs are not bystanders waiting for R&amp;D to deliver an approved drug. They are active participants who join the programme progressively from Phase IIb onwards. Below is the precise timeline of when each commercial and medical function activates, and what they are doing while R&amp;D completes Phase III and the FDA review.</p>

<div class="timeline" style="margin:28px 0;">
  <div class="tl-item">
    <div class="tl-marker" style="background:#3a2800">★</div>
    <div class="tl-line"></div>
    <div class="tl-body">
      <h4 style="color:#C8A030">Phase IIb PoC Read-out (T minus 5–7 years)</h4>
      <p><strong>Commercial Strategy team</strong> receives first TPP. Begins market opportunity assessment, preliminary competitive landscape, and disease area mapping. <strong>Medical Affairs</strong> drafts the Integrated Evidence Plan — gaps in the evidence that clinical development alone will not fill. <strong>HEOR team</strong> begins designing health economics models for eventual payer submission. <strong>Regulatory Affairs</strong> prepares for EoP2 FDA meeting and determines expedited programme eligibility.</p>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker" style="background:#1a2815">★</div>
    <div class="tl-line"></div>
    <div class="tl-body">
      <h4 style="color:#3AC870">Phase III Start (T minus 4–6 years)</h4>
      <p><strong>Brand team</strong> formally established. Brand planning cycle begins. Disease awareness campaigns may begin (unbranded). <strong>KOL development programme</strong> launched — Medical Affairs identifies and begins scientific engagement with key opinion leaders who will influence clinical practice at launch. <strong>Market access team</strong> begins payer landscape analysis. HEOR sub-studies embedded in Phase III protocol. <strong>Commercial manufacturing</strong> scale-up begins — separate from clinical manufacturing, this is the GMP-validated process that will supply commercial launch.</p>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker" style="background:#1a1845">★</div>
    <div class="tl-line"></div>
    <div class="tl-body">
      <h4 style="color:#6070C0">Phase III Data Read-out (T minus 18–24 months)</h4>
      <p><strong>NDA/BLA filing preparations</strong> begin. <strong>Sales force planning</strong> — sizing, structure, territory design, hiring timeline. <strong>Managed care contracting</strong> — preliminary discussions with major PBMs and payers about formulary positioning. <strong>Medical Education</strong> — planning for physician education programmes, CME content, publications strategy. <strong>Patient advocacy</strong> — partnerships with disease-state patient organisations. <strong>Medical Affairs field team</strong> (MSLs) hiring and training begins.</p>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker" style="background:#1e0808">★</div>
    <div class="tl-line"></div>
    <div class="tl-body">
      <h4 style="color:#C03030">NDA Submission (T minus 12–14 months)</h4>
      <p><strong>Sales force hired and in training.</strong> <strong>Pre-launch medical education</strong> underway — MSLs briefed on Phase III data, scientific slide decks developed and approved. <strong>Payer contracting</strong> intensifies — value dossiers submitted to PBMs, formulary position negotiations begin. <strong>Advisory boards</strong> — physician advisory boards reviewing launch strategies and messaging. <strong>Manufacturing ramp-up</strong> — product manufactured and placed in distribution pipeline. <strong>Regulatory Affairs</strong> responding to FDA information requests, preparing for pre-NDA meetings and potential AdCom.</p>
    </div>
  </div>
  <div class="tl-item">
    <div class="tl-marker" style="background:#062010">★</div>
    <div class="tl-body">
      <h4 style="color:#30C050">Day 0 — FDA Approval &amp; Launch</h4>
      <p>Everything that has been prepared over the preceding 3–5 years is activated simultaneously. <strong>Sales force begins detailing</strong> within 24–48 hours. <strong>Promotional materials</strong> (reviewed and approved through MLR) go live. <strong>Speaker programmes</strong> launch. <strong>Patient assistance programmes</strong> activated. <strong>Reimbursement hub services</strong> (supporting patients through the prior authorisation process) operational. <strong>Medical Affairs</strong> begins fielding medical information requests, MSLs engage with early-adopter physicians. First <strong>Phase 4</strong> post-marketing studies activated.</p>
    </div>
  </div>
</div>

<!-- ── R&D–COMMERCIAL INTERACTION ── -->
<h2 id="ch2-rd-commercial">R&amp;D and Commercial: How They Work Together</h2>
<p>The relationship between R&amp;D and Commercial is not a sequential handoff — it is a deepening collaboration that begins at Phase IIb and intensifies through approval. Each function brings different expertise and different strategic priorities, managed through formal governance structures.</p>

<div class="crm-obj-grid" style="margin:24px 0;">
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a1845">🏛️</div>
      <div>
        <div class="crm-obj-name">Joint Development Committee (JDC)</div>
        <div class="crm-obj-api">Governance body · Cross-functional · Senior leadership</div>
      </div>
    </div>
    <div class="crm-obj-desc">The <strong>Joint Development Committee</strong> is the primary governance forum where R&amp;D and Commercial decisions are aligned. Membership typically includes: Chief Medical Officer, Head of Regulatory Affairs, Head of Clinical Development, VP Commercial, VP Market Access, VP Medical Affairs, VP HEOR, and the Brand General Manager. The JDC reviews: TPP updates, Phase III data interim analyses (if available), regulatory milestone planning, launch readiness, resource allocation across programmes. The JDC also manages the most sensitive R&amp;D–Commercial interface: <strong>when Commercial insight should influence study design</strong> (endpoints, patient populations, comparator selection) without compromising scientific integrity or creating regulatory risk.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#0a2018">🗺️</div>
      <div>
        <div class="crm-obj-name">Target Product Profile (TPP) — The Living Contract</div>
        <div class="crm-obj-api">Updated at each phase gate · Commercial drives aspirational TPP</div>
      </div>
    </div>
    <div class="crm-obj-desc">The TPP exists in two versions that are maintained in parallel: the <strong>Aspirational TPP</strong> (Commercial-led: what does the drug need to look like to be commercially successful?) and the <strong>Minimum Acceptable TPP</strong> (R&amp;D/Regulatory-led: what is the minimum profile that will support approval?). The tension between these two profiles drives clinical programme design. If the aspirational TPP requires a head-to-head superiority trial against the standard of care but the minimum acceptable TPP only requires placebo-controlled trials, the JDC must decide how much commercial risk is acceptable versus the additional cost and risk of the superiority design. The TPP is updated at every major phase gate and directly informs: Phase III endpoint selection, NDA strategy, launch messaging, payer value story, and medical education content.</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#1a2815">📋</div>
      <div>
        <div class="crm-obj-name">Integrated Evidence Plan (IEP)</div>
        <div class="crm-obj-api">Medical Affairs-led · Bridges regulatory and commercial evidence needs</div>
      </div>
    </div>
    <div class="crm-obj-desc">The Integrated Evidence Plan maps all the evidence that needs to exist by launch — and identifies the gaps that Phase III clinical development alone will not fill. Medical Affairs owns the IEP and uses it to plan post-approval studies, registries, and real-world evidence generation. Evidence gaps commonly identified: <strong>Comparative effectiveness</strong> vs. specific competitors (trials compare to placebo; payers want head-to-head data). <strong>Long-term safety</strong> (pivotal trials run 6–24 months; patients will take the drug for years). <strong>Special populations</strong> excluded from Phase III (elderly, renal/hepatic impairment, paediatric). <strong>Quality of life and patient-reported outcomes</strong>. <strong>Real-world adherence and persistence</strong>. Each gap maps to a specific study type, timeline, and owner (Clinical Development, Medical Affairs, HEOR, or partner academic institution).</div>
  </div>
  <div class="crm-obj-card">
    <div class="crm-obj-header">
      <div class="crm-obj-icon" style="background:#3a2800">⚖️</div>
      <div>
        <div class="crm-obj-name">The R&amp;D–Commercial Firewall in Development</div>
        <div class="crm-obj-api">Scientific integrity · Regulatory risk · Blinding management</div>
      </div>
    </div>
    <div class="crm-obj-desc">While R&amp;D and Commercial must collaborate, specific boundaries exist to protect scientific integrity and regulatory compliance. <strong>Commercial teams must not have access to unblinded Phase III data</strong> until the study is officially unblinded and data is locked — early access could influence promotional activity before approval (off-label promotion) or create selective disclosure liability. <strong>Publication timelines must not be driven by commercial considerations</strong> — delaying or suppressing negative study results violates ICH E3 and FDA guidance and creates False Claims Act liability. <strong>Key Opinion Leader (KOL) relationships</strong> must be independently managed by Medical Affairs (scientific exchange) versus Commercial (speakers bureau, advisory boards) — the same physician cannot be engaged simultaneously by both functions for the same drug without documented safeguards. These boundaries are governed by the Commercial–Medical Firewall (detailed in Chapter 5).</div>
  </div>
</div>

<div class="callout insight" style="margin:32px 0 16px;">
  <div class="callout-title">💡 The Overall Attrition Picture</div>
  Of every 10,000 compounds that enter the discovery phase, approximately 250 will advance to pre-clinical testing, 10 will enter clinical trials, 1–2 will reach NDA submission, and roughly 1 will be approved. Average cost per approved medicine: $1–2.6 billion (Tufts CSDD estimates including cost of failures). Average development timeline: 10–15 years from target identification to approval. This extraordinary attrition rate is why pharmaceutical pricing is structured to recoup the cost of many failed programmes, not just the successful one — a reality that defines one of the most important commercial challenges facing the industry.
</div>

"""

# ── Load source files ─────────────────────────────────────────────────────────
try:
    with open(f'{UPLOADS}/pharma_visual_new.html', encoding='utf-8') as f:
        VIS = f.read()
    with open(f'{UPLOADS}/Pharma_Complete_Guide.html', encoding='utf-8') as f:
        BOOK = f.read()
except FileNotFoundError as e:
    sys.exit(f"ERROR: Could not open source file — {e}\n"
             f"Make sure both HTML files are in: {UPLOADS}")

# ── Extraction helpers ────────────────────────────────────────────────────────
def _extract_div(html, open_tag):
    start = html.find(open_tag)
    if start == -1:
        return ''
    depth, i = 0, start
    while i < len(html):
        if html[i:i+4] == '<div':
            depth += 1; i += 4
        elif html[i:i+6] == '</div>':
            depth -= 1; i += 6
            if depth == 0:
                return html[start:i]
        else:
            i += 1
    return html[start:]

def extract_sec(html, sec_id):
    return _extract_div(html, f'<div class="sec" id="{sec_id}">')

def extract_dbox(html, dbox_id):
    return _extract_div(html, f'<div class="dbox" id="{dbox_id}">')

def extract_chapter(html, ch_id):
    return _extract_div(html, f'<div class="chapter" id="{ch_id}">')

# ── Pull visual sections ──────────────────────────────────────────────────────
sec_eco   = extract_sec(VIS, 'eco')
sec_comm  = extract_sec(VIS, 'comm')
sec_med   = extract_sec(VIS, 'med')
sec_bp    = extract_sec(VIS, 'bp')
sec_rdb   = extract_sec(VIS, 'rdb')
sec_lt    = extract_sec(VIS, 'lt')
sec_ld    = extract_sec(VIS, 'ld')
sec_ic    = extract_sec(VIS, 'ic')
sec_hcp   = extract_sec(VIS, 'hcp')
sec_roles = extract_sec(VIS, 'roles')
sec_veeva = extract_sec(VIS, 'veeva')
dbox_mlr  = extract_dbox(VIS, 'mlr')

def wrap_visual(sec_html, title='Visual Reference'):
    return f'''
<figure class="vis-embed" aria-label="{title}">
  <div class="vis-label"><span class="vis-icon">◈</span> {title}</div>
  <div class="vis-inner">{sec_html}</div>
  <figcaption class="vis-cap">{title}</figcaption>
</figure>'''

# ── Pull chapters ─────────────────────────────────────────────────────────────
ch_intro = extract_chapter(BOOK, 'intro')
ch1  = extract_chapter(BOOK, 'ch1')
ch2  = extract_chapter(BOOK, 'ch2')
# Append expanded R&D detail (inside chapter div)
ch2 = ch2[:-6] + CH2_EXTRA + '</div>'
ch3  = extract_chapter(BOOK, 'ch3')
ch4  = extract_chapter(BOOK, 'ch4')
ch5  = extract_chapter(BOOK, 'ch5')
ch6  = extract_chapter(BOOK, 'ch6')
ch7  = extract_chapter(BOOK, 'ch7')
ch8  = extract_chapter(BOOK, 'ch8')
ch9  = extract_chapter(BOOK, 'ch9')
ch10 = extract_chapter(BOOK, 'ch10')
ch_gloss = extract_chapter(BOOK, 'glossary')

# ── Sanitise references ───────────────────────────────────────────────────────
def remove_xenon(html):
    html = re.sub(r'<h2>The Xenon Pharmaceuticals Context</h2>.*?(?=<h2|</div>)',
                  '', html, flags=re.DOTALL)
    html = html.replace('Xenon Pharmaceuticals', 'a leading pharmaceutical company')
    html = html.replace('Xenon', 'the company')
    html = html.replace('azetukalner (XEN1101)', 'a novel CNS therapy')
    html = html.replace('XEN1101', 'the investigational compound')
    return html

ch10 = remove_xenon(ch10)

# ── Inject visuals into chapters ──────────────────────────────────────────────
def inject_after(chapter_html, after_text, inject_html):
    idx = chapter_html.find(after_text)
    if idx == -1:
        return chapter_html + inject_html
    end = idx + len(after_text)
    return chapter_html[:end] + inject_html + chapter_html[end:]

ch1  = inject_after(ch1,  '<h2>The Critical Balance',
    wrap_visual(sec_eco,   '📊 Pharma Enterprise Ecosystem — Visual Map'))
ch3  = inject_after(ch3,  'id="brand-planning"',
    wrap_visual(sec_comm,  '📊 Commercial Affairs — End-to-End Process Flow'))
ch3  = inject_after(ch3,  'id="market-research"',
    wrap_visual(sec_bp,    '📊 Brand Planning Process — Visual Flow'))
ch3  = inject_after(ch3,  'id="hcp-eng"',
    wrap_visual(dbox_mlr,  '📊 MLR Review Workflow — Step by Step'))
ch3  = inject_after(ch3,  'id="market-access"',
    wrap_visual(sec_hcp,   '📊 HCP Journey &amp; Engagement Flow'))
ch4  = inject_after(ch4,  'id="med-strategy"',
    wrap_visual(sec_med,   '📊 Medical Affairs — End-to-End Process Flow'))
ch6  = inject_after(ch6,  '<h2>Stage 1',
    wrap_visual(sec_rdb,   '📊 R&amp;D → Commercial Bridge — Stage Gates'))
ch7  = inject_after(ch7,  '<h2>The Launch Clock',
    wrap_visual(sec_lt,    '📊 36-Month Launch Timeline — Milestones &amp; Workstreams'))
ch7  = inject_after(ch7,  '<h2>Launch Day',
    wrap_visual(sec_ld,    '📊 Launch Day — Hour by Hour Operations'))
ch8  = inject_after(ch8,  '<h2>Medical Affairs — Key Roles',
    wrap_visual(sec_roles, '📊 Org Structure Map — Commercial &amp; Medical Affairs'))
ch10 = inject_after(ch10, 'How the Pieces Connect',
    wrap_visual(sec_ic,    '📊 Cross-Functional Interconnections — Full System Map'))

# ── Tooltip definitions ───────────────────────────────────────────────────────
TOOLTIPS = {
    'MLR review': 'Medical-Legal-Regulatory: three-committee approval required for all promotional materials before external use.',
    'MLR': 'Medical-Legal-Regulatory review — all promotional content must be approved by Medical, Legal, and Regulatory reviewers.',
    'MSL': 'Medical Science Liaison — field-based PhD/PharmD/MD engaging KOLs with peer-level scientific exchange.',
    'KOL': 'Key Opinion Leader — influential HCP (often academic physician or guideline author) whose views shape prescribing patterns.',
    'HCP': 'Healthcare Professional — any licensed provider who can prescribe or recommend medicines.',
    'SFE': 'Sales Force Effectiveness — optimizing field force performance through targeting, IC design, and analytics.',
    'HEOR': 'Health Economics & Outcomes Research — evidence on economic and real-world value used in payer negotiations.',
    'PDMA': 'Prescription Drug Marketing Act (21 CFR Part 203) — governs sampling, requires signed receipts and full audit trail.',
    'NDA': 'New Drug Application — comprehensive FDA filing requesting approval to market a new drug.',
    'BLA': 'Biologics License Application — equivalent to NDA for biological medicines.',
    'PDUFA': 'Prescription Drug User Fee Act — sets FDA review timelines; PDUFA date is the target approval decision date.',
    'REMS': 'Risk Evaluation & Mitigation Strategy — mandatory FDA safety program for drugs with serious risks.',
    'CAPA': 'Corrective and Preventive Action — quality system response to deviations; root-cause analysis + fix + verification.',
    'GxP': 'Good Practice guidelines — GMP, GCP, GLP, GDP, GVP — FDA/ICH quality frameworks for the entire drug lifecycle.',
    'AKS': 'Anti-Kickback Statute — federal law prohibiting payments to induce prescribing; governs all HCP interactions.',
    'SRL': 'Standard Response Letter — pre-approved MLR-reviewed answer to a medical information inquiry.',
    'RWE': 'Real-World Evidence — clinical evidence from claims data, EHR, or registries showing how drugs perform in practice.',
    'P&T': 'Pharmacy & Therapeutics Committee — payer/hospital body that sets formulary placement and access criteria.',
    'IIS': 'Investigator-Initiated Study — research proposed by an external investigator, supported (not controlled) by the company.',
    'MDM': 'Master Data Management — maintaining a single clean HCP/HCO record across all systems (CRM, sampling, Sunshine Act).',
    'TRx': 'Total prescriptions — all prescriptions filled including refills; key commercial performance metric.',
    'NRx': 'New prescriptions — first-time prescriptions; measures new patient starts.',
    'QBR': 'Quarterly Business Review — formal cross-functional meeting to review brand performance and adjust strategy.',
}

TOOLTIP_JS = 'const TIPS = ' + str(TOOLTIPS).replace("'", '"') + ';\n'

# ── Chapter metadata (for navigation footer) ──────────────────────────────────
CHAPTERS = [
    ('intro',    '✦ Introduction'),
    ('ch1',      'Ch 1 · The Big Picture'),
    ('ch2',      'Ch 2 · R&D — Where It Begins'),
    ('ch3',      'Ch 3 · Commercial Affairs'),
    ('ch4',      'Ch 4 · Medical Affairs'),
    ('ch5',      'Ch 5 · The Firewall'),
    ('ch6',      'Ch 6 · R&D Bridge'),
    ('ch7',      'Ch 7 · The Launch'),
    ('ch8',      'Ch 8 · The People'),
    ('ch9',      'Ch 9 · The Rules'),
    ('ch10',     'Ch 10 · Putting It Together'),
    ('ch11',     'Ch 11 · Veeva Systems'),
    ('glossary', 'A–Z Glossary'),
]

def nav_footer(ch_id):
    ids = [c[0] for c in CHAPTERS]
    labels = [c[1] for c in CHAPTERS]
    try:
        idx = ids.index(ch_id)
    except ValueError:
        return ''
    prev_link = (f'<a class="ch-nav-link prev" href="#{ids[idx-1]}">'
                 f'<span class="ch-nav-arrow">←</span>'
                 f'<span class="ch-nav-text">{labels[idx-1]}</span></a>'
                 if idx > 0 else '<span></span>')
    next_link = (f'<a class="ch-nav-link next" href="#{ids[idx+1]}">'
                 f'<span class="ch-nav-text">{labels[idx+1]}</span>'
                 f'<span class="ch-nav-arrow">→</span></a>'
                 if idx < len(ids)-1 else '<span></span>')
    return '<div class="ch-nav-footer">' + prev_link + '<div class="ch-nav-dot">◈</div>' + next_link + '</div>'

# ── Pre-compute nav footers (avoids quoted calls inside the f-string) ─────────
nav_intro    = nav_footer('intro')
nav_ch1      = nav_footer('ch1')
nav_ch2      = nav_footer('ch2')
nav_ch3      = nav_footer('ch3')
nav_ch4      = nav_footer('ch4')
nav_ch5      = nav_footer('ch5')
nav_ch6      = nav_footer('ch6')
nav_ch7      = nav_footer('ch7')
nav_ch8      = nav_footer('ch8')
nav_ch9      = nav_footer('ch9')
nav_ch10     = nav_footer('ch10')
nav_ch11     = nav_footer('ch11')
nav_glossary = nav_footer('glossary')

# ── Full HTML ─────────────────────────────────────────────────────────────────
CRM_EXTRA2 = """

  <!-- ═══════════════════════════════════
       PRODUCT MANAGEMENT
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-products">Product Management in Veeva CRM</h3>

  <p>Every product a pharmaceutical company promotes lives in Veeva CRM as a chain of linked objects — from the master <strong>Product2</strong> record in the global catalog, through territory-level detail configurations, down to the individual Products Detailed child record created inside each Call Report. Brand teams control the detail hierarchy; reps cannot deviate from it. A territory manager cannot spontaneously add a competitor's product or detail a pipeline asset — the system enforces the approved detail list at the point of interaction.</p>

  <p>Product data in CRM is also the pivot point for analytics. Prescription data from IQVIA (NRx/TRx by HCP) is loaded into Veeva Align and surfaced in CRM as HCP-level performance metrics, driving the Next Best Action algorithm that prioritises the rep's daily call list. When a product's CLM engagement scores drop — fewer slides viewed, more negative key message reactions — the brand team sees it in the product dashboard within days and can initiate a content revision cycle through Vault PromoMats.</p>

  <!-- Product Management Object Cards -->
  <div class="crm-obj-grid">
    <div>
      <div class="crm-section-label comm">◈ Product Objects — Commercial</div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Product2 (Master Catalog)</div>
        <div class="crm-obj-api">Product2 — Salesforce standard object, global product master</div>
        <div class="crm-obj-desc">The foundation record for every product in the company portfolio. One Product2 record per brand, formulation, and indication. Linked to all downstream product objects. Brand teams maintain this record; reps have read-only access. Contains regulatory approval status, therapeutic area, and launch date — making it the single source of truth for what is and is not an approved, marketable asset.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">ProductCode</span>
          <span class="crm-field-pill">Therapeutic_Area__c</span>
          <span class="crm-field-pill">Indication__c</span>
          <span class="crm-field-pill">Launch_Date__c</span>
          <span class="crm-field-pill">Approval_Status__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Product Detail / Detail Group</div>
        <div class="crm-obj-api">Detail_Group_vod__c / Product_vod__c — controls rep-level detail rights</div>
        <div class="crm-obj-desc">The Detail Group object controls exactly which products a rep can detail and in what priority order (1st detail = primary focus, 2nd = secondary, 3rd = reminder mention only). Each cycle plan period, brand ops assigns the detail hierarchy per territory. A rep who attempts to detail a product not on their approved list receives a CRM validation error. Co-promote configurations (two companies co-promoting the same product) are also managed here.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Detail_Priority_vod__c</span>
          <span class="crm-field-pill">Territory2__c</span>
          <span class="crm-field-pill">Cycle_Plan_vod__c</span>
          <span class="crm-field-pill">Co_Promote_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Key Message Library (Key_Message_vod__c)</div>
        <div class="crm-obj-api">Key_Message_vod__c — MLR-approved promotional messages per product</div>
        <div class="crm-obj-desc">The Key Message object is the brand team's approved message library — every claim, benefit statement, and differentiator that reps are authorised to communicate. Messages are created by brand, reviewed through MLR, and published to the CRM content library linked to the relevant CLM slides. During a call, reps select the key messages discussed and capture the HCP's reaction (Strongly Agree → Strongly Disagree). This reaction data is the primary signal feeding the CLM closed-loop analytics.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Message_Text_vod__c</span>
          <span class="crm-field-pill">Product_vod__c</span>
          <span class="crm-field-pill">Category_vod__c</span>
          <span class="crm-field-pill">MLR_Status_vod__c</span>
          <span class="crm-field-pill">Expires_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Product Metrics (IQVIA Integration)</div>
        <div class="crm-obj-api">Rx_Data_vod__c / Veeva Align — prescription data at HCP level</div>
        <div class="crm-obj-desc">Monthly IQVIA prescription data (NRx, TRx, market share) is loaded into Veeva Align and surfaced in Veeva CRM as HCP-level product performance metrics. Territory managers see each HCP's prescribing volume and brand share directly on the account page. This data feeds the Cycle Plan Account targeting (high-decile prescribers get higher call frequency targets) and the AI-powered Next Best Action engine that recommends which HCP to call next and which message to lead with.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">NRx_vod__c</span>
          <span class="crm-field-pill">TRx_vod__c</span>
          <span class="crm-field-pill">Market_Share_vod__c</span>
          <span class="crm-field-pill">Decile_vod__c</span>
          <span class="crm-field-pill">Period_vod__c</span>
        </div>
      </div>
    </div>

    <div>
      <div class="crm-section-label comm">◈ Product Objects — Medical Affairs</div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Scientific Platform Messages</div>
        <div class="crm-obj-api">Key_Message_vod__c (Medical record type) — non-promotional scientific content</div>
        <div class="crm-obj-desc">Medical Affairs maintains a separate set of Key Message records with a Medical record type — the scientific platform. These messages are evidence-based statements about mechanism of action, clinical trial data, and real-world evidence that MSLs can share during scientific exchange. Unlike commercial messages, these are not subject to advertising regulations but must still be accurate, balanced, and supported by data. They are stored in Vault Medical and pulled into the MSL's CRM tablet for field use.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Record_Type = Medical</span>
          <span class="crm-field-pill">Evidence_Level_vod__c</span>
          <span class="crm-field-pill">Reference_vod__c</span>
          <span class="crm-field-pill">Clinical_Data_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Publication (Publication_vod__c)</div>
        <div class="crm-obj-api">Publication_vod__c — scientific publications linked to KOLs and products</div>
        <div class="crm-obj-desc">Tracks peer-reviewed publications (journal articles, congress abstracts, posters) that MSLs reference during scientific exchange. Each Publication record links to the relevant Product2 and to KOL author Contact records. MSLs can attach publications to call reports as supporting references. The publication database also tracks authorship — identifying which KOLs are publishing in therapeutic areas relevant to the company's pipeline, informing KOL engagement strategy.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">PubMed_ID_vod__c</span>
          <span class="crm-field-pill">Journal_vod__c</span>
          <span class="crm-field-pill">Publication_Date_vod__c</span>
          <span class="crm-field-pill">Author_Contact__c</span>
          <span class="crm-field-pill">Product_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Study / IIS (Study_vod__c)</div>
        <div class="crm-obj-api">Study_vod__c — investigator-initiated and company-sponsored study tracking</div>
        <div class="crm-obj-desc">Investigator-Initiated Studies (IIS) proposed by external HCPs, and company-sponsored post-marketing studies, are tracked through the Study object. Each record captures the study protocol, principal investigator (linked to Contact/Account), funding amount, study status, and publication timeline. MSLs managing IIS relationships update the study status and log interactions in their MSL call reports referencing the study. Ensures all financial support is documented for Sunshine Act reporting.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Study_Type_vod__c</span>
          <span class="crm-field-pill">PI_Contact__c</span>
          <span class="crm-field-pill">Funding_Amount_vod__c</span>
          <span class="crm-field-pill">Status_vod__c</span>
          <span class="crm-field-pill">Protocol_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Grant (Grant_vod__c)</div>
        <div class="crm-obj-api">Grant_vod__c — medical education and research grant management</div>
        <div class="crm-obj-desc">Pharmaceutical companies provide educational and research grants to medical institutions, professional societies, and independent medical education providers. Each grant record tracks recipient organisation, grant purpose (CME programme, research, patient education), amount, terms, and outcome reporting. Grant workflows enforce the separation of commercial intent — all grants must go through an independent grants committee and cannot be linked to prescribing expectations. Reported under the Sunshine Act and monitored for AKS compliance.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Grant_Type_vod__c</span>
          <span class="crm-field-pill">Recipient_Account__c</span>
          <span class="crm-field-pill">Amount_vod__c</span>
          <span class="crm-field-pill">Committee_Decision_vod__c</span>
          <span class="crm-field-pill">Sunshine_Flag_vod__c</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Product-to-Detail Flow SVG -->
  <figure class="vis-embed" aria-label="Product Management Flow">
    <div class="vis-label"><span class="vis-icon">◈</span> Product Management — From Catalog to Call Report &amp; Analytics</div>
    <div class="vis-inner" style="padding:22px 16px;">
      <svg viewBox="0 0 960 210" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:680px;display:block;">
        <defs>
          <marker id="pa" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#30363D"/></marker>
          <marker id="pb" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#1B3A6B"/></marker>
          <marker id="pg" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#4ABA6A"/></marker>
        </defs>
        <rect width="960" height="210" fill="#0D1117"/>

        <!-- Step 1: Product2 -->
        <rect x="8" y="30" width="140" height="120" rx="7" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <circle cx="78" cy="58" r="16" fill="#4A2080" fill-opacity=".3" stroke="#4A2080" stroke-width="1"/>
        <text x="78" y="63" text-anchor="middle" fill="#C0A0FF" font-size="13" font-weight="700">P2</text>
        <text x="78" y="90" text-anchor="middle" fill="#C0A0FF" font-size="11" font-weight="700">Product2</text>
        <text x="78" y="104" text-anchor="middle" fill="#7060A0" font-size="9">Master Catalog</text>
        <text x="78" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">Name · Code</text>
        <text x="78" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Indication · Status</text>
        <text x="78" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">Therapeutic Area</text>
        <circle cx="8" cy="30" r="9" fill="#4A2080"/>
        <text x="8" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">1</text>

        <!-- Step 2: Territory-Product Config -->
        <rect x="168" y="30" width="148" height="120" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <circle cx="242" cy="58" r="16" fill="#1B3A6B" fill-opacity=".4" stroke="#1B3A6B" stroke-width="1"/>
        <text x="242" y="63" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">T-P</text>
        <text x="242" y="90" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">Territory-Product</text>
        <text x="242" y="104" text-anchor="middle" fill="#3A6090" font-size="9">Config by Brand Ops</text>
        <text x="242" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">Territory → Brand mapping</text>
        <text x="242" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Co-promote rules</text>
        <text x="242" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">Cycle period window</text>
        <circle cx="168" cy="30" r="9" fill="#1B3A6B"/>
        <text x="168" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">2</text>

        <!-- Step 3: Detail Priority -->
        <rect x="336" y="30" width="148" height="120" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <circle cx="410" cy="58" r="16" fill="#1B3A6B" fill-opacity=".4" stroke="#1B3A6B" stroke-width="1"/>
        <text x="410" y="63" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">D#</text>
        <text x="410" y="90" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">Detail Priority</text>
        <text x="410" y="104" text-anchor="middle" fill="#3A6090" font-size="9">Per rep / per cycle</text>
        <text x="410" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">1st · 2nd · 3rd slot</text>
        <text x="410" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Key messages linked</text>
        <text x="410" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">CLM deck assigned</text>
        <circle cx="336" cy="30" r="9" fill="#1B3A6B"/>
        <text x="336" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">3</text>

        <!-- Step 4: CLM Presentation -->
        <rect x="504" y="30" width="148" height="120" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <circle cx="578" cy="58" r="16" fill="#1B3A6B" fill-opacity=".4" stroke="#1B3A6B" stroke-width="1"/>
        <text x="578" y="63" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">CLM</text>
        <text x="578" y="90" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">CLM Presentation</text>
        <text x="578" y="104" text-anchor="middle" fill="#3A6090" font-size="9">iPad visual aid</text>
        <text x="578" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">Vault PromoMats approved</text>
        <text x="578" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Slide ID + timing tracked</text>
        <text x="578" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">Auto-expires on review date</text>
        <circle cx="504" cy="30" r="9" fill="#1B3A6B"/>
        <text x="504" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">4</text>

        <!-- Step 5: Products Detailed -->
        <rect x="672" y="30" width="148" height="120" rx="7" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <circle cx="746" cy="58" r="16" fill="#0B5E5E" fill-opacity=".4" stroke="#0B5E5E" stroke-width="1"/>
        <text x="746" y="63" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">PD</text>
        <text x="746" y="90" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Products Detailed</text>
        <text x="746" y="104" text-anchor="middle" fill="#1A5050" font-size="9">Child of Call Report</text>
        <text x="746" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">Brand + priority + reaction</text>
        <text x="746" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Key msg reaction captured</text>
        <text x="746" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">Locked on call submit</text>
        <circle cx="672" cy="30" r="9" fill="#0B5E5E"/>
        <text x="672" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">5</text>

        <!-- Step 6: Analytics -->
        <rect x="840" y="30" width="115" height="120" rx="7" fill="#0D1A10" stroke="#2A7A3A" stroke-width="1.5"/>
        <circle cx="897" cy="58" r="16" fill="#2A7A3A" fill-opacity=".4" stroke="#2A7A3A" stroke-width="1"/>
        <text x="897" y="63" text-anchor="middle" fill="#4ABA6A" font-size="11" font-weight="700">∑</text>
        <text x="897" y="90" text-anchor="middle" fill="#4ABA6A" font-size="11" font-weight="700">Product SFE</text>
        <text x="897" y="104" text-anchor="middle" fill="#2A6A3A" font-size="9">Analytics Dashboard</text>
        <text x="897" y="118" text-anchor="middle" fill="#4A5568" font-size="8.5">NRx · TRx · share</text>
        <text x="897" y="130" text-anchor="middle" fill="#4A5568" font-size="8.5">Call rate per brand</text>
        <text x="897" y="142" text-anchor="middle" fill="#4A5568" font-size="8.5">Msg adoption score</text>
        <circle cx="840" cy="30" r="9" fill="#2A7A3A"/>
        <text x="840" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">6</text>

        <!-- Connecting arrows -->
        <line x1="148" y1="90" x2="168" y2="90" stroke="#4A2080" stroke-width="1.5" marker-end="url(#pa)"/>
        <line x1="316" y1="90" x2="336" y2="90" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#pb)"/>
        <line x1="484" y1="90" x2="504" y2="90" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#pb)"/>
        <line x1="652" y1="90" x2="672" y2="90" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#pb)"/>
        <line x1="820" y1="90" x2="840" y2="90" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#pa)"/>

        <!-- Return feedback arrow at bottom -->
        <path d="M897,155 Q897,185 580,195 Q265,200 78,185 L78,155" stroke="#2A7A3A" stroke-width="1" fill="none" stroke-dasharray="4,3" marker-end="url(#pg)"/>
        <text x="490" y="206" text-anchor="middle" fill="#2A6A3A" font-size="8.5" font-style="italic">CLM analytics feed back to brand team → content optimisation → back through MLR → updated CLM deck</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Product Management — from Product2 master record through territory config to call analytics and the CLM feedback loop</figcaption>
  </figure>

  <!-- ═══════════════════════════════════
       MIRF & MEDICAL INFORMATION
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-mirf">Medical Information Request Form (MIRF) — Lifecycle &amp; Objects</h3>

  <p>A Medical Information Request Form (MIRF) is the formal record of any question an HCP — or, in rare cases, a patient or caregiver — submits to a pharmaceutical company about one of its products. In Veeva CRM this is captured as a <strong>Medical_Inquiry_vod__c</strong> record, but the MIRF is a broader cross-channel process: the same object records an inquiry whether it arrives via a commercial rep during a field call, through the company's 1-800 Medical Information hotline, at a congress booth, or through a digital web form. What the channel determines is the urgency, the response method, and the compliance pathway — not the underlying data model.</p>

  <p>Every MIRF, regardless of source, triggers a mandatory <strong>Adverse Event (AE) screening</strong> within 24 hours of receipt. If the HCP's question contains any information suggesting a patient experienced a negative outcome while taking the product, a parallel AE workflow is opened in the Pharmacovigilance system — the MIRF is never closed until the AE report is resolved. For non-AE inquiries, the Medical Information team classifies the question, retrieves the appropriate Standard Response Letter (SRL) from Vault Medical, and responds within a defined SLA (typically 5 business days for standard inquiries, 24 hours for urgent clinical questions). Off-label inquiries can be answered only if the request was genuinely unsolicited — the system timestamps this classification and it cannot be changed after submission.</p>

  <!-- MIRF Lifecycle SVG -->
  <figure class="vis-embed" aria-label="MIRF Lifecycle Flowchart">
    <div class="vis-label"><span class="vis-icon">◈</span> MIRF Lifecycle — Medical_Inquiry_vod__c End-to-End Flow</div>
    <div class="vis-inner" style="padding:20px 16px;">
      <svg viewBox="0 0 960 480" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:680px;display:block;">
        <defs>
          <marker id="ma" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#30363D"/></marker>
          <marker id="mb" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#0B5E5E"/></marker>
          <marker id="mr" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#B01010"/></marker>
          <marker id="mg" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#2A7A3A"/></marker>
          <marker id="mo" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#E05A00"/></marker>
        </defs>
        <rect width="960" height="480" fill="#0D1117"/>

        <!-- ── ENTRY CHANNELS (top) ── -->
        <text x="480" y="20" text-anchor="middle" fill="#4A5568" font-size="9" font-weight="700" letter-spacing="2">ENTRY CHANNELS</text>

        <rect x="20" y="28" width="150" height="52" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="95" y="48" text-anchor="middle" fill="#7EC8C8" font-size="10.5" font-weight="700">Rep-Assisted</text>
        <text x="95" y="62" text-anchor="middle" fill="#4A5568" font-size="8.5">CRM Medical Inquiry</text>
        <text x="95" y="73" text-anchor="middle" fill="#4A5568" font-size="8.5">created during call</text>

        <rect x="192" y="28" width="150" height="52" rx="6" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="267" y="48" text-anchor="middle" fill="#2A9A9A" font-size="10.5" font-weight="700">HCP Direct</text>
        <text x="267" y="62" text-anchor="middle" fill="#4A5568" font-size="8.5">1-800 hotline or</text>
        <text x="267" y="73" text-anchor="middle" fill="#4A5568" font-size="8.5">web portal submission</text>

        <rect x="364" y="28" width="150" height="52" rx="6" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="439" y="48" text-anchor="middle" fill="#2A9A9A" font-size="10.5" font-weight="700">Congress / Event</text>
        <text x="439" y="62" text-anchor="middle" fill="#4A5568" font-size="8.5">MSL captures at</text>
        <text x="439" y="73" text-anchor="middle" fill="#4A5568" font-size="8.5">Medical_Event booth</text>

        <rect x="536" y="28" width="150" height="52" rx="6" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="611" y="48" text-anchor="middle" fill="#2A9A9A" font-size="10.5" font-weight="700">Digital / Email</text>
        <text x="611" y="62" text-anchor="middle" fill="#4A5568" font-size="8.5">Approved Email reply</text>
        <text x="611" y="73" text-anchor="middle" fill="#4A5568" font-size="8.5">or website inquiry form</text>

        <rect x="708" y="28" width="230" height="52" rx="6" fill="#1A1010" stroke="#5A2000" stroke-width="1.5"/>
        <text x="823" y="48" text-anchor="middle" fill="#FFA657" font-size="10.5" font-weight="700">Spontaneous / Literature</text>
        <text x="823" y="62" text-anchor="middle" fill="#4A5568" font-size="8.5">Published case report or</text>
        <text x="823" y="73" text-anchor="middle" fill="#4A5568" font-size="8.5">unsolicited patient report</text>

        <!-- Converge arrows -->
        <line x1="95" y1="80" x2="420" y2="116" stroke="#1B3A6B" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#ma)"/>
        <line x1="267" y1="80" x2="438" y2="116" stroke="#0B5E5E" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#mb)"/>
        <line x1="439" y1="80" x2="453" y2="116" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#mb)"/>
        <line x1="611" y1="80" x2="468" y2="116" stroke="#0B5E5E" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#mb)"/>
        <line x1="823" y1="80" x2="488" y2="116" stroke="#E05A00" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#mo)"/>

        <!-- ── STEP 1: Medical Inquiry Created ── -->
        <rect x="270" y="118" width="420" height="58" rx="7" fill="#071E1E" stroke="#2A9A9A" stroke-width="2"/>
        <text x="480" y="140" text-anchor="middle" fill="#2A9A9A" font-size="12" font-weight="700">Medical_Inquiry_vod__c — Record Created</text>
        <text x="480" y="155" text-anchor="middle" fill="#8B949E" font-size="9.5">Source · Product · Question text · HCP NPI · Inquiry Type · Urgency flag · Response method</text>
        <text x="480" y="168" text-anchor="middle" fill="#4A5568" font-size="8.5">Status = Open · Timestamp = intake datetime (21 CFR Part 11)</text>
        <circle cx="270" cy="118" r="10" fill="#0B5E5E"/>
        <text x="270" y="122" text-anchor="middle" fill="white" font-size="9" font-weight="700">①</text>

        <!-- ── STEP 2: AE Screening ── -->
        <line x1="480" y1="176" x2="480" y2="202" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#mb)"/>
        <!-- Diamond for AE decision -->
        <polygon points="480,205 560,232 480,260 400,232" fill="#200808" stroke="#B01010" stroke-width="2"/>
        <text x="480" y="228" text-anchor="middle" fill="#F87070" font-size="10.5" font-weight="700">AE Screening</text>
        <text x="480" y="242" text-anchor="middle" fill="#C85050" font-size="9">Mandatory · 24h SLA</text>
        <circle cx="400" cy="205" r="10" fill="#B01010"/>
        <text x="400" y="209" text-anchor="middle" fill="white" font-size="9" font-weight="700">②</text>

        <!-- AE Found branch (right) -->
        <line x1="560" y1="232" x2="650" y2="232" stroke="#B01010" stroke-width="1.5" marker-end="url(#mr)"/>
        <rect x="650" y="206" width="290" height="52" rx="6" fill="#200808" stroke="#B01010" stroke-width="1.5"/>
        <text x="795" y="226" text-anchor="middle" fill="#F87070" font-size="10.5" font-weight="700">⚠ AE Workflow Opened</text>
        <text x="795" y="240" text-anchor="middle" fill="#8B949E" font-size="8.5">Parallel PV report · 15-day FDA clock starts</text>
        <text x="795" y="252" text-anchor="middle" fill="#8B949E" font-size="8.5">MIRF stays open until AE resolved</text>
        <text x="562" y="222" fill="#B01010" font-size="8.5" font-weight="700">AE Found</text>

        <!-- No AE continue -->
        <text x="445" y="272" fill="#0B5E5E" font-size="8.5" font-weight="700">No AE</text>
        <line x1="480" y1="260" x2="480" y2="286" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#mb)"/>

        <!-- ── STEP 3: Classification ── -->
        <rect x="180" y="288" width="600" height="50" rx="7" fill="#061818" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="480" y="308" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Classify Inquiry Type</text>
        <text x="480" y="322" text-anchor="middle" fill="#4A5568" font-size="9">On-label Approved Use &nbsp;|&nbsp; Off-label (Unsolicited only) &nbsp;|&nbsp; Pipeline / Pre-approval &nbsp;|&nbsp; Competitor &nbsp;|&nbsp; Pharmacovigilance</text>
        <text x="480" y="334" text-anchor="middle" fill="#4A5568" font-size="8">Off-label classification is timestamped and immutable — confirms the inquiry was unsolicited before any response is given</text>
        <circle cx="180" cy="288" r="10" fill="#0B5E5E"/>
        <text x="180" y="292" text-anchor="middle" fill="white" font-size="9" font-weight="700">③</text>

        <line x1="480" y1="338" x2="480" y2="360" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#mb)"/>

        <!-- ── STEP 4: SRL Check (diamond) ── -->
        <polygon points="480,362 570,388 480,414 390,388" fill="#061818" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="480" y="384" text-anchor="middle" fill="#2A9A9A" font-size="10" font-weight="700">SRL Available?</text>
        <text x="480" y="398" text-anchor="middle" fill="#1A5050" font-size="8.5">Check Vault Medical</text>
        <circle cx="390" cy="362" r="10" fill="#0B5E5E"/>
        <text x="390" y="366" text-anchor="middle" fill="white" font-size="9" font-weight="700">④</text>

        <!-- YES → send SRL (right) -->
        <line x1="570" y1="388" x2="636" y2="388" stroke="#2A7A3A" stroke-width="1.5" marker-end="url(#mg)"/>
        <rect x="636" y="364" width="314" height="48" rx="6" fill="#0A1A0A" stroke="#2A7A3A" stroke-width="1.5"/>
        <text x="793" y="384" text-anchor="middle" fill="#4ABA6A" font-size="11" font-weight="700">✓ Send SRL + Cover Note</text>
        <text x="793" y="398" text-anchor="middle" fill="#4A5568" font-size="8.5">Retrieve from Vault Medical · Attach cover note confirming unsolicited nature</text>
        <text x="793" y="408" text-anchor="middle" fill="#4A5568" font-size="8.5">Log response · Status = Closed · Archive</text>
        <text x="572" y="380" fill="#2A7A3A" font-size="8.5" font-weight="700">Yes</text>

        <!-- NO → custom response (down) -->
        <text x="440" y="428" fill="#E05A00" font-size="8.5" font-weight="700">No SRL</text>
        <line x1="480" y1="414" x2="480" y2="436" stroke="#E05A00" stroke-width="1.5" marker-end="url(#mo)"/>
        <rect x="300" y="438" width="360" height="38" rx="6" fill="#1A0D00" stroke="#E05A00" stroke-width="1.5"/>
        <text x="480" y="455" text-anchor="middle" fill="#FFA657" font-size="10.5" font-weight="700">⑤ Draft Custom Response</text>
        <text x="480" y="468" text-anchor="middle" fill="#4A5568" font-size="8.5">Medical Affairs review → Approve → Respond → Consider creating new SRL</text>

        <!-- SLA annotation -->
        <rect x="8" y="362" width="175" height="52" rx="5" fill="#0A0A0A" stroke="#2A3020" stroke-width="1"/>
        <text x="95" y="380" text-anchor="middle" fill="#6A7A50" font-size="9" font-weight="700">Response SLA</text>
        <text x="95" y="394" text-anchor="middle" fill="#4A5568" font-size="8.5">Standard: 5 business days</text>
        <text x="95" y="406" text-anchor="middle" fill="#4A5568" font-size="8.5">Urgent / clinical: 24 hours</text>
        <text x="95" y="416" text-anchor="middle" fill="#4A5568" font-size="8.5">AE parallel: 15 days (FDA)</text>
      </svg>
    </div>
    <figcaption class="vis-cap">MIRF lifecycle — from multi-channel intake through AE screening, classification, SRL retrieval, and response</figcaption>
  </figure>

  <!-- MIRF Object Cards -->
  <div class="crm-obj-grid" style="margin-top:24px;">
    <div>
      <div class="crm-section-label med">◈ MIRF — Key Object Fields</div>
      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Medical Inquiry — Full Field Reference</div>
        <div class="crm-obj-api">Medical_Inquiry_vod__c — the MIRF object in Veeva CRM</div>
        <div class="crm-obj-desc">Every field in the Medical Inquiry object serves a specific compliance purpose. The Inquiry Type field locks at submission and cannot be changed — this is critical for off-label responses where the unsolicited nature must be permanently documented. The AE Flag, once checked, triggers a parallel Pharmacovigilance workflow that operates independently of the medical information response process. Response Delivery Method and Actual Response Date feed the SLA monitoring dashboard reviewed by the Medical Information director weekly.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Inquiry_Type_vod__c</span>
          <span class="crm-field-pill">Source_vod__c</span>
          <span class="crm-field-pill">Product_vod__c</span>
          <span class="crm-field-pill">AE_Flag_vod__c</span>
          <span class="crm-field-pill">Question_Text_vod__c</span>
          <span class="crm-field-pill">Response_Method_vod__c</span>
          <span class="crm-field-pill">SRL_vod__c</span>
          <span class="crm-field-pill">Response_Date_vod__c</span>
          <span class="crm-field-pill">Status_vod__c</span>
          <span class="crm-field-pill">Escalation_Flag_vod__c</span>
        </div>
      </div>
    </div>
    <div>
      <div class="crm-section-label med">◈ SRL — Standard Response Letter</div>
      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Standard Response Letter (SRL)</div>
        <div class="crm-obj-api">Stored in Vault Medical — retrieved via Medical_Inquiry_vod__c.SRL_vod__c lookup</div>
        <div class="crm-obj-desc">An SRL is a pre-written, MLR-reviewed answer to a commonly asked medical question. When a Medical Information specialist receives a MIRF, the first step is to search Vault Medical for a matching SRL by product and inquiry category. SRLs are versioned — if the clinical evidence changes, the old SRL is superseded and a new one is created through the MLR workflow. Off-label SRLs exist but can only be sent in documented response to a genuinely unsolicited question — they are never proactively distributed. Every SRL sent is logged against the Medical Inquiry record, creating the full response audit trail.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">SRL_ID</span>
          <span class="crm-field-pill">Product</span>
          <span class="crm-field-pill">Version</span>
          <span class="crm-field-pill">MLR_Approval_Date</span>
          <span class="crm-field-pill">Label_Status</span>
          <span class="crm-field-pill">Expiry_Date</span>
          <span class="crm-field-pill">Distribution_Log</span>
        </div>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════
       ADDITIONAL OBJECTS REFERENCE
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-ref">Additional CRM Objects — Complete Reference</h3>

  <p>Beyond the primary interaction objects, Veeva CRM contains a library of supporting objects that handle territory operations, compliance monitoring, scheduling, and field intelligence. The table below covers every significant object used by commercial and medical affairs teams — including several that are not covered in standard Veeva training but are critical to day-to-day operations.</p>

  <!-- Additional Objects — 3-column responsive grid -->
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin:22px 0 36px;">

    <!-- Commercial Supporting Objects -->
    <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;">
      <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#4A7ABF;margin-bottom:12px;padding-bottom:6px;border-bottom:1px solid #1B3A6B;">◈ Commercial — Territory &amp; Planning</div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Address_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">HCP practice location</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Primary/secondary practice addresses, used for territory routing, call planning, and sample shipment. Validated against Veeva Network.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">TSF_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Territory Sales Force</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Defines the hierarchy of territories — district, region, national — and maps each rep to their territory. Foundation of the SFE rollup reporting structure.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Account_Plan_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Strategic KAM account plan</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Used by Key Account Managers for hospital systems, IDNs, and large group practices. Captures account objectives, stakeholder map, P&amp;T committee timeline, and formulary status.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Scheduled_Call_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Pre-booked appointment</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Calendar-blocked visits with HCPs. Converts to a full Call Report on execution. Drives rep planning efficiency and reduces missed target HCP visits.</div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Alert_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">HQ-to-field notification</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Push messages from headquarters to field — new safety label update, competitive intelligence, launch activation, field force contests. Requires rep acknowledgement, creating a read-receipt audit trail.</div>
      </div>
    </div>

    <!-- Sample & Compliance Objects -->
    <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;">
      <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#4A7ABF;margin-bottom:12px;padding-bottom:6px;border-bottom:1px solid #1B3A6B;">◈ Commercial — Samples &amp; Compliance</div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Inventory_Monitoring_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Real-time rep sample inventory</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Each rep's live sample balance per product and lot. System alerts when inventory falls below reorder threshold or when a lot approaches expiry. Feeds quarterly PDMA reconciliation report.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Sample_Request_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">HCP-initiated sample request</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">When an HCP requests specific samples outside of a face-to-face rep visit (via portal, phone, or mail), a Sample Request record is created. It requires the same HCP signature and PDMA compliance as an in-person drop.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Multichannel_Consent_Line_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Per-channel consent record</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Child of Multichannel_Consent — one record per channel (email, SMS, remote detail). Stores opt-in date, method (verbal/written), and jurisdiction. A single withdrawal record suppresses all digital outreach within 24 hours.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Survey_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">HCP survey instrument</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Configurable survey forms delivered via CRM during or after a call. Used for brand perception research, patient identification questions, treatment landscape surveys. Responses feed Market Research analytics, not call metrics.</div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;color:#7EC8C8;margin-bottom:2px;">Route_vod__c</div>
        <div style="font-size:9px;color:#3A6090;font-family:monospace;margin-bottom:4px;">Daily call routing optimisation</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">AI-optimised routing sequences for a rep's daily call list, minimising drive time while maximising call count against high-priority Cycle Plan targets. Integrates with Google Maps via the Veeva CRM mobile app.</div>
      </div>
    </div>

    <!-- Medical Affairs Supporting Objects -->
    <div style="background:#0D1117;border:1px solid #21262D;border-radius:8px;padding:14px;">
      <div style="font-size:9px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#2A9A9A;margin-bottom:12px;padding-bottom:6px;border-bottom:1px solid #0B5E5E;">◈ Medical Affairs — Supporting Objects</div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#2A9A9A;margin-bottom:2px;">Medical_Event_Attendance_vod__c</div>
        <div style="font-size:9px;color:#1A5050;font-family:monospace;margin-bottom:4px;">HCP event participation record</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">One attendance record per HCP per event. Captures role (attendee/speaker/chair/moderator), all TOV items (honorarium, travel, accommodation, meals), and FMV validation. The primary Sunshine Act data source for the annual CMS Open Payments report.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#2A9A9A;margin-bottom:2px;">Publication_vod__c</div>
        <div style="font-size:9px;color:#1A5050;font-family:monospace;margin-bottom:4px;">Scientific literature tracker</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Journals, congress abstracts, posters, and manuscripts linked to KOL accounts. MSLs reference publications in call reports. Authorship mapping identifies publication-active KOLs for advisory board and IIS engagement.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#2A9A9A;margin-bottom:2px;">Study_vod__c (IIS)</div>
        <div style="font-size:9px;color:#1A5050;font-family:monospace;margin-bottom:4px;">Investigator-initiated study tracking</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Full lifecycle management of externally-proposed IIS: submission → scientific review → legal review → funding approval → study execution → publication. MSL manages the KOL relationship and logs all interactions via MSL Call Reports linked to the study record.</div>
      </div>
      <div style="margin-bottom:10px;">
        <div style="font-size:11px;font-weight:700;color:#2A9A9A;margin-bottom:2px;">Grant_vod__c</div>
        <div style="font-size:9px;color:#1A5050;font-family:monospace;margin-bottom:4px;">Medical education &amp; research grants</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Independent medical education (CME) grants and research support grants. All grants flow through an independent grants committee — commercial teams have no visibility. Grant amounts are captured for Sunshine Act reporting and AKS compliance audits.</div>
      </div>
      <div>
        <div style="font-size:11px;font-weight:700;color:#2A9A9A;margin-bottom:2px;">Insight_vod__c (Medical Insight)</div>
        <div style="font-size:9px;color:#1A5050;font-family:monospace;margin-bottom:4px;">Field intelligence from MSLs</div>
        <div style="font-size:10.5px;color:#8B949E;line-height:1.5;">Structured observations about treatment landscape, competitive activity, unmet medical needs, and prescriber sentiment. Submitted by MSLs, reviewed by MSL directors, and aggregated into quarterly Medical Affairs Insight Reports that directly inform medical strategy and evidence generation plans.</div>
      </div>
    </div>
  </div>

"""

VAULT_EXTRA = """
  <h2 id="veeva-vault">Vault PromoMats &#8212; MLR in the Cloud</h2>

  <p>Vault PromoMats is Veeva&#x27;s cloud-based content management and Medical-Legal-Regulatory (MLR) review platform. Every promotional and non-promotional piece of content a pharmaceutical company produces &#8212; from a rep&#x27;s iPad CLM deck to a patient brochure to a speaker slide set &#8212; must pass through PromoMats before it can ever reach a healthcare professional. The platform is the single system of record for content creation, review, approval, versioning, distribution, and retirement. It is 21 CFR Part 11 validated: every action &#8212; every save, every annotation, every vote &#8212; is permanently timestamped and attributed to an authenticated user, creating an FDA-auditable chain of evidence for every piece of promotional content.</p>

  <p>PromoMats sits at the centre of the pharmaceutical content supply chain. Brand teams upload creative briefs and draft copy; the platform routes the draft simultaneously to Medical, Legal, and Regulatory reviewers; each reviewer annotates the document and casts a binding vote; and the workflow engine enforces resolution of every objection before an approval can be issued. On the day of approval, a webhook fires to Veeva CRM and the content automatically appears in the field force&#x27;s approved content library. On the expiration date, the same mechanism withdraws it automatically &#8212; with no manual intervention and no risk of reps continuing to use outdated materials after a label change.</p>

  <p>PromoMats is not just a routing tool. It enforces the <strong>claims-and-references</strong> framework that underpins FDA promotional compliance: every factual claim in every document must be linked to a published, peer-reviewed reference. Regulatory reviewers verify the reference supports the exact claim made at the significance level stated. If a reference is later retracted, every document whose claims depend on it is automatically flagged for re-review. This architectural linkage transforms what was previously a manual compliance burden into a system-enforced quality gate that scales across hundreds of documents and dozens of products simultaneously.</p>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="promomats-docs">Promotional Document Types</h3>

  <p>PromoMats distinguishes between <strong>promotional materials</strong> &#8212; those subject to 21 CFR Part 202 that make comparative or efficacy claims &#8212; and <strong>non-promotional scientific materials</strong>, which communicate data without benefit claims and are governed by a different review standard. Both categories go through MLR, but a promotional Visual Aid requires a full fair-balance analysis and an FDA Form 2253 filing at first use, while an MSL scientific deck is reviewed purely for accuracy and label alignment without the fair-balance requirement.</p>

  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.2rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Visual Aid (VA) &#8212; CLM Presentation</div>
      <div class="crm-obj-api">Promotional &#183; Digital HTML5 or Print &#183; Primary rep detail vehicle</div>
      <div class="crm-obj-desc">The slide deck a rep presents on their iPad during an HCP call. In digital CLM form, each slide interaction &#8212; time on page, swipe direction, slides skipped &#8212; is captured as engagement data in the CRM Call Report. Reps cannot reorder or edit slides; navigation is locked to the approved structure. Each VA maps to a specific product indication and is linked to the Key Messages reps are authorised to discuss. The approved VA becomes the CLM content package pushed to iRep on approval.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Approved Email (AE) Template</div>
      <div class="crm-obj-api">Promotional &#183; Digital &#183; Rep-sent branded HCP emails via CRM</div>
      <div class="crm-obj-desc">Pre-written, MLR-approved email templates reps can personalise only in designated fields (salutation, signature). Body copy, images, safety information, and all claims are locked. Sending is gated by the HCP&#x27;s Multichannel Consent record in CRM; per-HCP cadence limits are enforced at send time. Open rate, click rate, and link engagement are tracked and fed back to brand marketing dashboards. The template lives in PromoMats; the sending module lives in CRM &#8212; the integration keeps them in sync.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Leave Behind (LBH) / Patient Brochure</div>
      <div class="crm-obj-api">Promotional &#183; Print or Digital PDF &#183; Left with HCP or patient post-call</div>
      <div class="crm-obj-desc">Printed or PDF materials left with an HCP or patient after a call. Leave Behinds summarise key efficacy and safety data discussed during the detail. Patient Brochures use plain language to help patients understand their diagnosis and treatment. Both must carry the approved indication, risk information, and prescribing information reference. Each distributed piece is logged in the CRM Call Report as a linked Approved Document, creating a complete audit trail of what was distributed to which HCP and when.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Reprint &#38; Cover Sheet</div>
      <div class="crm-obj-api">Promotional &#183; Published journal article with MLR-approved cover</div>
      <div class="crm-obj-desc">A peer-reviewed journal article distributed by a rep as supportive evidence. Reps cannot distribute reprints without an approved PromoMats cover sheet carrying required fair-balance language &#8212; the cover sheet itself goes through a full MLR cycle. Reprint distribution is logged per call; reps are prohibited from distributing reprints for off-label uses. Article selection bias and misleading cover framing are among the most common FDA enforcement areas for reprints.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4080C0;">
      <div class="crm-obj-name" style="color:#60A0E0;">Speaker Slide Deck</div>
      <div class="crm-obj-api">Promotional &#183; HCP speaker presents to peer audience at company-sponsored programs</div>
      <div class="crm-obj-desc">Slide decks used by HCP speakers at company-sponsored programs. Content is entirely MLR-approved &#8212; speakers sign agreements prohibiting modification. Programs run through Veeva Events Management; every honorarium, travel reimbursement, and meal is logged for Sunshine Act reporting. Post-program survey results and attendance records link back to Events Management in CRM. Speaker training attestations and program execution form a multi-step compliance chain that PromoMats anchors at the content level.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4080C0;">
      <div class="crm-obj-name" style="color:#60A0E0;">Journal Advertisement</div>
      <div class="crm-obj-api">Promotional &#183; Print or Digital &#183; FDA-regulated under 21 CFR Part 202</div>
      <div class="crm-obj-desc">Print or digital advertisements placed in medical journals. Subject to the FDA&#x27;s strictest promotional standards: every efficacy claim must be supported by substantial evidence (typically two or more adequate and well-controlled studies); risk information must appear with equal prominence; a brief summary of the full prescribing information is required. Journal ads are submitted to the FDA under Form 2253 at first use &#8212; tracked as a workflow step inside PromoMats with the submission date recorded in document metadata.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40B070;">Standard Response Letter (SRL)</div>
      <div class="crm-obj-api">Non-Promotional &#183; Vault Medical &#183; Medical Information use only</div>
      <div class="crm-obj-desc">Pre-written, MLR-reviewed answers to frequently asked medical questions. Unlike promotional materials, SRLs are non-promotional scientific documents used exclusively by Medical Information specialists in response to HCP inquiries (MIRF). SRLs are versioned &#8212; when clinical evidence or the label changes, a new version is created and the old one is superseded. Off-label SRLs exist but can only be sent in documented response to a genuinely unsolicited inquiry and are never proactively distributed.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40B070;">MSL Scientific Deck / IIS Presentation</div>
      <div class="crm-obj-api">Non-Promotional &#183; Vault Medical &#183; MSL peer-to-peer scientific exchange</div>
      <div class="crm-obj-desc">Scientific decks MSLs present during KOL meetings, containing clinical trial data, mechanism of action, pipeline updates, and unmet medical need context. Not subject to 21 CFR Part 202 promotional rules but reviewed by MLR for data accuracy and label alignment. Stored in Vault Medical; MSLs pull them onto MSL iRep tablets and engagement is logged in CRM Call Reports. Scientific exchange quality and HCP insight capture drive the MSL performance framework.</div>
    </div>

  </div>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="promomats-workflow">MLR Review Workflow &#38; Document Lifecycle</h3>

  <p>When a content owner submits a document, the workflow engine creates a <strong>Workflow Task</strong> for each assigned reviewer simultaneously. Assignment logic is product- and document-type-specific: an Oncology Visual Aid routes to the Oncology Medical Reviewer, not the Primary Care reviewer. Each reviewer annotates directly on the document &#8212; drawing boxes, highlighting text, boxing problematic claims, placing sticky notes. Annotations are attributed and timestamped. The content owner sees all annotations on receiving revisions. Resolved annotations are permanently retained so a compliance auditor can reconstruct exactly what each reviewer objected to and how it was resolved.</p>

  <p>On unanimous approval, the workflow stamps the document with the approval date, sets an expiration date (typically 24 months for promotional content, 12 months for digital assets), captures 21 CFR Part 11 e-signatures of all reviewers, and transitions the document to <em>Approved</em> status, firing the CRM integration webhook. When a new version is later created &#8212; triggered by a label change, reference update, or creative refresh &#8212; it must complete its own full MLR cycle. The old version remains active in the field until the new version achieves approval, preventing a gap in the rep&#x27;s content library during the revision cycle.</p>

  <!-- SVG: Vault PromoMats Document Lifecycle -->
  <figure class="vis-embed" aria-label="Vault PromoMats Document Lifecycle">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Vault PromoMats &#8212; Document Lifecycle &amp; MLR States</div>
    <svg viewBox="0 0 960 355" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:960px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="pmlA" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#6B7280"/></marker>
        <marker id="pmlR" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#C05030"/></marker>
        <marker id="pmlG" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#208050"/></marker>
      </defs>
      <rect width="960" height="355" rx="12" fill="#0D1117"/>
      <text x="480" y="28" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">Vault PromoMats &#8212; Document Lifecycle States</text>

      <!-- STATE 1: DRAFT -->
      <rect x="18" y="55" width="110" height="58" rx="8" fill="#1A1F2A" stroke="#4B5563" stroke-width="1.5"/>
      <text x="73" y="78" text-anchor="middle" fill="#9CA3AF" font-size="11" font-weight="700">DRAFT</text>
      <text x="73" y="93" text-anchor="middle" fill="#6B7280" font-size="8.5">Author creates /</text>
      <text x="73" y="105" text-anchor="middle" fill="#6B7280" font-size="8.5">edits content</text>
      <line x1="128" y1="84" x2="156" y2="84" stroke="#4B5563" stroke-width="1.5" marker-end="url(#pmlA)"/>

      <!-- STATE 2: SUBMITTED -->
      <rect x="158" y="55" width="120" height="58" rx="8" fill="#0F1E35" stroke="#3070B0" stroke-width="1.5"/>
      <text x="218" y="76" text-anchor="middle" fill="#60A0D8" font-size="10.5" font-weight="700">SUBMITTED</text>
      <text x="218" y="91" text-anchor="middle" fill="#9CA3AF" font-size="8.5">Locked for review</text>
      <text x="218" y="104" text-anchor="middle" fill="#6B7280" font-size="8">Reviewer tasks created</text>
      <line x1="278" y1="84" x2="308" y2="84" stroke="#4B5563" stroke-width="1.5" marker-end="url(#pmlA)"/>

      <!-- STATE 3: IN MLR REVIEW -->
      <rect x="310" y="42" width="162" height="84" rx="8" fill="#221608" stroke="#C08020" stroke-width="2"/>
      <text x="391" y="64" text-anchor="middle" fill="#E09030" font-size="11" font-weight="700">IN MLR REVIEW</text>
      <text x="391" y="80" text-anchor="middle" fill="#A07020" font-size="8.5">Medical &#8226; Legal &#8226; Regulatory</text>
      <text x="391" y="94" text-anchor="middle" fill="#6B7280" font-size="8">Simultaneous task routing</text>
      <text x="391" y="107" text-anchor="middle" fill="#6B7280" font-size="8">Annotations &#8226; Votes &#8226; Comments</text>
      <line x1="472" y1="84" x2="500" y2="84" stroke="#4B5563" stroke-width="1.5" marker-end="url(#pmlA)"/>
      <text x="486" y="76" text-anchor="middle" fill="#40A060" font-size="7.5">All approve</text>

      <!-- STATE 4: APPROVED -->
      <rect x="502" y="55" width="120" height="58" rx="8" fill="#092014" stroke="#208050" stroke-width="2"/>
      <text x="562" y="76" text-anchor="middle" fill="#40C070" font-size="11" font-weight="700">APPROVED</text>
      <text x="562" y="91" text-anchor="middle" fill="#9CA3AF" font-size="8.5">e-Sig stamped</text>
      <text x="562" y="104" text-anchor="middle" fill="#6B7280" font-size="8">Expiry date assigned</text>
      <line x1="622" y1="84" x2="652" y2="84" stroke="#4B5563" stroke-width="1.5" marker-end="url(#pmlA)"/>
      <text x="637" y="76" text-anchor="middle" fill="#2A90B0" font-size="7.5">Auto-push</text>

      <!-- STATE 5: ACTIVE IN CRM -->
      <rect x="654" y="55" width="148" height="58" rx="8" fill="#081828" stroke="#2070A0" stroke-width="2"/>
      <text x="728" y="74" text-anchor="middle" fill="#50A8D8" font-size="10.5" font-weight="700">ACTIVE IN CRM</text>
      <text x="728" y="88" text-anchor="middle" fill="#9CA3AF" font-size="8">Approved_Document_vod__c</text>
      <text x="728" y="100" text-anchor="middle" fill="#9CA3AF" font-size="8">CLM iRep &#8226; Approved Email</text>
      <text x="728" y="112" text-anchor="middle" fill="#6B7280" font-size="7.5">Field force can access</text>
      <line x1="728" y1="128" x2="728" y2="162" stroke="#904040" stroke-width="1.5" marker-end="url(#pmlR)"/>
      <text x="744" y="150" text-anchor="start" fill="#9CA3AF" font-size="7.5">Expiry date reached</text>

      <!-- STATE 6: EXPIRED -->
      <rect x="654" y="164" width="148" height="55" rx="8" fill="#220808" stroke="#804040" stroke-width="1.5"/>
      <text x="728" y="185" text-anchor="middle" fill="#C06060" font-size="11" font-weight="700">EXPIRED</text>
      <text x="728" y="199" text-anchor="middle" fill="#9CA3AF" font-size="8">Auto-withdrawn from CRM</text>
      <text x="728" y="211" text-anchor="middle" fill="#6B7280" font-size="7.5">Archived in Vault</text>

      <!-- REVISIONS REQUIRED arc -->
      <path d="M391,126 L391,180 L218,180 L218,128" fill="none" stroke="#C05030" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#pmlR)"/>
      <rect x="272" y="183" width="144" height="36" rx="6" fill="#200C08" stroke="#B04020" stroke-width="1.5"/>
      <text x="344" y="202" text-anchor="middle" fill="#D06040" font-size="9.5" font-weight="700">REVISIONS REQUIRED</text>
      <text x="344" y="214" text-anchor="middle" fill="#6B7280" font-size="7.5">Returned with annotations intact</text>

      <!-- NEW VERSION arc -->
      <path d="M562,55 Q562,16 391,16 Q220,16 218,55" fill="none" stroke="#208050" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#pmlG)"/>
      <text x="391" y="11" text-anchor="middle" fill="#40A060" font-size="7.5">New version &#8212; full MLR re-review; prior stays active until new version approved</text>

      <!-- REVIEWER BREAKDOWN -->
      <text x="391" y="256" text-anchor="middle" fill="#9CA3AF" font-size="9.5" font-weight="600">MLR Reviewer Responsibilities</text>

      <rect x="218" y="264" width="126" height="72" rx="6" fill="#082020" stroke="#206060" stroke-width="1.5"/>
      <text x="281" y="283" text-anchor="middle" fill="#30A090" font-size="10" font-weight="700">Medical</text>
      <text x="281" y="298" text-anchor="middle" fill="#6B7280" font-size="8">Scientific accuracy</text>
      <text x="281" y="311" text-anchor="middle" fill="#6B7280" font-size="8">Fair balance &#8212; benefits</text>
      <text x="281" y="324" text-anchor="middle" fill="#6B7280" font-size="8">vs. risks &#8226; Label alignment</text>

      <rect x="354" y="264" width="126" height="72" rx="6" fill="#140820" stroke="#504080" stroke-width="1.5"/>
      <text x="417" y="283" text-anchor="middle" fill="#8060B0" font-size="10" font-weight="700">Legal</text>
      <text x="417" y="298" text-anchor="middle" fill="#6B7280" font-size="8">IP &#8226; Litigation risk</text>
      <text x="417" y="311" text-anchor="middle" fill="#6B7280" font-size="8">AKS / FCPA compliance</text>
      <text x="417" y="324" text-anchor="middle" fill="#6B7280" font-size="8">Off-label risk assessment</text>

      <rect x="490" y="264" width="126" height="72" rx="6" fill="#1A1A04" stroke="#606010" stroke-width="1.5"/>
      <text x="553" y="283" text-anchor="middle" fill="#A0A020" font-size="10" font-weight="700">Regulatory</text>
      <text x="553" y="298" text-anchor="middle" fill="#6B7280" font-size="8">21 CFR Part 202/203</text>
      <text x="553" y="311" text-anchor="middle" fill="#6B7280" font-size="8">FDA Form 2253 submission</text>
      <text x="553" y="324" text-anchor="middle" fill="#6B7280" font-size="8">Claims-to-reference check</text>
    </svg>
    <figcaption class="vis-cap">Vault PromoMats document lifecycle &#8212; from draft through MLR review, approval, CRM activation, and expiration or supersession</figcaption>
  </figure>

  <!-- Vault Object Reference Cards -->
  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.4rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Document</div>
      <div class="crm-obj-api">Core Vault record &#8212; every uploaded file is a Document with versioned lifecycle</div>
      <div class="crm-obj-desc">The fundamental unit in Vault PromoMats. Each Document record holds the file (PDF, PPTX, HTML5 CLM package, MP4), its metadata, and full version history. Every save creates a Minor Version; every MLR submission creates a Major Version. The lifecycle state machine controls promotion from Draft through Approved to Expired. Key fields: <span class="crm-field-pill">status__v</span> <span class="crm-field-pill">expiration_date__v</span> <span class="crm-field-pill">product__v</span> <span class="crm-field-pill">document_number__v</span> <span class="crm-field-pill">document_type__v</span> <span class="crm-field-pill">indication__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #7040C0;">
      <div class="crm-obj-name" style="color:#A070E0;">Binder</div>
      <div class="crm-obj-api">Container grouping related documents into a campaign or launch package</div>
      <div class="crm-obj-desc">Binders group related documents &#8212; a &#x22;Q4 Launch Package&#x22; Binder might contain the Visual Aid, Leave Behind, Patient Brochure, and Approved Email template for one indication. Binders can have their own review workflow: approving a Binder simultaneously approves all contained documents in a single MLR cycle, a significant efficiency gain for large launches. Also used for regulatory submission packages and for grouping IND/NDA supporting documentation.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4080C0;">
      <div class="crm-obj-name" style="color:#60A0E0;">Annotation</div>
      <div class="crm-obj-api">Reviewer markup &#8212; comments and drawings placed directly on document pages</div>
      <div class="crm-obj-desc">Reviewers draw directly on any page &#8212; highlighting text, boxing problematic claims, striking through copy that must be removed, placing sticky notes. Annotations are attributed to the reviewer and timestamped. The content owner sees all annotations upon receiving revisions. Resolved annotations are permanently retained so a compliance auditor can reconstruct exactly what each reviewer objected to, how it was resolved, and who signed off on the resolution.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4080C0;">
      <div class="crm-obj-name" style="color:#60A0E0;">Claims &#38; References</div>
      <div class="crm-obj-api">Granular tracking of every promotional claim and its supporting published evidence</div>
      <div class="crm-obj-desc">Every factual claim &#8212; &#x22;Reduces HbA1c by X%&#x22;, &#x22;Superior to comparator in STUDY-001&#x22; &#8212; is a Claim record linked to one or more Reference records (published studies). Regulatory reviewers verify every claim has adequate references before approving. If a reference is later retracted, every document with claims linked to it is automatically flagged for re-review. The claims library also syncs to <strong>Key_Message_vod__c</strong> in CRM, ensuring reps can only communicate claims with active reference support.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40B070;">Workflow Task</div>
      <div class="crm-obj-api">The atomic unit of the MLR process &#8212; one task per reviewer per review cycle</div>
      <div class="crm-obj-desc">When a document enters review, the workflow engine creates one Task per reviewer. The record tracks: assigned reviewer, due date, SLA countdown, vote cast, date voted, delegation history. Escalation rules fire when SLAs are breached. The complete task history is the legal record demonstrating MLR due diligence. Fields: <span class="crm-field-pill">assignee__v</span> <span class="crm-field-pill">due_date__v</span> <span class="crm-field-pill">verdict__v</span> <span class="crm-field-pill">completed_date__v</span> <span class="crm-field-pill">instructions__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40B070;">Document Token (Matched Sample)</div>
      <div class="crm-obj-api">Per-page compliance ID on every approved promotional piece</div>
      <div class="crm-obj-desc">Every page of an approved promotional document carries a unique alphanumeric token encoding the document number, version, and approval date. This allows FDA inspectors to instantly verify that a physical or digital piece in the field corresponds to an active, approved Vault document. Token mismatches &#8212; a rep using material whose token no longer matches an active Vault approval &#8212; are a major audit red flag and can trigger Warning Letters. Tokens are the physical proof that field content and Vault approvals are synchronised.</div>
    </div>

  </div>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="promomats-crm-integration">PromoMats &#8596; Veeva CRM &#8212; Integration &#38; Data Transfer</h3>

  <p>The PromoMats-CRM integration is an event-driven, bi-directional synchronisation managed by Veeva&#x27;s middleware layer. The primary flow runs from Vault outward: a document approval in PromoMats fires a webhook that creates or updates the corresponding <strong>Approved_Document_vod__c</strong> record in CRM, pushes CLM deck packages to iRep, publishes Approved Email templates, and activates Key Message records. The secondary flow runs inward: CLM engagement data captured in CRM &#8212; which slides were viewed, for how long, which key messages got positive HCP reactions &#8212; feeds back into PromoMats brand analytics dashboards, informing decisions about whether to initiate a content revision cycle. This closed loop transforms content management from a compliance function into a strategic brand optimisation engine.</p>

  <p>The integration also enforces content governance in the field automatically. When a document&#x27;s <span class="crm-field-pill">expiration_date__v</span> is reached in Vault, a nightly batch job deactivates the Approved_Document_vod__c record, removes the CLM deck from iRep on the next sync, and withdraws the Approved Email template. Field force managers receive automated notifications 30 days before expiration. No manual recall, no version confusion, no risk of reps using outdated materials after a label change &#8212; the system enforces the control automatically at scale across hundreds of reps and dozens of documents simultaneously.</p>

  <!-- SVG: PromoMats -> CRM Integration Data Transfer -->
  <figure class="vis-embed" aria-label="PromoMats CRM Integration Architecture">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Vault PromoMats &#8596; Veeva CRM &#8212; Data Transfer Architecture</div>
    <svg viewBox="0 0 940 420" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:940px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="pmiA"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#3070C0"/></marker>
        <marker id="pmiT"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#208060"/></marker>
        <marker id="pmiO"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#B07010"/></marker>
        <marker id="pmiAL" markerWidth="8" markerHeight="6" refX="0" refY="3" orient="auto"><polygon points="8 0,0 3,8 6" fill="#20A060"/></marker>
      </defs>
      <rect width="940" height="420" rx="12" fill="#0D1117"/>
      <text x="470" y="28" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">PromoMats &#8596; Veeva CRM &#8212; Data Transfer Architecture</text>

      <!-- LEFT PANEL: VAULT PROMOMATS -->
      <rect x="16" y="44" width="248" height="328" rx="10" fill="#120818" stroke="#7040C0" stroke-width="1.5"/>
      <text x="140" y="66" text-anchor="middle" fill="#A070E0" font-size="12" font-weight="700">Vault PromoMats</text>
      <text x="140" y="82" text-anchor="middle" fill="#6B7280" font-size="8.5">Content Mgmt &#38; MLR Workflow</text>
      <line x1="28" y1="90" x2="252" y2="90" stroke="#4B2080" stroke-width="1"/>

      <rect x="28" y="98"  width="224" height="38" rx="5" fill="#1C0D2A" stroke="#5030A0" stroke-width="1"/>
      <text x="140" y="115" text-anchor="middle" fill="#C0A0E8" font-size="9.5" font-weight="600">Visual Aid / CLM Deck</text>
      <text x="140" y="128" text-anchor="middle" fill="#6B7280" font-size="8">HTML5 package &#8226; slide-level metadata</text>

      <rect x="28" y="144" width="224" height="38" rx="5" fill="#1C0D2A" stroke="#5030A0" stroke-width="1"/>
      <text x="140" y="161" text-anchor="middle" fill="#C0A0E8" font-size="9.5" font-weight="600">Approved Email Template</text>
      <text x="140" y="174" text-anchor="middle" fill="#6B7280" font-size="8">Locked body &#8226; consent-gated send rules</text>

      <rect x="28" y="190" width="224" height="38" rx="5" fill="#1C0D2A" stroke="#5030A0" stroke-width="1"/>
      <text x="140" y="207" text-anchor="middle" fill="#C0A0E8" font-size="9.5" font-weight="600">Claims &#38; Key Messages</text>
      <text x="140" y="220" text-anchor="middle" fill="#6B7280" font-size="8">MLR-approved talking points per indication</text>

      <rect x="28" y="236" width="224" height="38" rx="5" fill="#1C0D2A" stroke="#5030A0" stroke-width="1"/>
      <text x="140" y="253" text-anchor="middle" fill="#C0A0E8" font-size="9.5" font-weight="600">Leave Behind / Reprint Cover</text>
      <text x="140" y="266" text-anchor="middle" fill="#6B7280" font-size="8">PDF &#8226; distributed doc record per call</text>

      <rect x="28" y="282" width="224" height="38" rx="5" fill="#1C0D2A" stroke="#5030A0" stroke-width="1"/>
      <text x="140" y="299" text-anchor="middle" fill="#C0A0E8" font-size="9.5" font-weight="600">SRL / MSL Scientific Deck</text>
      <text x="140" y="312" text-anchor="middle" fill="#6B7280" font-size="8">Vault Medical &#8226; MIRF response content</text>

      <rect x="28" y="328" width="224" height="38" rx="5" fill="#1C0D2A" stroke="#804040" stroke-width="1"/>
      <text x="140" y="345" text-anchor="middle" fill="#D08080" font-size="9.5" font-weight="600">Expiry / Superseded Signal</text>
      <text x="140" y="358" text-anchor="middle" fill="#6B7280" font-size="8">Triggers CRM auto-withdrawal</text>

      <!-- CENTRE LABELS -->
      <text x="470" y="124" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; CLM Deck Push to iRep</text>
      <text x="470" y="170" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; Email Template Publish</text>
      <text x="470" y="216" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; Key_Message_vod__c Sync</text>
      <text x="470" y="262" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; Approved_Document_vod__c Created</text>
      <text x="470" y="308" text-anchor="middle" fill="#208060" font-size="8" font-weight="600">&#8594; SRL linked to Medical_Inquiry_vod__c</text>
      <text x="470" y="354" text-anchor="middle" fill="#B07010" font-size="8" font-weight="600">&#8594; CRM Content Deactivated</text>
      <text x="470" y="395" text-anchor="middle" fill="#20A060" font-size="8.5" font-weight="600">&#8592; CLM engagement &#8226; Key Message reactions &#8226; AE analytics &#8212; PromoMats brand dashboard</text>

      <!-- ARROWS: left to right -->
      <line x1="252" y1="117" x2="676" y2="117" stroke="#3070C0" stroke-width="1.2" marker-end="url(#pmiA)"/>
      <line x1="252" y1="163" x2="676" y2="163" stroke="#3070C0" stroke-width="1.2" marker-end="url(#pmiA)"/>
      <line x1="252" y1="209" x2="676" y2="209" stroke="#3070C0" stroke-width="1.2" marker-end="url(#pmiA)"/>
      <line x1="252" y1="255" x2="676" y2="255" stroke="#3070C0" stroke-width="1.2" marker-end="url(#pmiA)"/>
      <line x1="252" y1="301" x2="676" y2="301" stroke="#208060" stroke-width="1.2" marker-end="url(#pmiT)"/>
      <line x1="252" y1="347" x2="676" y2="347" stroke="#B07010" stroke-width="1.2" marker-end="url(#pmiO)"/>
      <!-- Feedback arc -->
      <path d="M676,382 Q470,408 252,382" fill="none" stroke="#20A060" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#pmiAL)"/>

      <!-- RIGHT PANEL: VEEVA CRM -->
      <rect x="678" y="44" width="248" height="328" rx="10" fill="#080E1A" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="802" y="66" text-anchor="middle" fill="#6090D8" font-size="12" font-weight="700">Veeva CRM</text>
      <text x="802" y="82" text-anchor="middle" fill="#6B7280" font-size="8.5">iRep &#8226; Call Reports &#8226; Field Execution</text>
      <line x1="690" y1="90" x2="914" y2="90" stroke="#1B3A6B" stroke-width="1"/>

      <rect x="690" y="98"  width="224" height="38" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="802" y="115" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">CLM Content Library (iRep)</text>
      <text x="802" y="128" text-anchor="middle" fill="#6B7280" font-size="8">Slide view &#8226; dwell time &#8226; sequence logged</text>

      <rect x="690" y="144" width="224" height="38" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="802" y="161" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">Approved Email Module</text>
      <text x="802" y="174" text-anchor="middle" fill="#6B7280" font-size="8">Consent-gated &#8226; open / click analytics</text>

      <rect x="690" y="190" width="224" height="38" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="802" y="207" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">Key_Message_vod__c</text>
      <text x="802" y="220" text-anchor="middle" fill="#6B7280" font-size="8">HCP reaction (Agree &#8594; Disagree) captured</text>

      <rect x="690" y="236" width="224" height="38" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="802" y="253" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">Approved_Document_vod__c</text>
      <text x="802" y="266" text-anchor="middle" fill="#6B7280" font-size="8">Linked to Call Reports &#8226; status &#8226; expiry</text>

      <rect x="690" y="282" width="224" height="38" rx="5" fill="#081818" stroke="#208060" stroke-width="1"/>
      <text x="802" y="299" text-anchor="middle" fill="#40B090" font-size="9.5" font-weight="600">Medical_Inquiry_vod__c &#38; MSL iRep</text>
      <text x="802" y="312" text-anchor="middle" fill="#6B7280" font-size="8">SRL retrieved &#8226; MIRF response logged</text>

      <rect x="690" y="328" width="224" height="38" rx="5" fill="#180808" stroke="#804040" stroke-width="1"/>
      <text x="802" y="345" text-anchor="middle" fill="#D08080" font-size="9.5" font-weight="600">Content Deactivated / Removed</text>
      <text x="802" y="358" text-anchor="middle" fill="#6B7280" font-size="8">Rep library updated &#8226; 30-day advance warning</text>
    </svg>
    <figcaption class="vis-cap">PromoMats to CRM integration &#8212; six data transfer channels plus CLM engagement feedback loop</figcaption>
  </figure>

  <!-- Integration Object Cards -->
  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.4rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #3070C0;">
      <div class="crm-obj-name" style="color:#60A0D8;">Approved_Document_vod__c &#8212; CRM Content Record</div>
      <div class="crm-obj-api">Auto-created on PromoMats approval; auto-deactivated on expiry</div>
      <div class="crm-obj-desc">The CRM representation of every approved promotional piece. Reps see these in their content library and link them to Call Reports as distributed materials. The record carries document name, type, product indication, approval date, expiration date, and a deep link back to the Vault document. On expiration, the integration sets <span class="crm-field-pill">Status_vod__c</span> to Inactive and the record disappears from the rep&#x27;s library automatically. Key fields: <span class="crm-field-pill">Expiration_Date_vod__c</span> <span class="crm-field-pill">Document_Number_vod__c</span> <span class="crm-field-pill">Product_vod__c</span> <span class="crm-field-pill">Approved_Document_Type_vod__c</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #3070C0;">
      <div class="crm-obj-name" style="color:#60A0D8;">CLM Deck Push to iRep</div>
      <div class="crm-obj-api">Approved VA HTML5 packages pushed directly to rep iPad CLM library</div>
      <div class="crm-obj-desc">When a digital Visual Aid is approved in PromoMats, the integration packages it and queues it for rep iPads. After overnight sync, the deck appears in the CLM library. Navigation structure, mandatory views, and slide order are locked to the approved package. Every interaction is logged: <span class="crm-field-pill">CLM_Presentation_vod__c</span> captures slide ID, time on slide, reaction, and whether the slide was presented or skipped. This raw engagement data feeds PromoMats analytics within 48 hours, closing the brand feedback loop.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #3070C0;">
      <div class="crm-obj-name" style="color:#60A0D8;">Key_Message_vod__c Sync &#38; Reaction Feedback</div>
      <div class="crm-obj-api">Approved claims synced as Key Messages; HCP reactions flow back to PromoMats analytics</div>
      <div class="crm-obj-desc">Individual approved claims from the Visual Aid are synchronised as <strong>Key_Message_vod__c</strong> records. Reps select discussed messages during a call and capture HCP reactions on a 5-point Likert scale. Reaction data aggregates into brand-level analytics in PromoMats dashboards &#8212; which messages resonate with which HCP segment, which generate pushback, which are consistently skipped. Declining engagement on specific messages is the primary trigger for a PromoMats content revision cycle back through MLR.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #3070C0;">
      <div class="crm-obj-name" style="color:#60A0D8;">Approved Email &#8212; End-to-End Flow</div>
      <div class="crm-obj-api">Template in PromoMats; sending governed by CRM consent and cadence rules</div>
      <div class="crm-obj-desc">An Approved Email template approved in PromoMats is pushed to the CRM Approved Email module. CRM gates sending against the HCP&#x27;s <strong>Multichannel_Consent_Line_vod__c</strong> (must be opted in) and enforces per-HCP cadence limits. Open events, click events, and link-level engagement are captured and written back to CRM. PromoMats analytics surfaces aggregate performance: open rate by HCP segment, click-through rate by CTA, and comparison across template versions to guide the next content refresh.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208060;">
      <div class="crm-obj-name" style="color:#40B090;">Vault Medical &#8596; MSL iRep &#38; MIRF</div>
      <div class="crm-obj-api">Non-promotional scientific content in Vault Medical accessed via MSL iRep</div>
      <div class="crm-obj-desc">Vault Medical (same platform as PromoMats, separate instance) manages SRLs, MSL scientific decks, congress presentations, and IIS-related documents. MSL iRep in CRM connects to Vault Medical: MSLs see their approved scientific content library and log usage in Call Reports. When a Medical Information specialist responds to a MIRF, they retrieve the SRL from Vault Medical via a lookup on <strong>Medical_Inquiry_vod__c</strong> &#8212; the response and SRL version used are permanently logged for audit.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #B07010;">
      <div class="crm-obj-name" style="color:#D0A030;">Auto-Withdrawal &#38; Expiry Governance</div>
      <div class="crm-obj-api">Vault expiry dates drive automatic CRM withdrawal &#8212; no manual recall needed</div>
      <div class="crm-obj-desc">On expiration, a nightly batch: (1) sets Approved_Document_vod__c <span class="crm-field-pill">Status_vod__c</span> to Inactive; (2) removes CLM decks from iRep on next sync; (3) pulls the Approved Email template; (4) deactivates linked Key Messages. A 30-day advance notification goes to the district manager and brand team. This system-enforced withdrawal means a company can demonstrate to any FDA inspector that as of any given date, every rep had access only to current, approved promotional content &#8212; a compliance posture impossible to maintain manually at scale across hundreds of reps.</div>
    </div>

  </div>
"""

NETWORK_EXTRA = """
  <h2 id="veeva-network">Veeva Network &#8212; The Master Data Record</h2>

  <p>Veeva Network is the Master Data Management (MDM) platform that underpins the entire Veeva commercial and medical stack. It maintains a single, authoritative, validated record for every Healthcare Professional (HCP) and Healthcare Organization (HCO) a pharmaceutical company may ever interact with &#8212; not just those in the current target list, but every licensed prescriber, hospital, clinic, IDN, pharmacy, and payer organisation in the relevant geographies. Every CRM Account and Contact record is anchored to a Network master record via a <strong>Veeva ID (VID)</strong>, a globally unique identifier. When Network updates a master record &#8212; because a physician has moved practice, changed specialty, or been added to an OIG exclusion list &#8212; that correction propagates to CRM, Veeva Align, and every downstream analytics system automatically. There is no manual reconciliation.</p>

  <p>The platform ingests data from more than 30 external reference sources simultaneously and applies machine learning deduplication to reconcile them into clean, non-duplicate master records. The sources include the AMA Physician Masterfile (the most comprehensive physician database in the US), the CMS NPI Registry, DEA registrations for all Schedule II&#8211;V controlled substance authorisations, all 50 state medical board licensing databases, the OIG List of Excluded Individuals/Entities (LEIE), GSA System for Award Management (SAM) exclusions, IQVIA OneKey, Definitive Healthcare IDN data, and Veeva&#x27;s own <strong>OpenData</strong> &#8212; a curated, continuously updated global reference database of HCPs and HCOs that clients subscribe to as a managed data service. When sources conflict, Network&#x27;s stewardship rules determine which source wins for each field type &#8212; NPI from the federal registry takes precedence over an IMS record; specialty from the state board overrides a rep&#x27;s manual submission.</p>

  <p>For pharmaceutical companies, Veeva Network solves a problem that has historically consumed enormous operational resources: maintaining clean HCP/HCO master data across a field force that has hundreds of reps updating records, multiple data vendors with overlapping and conflicting information, regulatory databases that update on different cycles, and compliance requirements that demand validated credentials for every sample transaction and every transfer of value. Network centralises all of this into a single system with a governance framework &#8212; a data stewardship team that reviews Data Change Requests, resolves conflicts, and maintains data quality SLAs &#8212; so that the field force, the MLR team, the compliance team, and the analytics team are all working from the same validated master record at all times.</p>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="network-entities">Core Data Entities</h3>

  <p>Veeva Network organises its master data into five primary entity types. Each is managed independently with its own lifecycle, validation rules, and stewardship workflow, but they are tightly linked &#8212; an HCP&#x27;s professional identity is only complete when their License records are validated, their HCO affiliations are confirmed, and their OIG exclusion status is current. The commercial team sees a simplified view of this in CRM (Account and Contact), but the underlying Network data model is significantly richer.</p>

  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.2rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #1B3A6B;">
      <div class="crm-obj-name" style="color:#6090D8;">HCP (Healthcare Professional)</div>
      <div class="crm-obj-api">Individual licensed prescribers and recommenders &#8212; the primary target of commercial and medical engagement</div>
      <div class="crm-obj-desc">The HCP entity covers every physician (MD/DO), nurse practitioner (NP), physician assistant (PA), pharmacist (PharmD), registered nurse (RN), and any other licensed practitioner who prescribes, recommends, or influences the use of prescription drugs. The master HCP record holds: VID, NPI (National Provider Identifier), primary specialty and up to 3 sub-specialties, DEA registration number and schedule authorisations, primary and secondary practice addresses, OIG/GSA exclusion status, prescriber tier classification, and active/inactive/deceased status. Key fields: <span class="crm-field-pill">vid__v</span> <span class="crm-field-pill">npi__v</span> <span class="crm-field-pill">primary_specialty__v</span> <span class="crm-field-pill">dea_number__v</span> <span class="crm-field-pill">oig_exclusion_status__v</span> <span class="crm-field-pill">entity_status__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #1B3A6B;">
      <div class="crm-obj-name" style="color:#6090D8;">HCO (Healthcare Organisation)</div>
      <div class="crm-obj-api">Hospitals, clinics, IDNs, pharmacies, group practices &#8212; managed through Key Account Management</div>
      <div class="crm-obj-desc">HCO records cover every type of healthcare organisation: acute care hospitals, outpatient clinics, academic medical centres, IDNs (Integrated Delivery Networks), pharmacy chains, long-term care facilities, and payer organisations. The critical feature is the <strong>parent-child hierarchy</strong>: a large IDN like Kaiser Permanente or HCA Healthcare is the parent; individual hospitals are children; clinics and departments are grandchildren. This hierarchy is essential for Key Account Management (KAM) teams who negotiate at the IDN level and for formulary access work with P&#38;T committees. Fields: <span class="crm-field-pill">vid__v</span> <span class="crm-field-pill">hco_type__v</span> <span class="crm-field-pill">parent_hco__v</span> <span class="crm-field-pill">npi__v</span> <span class="crm-field-pill">hospital_beds__v</span> <span class="crm-field-pill">magnet_status__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4A2080;">
      <div class="crm-obj-name" style="color:#9060C0;">HCP&#8211;HCO Affiliation</div>
      <div class="crm-obj-api">Links HCPs to their practice locations &#8212; drives territory assignment, rep ownership, and call routing</div>
      <div class="crm-obj-desc">The Affiliation record is the relationship between an HCP and an HCO where they practise. An HCP can have multiple affiliations simultaneously &#8212; a cardiologist might be an attending at a teaching hospital, a partner at a private practice clinic, and a consulting physician at a cardiac rehabilitation centre. Each affiliation carries a <strong>primary flag</strong>: the primary affiliation determines which territory the HCP is assigned to and which rep owns the relationship. When an HCP moves their primary practice, the affiliation record is updated, and the territory alignment in Veeva Align re-assigns the HCP to the new territory&#x27;s rep automatically. Fields: <span class="crm-field-pill">hcp_vid__v</span> <span class="crm-field-pill">hco_vid__v</span> <span class="crm-field-pill">relationship_type__v</span> <span class="crm-field-pill">primary_flag__v</span> <span class="crm-field-pill">start_date__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4A2080;">
      <div class="crm-obj-name" style="color:#9060C0;">License &#38; Credential</div>
      <div class="crm-obj-api">State medical licenses, DEA registrations, board certifications &#8212; PDMA compliance anchors</div>
      <div class="crm-obj-desc">Each HCP&#x27;s professional credentials are stored as separate License records linked to the HCP master. This includes: state medical licence per state (an HCP licensed in multiple states has one record per state), DEA registration (with the specific controlled substance schedules authorised &#8212; Schedule II through V), and board certifications from specialty boards (ABIM, ABFM, ABS, etc.). License expiration dates are monitored &#8212; if a DEA registration lapses, the OIG exclusion flag triggers automatically and CRM blocks sample transactions to that HCP. The DEA number and schedule authorisation is the legal gate for PDMA-compliant sample distribution under 21 CFR Part 203. Fields: <span class="crm-field-pill">license_number__v</span> <span class="crm-field-pill">license_type__v</span> <span class="crm-field-pill">issuing_state__v</span> <span class="crm-field-pill">expiration_date__v</span> <span class="crm-field-pill">dea_schedule__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">Data Change Request (DCR)</div>
      <div class="crm-obj-api">Stewardship workflow &#8212; how reps and MSLs correct Network master data from the field</div>
      <div class="crm-obj-desc">When a rep or MSL discovers that data in CRM is wrong &#8212; an HCP has moved to a new practice, retired, changed specialty, or been miscategorised &#8212; they submit a Data Change Request through CRM. The DCR enters a stewardship queue in Network. Stewards &#8212; data management professionals employed by or contracted to the pharma company &#8212; validate the change against reference sources and either approve or reject it. Approved changes update the master record and propagate to CRM automatically. DCRs carry a full audit trail: who submitted, what change was requested, which reference source validated it, who approved it, and when it was applied. DCR types: Add HCP/HCO, Edit Address, Edit Specialty, Merge Duplicates, Inactivate Record. Fields: <span class="crm-field-pill">request_type__v</span> <span class="crm-field-pill">entity_vid__v</span> <span class="crm-field-pill">new_value__v</span> <span class="crm-field-pill">submitted_by__v</span> <span class="crm-field-pill">status__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">Subscription &#38; OpenData</div>
      <div class="crm-obj-api">What data the client receives &#8212; geography, specialty, entity type scope configured at the subscription level</div>
      <div class="crm-obj-desc"><strong>Veeva OpenData</strong> is Veeva&#x27;s managed reference database &#8212; a commercial data service where Veeva maintains the underlying HCP/HCO data and the client subscribes to receive it. A subscription defines the scope: which countries, which specialties, which entity types (HCP only, HCO only, or both), and which data fields are included. OpenData is continuously updated by Veeva&#x27;s own data operations team, so clients whose reps discover new HCPs can submit Add requests that Veeva validates and adds to the OpenData product, benefiting all subscribers. Clients can also supplement OpenData with their own <strong>Customer Managed</strong> data &#8212; proprietary intelligence such as call history, tiering, and targeting that is not shared with other subscribers.</div>
    </div>

  </div>

  <!-- SVG 1: Data Sources -> Network -> Master Records -->
  <figure class="vis-embed" aria-label="Veeva Network Data Sources and Master Record Model">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Veeva Network &#8212; Data Sources, Validation Engine &#38; Master Record Model</div>
    <svg viewBox="0 0 960 400" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:960px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="netA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#4B5563"/></marker>
        <marker id="netB" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#1B3A6B"/></marker>
        <marker id="netC" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#0B5E5E"/></marker>
      </defs>
      <rect width="960" height="400" rx="12" fill="#0D1117"/>
      <text x="480" y="26" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">Veeva Network &#8212; Data Sources &#8594; Validation &#8594; Master Records</text>

      <!-- ── LEFT: EXTERNAL SOURCES ── -->
      <text x="110" y="50" text-anchor="middle" fill="#9CA3AF" font-size="9.5" font-weight="600">External Reference Sources</text>

      <rect x="14"  y="58"  width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="75"  text-anchor="middle" fill="#A0A0C8" font-size="8.5">AMA Physician Masterfile</text>

      <rect x="14"  y="90"  width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="107" text-anchor="middle" fill="#A0A0C8" font-size="8.5">CMS NPI Registry</text>

      <rect x="14"  y="122" width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="139" text-anchor="middle" fill="#A0A0C8" font-size="8.5">DEA Registration Database</text>

      <rect x="14"  y="154" width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="171" text-anchor="middle" fill="#A0A0C8" font-size="8.5">State Medical Boards (50)</text>

      <rect x="14"  y="186" width="192" height="26" rx="5" fill="#1A222A" stroke="#204060" stroke-width="1"/>
      <text x="110" y="203" text-anchor="middle" fill="#80B0D0" font-size="8.5">OIG LEIE / GSA SAM Exclusions</text>

      <rect x="14"  y="218" width="192" height="26" rx="5" fill="#1A222A" stroke="#204060" stroke-width="1"/>
      <text x="110" y="235" text-anchor="middle" fill="#80B0D0" font-size="8.5">Veeva OpenData (managed)</text>

      <rect x="14"  y="250" width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="267" text-anchor="middle" fill="#A0A0C8" font-size="8.5">IQVIA OneKey / Definitive HC</text>

      <rect x="14"  y="282" width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="299" text-anchor="middle" fill="#A0A0C8" font-size="8.5">ABMS Board Certifications</text>

      <rect x="14"  y="314" width="192" height="26" rx="5" fill="#1A1A2A" stroke="#404060" stroke-width="1"/>
      <text x="110" y="331" text-anchor="middle" fill="#A0A0C8" font-size="8.5">CMS Open Payments</text>

      <rect x="14"  y="346" width="192" height="26" rx="5" fill="#141A14" stroke="#305030" stroke-width="1"/>
      <text x="110" y="363" text-anchor="middle" fill="#80C080" font-size="8.5">Field DCR submissions (CRM)</text>

      <!-- Arrows: sources -> network engine -->
      <line x1="206" y1="71"  x2="290" y2="140" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="103" x2="290" y2="155" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="135" x2="290" y2="170" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="167" x2="290" y2="185" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="199" x2="290" y2="200" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="231" x2="290" y2="215" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="263" x2="290" y2="230" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="295" x2="290" y2="245" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="327" x2="290" y2="255" stroke="#304050" stroke-width="1" marker-end="url(#netA)"/>
      <line x1="206" y1="359" x2="290" y2="265" stroke="#305030" stroke-width="1" marker-end="url(#netA)"/>

      <!-- ── CENTRE: NETWORK MDM ENGINE ── -->
      <rect x="292" y="110" width="200" height="180" rx="10" fill="#080E18" stroke="#1B3A6B" stroke-width="2"/>
      <text x="392" y="132" text-anchor="middle" fill="#6090D8" font-size="11" font-weight="700">Veeva Network MDM</text>
      <line x1="304" y1="140" x2="480" y2="140" stroke="#1B3A6B" stroke-width="1"/>

      <rect x="304" y="148" width="176" height="30" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="392" y="160" text-anchor="middle" fill="#60A0D8" font-size="8.5" font-weight="600">1. Ingest &#38; Parse</text>
      <text x="392" y="172" text-anchor="middle" fill="#6B7280" font-size="7.5">Normalise formats &#8226; dedup keys</text>

      <rect x="304" y="186" width="176" height="30" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="392" y="198" text-anchor="middle" fill="#60A0D8" font-size="8.5" font-weight="600">2. ML Deduplication</text>
      <text x="392" y="210" text-anchor="middle" fill="#6B7280" font-size="7.5">Match &#8226; merge &#8226; survivorship rules</text>

      <rect x="304" y="224" width="176" height="30" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="392" y="236" text-anchor="middle" fill="#60A0D8" font-size="8.5" font-weight="600">3. Credential Validation</text>
      <text x="392" y="248" text-anchor="middle" fill="#6B7280" font-size="7.5">NPI &#8226; DEA &#8226; Licence &#8226; OIG/GSA</text>

      <rect x="304" y="262" width="176" height="22" rx="5" fill="#0A2020" stroke="#208060" stroke-width="1.5"/>
      <text x="392" y="277" text-anchor="middle" fill="#40B080" font-size="8.5" font-weight="600">Master Record Created / Updated</text>

      <!-- Arrow: engine -> right panel -->
      <line x1="492" y1="200" x2="524" y2="200" stroke="#1B3A6B" stroke-width="2" marker-end="url(#netB)"/>

      <!-- ── RIGHT: MASTER RECORDS ── -->
      <!-- HCP Record -->
      <rect x="526" y="58" width="196" height="150" rx="8" fill="#081020" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="624" y="79" text-anchor="middle" fill="#6090D8" font-size="10.5" font-weight="700">HCP Master Record</text>
      <line x1="538" y1="86" x2="710" y2="86" stroke="#1B3A6B" stroke-width="1"/>
      <text x="538" y="101" fill="#9CA3AF" font-size="8">&#9656; VID (Veeva unique ID)</text>
      <text x="538" y="115" fill="#9CA3AF" font-size="8">&#9656; NPI &#8226; DEA &#38; schedule auth.</text>
      <text x="538" y="129" fill="#9CA3AF" font-size="8">&#9656; Primary specialty (+ sub-spec.)</text>
      <text x="538" y="143" fill="#9CA3AF" font-size="8">&#9656; Primary &#38; secondary address</text>
      <text x="538" y="157" fill="#9CA3AF" font-size="8">&#9656; OIG / GSA exclusion status</text>
      <text x="538" y="171" fill="#9CA3AF" font-size="8">&#9656; State licence(s) + expiry dates</text>
      <text x="538" y="185" fill="#9CA3AF" font-size="8">&#9656; Entity status (active / deceased)</text>
      <text x="538" y="199" fill="#6B7280" font-size="7.5" font-style="italic">Linked to CRM Contact via vid__v</text>

      <!-- Affiliation arrow -->
      <line x1="624" y1="208" x2="624" y2="230" stroke="#4A2080" stroke-width="1.5" stroke-dasharray="4,2" marker-end="url(#netA)"/>
      <text x="640" y="224" fill="#9060C0" font-size="7.5">affiliation</text>

      <!-- HCO Record -->
      <rect x="526" y="232" width="196" height="150" rx="8" fill="#0A1010" stroke="#0B5E5E" stroke-width="1.5"/>
      <text x="624" y="253" text-anchor="middle" fill="#2A9A9A" font-size="10.5" font-weight="700">HCO Master Record</text>
      <line x1="538" y1="260" x2="710" y2="260" stroke="#0B5E5E" stroke-width="1"/>
      <text x="538" y="275" fill="#9CA3AF" font-size="8">&#9656; VID &#8226; NPI &#8226; HCO type</text>
      <text x="538" y="289" fill="#9CA3AF" font-size="8">&#9656; Parent HCO (IDN hierarchy)</text>
      <text x="538" y="303" fill="#9CA3AF" font-size="8">&#9656; Address (validated USPS)</text>
      <text x="538" y="317" fill="#9CA3AF" font-size="8">&#9656; Hospital beds &#8226; Magnet status</text>
      <text x="538" y="331" fill="#9CA3AF" font-size="8">&#9656; P&#38;T committee access flag</text>
      <text x="538" y="345" fill="#9CA3AF" font-size="8">&#9656; Academic Medical Centre flag</text>
      <text x="538" y="365" fill="#6B7280" font-size="7.5" font-style="italic">Linked to CRM Account via vid__v</text>

      <!-- IDN Hierarchy label -->
      <rect x="732" y="58" width="216" height="110" rx="8" fill="#0A0A18" stroke="#304060" stroke-width="1.5"/>
      <text x="840" y="77" text-anchor="middle" fill="#8080B0" font-size="10" font-weight="700">IDN Hierarchy Example</text>
      <line x1="744" y1="84" x2="936" y2="84" stroke="#304060" stroke-width="1"/>
      <text x="756" y="100" fill="#6B7280" font-size="8">IDN (Kaiser Permanente)</text>
      <text x="772" y="115" fill="#6B7280" font-size="8">&#9500; Regional Hospital</text>
      <text x="788" y="130" fill="#6B7280" font-size="8">&#9500; Outpatient Clinic</text>
      <text x="804" y="145" fill="#6B7280" font-size="8">&#9492; Department (Cardiology)</text>
      <text x="840" y="162" text-anchor="middle" fill="#4B5563" font-size="7.5" font-style="italic">Each node = HCO record with parent_hco__v link</text>

      <!-- CRM sync indicator -->
      <rect x="732" y="185" width="216" height="60" rx="8" fill="#081020" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="840" y="205" text-anchor="middle" fill="#6090D8" font-size="9" font-weight="600">Veeva CRM Sync</text>
      <text x="840" y="221" text-anchor="middle" fill="#6B7280" font-size="8">Nightly: Account &#38; Contact updated</text>
      <text x="840" y="235" text-anchor="middle" fill="#6B7280" font-size="8">via VID linkage &#8226; OIG flag real-time</text>

      <!-- Arrow from master records to CRM sync box -->
      <line x1="722" y1="130" x2="732" y2="200" stroke="#1B3A6B" stroke-width="1" marker-end="url(#netB)"/>

      <!-- Veeva Align box -->
      <rect x="732" y="262" width="216" height="58" rx="8" fill="#0A1808" stroke="#305010" stroke-width="1.5"/>
      <text x="840" y="282" text-anchor="middle" fill="#70A030" font-size="9" font-weight="600">Veeva Align (Territory)</text>
      <text x="840" y="297" text-anchor="middle" fill="#6B7280" font-size="8">Primary affiliation &#8594; territory</text>
      <text x="840" y="311" text-anchor="middle" fill="#6B7280" font-size="8">alignment &#8594; rep ownership</text>

      <line x1="722" y1="310" x2="732" y2="295" stroke="#305010" stroke-width="1" marker-end="url(#netA)"/>
    </svg>
    <figcaption class="vis-cap">Veeva Network &#8212; 10+ external sources converge through ML deduplication and credential validation into clean HCP/HCO master records, linked to CRM via VID and to Veeva Align for territory management</figcaption>
  </figure>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="network-stewardship">Data Stewardship &#38; DCR Workflow</h3>

  <p>Data quality in a pharmaceutical master data system is not a one-time project; it is an ongoing operational discipline. Veeva Network implements <strong>data stewardship</strong> as a formal workflow &#8212; a team of data management professionals (typically 5&#8211;30 people depending on company size) who review incoming Data Change Requests, resolve conflicts between sources, and maintain data quality SLAs. When a rep in the field notices that an HCP has moved to a new clinic, they submit a DCR through CRM in under 60 seconds. That DCR enters the stewardship queue, the steward validates the new address against the relevant state medical board or practice website, approves the change, and the corrected address propagates to CRM within 24&#8211;48 hours. The rep sees the corrected record the next morning when their iPad syncs. No email thread, no spreadsheet ticket, no manual CRM update.</p>

  <p>Beyond field-submitted corrections, Network&#x27;s ingestion pipeline continuously detects data quality issues: a physician whose NPI was listed in multiple state board databases with two different first-name spellings; an HCP who appears in IQVIA under one NPI and in the AMA database under a different one; an HCO that appears as both &#x22;Mass General Hospital&#x22; and &#x22;Massachusetts General Hospital&#x22; in different source datasets. The ML deduplication engine flags these as potential duplicates and creates stewardship tasks. The steward investigates, confirms the match or mismatch, and either merges the records (creating one master with the surviving VID) or confirms they are distinct entities. Merges propagate to CRM: the losing VID is deactivated, all CRM records linked to it are re-linked to the surviving VID, and the merge history is permanently retained for audit.</p>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="network-crm-integration">Network &#8596; Veeva CRM &#38; Align &#8212; Integration &#38; Data Flow</h3>

  <p>The Network-CRM integration operates on two cadences: a <strong>nightly batch sync</strong> that updates all changed records overnight, and a <strong>real-time event stream</strong> for critical compliance changes. The nightly sync covers routine updates: specialty changes, address corrections, affiliation updates, and new HCPs added by the stewardship team. The real-time stream covers OIG/GSA exclusion changes &#8212; if an HCP is added to the federal exclusion list during the day, their CRM record is flagged within hours, not the next morning, because PDMA and Anti-Kickback compliance cannot wait for a nightly batch. A rep who tries to submit a sample request or expense reimbursement for an excluded HCP will receive an immediate block in CRM, with a compliance alert routed to their district manager.</p>

  <p><strong>Veeva Align</strong> sits between Network and CRM as the territory management layer. Align takes the HCP/HCO master records from Network (specifically the primary affiliation and primary address), overlays the company&#x27;s geographic territory boundaries, and produces the territory-to-HCP mapping that drives rep ownership in CRM. When a rep&#x27;s territory boundary changes (during a re-alignment), Align re-computes the assignments and pushes the updated ownership to CRM. When an HCP changes their primary affiliation (captured in Network via DCR), Align detects the address change, re-evaluates which territory the new address falls in, and may re-assign the HCP to a different rep&#x27;s territory &#8212; all automatically. The outgoing rep&#x27;s manager is notified; the incoming rep sees the new HCP in their CRM target list the next morning.</p>

  <!-- SVG 2: Network <-> CRM / Align Integration -->
  <figure class="vis-embed" aria-label="Network CRM Align Integration Flow">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Veeva Network &#8596; CRM &#38; Align &#8212; Integration &#38; Data Transfer</div>
    <svg viewBox="0 0 940 390" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:940px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="ncA"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#1B3A6B"/></marker>
        <marker id="ncAL" markerWidth="8" markerHeight="6" refX="0" refY="3" orient="auto"><polygon points="8 0,0 3,8 6" fill="#1B3A6B"/></marker>
        <marker id="ncG"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#305010"/></marker>
        <marker id="ncR"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#903030"/></marker>
        <marker id="ncO"  markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#206060"/></marker>
      </defs>
      <rect width="940" height="390" rx="12" fill="#0D1117"/>
      <text x="470" y="27" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">Veeva Network &#8596; CRM &#38; Align &#8212; Data Transfer</text>

      <!-- LEFT PANEL: NETWORK -->
      <rect x="15" y="42" width="256" height="312" rx="10" fill="#080E18" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="143" y="64" text-anchor="middle" fill="#6090D8" font-size="12" font-weight="700">Veeva Network</text>
      <text x="143" y="80" text-anchor="middle" fill="#6B7280" font-size="8.5">HCP / HCO Master Data (MDM)</text>
      <line x1="27" y1="88" x2="259" y2="88" stroke="#1B3A6B" stroke-width="1"/>

      <rect x="27" y="96"  width="232" height="36" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="143" y="112" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">HCP Master Record</text>
      <text x="143" y="124" text-anchor="middle" fill="#6B7280" font-size="8">VID &#8226; NPI &#8226; DEA &#8226; specialty &#8226; address</text>

      <rect x="27" y="140" width="232" height="36" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="143" y="156" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">HCO Master Record</text>
      <text x="143" y="168" text-anchor="middle" fill="#6B7280" font-size="8">VID &#8226; NPI &#8226; type &#8226; parent hierarchy</text>

      <rect x="27" y="184" width="232" height="36" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="143" y="200" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">Affiliation (HCP &#8596; HCO)</text>
      <text x="143" y="212" text-anchor="middle" fill="#6B7280" font-size="8">Primary flag &#8226; address &#8226; role</text>

      <rect x="27" y="228" width="232" height="36" rx="5" fill="#1A0808" stroke="#903030" stroke-width="1"/>
      <text x="143" y="244" text-anchor="middle" fill="#D06060" font-size="9.5" font-weight="600">OIG / GSA Exclusion Flag</text>
      <text x="143" y="256" text-anchor="middle" fill="#6B7280" font-size="8">Real-time stream &#8226; blocks sample &#38; spend</text>

      <rect x="27" y="272" width="232" height="36" rx="5" fill="#0A1A0A" stroke="#305010" stroke-width="1"/>
      <text x="143" y="288" text-anchor="middle" fill="#70A030" font-size="9.5" font-weight="600">Licence &#38; DEA Credential</text>
      <text x="143" y="300" text-anchor="middle" fill="#6B7280" font-size="8">Schedule auth. &#8226; expiry &#8226; state</text>

      <rect x="27" y="316" width="232" height="32" rx="5" fill="#082020" stroke="#0B5E5E" stroke-width="1"/>
      <text x="143" y="332" text-anchor="middle" fill="#2A9A9A" font-size="9.5" font-weight="600">DCR (stewardship queue)</text>
      <text x="143" y="344" text-anchor="middle" fill="#6B7280" font-size="8">Field corrections &#8594; validated &#8594; applied</text>

      <!-- CENTRE LABELS -->
      <text x="470" y="116" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; Account &#38; Contact nightly sync (VID-linked)</text>
      <text x="470" y="160" text-anchor="middle" fill="#3070C0" font-size="8" font-weight="600">&#8594; HCO hierarchy &#8594; Key Account Mgmt</text>
      <text x="470" y="205" text-anchor="middle" fill="#60A030" font-size="8" font-weight="600">&#8594; Primary affiliation &#8594; Align territory assign</text>
      <text x="470" y="249" text-anchor="middle" fill="#C03030" font-size="8" font-weight="600">&#8594; OIG flag real-time &#8594; CRM compliance block</text>
      <text x="470" y="293" text-anchor="middle" fill="#60A030" font-size="8" font-weight="600">&#8594; DEA validation &#8594; PDMA sample gate</text>
      <text x="470" y="337" text-anchor="middle" fill="#2A9A9A" font-size="8" font-weight="600">&#8592; DCR submitted from CRM &#8594; Network stewardship</text>
      <text x="470" y="368" text-anchor="middle" fill="#808080" font-size="7.5">&#8592; Add HCP / address change / merge request &#8212; validated &#8594; propagated back to CRM</text>

      <!-- Arrows -->
      <line x1="271" y1="114" x2="660" y2="114" stroke="#3070C0" stroke-width="1.2" marker-end="url(#ncA)"/>
      <line x1="271" y1="158" x2="660" y2="158" stroke="#3070C0" stroke-width="1.2" marker-end="url(#ncA)"/>
      <line x1="271" y1="202" x2="660" y2="202" stroke="#305010" stroke-width="1.2" marker-end="url(#ncG)"/>
      <line x1="271" y1="246" x2="660" y2="246" stroke="#903030" stroke-width="1.2" marker-end="url(#ncR)"/>
      <line x1="271" y1="290" x2="660" y2="290" stroke="#305010" stroke-width="1.2" marker-end="url(#ncG)"/>
      <!-- DCR reverse arrow -->
      <path d="M660,330 Q470,355 271,330" fill="none" stroke="#0B5E5E" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#ncAL)"/>

      <!-- RIGHT PANEL: CRM + ALIGN -->
      <rect x="662" y="42" width="264" height="312" rx="10" fill="#06100A" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="794" y="64" text-anchor="middle" fill="#6090D8" font-size="12" font-weight="700">Veeva CRM &#38; Align</text>
      <text x="794" y="80" text-anchor="middle" fill="#6B7280" font-size="8.5">Field Force Execution &#38; Territory Mgmt</text>
      <line x1="674" y1="88" x2="914" y2="88" stroke="#1B3A6B" stroke-width="1"/>

      <rect x="674" y="96"  width="240" height="36" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="794" y="112" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">Account &#38; Contact (CRM)</text>
      <text x="794" y="124" text-anchor="middle" fill="#6B7280" font-size="8">vid__v field links to Network master</text>

      <rect x="674" y="140" width="240" height="36" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="794" y="156" text-anchor="middle" fill="#60A0D8" font-size="9.5" font-weight="600">KAM / Strategic Accounts</text>
      <text x="794" y="168" text-anchor="middle" fill="#6B7280" font-size="8">IDN hierarchy for formulary &#38; P&#38;T access</text>

      <rect x="674" y="184" width="240" height="36" rx="5" fill="#0A180A" stroke="#305010" stroke-width="1"/>
      <text x="794" y="200" text-anchor="middle" fill="#70A030" font-size="9.5" font-weight="600">Veeva Align &#8212; Territory Map</text>
      <text x="794" y="212" text-anchor="middle" fill="#6B7280" font-size="8">HCP &#8594; territory &#8594; rep ownership</text>

      <rect x="674" y="228" width="240" height="36" rx="5" fill="#1A0808" stroke="#903030" stroke-width="1"/>
      <text x="794" y="244" text-anchor="middle" fill="#D06060" font-size="9.5" font-weight="600">Compliance Block (OIG)</text>
      <text x="794" y="256" text-anchor="middle" fill="#6B7280" font-size="8">Sample &#38; spend blocked &#8226; manager alerted</text>

      <rect x="674" y="272" width="240" height="36" rx="5" fill="#0A180A" stroke="#305010" stroke-width="1"/>
      <text x="794" y="288" text-anchor="middle" fill="#70A030" font-size="9.5" font-weight="600">PDMA Sample Gate</text>
      <text x="794" y="300" text-anchor="middle" fill="#6B7280" font-size="8">DEA &#38; licence verified before sample drop</text>

      <rect x="674" y="316" width="240" height="32" rx="5" fill="#082020" stroke="#0B5E5E" stroke-width="1"/>
      <text x="794" y="332" text-anchor="middle" fill="#2A9A9A" font-size="9.5" font-weight="600">Rep submits DCR from CRM</text>
      <text x="794" y="344" text-anchor="middle" fill="#6B7280" font-size="8">&#x22;Add HCP&#x22; / address fix &#8594; Network queue</text>
    </svg>
    <figcaption class="vis-cap">Network &#8596; CRM/Align integration &#8212; nightly batch for routine data plus real-time stream for compliance-critical OIG flags; DCR feedback loop keeps master data current from the field</figcaption>
  </figure>

  <!-- Integration reference cards -->
  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.4rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #1B3A6B;">
      <div class="crm-obj-name" style="color:#6090D8;">VID Linkage &#8212; Account &#38; Contact Sync</div>
      <div class="crm-obj-api">Every CRM Account and Contact record links to a Network master via vid__v (Veeva ID)</div>
      <div class="crm-obj-desc">The <span class="crm-field-pill">Network_VID__c</span> field on every CRM Account and Contact is the anchor of the entire integration. When Network updates the master record (new address, specialty change, new affiliation), the nightly sync propagates the change to all CRM records sharing that VID. Reps never need to manually update an HCP&#x27;s address &#8212; if the DCR is accepted, the correction appears in CRM automatically. The VID also enables cross-system analytics: an HCP&#x27;s CRM call history, PromoMats content exposure, and Events Management payments are all linkable through the shared VID.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #1B3A6B;">
      <div class="crm-obj-name" style="color:#6090D8;">Veeva Align &#8212; Territory Assignment</div>
      <div class="crm-obj-api">Network affiliation + address feeds Align territory logic; HCP re-assignment is automatic on move</div>
      <div class="crm-obj-desc">Veeva Align is the territory management layer between Network and CRM. Align takes the HCP&#x27;s primary affiliation address from Network, overlays the company&#x27;s territory geometry (defined as zip codes, bricks, or counties), and produces the rep ownership assignment. When the company does a territory re-alignment (a major periodic event, often annual), Align recomputes all assignments and pushes new ownership to CRM. When an individual HCP changes their primary practice (Network detects via DCR or source feed), Align re-evaluates that HCP&#x27;s territory automatically &#8212; the outgoing rep loses the record; the incoming rep gains it.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #903030;">
      <div class="crm-obj-name" style="color:#D06060;">OIG / GSA Exclusion &#8212; Real-Time Compliance Block</div>
      <div class="crm-obj-api">Exclusion status propagated in real-time; CRM blocks samples, payments, and speaker programs</div>
      <div class="crm-obj-desc">The OIG List of Excluded Individuals/Entities (LEIE) and GSA System for Award Management (SAM) are updated continuously. Veeva Network monitors these sources and pushes exclusion status changes to CRM in near-real-time (not waiting for the nightly batch). When an HCP&#x27;s <span class="crm-field-pill">oig_exclusion_status__v</span> is set to Excluded, CRM immediately blocks: (1) sample transaction submissions for that HCP, (2) Events Management expense reimbursements, and (3) speaker program nominations. The rep&#x27;s district manager receives a compliance alert. Attempting to override the block creates a compliance audit record that routes to the company&#x27;s compliance officer.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #305010;">
      <div class="crm-obj-name" style="color:#70A030;">DEA Validation &#8212; PDMA Sample Gate</div>
      <div class="crm-obj-api">Network validates DEA number and schedule authorisation before CRM allows sample transactions</div>
      <div class="crm-obj-desc">Under 21 CFR Part 203 (PDMA), pharmaceutical samples of controlled substances (Schedule II&#8211;V) can only be distributed to practitioners with an active DEA registration authorised for the relevant schedule. Network maintains the DEA registration data from the DEA database and validates it continuously. When a rep initiates a sample transaction in CRM for a Schedule II&#8211;V product, CRM queries Network in real-time to confirm: (1) the HCP has an active DEA registration, (2) the registration covers the relevant schedule, and (3) the registration has not expired. If any check fails, the transaction is blocked and the rep cannot proceed.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">DCR Workflow &#8212; Field-to-Master Correction Loop</div>
      <div class="crm-obj-api">Reps submit corrections from CRM; Network stewards validate and apply; CRM updated automatically</div>
      <div class="crm-obj-desc">The DCR workflow is the primary mechanism for keeping Network data current with real-world changes that external sources have not yet captured. DCR types cover: <em>Add HCP</em> (new prescriber not yet in Network), <em>Add HCO</em>, <em>Edit Address</em> (practice move), <em>Edit Specialty</em>, <em>Merge Duplicates</em> (rep discovers two CRM accounts for the same HCP), and <em>Inactivate</em> (HCP retired or deceased). Each DCR carries a full audit trail. Most companies target a 24&#8211;48 hour stewardship SLA for field-submitted DCRs. High-volume DCR queues indicate a data quality problem in the underlying reference sources that needs to be escalated to the data operations team.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">HCO Hierarchy &#8212; Key Account Management</div>
      <div class="crm-obj-api">IDN parent-child hierarchy from Network drives strategic account planning in CRM</div>
      <div class="crm-obj-desc">The HCO hierarchy maintained in Network (IDN &#8594; health system &#8594; hospital &#8594; clinic &#8594; department) is the foundation of Key Account Management (KAM) strategy. KAMs who negotiate formulary access at the IDN level need visibility into which hospitals and clinics fall under that IDN, which P&#38;T committees govern formulary decisions at each node, and which HCPs practise at each facility. Network&#x27;s hierarchy data feeds CRM Account hierarchy views that KAMs use to plan their multi-stakeholder engagement strategy. Changes in ownership (a hospital acquired by a larger IDN) are captured in Network and propagate to CRM Account parent-child relationships automatically.</div>
    </div>

  </div>
"""

CLM_EXTRA_NEW = """

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="clm-crm-mechanics">CLM in Veeva CRM &#8212; How It Works</h3>

  <p>The CLM engine in Veeva CRM transforms a conventional sales call into a data-collection event. Every interaction between a rep&#x27;s iPad and an HCP &#8212; every slide viewed, every swipe, every second of dwell time, every key message reaction &#8212; is recorded as a structured data record in CRM. This is not survey data or rep recall: it is a system-generated audit log captured automatically in real time, attached to the parent Call Report, and available for analytics within 24 hours of sync. The data is granular enough to answer questions like: &#x22;Do cardiologists in the North-East skip the safety profile slide?&#x22; or &#x22;Which version of the efficacy headline message gets Agree or higher from HCPs with 10&#43; years of prescribing experience?&#x22;</p>

  <p>The technical flow begins when a rep opens iRep (Veeva&#x27;s iPad CRM application) and navigates to an HCP&#x27;s account. The system checks the rep&#x27;s active Cycle Plan to confirm the HCP is a target for this cycle, loads the approved CLM content library for the products assigned to the rep&#x27;s territory, and presents the available decks. The rep starts the call &#8212; creating a <strong>Call_vod__c</strong> record in real time &#8212; then taps a CLM presentation to launch it. CRM logs the <strong>CLM_Presentation_vod__c</strong> record for this call: which approved deck was used, the start timestamp, and the Approved_Document_vod__c it links to. From this point, every slide transition fires a write to the database: the slide ID, the entry timestamp, and the exit timestamp. When the rep notes a key message discussion and the HCP&#x27;s reaction, a <strong>Key_Message_Reaction_vod__c</strong> record is created. Products Detailed, sample drops, and any business rules (mandatory slides, required reactions before advancing) are enforced by the CLM engine in real time &#8212; a rep cannot advance past a mandatory slide without acknowledging it.</p>

  <p>On call signature, the entire session &#8212; Call record, CLM slide records, Key Message reactions, Products Detailed, and Sample Transactions &#8212; is committed to the CRM database and queued for sync to the cloud. The nightly or real-time sync pushes this engagement data to Veeva&#x27;s analytics layer, where it is aggregated by product, slide, territory, rep, HCP specialty, prescribing tier, and call date. Brand teams access these aggregated views via the PromoMats analytics dashboard within 48 hours of the call. The brand manager who commissioned the Visual Aid can see, before the end of the working week, exactly how HCPs responded to each slide and message in every call made that week &#8212; not as a survey but as behavioural data from thousands of actual sales calls.</p>

  <!-- SVG: In-Call CLM Data Capture -->
  <figure class="vis-embed" aria-label="In-Call CLM Data Capture Flow">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> CLM In-Call Data Capture &#8212; from iRep Launch to CRM Analytics Record</div>
    <svg viewBox="0 0 960 380" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:960px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="clmA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#1B3A6B"/></marker>
        <marker id="clmG" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#208050"/></marker>
        <marker id="clmO" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#0B5E5E"/></marker>
      </defs>
      <rect width="960" height="380" rx="12" fill="#0D1117"/>
      <text x="480" y="26" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">CLM In-Call Data Capture &#8212; iRep to CRM Analytics</text>

      <!-- ── LEFT: CALL SETUP STEPS ── -->
      <text x="88" y="50" text-anchor="middle" fill="#9CA3AF" font-size="9.5" font-weight="600">Call Setup</text>

      <rect x="14" y="58" width="148" height="34" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="88" y="74" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Rep opens iRep</text>
      <text x="88" y="86" text-anchor="middle" fill="#6B7280" font-size="7.5">Cycle plan loaded</text>

      <line x1="88" y1="92" x2="88" y2="104" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>

      <rect x="14" y="106" width="148" height="34" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="88" y="122" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Select HCP Account</text>
      <text x="88" y="134" text-anchor="middle" fill="#6B7280" font-size="7.5">Network VID validated</text>

      <line x1="88" y1="140" x2="88" y2="152" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>

      <rect x="14" y="154" width="148" height="34" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="88" y="170" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Open Call Record</text>
      <text x="88" y="182" text-anchor="middle" fill="#6B7280" font-size="7.5">Call_vod__c created</text>

      <line x1="88" y1="188" x2="88" y2="200" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>

      <rect x="14" y="202" width="148" height="34" rx="6" fill="#0A2014" stroke="#208050" stroke-width="1.5"/>
      <text x="88" y="218" text-anchor="middle" fill="#40C070" font-size="9" font-weight="600">Launch CLM Deck</text>
      <text x="88" y="230" text-anchor="middle" fill="#6B7280" font-size="7.5">CLM_Presentation_vod__c logged</text>

      <line x1="88" y1="236" x2="88" y2="248" stroke="#208050" stroke-width="1.2" marker-end="url(#clmG)"/>

      <rect x="14" y="250" width="148" height="34" rx="6" fill="#0A1A0A" stroke="#208050" stroke-width="1.5"/>
      <text x="88" y="266" text-anchor="middle" fill="#40C070" font-size="9" font-weight="600">Present &#38; Discuss</text>
      <text x="88" y="278" text-anchor="middle" fill="#6B7280" font-size="7.5">Slides &#8226; Key Messages &#8226; Reactions</text>

      <line x1="88" y1="284" x2="88" y2="296" stroke="#208050" stroke-width="1.2" marker-end="url(#clmG)"/>

      <rect x="14" y="298" width="148" height="34" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="88" y="314" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">HCP Signature</text>
      <text x="88" y="326" text-anchor="middle" fill="#6B7280" font-size="7.5">Call committed &#8226; sync queued</text>

      <!-- Arrows from setup to center iPad -->
      <line x1="162" y1="190" x2="214" y2="190" stroke="#208050" stroke-width="1.5" marker-end="url(#clmG)"/>

      <!-- ── CENTRE: iPAD SLIDE SESSION ── -->
      <!-- iPad frame -->
      <rect x="216" y="44" width="380" height="320" rx="18" fill="#111820" stroke="#3060A0" stroke-width="2.5"/>
      <rect x="228" y="56" width="356" height="296" rx="8" fill="#0A0F16" stroke="#204080" stroke-width="1"/>
      <text x="406" y="76" text-anchor="middle" fill="#6090D8" font-size="10.5" font-weight="700">iRep CLM Presentation</text>
      <line x1="230" y1="84" x2="582" y2="84" stroke="#204080" stroke-width="1"/>

      <!-- Slide 1 -->
      <rect x="234" y="92" width="340" height="42" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <rect x="234" y="92" width="5" height="42" rx="2" fill="#2050A0"/>
      <text x="252" y="109" fill="#60A0D8" font-size="9" font-weight="700">Slide 1 &#8212; Product Overview</text>
      <text x="252" y="122" fill="#6B7280" font-size="8">Dwell: 48 sec &#8226; Fully viewed</text>
      <text x="512" y="114" text-anchor="middle" fill="#40C070" font-size="8.5" font-weight="700">SHOWN</text>

      <!-- Slide 2 -->
      <rect x="234" y="142" width="340" height="42" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <rect x="234" y="142" width="5" height="42" rx="2" fill="#2050A0"/>
      <text x="252" y="159" fill="#60A0D8" font-size="9" font-weight="700">Slide 2 &#8212; Phase III Efficacy Data</text>
      <text x="252" y="172" fill="#6B7280" font-size="8">Dwell: 2 min 14 sec &#8226; Reaction: Agree &#9733;</text>
      <text x="512" y="162" text-anchor="middle" fill="#40C070" font-size="8.5" font-weight="700">SHOWN</text>
      <text x="512" y="173" text-anchor="middle" fill="#A0C080" font-size="7.5">KM Reaction: 4</text>

      <!-- Slide 3 -->
      <rect x="234" y="192" width="340" height="42" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <rect x="234" y="192" width="5" height="42" rx="2" fill="#2050A0"/>
      <text x="252" y="209" fill="#60A0D8" font-size="9" font-weight="700">Slide 3 &#8212; Safety Profile</text>
      <text x="252" y="222" fill="#6B7280" font-size="8">Dwell: 1 min 32 sec &#8226; Reaction: Neutral</text>
      <text x="512" y="212" text-anchor="middle" fill="#40C070" font-size="8.5" font-weight="700">SHOWN</text>
      <text x="512" y="223" text-anchor="middle" fill="#A0A060" font-size="7.5">KM Reaction: 3</text>

      <!-- Slide 4 SKIPPED -->
      <rect x="234" y="242" width="340" height="42" rx="5" fill="#1A1010" stroke="#503030" stroke-width="1" stroke-dasharray="4,3"/>
      <rect x="234" y="242" width="5" height="42" rx="2" fill="#503030"/>
      <text x="252" y="259" fill="#9CA3AF" font-size="9" font-weight="600">Slide 4 &#8212; Dosing Chart</text>
      <text x="252" y="272" fill="#6B7280" font-size="8">Dwell: 0 sec &#8226; Swiped past</text>
      <text x="512" y="262" text-anchor="middle" fill="#C06060" font-size="8.5" font-weight="700">SKIPPED</text>

      <!-- Slide 5 -->
      <rect x="234" y="292" width="340" height="48" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <rect x="234" y="292" width="5" height="48" rx="2" fill="#2050A0"/>
      <text x="252" y="309" fill="#60A0D8" font-size="9" font-weight="700">Slide 5 &#8212; Payer Access / Coverage</text>
      <text x="252" y="322" fill="#6B7280" font-size="8">Dwell: 54 sec &#8226; Mandatory &#8212; cannot skip</text>
      <text x="252" y="333" fill="#6B7280" font-size="8">Key Message: &#x22;Tier 2 formulary 85% plans&#x22;</text>
      <text x="512" y="316" text-anchor="middle" fill="#40C070" font-size="8.5" font-weight="700">SHOWN</text>

      <!-- Arrows from iPad to right panel -->
      <line x1="596" y1="130" x2="628" y2="115" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>
      <line x1="596" y1="175" x2="628" y2="165" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>
      <line x1="596" y1="220" x2="628" y2="215" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>
      <line x1="596" y1="262" x2="628" y2="260" stroke="#903030" stroke-width="1.2" marker-end="url(#clmA)"/>
      <line x1="596" y1="318" x2="628" y2="310" stroke="#1B3A6B" stroke-width="1.2" marker-end="url(#clmA)"/>

      <!-- ── RIGHT: CRM RECORDS CREATED ── -->
      <text x="788" y="50" text-anchor="middle" fill="#9CA3AF" font-size="9.5" font-weight="600">CRM Records Created</text>

      <rect x="630" y="58" width="316" height="38" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="788" y="74" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Call_vod__c (parent)</text>
      <text x="788" y="86" text-anchor="middle" fill="#6B7280" font-size="7.5">HCP VID &#8226; call date &#8226; duration &#8226; CLM flag &#8226; signature</text>

      <rect x="630" y="104" width="316" height="52" rx="6" fill="#0A1A0A" stroke="#208050" stroke-width="1.5"/>
      <text x="788" y="120" text-anchor="middle" fill="#40C070" font-size="9" font-weight="600">CLM_Presentation_vod__c</text>
      <text x="788" y="133" text-anchor="middle" fill="#6B7280" font-size="7.5">Approved doc link &#8226; deck version &#8226; start time</text>
      <text x="788" y="146" text-anchor="middle" fill="#6B7280" font-size="7.5">slides_shown__v &#8226; slides_skipped__v</text>

      <rect x="630" y="164" width="316" height="62" rx="6" fill="#0A1A0A" stroke="#208050" stroke-width="1.5"/>
      <text x="788" y="180" text-anchor="middle" fill="#40C070" font-size="9" font-weight="600">Clm_Presentation_Slide_vod__c</text>
      <text x="788" y="193" text-anchor="middle" fill="#6B7280" font-size="7.5">Per-slide record: slide_id &#8226; entry_time</text>
      <text x="788" y="205" text-anchor="middle" fill="#6B7280" font-size="7.5">exit_time &#8226; dwell_sec &#8226; reaction_vod__c</text>
      <text x="788" y="217" text-anchor="middle" fill="#6B7280" font-size="7.5">swipe_direction &#8226; presented_flag</text>

      <rect x="630" y="234" width="316" height="48" rx="6" fill="#081818" stroke="#0B5E5E" stroke-width="1.5"/>
      <text x="788" y="250" text-anchor="middle" fill="#2A9A9A" font-size="9" font-weight="600">Key_Message_vod__c + Reaction</text>
      <text x="788" y="263" text-anchor="middle" fill="#6B7280" font-size="7.5">message_id &#8226; reaction_vod__c (1&#8211;5)</text>
      <text x="788" y="276" text-anchor="middle" fill="#6B7280" font-size="7.5">1=Strongly Agree &#8230; 5=Strongly Disagree</text>

      <rect x="630" y="290" width="316" height="48" rx="6" fill="#0C1828" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="788" y="306" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Products_Detailed_vod__c</text>
      <text x="788" y="319" text-anchor="middle" fill="#6B7280" font-size="7.5">product &#8226; detail priority (1st/2nd/3rd)</text>
      <text x="788" y="332" text-anchor="middle" fill="#6B7280" font-size="7.5">CLM_presentation_vod__c &#8226; sample drop ref</text>

      <!-- analytics arrow from CRM records -->
      <path d="M788,348 Q788,368 480,368 Q172,368 88,348" fill="none" stroke="#0B5E5E" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#clmO)"/>
      <text x="480" y="363" text-anchor="middle" fill="#2A9A9A" font-size="7.5">Sync to analytics engine &#8212; aggregated by slide &#8226; territory &#8226; specialty &#8226; prescribing tier &#8226; date &#8594; PromoMats brand dashboard</text>
    </svg>
    <figcaption class="vis-cap">CLM in-call data capture &#8212; every slide shown, skipped, or reacted to creates a structured CRM record available to brand analytics within 48 hours</figcaption>
  </figure>

  <!-- CLM CRM Object Reference Cards -->
  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.4rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40C070;">CLM_Presentation_vod__c</div>
      <div class="crm-obj-api">The approved deck used in a specific call &#8212; links the call to the PromoMats-approved content</div>
      <div class="crm-obj-desc">One record per CLM deck used per call. Links the <strong>Call_vod__c</strong> to the <strong>Approved_Document_vod__c</strong> it was launched from. Captures deck-level metadata: presentation start timestamp, end timestamp, total slides in deck, slides shown count, slides skipped count, and whether all mandatory slides were presented. If a rep fails to show a mandatory slide (a compliance rule set by brand), the record flags it and the Call cannot be submitted until the mandatory slide is shown or an exception reason is logged. Fields: <span class="crm-field-pill">Approved_Document_vod__c</span> <span class="crm-field-pill">Start_Time_vod__c</span> <span class="crm-field-pill">Slides_Shown_vod__c</span> <span class="crm-field-pill">Mandatory_Slides_Flag_vod__c</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #208050;">
      <div class="crm-obj-name" style="color:#40C070;">Clm_Presentation_Slide_vod__c</div>
      <div class="crm-obj-api">Per-slide engagement record &#8212; the atomic unit of CLM analytics</div>
      <div class="crm-obj-desc">One record per slide per call. This is the raw CLM engagement data. Each record captures: the slide ID (linking back to the CLM_Slide_vod__c in the approved deck), entry timestamp, exit timestamp, calculated dwell time in seconds, swipe direction on exit, and an optional reaction code if the rep tapped a reaction button during that slide. Skipped slides (swiped past without dwell) are recorded with dwell = 0 and presented_flag = false. This per-slide granularity enables slide heatmaps showing exactly which slides get attention and which get skipped, aggregated across thousands of calls. Fields: <span class="crm-field-pill">slide_id__v</span> <span class="crm-field-pill">entry_time__v</span> <span class="crm-field-pill">exit_time__v</span> <span class="crm-field-pill">dwell_seconds__v</span> <span class="crm-field-pill">presented_flag__v</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">Key_Message_vod__c &#38; Reaction</div>
      <div class="crm-obj-api">Approved talking points with HCP reaction captured on 5-point Likert scale</div>
      <div class="crm-obj-desc">Each Key Message record represents an MLR-approved claim that reps are authorised to discuss. During a call, reps tap the message(s) they discussed and capture the HCP&#x27;s reaction: <strong>1 = Strongly Agree</strong>, 2 = Agree, 3 = Neutral, 4 = Disagree, <strong>5 = Strongly Disagree</strong>. The reaction is not the rep&#x27;s self-assessment &#8212; it is the rep&#x27;s observation of the HCP&#x27;s verbal and non-verbal response. Reaction data aggregates into brand-level message adoption scores. A message consistently scoring 4&#8211;5 (Disagree) across a segment is a brand strategy alert and the primary trigger for a PromoMats content revision cycle. Fields: <span class="crm-field-pill">Key_Message_vod__c</span> <span class="crm-field-pill">CLM_Presentation_vod__c</span> <span class="crm-field-pill">Reaction_vod__c</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #1B3A6B;">
      <div class="crm-obj-name" style="color:#6090D8;">Products_Detailed_vod__c</div>
      <div class="crm-obj-api">Which products were detailed in the call and at which priority &#8212; enforces brand detail strategy</div>
      <div class="crm-obj-desc">Records which products were promoted during the call and at what priority (1st detail = primary focus, 2nd detail = secondary, 3rd = brief mention). CRM enforces that reps can only detail products on the approved Cycle Plan&#x27;s detail list &#8212; no ad-hoc detailing of unapproved products or off-cycle competitors. Each Products_Detailed record links to the CLM_Presentation_vod__c used for that product, creating an auditable link: product promoted &#8594; deck used &#8594; slides shown &#8594; messages discussed &#8594; reactions captured. Fields: <span class="crm-field-pill">Product_vod__c</span> <span class="crm-field-pill">Detail_Priority_vod__c</span> <span class="crm-field-pill">CLM_Presentation_vod__c</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4A2080;">
      <div class="crm-obj-name" style="color:#9060C0;">CLM Slide Library (CLM_Slide_vod__c)</div>
      <div class="crm-obj-api">Slide-level metadata in the approved deck &#8212; defines mandatory slides, slide sequence, and linked key messages</div>
      <div class="crm-obj-desc">Each individual slide in an approved CLM presentation is a CLM_Slide_vod__c record. Slide records define: the slide&#x27;s position in the deck, whether it is mandatory (cannot be skipped), which Key Messages are associated with it, and the slide content URL (the HTML5 file served to iRep). When brand teams build a new CLM deck in PromoMats, the slide structure, mandatory rules, and Key Message associations are configured here. The slide library is what gets pushed to iRep &#8212; the rep sees slides, not these records, but every interaction maps back to a specific slide record. Fields: <span class="crm-field-pill">CLM_Presentation_vod__c</span> <span class="crm-field-pill">Slide_Order_vod__c</span> <span class="crm-field-pill">Mandatory_vod__c</span> <span class="crm-field-pill">Key_Messages_vod__c</span></div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #4A2080;">
      <div class="crm-obj-name" style="color:#9060C0;">CLM Analytics &#8212; Brand Dashboard</div>
      <div class="crm-obj-api">Aggregated engagement metrics surfaced to brand teams via PromoMats analytics and CRM MyInsights</div>
      <div class="crm-obj-desc">The raw Clm_Presentation_Slide_vod__c and Key Message reaction records are aggregated by Veeva&#x27;s analytics engine into brand dashboards accessible from PromoMats and CRM MyInsights. Key metrics: <strong>Slide Show Rate</strong> (% of calls where a slide was shown), <strong>Slide Skip Rate</strong>, <strong>Average Dwell Time</strong> per slide, <strong>Message Adoption Rate</strong> (% of calls where a message was discussed), and <strong>Reaction Distribution</strong> (% Agree vs. Disagree per message, segmented by HCP specialty, prescribing tier, and geography). Brand teams can slice these metrics by rep, territory, time period, and HCP segment to identify content optimisation opportunities within days of launch.</div>
    </div>

  </div>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="clm-promomats">PromoMats &#8596; CLM &#8212; The Content-Engagement-Revision Cycle</h3>

  <p>The PromoMats-CLM integration is the commercial operating system of pharmaceutical brand management. It connects four distinct functions &#8212; content creation, regulatory review, field execution, and analytics &#8212; into a single closed feedback loop. The data transfer between PromoMats and CRM&#x27;s CLM module is bidirectional: PromoMats pushes content to the field (the outbound flow), and CRM returns engagement data to the brand team (the inbound flow). Each direction carries different data types, different cadences, and different compliance implications.</p>

  <p>The <strong>outbound flow</strong> begins when a Visual Aid achieves Approved status in PromoMats. Three things happen simultaneously: (1) an <strong>Approved_Document_vod__c</strong> record is created in CRM; (2) the HTML5 CLM package is packaged and queued for distribution to all eligible rep iPads; (3) the Key Messages associated with the approved claims are synchronised to <strong>Key_Message_vod__c</strong> records, defining what reps can discuss. The next time a rep syncs their iPad (overnight or on Wi-Fi), the new deck appears in their CLM library. The rep can open it immediately. The deck version, approval date, and expiration date are all embedded in the <strong>CLM_Presentation_vod__c</strong> metadata &#8212; if the rep somehow had the previous version loaded, the sync replaces it. When the document expires in PromoMats, the nightly batch removes it from iRep automatically.</p>

  <p>The <strong>inbound flow</strong> begins with the call sync. As CLM engagement records (slide records, key message reactions, products detailed) sync to the cloud, the analytics engine aggregates them against the PromoMats document number and version. Within 24&#8211;48 hours of a call, the brand manager can see updated slide performance metrics for every deck in the field. The signal the brand team watches most closely is the <strong>Key Message Reaction Trend</strong>: if a core efficacy message drops below a 60% Agree rate in a high-priority HCP segment, that is a brand strategy event. The brand team may respond by: redesigning the slide supporting that message, adding a new slide with supporting clinical evidence, or changing the message text &#8212; any of which requires a new PromoMats submission, a full MLR re-review, and a new version push to iRep. The CLM loop completes when the revised deck reaches the field and brand teams begin tracking whether the new message performs better than the old one.</p>

  <div class="ornament" style="font-size:1rem;color:var(--border-2);text-align:center;margin:1.8rem 0;">&#10022; &nbsp; &#10022; &nbsp; &#10022;</div>

  <h3 id="clm-medcomm">Veeva MedComm &#38; Medical Affairs CLM</h3>

  <p>Veeva MedComm refers to the Medical Communications capability within the Veeva ecosystem &#8212; the integration of scientific content management, MSL field execution, remote engagement, and medical insight analytics. While the commercial CLM loop runs on promotional Visual Aids approved through PromoMats, the Medical Affairs CLM loop runs on scientific decks approved through <strong>Vault Medical</strong> and executed through <strong>MSL iRep</strong>. The data model is the same (Call_vod__c, CLM_Presentation_vod__c, Key_Message equivalents) but the content type, the compliance framework, and the analytics objectives are fundamentally different.</p>

  <p>In MSL iRep, the CLM capability presents non-promotional scientific decks during KOL meetings. The MSL launches a scientific platform presentation, and engagement is tracked at the slide level just as in commercial CLM &#8212; but the outcome being measured is not message adoption; it is <strong>scientific exchange quality</strong> and <strong>KOL insight generation</strong>. After each slide, the MSL can add a free-text note capturing the KOL&#x27;s scientific feedback, question, or insight. These notes are stored as <strong>Insight_vod__c</strong> records linked to both the Call and the specific slide where the insight was generated. The aggregation of insights across all MSLs &#8212; which scientific questions are KOLs asking most frequently, which clinical gaps are they identifying &#8212; is the Medical Affairs equivalent of the commercial brand team&#x27;s key message reaction dashboard. It informs publication strategy, IIS prioritisation, and Phase IV trial design.</p>

  <p><strong>Veeva Engage</strong> extends the CLM capability to remote and hybrid interactions. Using Veeva Engage Meeting (a video conferencing layer integrated directly into iRep and MSL iRep), a rep or MSL can conduct a video call with an HCP and present their CLM deck simultaneously &#8212; the slides appear on both the rep&#x27;s screen and the HCP&#x27;s browser window, mirrored in real time. Every engagement metric captured in a face-to-face CLM session &#8212; slide dwell time, key message reactions, products detailed &#8212; is captured identically in a remote Engage session. The Call_vod__c record type for an Engage session is flagged as <em>Remote_Meeting_vod__c</em> but feeds the same analytics pipeline. From a brand analytics perspective, there is no difference between a slide shown in person in Boston and the same slide shown via video call in Seattle &#8212; the engagement data is structurally identical.</p>

  <!-- SVG: Full CLM Ecosystem -->
  <figure class="vis-embed" aria-label="Full CLM Ecosystem">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> CLM Full Ecosystem &#8212; PromoMats &#8226; CRM &#8226; MedComm &#8226; Analytics &#8226; Engage</div>
    <svg viewBox="0 0 960 440" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:960px;font-family:system-ui,sans-serif;display:block;">
      <defs>
        <marker id="ecoA"  markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#3070C0"/></marker>
        <marker id="ecoG"  markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#208050"/></marker>
        <marker id="ecoT"  markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#0B5E5E"/></marker>
        <marker id="ecoP"  markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#7040C0"/></marker>
        <marker id="ecoAL" markerWidth="7" markerHeight="5" refX="0"  refY="2.5" orient="auto"><polygon points="7 0,0 2.5,7 5" fill="#3070C0"/></marker>
        <marker id="ecoTL" markerWidth="7" markerHeight="5" refX="0"  refY="2.5" orient="auto"><polygon points="7 0,0 2.5,7 5" fill="#0B5E5E"/></marker>
      </defs>
      <rect width="960" height="440" rx="12" fill="#0D1117"/>
      <text x="480" y="26" text-anchor="middle" fill="#E6EDF3" font-size="13" font-weight="700">CLM Full Ecosystem &#8212; Integrations Across PromoMats, CRM, MedComm &#38; Analytics</text>

      <!-- ── TOP: CONTENT CREATION ── -->
      <!-- PromoMats (top-left) -->
      <rect x="30" y="42" width="210" height="110" rx="10" fill="#120818" stroke="#7040C0" stroke-width="1.5"/>
      <text x="135" y="62" text-anchor="middle" fill="#A070E0" font-size="11" font-weight="700">Vault PromoMats</text>
      <text x="135" y="77" text-anchor="middle" fill="#6B7280" font-size="8">MLR-approved promotional content</text>
      <line x1="42" y1="84" x2="228" y2="84" stroke="#4B2080" stroke-width="1"/>
      <text x="42"  y="97"  fill="#9CA3AF" font-size="8">&#9656; Visual Aid / CLM deck (HTML5)</text>
      <text x="42"  y="111" fill="#9CA3AF" font-size="8">&#9656; Approved Email templates</text>
      <text x="42"  y="125" fill="#9CA3AF" font-size="8">&#9656; Claims &#38; Key Message library</text>
      <text x="42"  y="139" fill="#9CA3AF" font-size="8">&#9656; Expiry / auto-withdrawal signal</text>

      <!-- Vault Medical (top-right) -->
      <rect x="720" y="42" width="210" height="110" rx="10" fill="#081818" stroke="#0B5E5E" stroke-width="1.5"/>
      <text x="825" y="62" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Vault Medical</text>
      <text x="825" y="77" text-anchor="middle" fill="#6B7280" font-size="8">Scientific content (non-promotional)</text>
      <line x1="732" y1="84" x2="918" y2="84" stroke="#0B5E5E" stroke-width="1"/>
      <text x="732" y="97"  fill="#9CA3AF" font-size="8">&#9656; MSL scientific decks</text>
      <text x="732" y="111" fill="#9CA3AF" font-size="8">&#9656; Standard Response Letters (SRL)</text>
      <text x="732" y="125" fill="#9CA3AF" font-size="8">&#9656; Congress presentations</text>
      <text x="732" y="139" fill="#9CA3AF" font-size="8">&#9656; IIS / Grant documents</text>

      <!-- ── CENTRE: CLM ENGINE ── -->
      <rect x="330" y="80" width="300" height="160" rx="12" fill="#080E18" stroke="#1B3A6B" stroke-width="2"/>
      <text x="480" y="102" text-anchor="middle" fill="#6090D8" font-size="12" font-weight="700">CLM Engine &#8212; Veeva CRM</text>
      <text x="480" y="117" text-anchor="middle" fill="#6B7280" font-size="8.5">iRep &#8226; MSL iRep &#8226; Veeva Engage</text>
      <line x1="342" y1="124" x2="618" y2="124" stroke="#1B3A6B" stroke-width="1"/>

      <rect x="344" y="132" width="130" height="40" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="409" y="149" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">iRep (Commercial)</text>
      <text x="409" y="162" text-anchor="middle" fill="#6B7280" font-size="7.5">Promotional CLM sessions</text>

      <rect x="486" y="132" width="120" height="40" rx="5" fill="#081818" stroke="#208060" stroke-width="1"/>
      <text x="546" y="149" text-anchor="middle" fill="#40B090" font-size="9" font-weight="600">MSL iRep (Medical)</text>
      <text x="546" y="162" text-anchor="middle" fill="#6B7280" font-size="7.5">Scientific CLM + Insights</text>

      <rect x="344" y="180" width="130" height="40" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="409" y="197" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">Call_vod__c</text>
      <text x="409" y="210" text-anchor="middle" fill="#6B7280" font-size="7.5">All channels &#8226; in-person &#38; remote</text>

      <rect x="486" y="180" width="120" height="40" rx="5" fill="#0C1828" stroke="#2050A0" stroke-width="1"/>
      <text x="546" y="197" text-anchor="middle" fill="#60A0D8" font-size="9" font-weight="600">CLM Slide Records</text>
      <text x="546" y="210" text-anchor="middle" fill="#6B7280" font-size="7.5">Per-slide engagement data</text>

      <!-- ── BOTTOM-LEFT: ANALYTICS ── -->
      <rect x="30" y="290" width="210" height="120" rx="10" fill="#080E18" stroke="#1B3A6B" stroke-width="1.5"/>
      <text x="135" y="311" text-anchor="middle" fill="#6090D8" font-size="11" font-weight="700">Brand Analytics</text>
      <text x="135" y="326" text-anchor="middle" fill="#6B7280" font-size="8">SFE &#38; PromoMats dashboards</text>
      <line x1="42" y1="333" x2="228" y2="333" stroke="#1B3A6B" stroke-width="1"/>
      <text x="42"  y="346" fill="#9CA3AF" font-size="8">&#9656; Slide show / skip rate</text>
      <text x="42"  y="360" fill="#9CA3AF" font-size="8">&#9656; KM reaction trends by segment</text>
      <text x="42"  y="374" fill="#9CA3AF" font-size="8">&#9656; Content revision triggers</text>
      <text x="42"  y="388" fill="#9CA3AF" font-size="8">&#9656; Rep performance vs. peer</text>

      <!-- ── BOTTOM-RIGHT: MEDICAL INSIGHTS ── -->
      <rect x="720" y="290" width="210" height="120" rx="10" fill="#081818" stroke="#0B5E5E" stroke-width="1.5"/>
      <text x="825" y="311" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Medical Analytics</text>
      <text x="825" y="326" text-anchor="middle" fill="#6B7280" font-size="8">Insight aggregation &#38; MedComms</text>
      <line x1="732" y1="333" x2="918" y2="333" stroke="#0B5E5E" stroke-width="1"/>
      <text x="732" y="346" fill="#9CA3AF" font-size="8">&#9656; Insight_vod__c aggregated</text>
      <text x="732" y="360" fill="#9CA3AF" font-size="8">&#9656; KOL question patterns</text>
      <text x="732" y="374" fill="#9CA3AF" font-size="8">&#9656; Publication / IIS strategy</text>
      <text x="732" y="388" fill="#9CA3AF" font-size="8">&#9656; Med strategy &#38; gap analysis</text>

      <!-- ── BOTTOM-CENTRE: VEEVA ENGAGE ── -->
      <rect x="360" y="308" width="240" height="84" rx="10" fill="#0A1020" stroke="#304080" stroke-width="1.5"/>
      <text x="480" y="328" text-anchor="middle" fill="#6090A8" font-size="11" font-weight="700">Veeva Engage</text>
      <text x="480" y="343" text-anchor="middle" fill="#6B7280" font-size="8">Remote video meeting + CLM mirroring</text>
      <line x1="372" y1="350" x2="588" y2="350" stroke="#304080" stroke-width="1"/>
      <text x="480" y="363" text-anchor="middle" fill="#9CA3AF" font-size="8">Same CLM data capture as in-person</text>
      <text x="480" y="376" text-anchor="middle" fill="#9CA3AF" font-size="8">Remote_Meeting_vod__c record type</text>

      <!-- ── ARROWS ── -->
      <!-- PromoMats -> CLM Engine -->
      <line x1="240" y1="97" x2="330" y2="140" stroke="#7040C0" stroke-width="1.5" marker-end="url(#ecoP)"/>
      <text x="282" y="113" text-anchor="middle" fill="#7040C0" font-size="7.5">CLM push</text>
      <!-- Vault Medical -> CLM Engine -->
      <line x1="720" y1="97" x2="630" y2="140" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#ecoT)"/>
      <text x="678" y="113" text-anchor="middle" fill="#0B5E5E" font-size="7.5">Sci. deck push</text>
      <!-- CLM Engine -> Brand Analytics -->
      <line x1="390" y1="240" x2="200" y2="290" stroke="#3070C0" stroke-width="1.5" marker-end="url(#ecoA)"/>
      <text x="285" y="270" text-anchor="middle" fill="#3070C0" font-size="7.5">Engagement data</text>
      <!-- CLM Engine -> Medical Analytics -->
      <line x1="570" y1="240" x2="760" y2="290" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#ecoT)"/>
      <text x="675" y="270" text-anchor="middle" fill="#0B5E5E" font-size="7.5">Insights &#38; MSL data</text>
      <!-- CLM Engine -> Engage -->
      <line x1="480" y1="240" x2="480" y2="308" stroke="#3060A0" stroke-width="1.5" marker-end="url(#ecoA)"/>
      <text x="498" y="278" fill="#3060A0" font-size="7.5">Remote channel</text>
      <!-- Brand Analytics -> PromoMats (feedback) -->
      <path d="M135,290 Q100,220 135,152" fill="none" stroke="#7040C0" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#ecoP)"/>
      <text x="52" y="218" text-anchor="middle" fill="#7040C0" font-size="7.5" transform="rotate(-80,52,218)">Content revision</text>
      <!-- Medical Analytics -> Vault Medical (feedback) -->
      <path d="M825,290 Q860,220 825,152" fill="none" stroke="#0B5E5E" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#ecoT)"/>
      <text x="908" y="218" text-anchor="middle" fill="#0B5E5E" font-size="7.5" transform="rotate(80,908,218)">Med strategy</text>
      <!-- Engage -> Analytics -->
      <line x1="360" y1="360" x2="240" y2="360" stroke="#304080" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#ecoA)"/>
      <line x1="600" y1="360" x2="720" y2="360" stroke="#304080" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#ecoT)"/>
    </svg>
    <figcaption class="vis-cap">CLM full ecosystem &#8212; PromoMats and Vault Medical feed content to iRep and MSL iRep; engagement data flows to Brand Analytics and Medical Analytics; Veeva Engage extends CLM to remote channels; feedback loops drive content revision</figcaption>
  </figure>

  <!-- MedComm Reference Cards -->
  <div class="crm-obj-grid" style="grid-template-columns:repeat(2,1fr);gap:14px;margin:1.4rem 0 2rem 0;">

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">MSL iRep &#8212; Medical CLM Execution</div>
      <div class="crm-obj-api">Scientific CLM for MSLs &#8212; same engine as commercial iRep, different content and compliance rules</div>
      <div class="crm-obj-desc">MSL iRep is the Medical Affairs version of iRep, using the same Veeva CRM CLM engine but operating under a different permission profile and content library. Scientific decks from Vault Medical replace promotional Visual Aids. The Call record type used by MSLs omits all commercial fields (no Products Detailed, no sample drop, no Approved Email) and replaces them with scientific exchange fields: <span class="crm-field-pill">Discussion_Topic_vod__c</span>, <span class="crm-field-pill">Insight_vod__c</span>, <span class="crm-field-pill">Follow_Up_Action_vod__c</span>. The MSL&#x27;s call data is invisible to the commercial field force at the data layer &#8212; system-enforced, not just policy. CLM engagement from MSL sessions tracks scientific slide dwell time and insight notes per slide, feeding Medical Affairs analytics.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #0B5E5E;">
      <div class="crm-obj-name" style="color:#2A9A9A;">Insight_vod__c &#8212; Medical Intelligence Capture</div>
      <div class="crm-obj-api">Free-text KOL feedback captured during MSL CLM sessions &#8212; the medical equivalent of KM reactions</div>
      <div class="crm-obj-desc">Where commercial CLM captures structured key message reactions (1&#8211;5 scale), the medical CLM captures free-text insights via <strong>Insight_vod__c</strong> records. Each insight is linked to the specific Call, the KOL Contact, the product or therapeutic area, and optionally the specific CLM slide where the insight arose. Insight types include: Unmet Medical Need, Competitive Intelligence, Clinical Data Question, Mechanism of Action Query, and Publication Interest. Aggregated across all MSLs, Insight_vod__c data feeds the Medical Affairs strategy dashboard &#8212; identifying which scientific questions are being raised most frequently by which KOL segments, informing publication plans, IIS priorities, and Advisory Board agendas.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #304080;">
      <div class="crm-obj-name" style="color:#6090A8;">Veeva Engage &#8212; Remote CLM Meeting</div>
      <div class="crm-obj-api">Video meeting platform integrated with iRep and MSL iRep &#8212; CLM runs identically in remote sessions</div>
      <div class="crm-obj-desc">Veeva Engage Meeting is a browser-based video conferencing layer built directly into iRep and MSL iRep. When a rep or MSL initiates an Engage session, the HCP receives a link; on joining, the CLM presentation appears simultaneously on both screens, mirrored in real time. The rep controls navigation; the HCP can see every slide but cannot control the deck. All CLM engagement metrics &#8212; slide dwell time, key message reactions, products detailed &#8212; are captured identically to an in-person session. The Call_vod__c record is flagged as <em>Remote_Meeting</em> in the call type field but populates the same analytics pipeline. HCP consent for digital interaction is validated against <strong>Multichannel_Consent_Line_vod__c</strong> before an Engage session can be initiated.</div>
    </div>

    <div class="crm-obj-card" style="border-left:3px solid #304080;">
      <div class="crm-obj-name" style="color:#6090A8;">MedComms Analytics &#8212; Medical Strategy Feedback Loop</div>
      <div class="crm-obj-api">Aggregated medical insight and CLM data informing publication strategy, IIS, and advisory board agendas</div>
      <div class="crm-obj-desc">Medical Communications analytics closes the medical equivalent of the commercial CLM loop. Aggregated Insight_vod__c data, MSL CLM slide engagement, and MIRF pattern analysis (what questions HCPs are asking through medical information) are presented on the Medical Affairs analytics dashboard. If a cluster of MSLs is consistently capturing the insight &#x22;HCPs asking about long-term safety data beyond 2 years,&#x22; the Medical Affairs team receives a quantified signal to prioritise a long-term follow-up study or commission a real-world evidence analysis. This closes the loop from HCP scientific question &#8594; MSL insight capture &#8594; medical strategy &#8594; Vault Medical content update &#8594; updated MSL deck &#8594; next KOL meeting. The medical loop operates on a longer cycle than the commercial CLM loop (months, not weeks) but the data infrastructure is identical.</div>
    </div>

  </div>
"""

VAULT_MED_EXTRA = """
  <h2 id="veeva-med">Vault Medical &#8212; Scientific Content Management</h2>

  <p>Vault Medical is the Medical Affairs division of the Veeva Vault platform &#8212; a separate Vault instance from PromoMats, operating under the same 21 CFR Part 11 validated infrastructure but governed by an entirely different content mandate. Where PromoMats manages promotional materials subject to FDA advertising regulations (21 CFR Part 202), Vault Medical manages non-promotional scientific content: the Standard Response Letters a Medical Information specialist sends to an HCP who asks a clinical question, the scientific exchange decks an MSL presents to a KOL, the IIS (Investigator-Initiated Study) documentation a Medical Affairs team tracks from grant through publication. The separation is not cosmetic &#8212; it is a regulatory firewall. Promotional and medical content cannot share a library, a workflow, or a distribution channel without triggering a compliance violation.</p>

  <p>Vault Medical uses the same document object model as PromoMats &#8212; documents have lifecycle states, workflow tasks, annotations, and audit trails &#8212; but the specific lifecycle states and the roles authorised to move documents through them reflect the medical review process rather than the MLR commercial review process. The review body is the <strong>Medical Review Board (MRB)</strong>, which typically includes a Medical Director, a Regulatory Affairs liaison, and a Legal reviewer. Unlike MLR for promotional content, the MRB does not include a Marketing reviewer &#8212; the moment a marketing voice enters the review of a medical document, the document's non-promotional classification becomes legally vulnerable. System-enforced role separation in Vault Medical prevents this at the permission level.</p>

  <p>The content stored in Vault Medical spans the full lifecycle of Medical Affairs activity: from pre-launch where Medical Information teams build SRL libraries answering anticipated clinical questions, through launch where MSLs need current scientific platform decks updated with the latest trial data, through post-market where Real World Evidence summaries and long-term safety updates must be versioned and distributed to the field. Each update to a scientific document supersedes its predecessor &#8212; the old version is retired in the system but permanently preserved in the audit trail, so the Medical Information team can always demonstrate which version of an SRL was sent to which HCP on which date.</p>

  <h3 id="vmed-doctypes">Document Types in Vault Medical</h3>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Standard Response Letter (SRL)</div>
      <div class="crm-obj-api">Medical Information &#183; Reactive Distribution Only</div>
      <div class="crm-obj-desc">Pre-written, MRB-reviewed answer to a commonly asked medical or clinical question. Organised by product and inquiry category (mechanism of action, dosing, drug interactions, safety, off-label use). Retrieved by Medical Information specialists via the <span class="crm-field-pill">Medical_Inquiry_vod__c.SRL_vod__c</span> lookup when responding to a MIRF. Off-label SRLs exist but may only be sent in documented response to a genuinely unsolicited HCP question &#8212; the system timestamps the unsolicited classification and it cannot be modified post-submission. Every SRL sent is permanently logged against the Medical Inquiry record for audit and aggregate analysis.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">MSL Scientific Platform Deck</div>
      <div class="crm-obj-api">MSL iRep &#183; CLM Scientific Exchange</div>
      <div class="crm-obj-desc">Scientific presentation decks MSLs use during KOL and HCP meetings &#8212; mechanism of action deep-dives, clinical trial data summaries, pipeline compound profiles, unmet medical need context, and real-world evidence. Not subject to 21 CFR Part 202 promotional advertising rules but reviewed by MRB for data accuracy, label alignment, and balance. Stored in Vault Medical; MSLs pull them onto MSL iRep tablets via the content sync. Slide-level engagement (dwell time, notes, insights) is captured in <span class="crm-field-pill">Clm_Presentation_Slide_vod__c</span> and stored against the Call record. Updated as new trial data becomes available &#8212; version supersession ensures MSLs always present current data.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Congress / Symposium Presentation</div>
      <div class="crm-obj-api">Medical Affairs &#183; Scientific Exchange</div>
      <div class="crm-obj-desc">Presentations delivered at medical conferences, advisory boards, and symposia. Congress presentations include poster presentations, oral abstracts, and platform talks. Stored in Vault Medical post-congress for internal reference and as source documents for subsequent MSL scientific exchange. May be cross-referenced in PromoMats claims when congress data supports a promotional message &#8212; the cross-reference link creates an auditable chain from the promotional claim back to its scientific source. Congress presentations are often the first point of entry for new clinical data into the Vault Medical library before formal publication.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">IIS Documentation Package</div>
      <div class="crm-obj-api">Medical Affairs &#183; Investigator-Initiated Studies</div>
      <div class="crm-obj-desc">The complete documentation for an Investigator-Initiated Study grant: the scientific concept review, the grant application, the budget approval, the safety monitoring plan, the interim data reports, and the final publication manuscript. Vault Medical manages the full IIS lifecycle as a Binder &#8212; all documents associated with a single IIS are grouped under one parent Binder record with status tracking through concept review, grant approval, enrolment, data collection, analysis, and publication. The IIS Binder provides Medical Affairs leadership with a complete view of the company&#x27;s externally-funded research portfolio and its output.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Medical Policy Document</div>
      <div class="crm-obj-api">Medical Affairs Governance &#183; Internal Reference</div>
      <div class="crm-obj-desc">Internal Medical Affairs policies governing how MSLs engage with HCPs, how off-label questions are handled, how AE information is collected and reported, and how medical information requests are classified and responded to. Stored in Vault Medical to provide an auditable record of the policies in force at any given time &#8212; critical in litigation where a company must demonstrate that its Medical Affairs team was operating under a documented, compliant framework at the time of a disputed interaction. Policy documents go through MRB review and have the same lifecycle and supersession control as external-facing content.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Real World Evidence (RWE) Summary</div>
      <div class="crm-obj-api">Medical Affairs &#183; Post-Market Science</div>
      <div class="crm-obj-desc">Summaries of real-world evidence studies &#8212; retrospective claims analyses, registry studies, electronic health record analyses &#8212; that characterise product performance in routine clinical practice outside the controlled trial environment. RWE is increasingly central to payer negotiations and formulary decisions. Vault Medical stores both the full study report and a condensed MSL-ready slide deck. MRB review ensures that RWE summaries do not overstate efficacy or understate safety limitations relative to the trial data. Cross-referenced in PromoMats when RWE data supports a promotional claim pending FDA review of expanded labelling.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Pharmacovigilance Safety Communication</div>
      <div class="crm-obj-api">PV / Drug Safety &#183; Regulatory Compliance</div>
      <div class="crm-obj-desc">Safety communications generated when pharmacovigilance surveillance identifies a new signal or when FDA requires a label update, REMS modification, or Dear Healthcare Provider letter. These documents are created by the Drug Safety team, reviewed by Medical Affairs and Regulatory, and stored in Vault Medical. Once issued, a notification workflow alerts MSL field force managers and Medical Information supervisors to update their field teams. The prior version is immediately superseded and retired &#8212; MSLs pulling content from Vault Medical via MSL iRep cannot access a superseded safety communication. AE field force reporting links directly back to these records.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Clinical Study Report Summary (CSRS)</div>
      <div class="crm-obj-api">Medical Affairs &#183; Clinical Data Dissemination</div>
      <div class="crm-obj-desc">Condensed summaries of full Clinical Study Reports prepared for Medical Affairs field use. Full CSRs are regulatory submission documents that can run to thousands of pages; CSRSs are MRB-reviewed distillations that give MSLs a complete but field-usable scientific reference for a specific trial. Each CSRS is linked to the trial it summarises, the indication, the primary and secondary endpoints, and key safety findings. When a KOL asks an MSL a detailed question about trial methodology, the MSL can reference the CSRS. Insights generated from CSRS-related scientific exchange are captured as <span class="crm-field-pill">Insight_vod__c</span> records in CRM and aggregate into the Medical Affairs feedback loop.</div>
    </div>
  </div>

  <h3 id="vmed-lifecycle">Vault Medical Document Lifecycle &#8212; MRB Review Workflow</h3>

  <figure class="vis-embed" aria-label="Vault Medical document lifecycle">
    <div class="vis-label"><span class="vis-icon">◈</span> Vault Medical &#8212; MRB Review Lifecycle &amp; Document States</div>
    <div class="vis-inner">
      <svg viewBox="0 0 900 310" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vault Medical MRB lifecycle diagram">
        <defs>
          <marker id="vmA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#2A9A9A"/></marker>
          <marker id="vmR" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#C0392B"/></marker>
          <marker id="vmG" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#27AE60"/></marker>
        </defs>
        <rect width="900" height="310" fill="#F0F7F7" rx="10"/>

        <!-- Title -->
        <text x="450" y="24" text-anchor="middle" fill="#0D3535" font-size="13" font-weight="700" font-family="sans-serif">Vault Medical &#8212; MRB Document Lifecycle</text>

        <!-- State boxes -->
        <!-- Draft -->
        <rect x="20" y="50" width="100" height="44" rx="6" fill="#E8F4F4" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="70" y="68" text-anchor="middle" fill="#0D3535" font-size="10" font-weight="700" font-family="sans-serif">Draft</text>
        <text x="70" y="82" text-anchor="middle" fill="#5A7A7A" font-size="8" font-family="sans-serif">Medical Writer</text>

        <!-- Medical Writing Review -->
        <rect x="160" y="50" width="120" height="44" rx="6" fill="#D8EEEE" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="220" y="68" text-anchor="middle" fill="#0D3535" font-size="10" font-weight="700" font-family="sans-serif">Medical Writing</text>
        <text x="220" y="82" text-anchor="middle" fill="#5A7A7A" font-size="8" font-family="sans-serif">Internal QC Review</text>

        <!-- Medical Review -->
        <rect x="330" y="50" width="120" height="44" rx="6" fill="#C0E0E0" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="390" y="68" text-anchor="middle" fill="#0D3535" font-size="10" font-weight="700" font-family="sans-serif">Medical Review</text>
        <text x="390" y="82" text-anchor="middle" fill="#5A7A7A" font-size="8" font-family="sans-serif">Medical Director</text>

        <!-- Legal / Regulatory -->
        <rect x="500" y="50" width="120" height="44" rx="6" fill="#A8D4D4" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="560" y="68" text-anchor="middle" fill="#0D3535" font-size="10" font-weight="700" font-family="sans-serif">Legal / Reg Review</text>
        <text x="560" y="82" text-anchor="middle" fill="#5A7A7A" font-size="8" font-family="sans-serif">Compliance Gate</text>

        <!-- Scientific Approval -->
        <rect x="670" y="50" width="120" height="44" rx="6" fill="#80BCBC" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="730" y="68" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" font-family="sans-serif">Scientific Approval</text>
        <text x="730" y="82" text-anchor="middle" fill="#E0F4F4" font-size="8" font-family="sans-serif">MRB Sign-Off</text>

        <!-- Active -->
        <rect x="790" y="130" width="90" height="44" rx="6" fill="#2A9A9A" stroke="#1A6A6A" stroke-width="1.5"/>
        <text x="835" y="148" text-anchor="middle" fill="#fff" font-size="10" font-weight="700" font-family="sans-serif">Active</text>
        <text x="835" y="162" text-anchor="middle" fill="#D0F0F0" font-size="8" font-family="sans-serif">Field Available</text>

        <!-- Superseded -->
        <rect x="670" y="220" width="120" height="44" rx="6" fill="#F5EBE0" stroke="#C09060" stroke-width="1.5"/>
        <text x="730" y="238" text-anchor="middle" fill="#8B5E30" font-size="10" font-weight="700" font-family="sans-serif">Superseded</text>
        <text x="730" y="252" text-anchor="middle" fill="#9A7050" font-size="8" font-family="sans-serif">Replaced by new version</text>

        <!-- Retired -->
        <rect x="500" y="220" width="120" height="44" rx="6" fill="#ECDEDE" stroke="#C03030" stroke-width="1.5"/>
        <text x="560" y="238" text-anchor="middle" fill="#7A2020" font-size="10" font-weight="700" font-family="sans-serif">Retired</text>
        <text x="560" y="252" text-anchor="middle" fill="#9A4040" font-size="8" font-family="sans-serif">Permanently withdrawn</text>

        <!-- Rejected -->
        <rect x="330" y="220" width="120" height="44" rx="6" fill="#F0E0E0" stroke="#C05050" stroke-width="1.5"/>
        <text x="390" y="238" text-anchor="middle" fill="#7A3030" font-size="10" font-weight="700" font-family="sans-serif">Rejected</text>
        <text x="390" y="252" text-anchor="middle" fill="#9A5050" font-size="8" font-family="sans-serif">Returns to Draft</text>

        <!-- AE Check branch -->
        <rect x="160" y="150" width="120" height="44" rx="6" fill="#FFF3E0" stroke="#E08030" stroke-width="1.5" stroke-dasharray="5,3"/>
        <text x="220" y="168" text-anchor="middle" fill="#7A4010" font-size="10" font-weight="700" font-family="sans-serif">AE / PV Check</text>
        <text x="220" y="182" text-anchor="middle" fill="#9A6030" font-size="8" font-family="sans-serif">Parallel safety screen</text>

        <!-- Forward arrows -->
        <line x1="120" y1="72" x2="158" y2="72" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>
        <line x1="280" y1="72" x2="328" y2="72" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>
        <line x1="450" y1="72" x2="498" y2="72" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>
        <line x1="620" y1="72" x2="668" y2="72" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>

        <!-- Approval to Active -->
        <line x1="790" y1="72" x2="835" y2="72" stroke="#2A9A9A" stroke-width="1.5"/>
        <line x1="835" y1="72" x2="835" y2="128" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>

        <!-- Active to Superseded -->
        <line x1="835" y1="174" x2="835" y2="242" stroke="#C09060" stroke-width="1.5"/>
        <line x1="835" y1="242" x2="792" y2="242" stroke="#C09060" stroke-width="1.5" marker-end="url(#vmA)"/>

        <!-- Active to Retired -->
        <line x1="790" y1="155" x2="625" y2="242" stroke="#C03030" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmR)"/>

        <!-- Medical Review reject down -->
        <line x1="390" y1="94" x2="390" y2="218" stroke="#C05050" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#vmR)"/>

        <!-- Legal reject down -->
        <line x1="560" y1="94" x2="560" y2="218" stroke="#C03030" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#vmR)"/>

        <!-- AE check branch from Medical Writing -->
        <line x1="220" y1="94" x2="220" y2="148" stroke="#E08030" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmA)"/>

        <!-- Step labels -->
        <text x="139" y="66" text-anchor="middle" fill="#2A9A9A" font-size="7.5" font-family="sans-serif">submit</text>
        <text x="304" y="66" text-anchor="middle" fill="#2A9A9A" font-size="7.5" font-family="sans-serif">QC pass</text>
        <text x="474" y="66" text-anchor="middle" fill="#2A9A9A" font-size="7.5" font-family="sans-serif">MD approve</text>
        <text x="644" y="66" text-anchor="middle" fill="#2A9A9A" font-size="7.5" font-family="sans-serif">legal clear</text>
        <text x="224" y="128" text-anchor="start" fill="#E08030" font-size="7.5" font-family="sans-serif">parallel</text>

        <!-- Legend -->
        <line x1="30" y1="290" x2="55" y2="290" stroke="#2A9A9A" stroke-width="1.5" marker-end="url(#vmA)"/>
        <text x="60" y="294" fill="#5A7A7A" font-size="8" font-family="sans-serif">Approval path</text>
        <line x1="160" y1="290" x2="185" y2="290" stroke="#C03030" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#vmR)"/>
        <text x="190" y="294" fill="#5A7A7A" font-size="8" font-family="sans-serif">Rejection / withdrawal</text>
        <line x1="340" y1="290" x2="365" y2="290" stroke="#E08030" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmA)"/>
        <text x="370" y="294" fill="#5A7A7A" font-size="8" font-family="sans-serif">Parallel AE/PV screen</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Vault Medical MRB lifecycle &#8212; documents progress from Draft through Medical Writing QC, Medical Director review, Legal/Regulatory gate, and full MRB sign-off before reaching Active status; a parallel AE/PV safety screen runs throughout; supersession preserves version history while ensuring only current documents reach the field</figcaption>
  </figure>

  <h3 id="vmed-objects">Vault Medical Object Model</h3>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Document</div>
      <div class="crm-obj-api">Core Vault Object &#183; Versioned &#183; 21 CFR Part 11</div>
      <div class="crm-obj-desc">The fundamental unit in Vault Medical. Every SRL, MSL deck, policy, CSRS, and safety communication is a Document object. Key fields: <span class="crm-field-pill">document_type__v</span> (SRL, Scientific Deck, Policy, etc.), <span class="crm-field-pill">product__v</span>, <span class="crm-field-pill">indication__v</span>, <span class="crm-field-pill">lifecycle_state__v</span>, <span class="crm-field-pill">version_label__v</span>, <span class="crm-field-pill">major_version_number__v</span>, <span class="crm-field-pill">minor_version_number__v</span>, <span class="crm-field-pill">created_by__v</span>, and a complete, immutable audit trail. Major version changes (e.g., 1.0 &#8594; 2.0) are triggered by substantive scientific updates; minor versions (e.g., 1.0 &#8594; 1.1) for formatting or non-substantive corrections. Each version transition is timestamped and user-attributed for regulatory audit.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Binder</div>
      <div class="crm-obj-api">Document Grouping &#183; IIS / Safety Packages</div>
      <div class="crm-obj-desc">A Binder is a structured container that groups related Documents into a single auditable package. Used for IIS documentation (all documents for a single study under one Binder), safety communication packages (label change + Dear HCP letter + internal briefing in one Binder), and congress presentation packages (abstract + poster + slide deck). Binders have their own lifecycle and can be submitted as a package through MRB review. A Binder&#x27;s status reflects the lowest-state document within it &#8212; the whole package cannot reach Active until every component document has been approved.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Workflow Task</div>
      <div class="crm-obj-api">MRB Review Routing &#183; Task Assignment</div>
      <div class="crm-obj-desc">Represents a single step in the MRB review workflow: a Medical Director review task, a Legal review task, a final MRB sign-off task. Each Workflow Task is assigned to a specific user or role, has a due date, and requires a discrete action (approve, reject, send back). The task queue is the primary interface for MRB members &#8212; they log in to Vault Medical and see all documents awaiting their review. Key fields: <span class="crm-field-pill">assigned_to__v</span>, <span class="crm-field-pill">due_date__v</span>, <span class="crm-field-pill">verdict__v</span> (Approve / Reject / Abstain), <span class="crm-field-pill">verdict_reason__v</span>. All task completions are permanently recorded &#8212; if a document is later challenged, the company can show exactly who reviewed it and when.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Annotation</div>
      <div class="crm-obj-api">Reviewer Comments &#183; In-Document Markup</div>
      <div class="crm-obj-desc">Inline comments and mark-ups attached to specific locations within a document during MRB review. A Medical Director may annotate a specific claim in an SRL flagging insufficient citation support; a Legal reviewer may annotate a paragraph in a policy document requesting stricter language. Annotations are threaded &#8212; the author can respond, and the exchange is preserved in full. Annotations must be resolved (accepted or rejected with a documented reason) before a document can advance past the review state. This creates a complete record of every substantive scientific or legal concern raised during the review and how it was addressed.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Document Token / Distribution Record</div>
      <div class="crm-obj-api">Controlled Distribution &#183; Access Audit</div>
      <div class="crm-obj-desc">When an Active document is distributed &#8212; for example, when an SRL is sent to an HCP via Medical Information, or when a scientific deck is published to the MSL iRep content library &#8212; Vault Medical generates a Distribution Record linking the document version, the recipient, the distribution channel, and the timestamp. This creates an unambiguous audit trail: if a regulatory inquiry asks which version of a specific SRL was in circulation on a given date, the Distribution Record provides the answer. MSL iRep content sync events generate Distribution Records automatically when a document is pushed to a tablet.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Claims &amp; References (Scientific)</div>
      <div class="crm-obj-api">Evidence Traceability &#183; Data Accuracy</div>
      <div class="crm-obj-desc">Medical claims within Vault Medical documents &#8212; efficacy statements, safety characterisations, mechanism of action descriptions &#8212; are linked to their source references: clinical study reports, published journal articles, regulatory submission data. Unlike PromoMats claims (which link to approved promotional language), Vault Medical claims link to primary scientific sources. Each claim-to-reference link is created during Medical Writing and validated during MRB review. If a reference is superseded by new data (e.g., a more recent trial has different results), a cascade flag alerts the Medical Affairs team that all documents containing that reference require re-review. This prevents outdated science from persisting in active SRLs.</div>
    </div>
  </div>

  <h3 id="vmed-integration">Vault Medical Integrations</h3>

  <p>Vault Medical sits at the centre of a data exchange network spanning field execution (MSL iRep), Medical Information (MIRF response workflow), safety reporting (Pharmacovigilance), commercial content (PromoMats cross-reference), and analytics (Medical Affairs KPIs). The integrations are purpose-specific and permission-bounded: MSL iRep can pull from the scientific content library but cannot modify documents; Medical Information specialists can retrieve SRLs and log their use but cannot create or edit them; the safety system receives AE-linked document triggers but cannot alter document lifecycle states. This layered access architecture keeps the MRB review process tamper-proof while enabling field teams to access current scientific content efficiently.</p>

  <p>The most operationally critical integration is with the Veeva CRM MSL iRep module. When an MSL launches their tablet, a scheduled content sync checks Vault Medical for any new or updated scientific documents in their assigned therapeutic area. If a new version of the product&#x27;s scientific platform deck was approved overnight, it is pushed to the MSL&#x27;s tablet before their first meeting &#8212; the old version is simultaneously retired from the local cache, making it inaccessible. This ensures the entire MSL field force is presenting current data within 24 hours of a content update. The sync event is logged as a Distribution Record in Vault Medical, so the Medical Affairs team can confirm that every active MSL received the updated content before a particular conference or key data presentation.</p>

  <figure class="vis-embed" aria-label="Vault Medical integration map">
    <div class="vis-label"><span class="vis-icon">◈</span> Vault Medical &#8212; System Integration Map</div>
    <div class="vis-inner">
      <svg viewBox="0 0 900 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Vault Medical integration diagram">
        <defs>
          <marker id="vmiA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#2A9A9A"/></marker>
          <marker id="vmiB" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#8B5E30"/></marker>
          <marker id="vmiC" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#C03030"/></marker>
          <marker id="vmiD" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#4060A0"/></marker>
          <marker id="vmiAL" markerWidth="7" markerHeight="5" refX="0" refY="2.5" orient="auto"><polygon points="7 0,0 2.5,7 5" fill="#2A9A9A"/></marker>
        </defs>
        <rect width="900" height="420" fill="#F0F7F7" rx="10"/>

        <!-- Title -->
        <text x="450" y="24" text-anchor="middle" fill="#0D3535" font-size="13" font-weight="700" font-family="sans-serif">Vault Medical &#8212; Integration Map</text>

        <!-- Central: Vault Medical -->
        <rect x="330" y="160" width="240" height="80" rx="10" fill="#2A9A9A" stroke="#1A6A6A" stroke-width="2"/>
        <text x="450" y="192" text-anchor="middle" fill="#fff" font-size="14" font-weight="700" font-family="sans-serif">Vault Medical</text>
        <text x="450" y="210" text-anchor="middle" fill="#C0ECEC" font-size="9.5" font-family="sans-serif">Scientific Content Repository</text>
        <text x="450" y="224" text-anchor="middle" fill="#C0ECEC" font-size="8.5" font-family="sans-serif">SRLs &#183; MSL Decks &#183; Policies &#183; IIS &#183; RWE &#183; Safety Comms</text>

        <!-- MSL iRep / CRM (top-left) -->
        <rect x="40" y="40" width="180" height="72" rx="8" fill="#E8F4F4" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="130" y="64" text-anchor="middle" fill="#0D3535" font-size="11" font-weight="700" font-family="sans-serif">MSL iRep / Veeva CRM</text>
        <text x="130" y="80" text-anchor="middle" fill="#5A7A7A" font-size="8.5" font-family="sans-serif">Content sync to tablet</text>
        <text x="130" y="93" text-anchor="middle" fill="#5A7A7A" font-size="8.5" font-family="sans-serif">CLM scientific engagement</text>

        <!-- Medical Information / MIRF (top-right) -->
        <rect x="680" y="40" width="180" height="72" rx="8" fill="#E8F4F4" stroke="#2A9A9A" stroke-width="1.5"/>
        <text x="770" y="64" text-anchor="middle" fill="#0D3535" font-size="11" font-weight="700" font-family="sans-serif">Medical Information</text>
        <text x="770" y="80" text-anchor="middle" fill="#5A7A7A" font-size="8.5" font-family="sans-serif">SRL retrieval for MIRF</text>
        <text x="770" y="93" text-anchor="middle" fill="#5A7A7A" font-size="8.5" font-family="sans-serif">Response audit logging</text>

        <!-- Vault PromoMats (bottom-left) -->
        <rect x="40" y="310" width="180" height="72" rx="8" fill="#EEF0F8" stroke="#4060A0" stroke-width="1.5"/>
        <text x="130" y="334" text-anchor="middle" fill="#1A2060" font-size="11" font-weight="700" font-family="sans-serif">Vault PromoMats</text>
        <text x="130" y="350" text-anchor="middle" fill="#5A5A8A" font-size="8.5" font-family="sans-serif">Cross-reference to promo claims</text>
        <text x="130" y="363" text-anchor="middle" fill="#5A5A8A" font-size="8.5" font-family="sans-serif">Scientific source audit chain</text>

        <!-- Pharmacovigilance (bottom-right) -->
        <rect x="680" y="310" width="180" height="72" rx="8" fill="#FDECEA" stroke="#C03030" stroke-width="1.5"/>
        <text x="770" y="334" text-anchor="middle" fill="#7A0000" font-size="11" font-weight="700" font-family="sans-serif">Pharmacovigilance</text>
        <text x="770" y="350" text-anchor="middle" fill="#9A3030" font-size="8.5" font-family="sans-serif">AE signal &#8594; safety comms</text>
        <text x="770" y="363" text-anchor="middle" fill="#9A3030" font-size="8.5" font-family="sans-serif">REMS / label update trigger</text>

        <!-- Medical Analytics (bottom-center) -->
        <rect x="330" y="330" width="240" height="60" rx="8" fill="#F0F4E8" stroke="#608030" stroke-width="1.5"/>
        <text x="450" y="355" text-anchor="middle" fill="#303A10" font-size="11" font-weight="700" font-family="sans-serif">Medical Analytics</text>
        <text x="450" y="371" text-anchor="middle" fill="#6A7A40" font-size="8.5" font-family="sans-serif">Insight aggregation &#8594; content gap &#8594; Vault Medical update</text>

        <!-- Arrows: MSL iRep ↔ Vault Medical -->
        <!-- content push to MSL -->
        <line x1="220" y1="76" x2="328" y2="176" stroke="#2A9A9A" stroke-width="1.8" marker-end="url(#vmiA)"/>
        <!-- engagement data back -->
        <line x1="330" y1="190" x2="222" y2="90" stroke="#2A9A9A" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmiA)"/>
        <text x="240" y="120" fill="#2A9A9A" font-size="8" font-family="sans-serif" transform="rotate(-35,240,120)">content sync</text>
        <text x="310" y="148" fill="#2A9A9A" font-size="8" font-family="sans-serif" transform="rotate(-35,310,148)">call data</text>

        <!-- Arrows: Vault Medical ↔ Medical Information -->
        <!-- SRL retrieval -->
        <line x1="570" y1="176" x2="678" y2="90" stroke="#2A9A9A" stroke-width="1.8" marker-end="url(#vmiA)"/>
        <!-- response logged -->
        <line x1="680" y1="76" x2="572" y2="190" stroke="#2A9A9A" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmiA)"/>
        <text x="596" y="118" fill="#2A9A9A" font-size="8" font-family="sans-serif" transform="rotate(35,596,118)">SRL pull</text>
        <text x="648" y="150" fill="#2A9A9A" font-size="8" font-family="sans-serif" transform="rotate(35,648,150)">log sent</text>

        <!-- Arrows: Vault Medical ↔ PromoMats -->
        <line x1="330" y1="216" x2="222" y2="312" stroke="#4060A0" stroke-width="1.5" stroke-dasharray="6,3" marker-end="url(#vmiD)"/>
        <line x1="220" y1="310" x2="328" y2="218" stroke="#4060A0" stroke-width="1.2" stroke-dasharray="4,3" marker-end="url(#vmiD)"/>
        <text x="240" y="278" fill="#4060A0" font-size="8" font-family="sans-serif" transform="rotate(45,240,278)">cross-ref</text>

        <!-- Arrows: Vault Medical ↔ Pharmacovigilance -->
        <line x1="570" y1="216" x2="678" y2="312" stroke="#C03030" stroke-width="1.5" marker-end="url(#vmiC)"/>
        <line x1="680" y1="310" x2="572" y2="218" stroke="#C03030" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#vmiC)"/>
        <text x="608" y="254" fill="#C03030" font-size="8" font-family="sans-serif" transform="rotate(-45,608,254)">AE flag</text>
        <text x="644" y="276" fill="#C03030" font-size="8" font-family="sans-serif" transform="rotate(-45,644,276)">safety doc</text>

        <!-- Arrows: Medical Analytics ↔ Vault Medical (feedback loop) -->
        <line x1="450" y1="330" x2="450" y2="242" stroke="#608030" stroke-width="1.5" stroke-dasharray="6,3" marker-end="url(#vmiA)"/>
        <text x="455" y="294" fill="#608030" font-size="8" font-family="sans-serif">insight &#8594; content update</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Vault Medical integration map &#8212; MSL iRep receives content syncs and returns call engagement data; Medical Information retrieves SRLs and logs responses; Vault PromoMats cross-references scientific sources for promotional claims; Pharmacovigilance triggers safety document creation and receives AE signals; Medical Analytics feeds KOL insights back to drive content updates</figcaption>
  </figure>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">MSL iRep &#8596; Vault Medical</div>
      <div class="crm-obj-api">Bi-directional &#183; Content Out, Engagement In</div>
      <div class="crm-obj-desc">Vault Medical pushes Active scientific content to MSL tablets via a scheduled sync integrated with Veeva CRM. When a new version of an MSL deck is approved in Vault Medical, it is automatically distributed to the MSL content library overnight &#8212; previous versions are retired from the tablet cache simultaneously. MSL engagement data flows back: <span class="crm-field-pill">Clm_Presentation_Slide_vod__c</span> records capturing dwell time and <span class="crm-field-pill">Insight_vod__c</span> records capturing scientific exchange notes are aggregated in Medical Analytics. The insight signal &#8212; which slides generate the most KOL questions, which scientific gaps are most frequently surfaced &#8212; informs the Medical Writing team when to initiate a document update cycle in Vault Medical. This is the Medical Affairs equivalent of the commercial CLM feedback loop.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Medical Information &#8596; Vault Medical</div>
      <div class="crm-obj-api">SRL Retrieval &#183; MIRF Response Audit</div>
      <div class="crm-obj-desc">When a Medical Information specialist responds to a MIRF (Medical Information Request Form), their primary tool is Vault Medical&#x27;s SRL library. The specialist searches by product and inquiry category, retrieves the current Active version of the appropriate SRL, and attaches it to the response. The <span class="crm-field-pill">Medical_Inquiry_vod__c.SRL_vod__c</span> lookup field records exactly which SRL version was sent to which HCP on which date. For off-label inquiries, the unsolicited flag is set, timestamped, and locked before the SRL is retrieved &#8212; the system enforces the sequencing to prevent retroactive unsolicited classification. Aggregate MIRF data (which SRLs are requested most, which clinical questions have no existing SRL) drives Medical Information&#x27;s annual SRL library review.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4060A0;">Vault PromoMats &#8596; Vault Medical</div>
      <div class="crm-obj-api">Cross-Reference &#183; Scientific Source Chain</div>
      <div class="crm-obj-desc">When commercial MLR reviewers in Vault PromoMats need to substantiate a promotional claim with scientific data &#8212; for example, a promotional piece states a specific efficacy number from a clinical trial &#8212; the claim is cross-referenced to the source document in Vault Medical (typically a CSRS or congress presentation). The cross-reference link creates an auditable chain from the promotional claim back through the approved scientific content. If the source document in Vault Medical is later superseded or retired (because new data changes the interpretation), PromoMats is notified and the affected promotional pieces are flagged for review. This prevents stale science from being cited in active promotional materials without detection.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#C03030;">Pharmacovigilance &#8596; Vault Medical</div>
      <div class="crm-obj-api">AE Signal &#8594; Safety Document &#183; Regulatory Compliance</div>
      <div class="crm-obj-desc">When the Pharmacovigilance system identifies a new safety signal &#8212; a cluster of adverse events, a serious unlabelled adverse reaction, or an FDA safety query &#8212; it triggers a workflow in Vault Medical to initiate a safety communication document. The Drug Safety team authors the communication, the MRB fast-tracks review under a compressed timeline (often 24&#8211;48 hours for urgent signals), and upon approval the Distribution workflow immediately notifies all MSL managers and Medical Information supervisors. Simultaneously, the existing product labelling document in Vault Medical is flagged pending a label revision workflow. AE-linked MIRF records in CRM are also flagged to ensure the Medical Information team applies the updated information to any ongoing or future HCP communications about the affected product.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#608030;">Medical Analytics &#8596; Vault Medical</div>
      <div class="crm-obj-api">Insight Aggregation &#183; Content Gap Analysis &#183; Update Triggers</div>
      <div class="crm-obj-desc">Medical Analytics aggregates <span class="crm-field-pill">Insight_vod__c</span> data from all MSL call reports, MIRF pattern data from Medical Information, and MSL CLM engagement metrics. The output is a content gap analysis: which scientific questions KOLs are asking most (via Insight_vod__c aggregation), which MIRF inquiry categories have the highest volume or unanswered rate (from Medical Information data), and which MSL deck slides have unusually low engagement (suggesting the data is not landing). This analysis is the primary input to the Medical Affairs content calendar &#8212; it identifies when existing SRLs need updating, when a new scientific topic needs a dedicated deck, and when a CSRS needs to be commissioned for a recently published study. The cycle from KOL insight to updated Vault Medical content is the Medical Affairs equivalent of the commercial CLM closed loop.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Veeva Network &#8596; Vault Medical</div>
      <div class="crm-obj-api">HCP Identity &#183; KOL Tier &#183; Speciality Targeting</div>
      <div class="crm-obj-desc">Vault Medical uses Veeva Network&#x27;s HCP master data to ensure scientific content is targeted to the right specialties and HCP tiers. Scientific deck variants &#8212; a highly detailed mechanistic deck for KOL-tier academic physicians vs. a clinical practice deck for community specialists &#8212; are tagged with target HCP speciality and KOL tier metadata derived from Network. When an MSL&#x27;s content library is synced, Vault Medical filters the available documents based on the MSL&#x27;s assigned territory HCP profiles from Network. This prevents an MSL specialising in community rheumatology from accidentally presenting a Phase III academic KOL deck at an inappropriate level of scientific detail for the audience, maintaining the integrity of scientific exchange.</div>
    </div>
  </div>
"""

FDA_REGS_EXTRA = """
    <dt id="g-cfr">Key FDA Regulations Summary</dt>
    <dd>
      <p style="margin:0 0 16px 0; color:#374151; line-height:1.6;">Pharmaceutical commercial and medical affairs operations sit at the intersection of more than a dozen federal regulatory frameworks. The table below provides a working reference: what each regulation covers, its core requirements, its enforcement mechanism, and its operational impact on field teams and Veeva systems. Regulations are grouped by function &#8212; compliance failures in any category can trigger criminal liability, product recall, or exclusion from federal healthcare programs.</p>

      <p style="font-weight:700; color:#1B3A6B; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #1B3A6B; padding-bottom:4px;">&#9670; Data Integrity &amp; System Validation</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#1B3A6B;">21 CFR Part 11 &#8212; Electronic Records &amp; Electronic Signatures</div>
          <div class="crm-obj-api">Scope: Any FDA-regulated computer system creating, modifying, maintaining, archiving, retrieving, or transmitting electronic records that substitute for paper records or handwritten signatures</div>
          <div class="crm-obj-desc"><strong>Core requirements:</strong> (1) System validation &#8212; documented evidence the system consistently produces results meeting specifications; (2) Audit trails &#8212; automatically generated, computer-generated, date/time-stamped records of operator entries and actions, not editable or deletable by any user; (3) Unique user credentials &#8212; no shared logins; each action attributed to a specific individual; (4) Electronic signature binding &#8212; each e-signature linked to the record with full name, date/time, and the meaning of the signature (e.g., "Approved," "Reviewed"); (5) Logical access controls preventing unauthorised creation, alteration, or deletion of records. <strong>Veeva relevance:</strong> Vault PromoMats, Vault Medical, Veeva CRM, and Veeva Network are all deployed as 21 CFR Part 11 validated systems. Every MLR approval action, document lifecycle state change, SRL distribution, sample signature, and Call Report submission is an electronic record with an immutable audit trail. <strong>Enforcement consequence:</strong> An FDA inspection finding Part 11 deficiencies in a system used to generate NDA/BLA submission data can result in FDA refusing to accept or consider that data &#8212; invalidating years of clinical development work.</div>
        </div>
      </div>

      <p style="font-weight:700; color:#27674D; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #27674D; padding-bottom:4px;">&#9670; GxP Frameworks &#8212; Good Practice Standards</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#27674D;">21 CFR Part 58 &#8212; Good Laboratory Practice (GLP)</div>
          <div class="crm-obj-api">Scope: Non-clinical laboratory safety studies conducted to support an IND or NDA/BLA submission &#8212; toxicology, pharmacokinetics, genotoxicity, reproductive toxicity, carcinogenicity</div>
          <div class="crm-obj-desc"><strong>What it does NOT cover:</strong> basic exploratory/discovery research, clinical trials (governed by ICH E6), or manufacturing (Parts 210/211). <strong>Core requirements:</strong> A qualified Study Director with single-point accountability for each study; a Quality Assurance Unit independent of study conduct that inspects facilities, audits study conduct, and reviews final reports; written SOPs for every procedure; characterisation and chain of custody for all test articles and control articles; raw data archived for the life of the product in sponsor&#x27;s possession; facility inspections-ready at any time. <strong>Consequence of failure:</strong> FDA can issue a Finding of Disqualification for a non-clinical testing facility, causing all studies from that lab to be inadmissible in any future FDA submission &#8212; even if the studies were scientifically sound. GLP failures are among the most irreversible regulatory setbacks a development programme can encounter.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#27674D;">21 CFR Parts 210 &amp; 211 &#8212; Current Good Manufacturing Practice (cGMP)</div>
          <div class="crm-obj-api">Scope: Finished pharmaceutical manufacturing &#8212; Part 210 (definitional); Part 211 (organisation, buildings, equipment, production, process controls, laboratory controls, records, returned/salvaged drugs)</div>
          <div class="crm-obj-desc"><strong>Key requirements:</strong> Master Batch Record (MBR) specifying every manufacturing step for each product/lot size; individual Batch Production Record (BPR) completed in real time for each manufactured lot &#8212; any deviation from the MBR must be documented and investigated; in-process controls with defined acceptance criteria; out-of-specification (OOS) investigation procedure with root cause analysis; stability testing programme establishing shelf-life expiry; Annual Product Review (APR) evaluating all batches, complaints, and deviations; Change Control requiring documented risk assessment and validation before any change to process, equipment, or facility. <strong>Enforcement:</strong> FDA Form 483 (inspectional observations) &#8594; Warning Letter &#8594; Consent Decree &#8594; Import Alert (banning product entry to US). cGMP failures are the primary cause of drug recalls. A Warning Letter citing cGMP deficiencies halts approval of any pending NDA/sNDA for that facility until remediation is complete and verified.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#27674D;">ICH E6 (R2) &#8212; Good Clinical Practice (GCP)</div>
          <div class="crm-obj-api">Scope: Design, conduct, performance, monitoring, auditing, recording, analysis, and reporting of clinical trials that generate data submitted to FDA, EMA, or PMDA &#8212; an international standard (not a US CFR), but FDA enforces it via 21 CFR Parts 312 and 314</div>
          <div class="crm-obj-desc"><strong>Core requirements:</strong> IRB/Ethics Committee approval and ongoing oversight for all study sites; Informed Consent documenting subject understanding of risks and voluntary participation; qualified Principal Investigator (PI) with signed Investigator Agreement; Sponsor responsibilities including site selection, monitoring visits, and audit programme; Trial Master File (TMF) containing all essential documents required to evaluate conduct and data quality; expedited reporting of Serious Unexpected Suspected Adverse Reactions (SUSARs) &#8212; fatal/life-threatening within 7 days, all others within 15 days &#8212; to FDA and all active investigators; final Clinical Study Report (CTD Module 5) meeting ICH E3 format. <strong>Relevance to Medical Affairs:</strong> GCP-compliant clinical data is the scientific foundation for MSL scientific exchange &#8212; if the trials supporting the product were not conducted to GCP, the data cannot be included in the label or discussed in scientific exchange without misrepresentation risk.</div>
        </div>
      </div>

      <p style="font-weight:700; color:#8B4513; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #8B4513; padding-bottom:4px;">&#9670; Drug &amp; Biologics Approval Pathways</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#8B4513;">21 CFR Part 314 &#8212; New Drug Applications (NDA)</div>
          <div class="crm-obj-api">Scope: Approval of new chemical entities (NCEs) and new formulations/dosage forms of existing molecules for human use in the United States</div>
          <div class="crm-obj-desc"><strong>Submission pathways:</strong> &#167;505(b)(1) &#8212; full NDA with all sponsor-generated safety and efficacy data; &#167;505(b)(2) &#8212; hybrid NDA relying in part on published literature or prior FDA findings for a referenced drug (used for reformulations, new delivery systems, new indications of existing molecules &#8212; accelerates development by avoiding fully redundant studies); &#167;505(j) &#8212; ANDA (Abbreviated NDA) for generics, requiring bioequivalence demonstration only. <strong>PDUFA review timelines:</strong> Standard Review &#8212; 12-month FDA review goal (10 months from filing date); Priority Review &#8212; 6 months (for drugs offering significant improvement over available therapy). <strong>Market exclusivity:</strong> 5-year NCE exclusivity (new chemical entity, no generics during period); 3-year exclusivity for new clinical investigations; Orphan Drug 7-year exclusivity + tax credits; paediatric 6-month add-on to any exclusivity. <strong>&#167;314.81 post-approval reports:</strong> Annual progress reports due within 60 days of anniversary of approval; Field Alert Reports (FARs) within 3 business days if distributed product found contaminated, misbranded, or below shelf-life specification.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#8B4513;">21 CFR Part 601 &#8212; Biologics License Applications (BLA) &amp; Biosimilars</div>
          <div class="crm-obj-api">Scope: Vaccines, blood products, cellular and gene therapies, monoclonal antibodies, fusion proteins, therapeutic enzymes &#8212; biological products licensed under the Public Health Service Act &#167;351</div>
          <div class="crm-obj-desc"><strong>Original BLA (&#167;351(a)):</strong> Requires full safety, purity, and potency data. Critically, the manufacturing facility is integral to the BLA &#8212; the licence is granted to a specific facility, not just a molecule. A manufacturing site change requires a Prior Approval Supplement, not merely notification. <strong>Biosimilar pathway (&#167;351(k), created by BPCIA 2009):</strong> Applicant must demonstrate no clinically meaningful differences in safety, purity, and potency compared to the FDA-licensed reference product. Comparative analytical studies, PK/PD studies, and at least one clinical immunogenicity study required. Reference product exclusivity: 12 years from original approval (vs. 5 years for small molecules) &#8212; biosimilar application cannot be approved within this window. <strong>Interchangeability:</strong> A biosimilar may be designated interchangeable (can be substituted by pharmacist without prescriber intervention) if it produces the same clinical result in any given patient &#8212; a significantly higher evidentiary bar than biosimilarity alone. <strong>Key difference from generics:</strong> Biologics cannot be true generics because their molecular complexity makes exact replication impossible &#8212; only biosimilarity can be demonstrated.</div>
        </div>
      </div>

      <p style="font-weight:700; color:#B03060; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #B03060; padding-bottom:4px;">&#9670; Post-Market Safety Obligations</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#B03060;">21 CFR &#167;314.81 &#8212; Post-Marketing Safety Reporting</div>
          <div class="crm-obj-api">Scope: All NDA/sNDA holders; parallel provisions at 21 CFR &#167;600.80 for BLA holders and 21 CFR &#167;312.32 for IND holders during clinical development</div>
          <div class="crm-obj-desc"><strong>15-day expedited reports:</strong> Any serious and unexpected adverse drug experience (ADE) with a reasonable possibility of causal association must be reported to FDA within 15 calendar days of the company&#x27;s first receipt. "Serious" means death, life-threatening, hospitalisation, disability, congenital anomaly, or requires medical intervention to prevent these outcomes. "Unexpected" means not in the current labelling &#8212; even if the event type is known, a new severity, frequency, or population makes it unexpected. <strong>Periodic Adverse Drug Experience Reports (PADER):</strong> Quarterly for the first 3 years post-approval; annually thereafter. Must include all ADE reports received, signal detection analysis, literature review, and cumulative safety data. <strong>Field Alert Reports (FAR):</strong> Within 3 business days of receiving information about distributed product with bacteriological contamination, significant chemical or physical breakdown, labelling mix-up, or marked deterioration before the expiry date. <strong>Annual reports:</strong> Full product status update &#8212; labelling changes, distribution data, nonclinical studies completed, ongoing clinical studies, pharmacoepidemiology studies. Failure to submit 15-day reports is one of the most frequently cited FDA Warning Letter findings.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#B03060;">REMS &#8212; Risk Evaluation &amp; Mitigation Strategy (FDAAA 2007)</div>
          <div class="crm-obj-api">Scope: FDA may require as a condition of approval (or post-approval) when a drug&#x27;s benefits outweigh its risks only if specific safety measures are in place; authorised under FDCA &#167;505-1</div>
          <div class="crm-obj-desc"><strong>REMS elements (in order of intensity):</strong> (1) Medication Guide &#8212; patient-facing document dispensed with every prescription explaining risks (e.g., NSAIDs cardiovascular risk); (2) Communication Plan &#8212; sponsor sends targeted safety letters to prescribers, pharmacists, and patient advocacy groups; (3) Elements to Assure Safe Use (ETASU) &#8212; the most restrictive tier, requiring one or more of: prescriber certification (only trained/certified HCPs can prescribe), pharmacy certification (only enrolled pharmacies can dispense), patient enrolment/monitoring (patients must be enrolled in a registry and/or have documented lab values before dispensing). <strong>Notable examples:</strong> iPLEDGE (isotretinoin &#8212; teratogenicity); CLOZAPINE REMS (agranulocytosis monitoring); Opioid Analgesic REMS (prescriber education); THALIDOMID/POMALYST (severe teratogenicity, strict patient/prescriber/pharmacy certification). <strong>Medical Affairs role:</strong> MSLs and Medical Information teams are responsible for HCP education about REMS requirements &#8212; a prescriber who is not REMS-certified cannot legally receive the product. Non-compliance with REMS by the sponsor is a misbranding violation under FDCA &#167;502(q).</div>
        </div>
      </div>

      <p style="font-weight:700; color:#6B2A8B; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #6B2A8B; padding-bottom:4px;">&#9670; Promotional &amp; Marketing Compliance</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#6B2A8B;">21 CFR Part 202 &#8212; Prescription Drug Advertising</div>
          <div class="crm-obj-api">Enforced by: FDA&#x27;s Office of Prescription Drug Promotion (OPDP) &#8212; issues Untitled Letters (informal) and Warning Letters (formal); enforces FDCA &#167;502(a) (misbranding) and &#167;502(n) (advertising without brief summary)</div>
          <div class="crm-obj-desc"><strong>Key provisions:</strong> &#167;202.1(e)(1) &#8212; all advertising must present a true statement of information about the drug&#x27;s uses and directions; &#167;202.1(e)(3)(iii) &#8212; <em>brief summary</em> requirement &#8212; every print/digital ad must include a brief summary of all material conditions, side effects, and contraindications (typically the PI condensed form); &#167;202.1(e)(5) &#8212; <em>fair balance</em> &#8212; risk information must appear with comparable prominence and readability to benefit claims; broadcast ads must present major risks in audio (the "major statement"); &#167;202.1(e)(6) &#8212; no false or misleading representations about the drug&#x27;s composition, properties, or safety/efficacy. <strong>Off-label prohibition:</strong> Promoting an approved drug for an unapproved indication violates FDCA &#167;502(a) misbranding. This is the primary basis for DOJ pharmaceutical marketing prosecutions. <strong>MLR relevance:</strong> Every promotional piece must pass Medical-Legal-Regulatory (MLR) review specifically to verify Part 202 compliance &#8212; the Regulatory reviewer in MLR is the primary Part 202 gatekeeper. The entirety of Vault PromoMats workflow exists to enforce this regulation.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#6B2A8B;">21 CFR Part 203 &#8212; Prescription Drug Marketing Act (PDMA) &#8212; Samples</div>
          <div class="crm-obj-api">Scope: Distribution of prescription drug samples to licensed practitioners; wholesale distribution of prescription drugs; prohibitions on resale of samples and reimportation</div>
          <div class="crm-obj-desc"><strong>Sampling requirements (&#167;203.30&#8211;203.39):</strong> HCP must submit a written sample request (signed, specifying drug, quantity, strength) before each sample distribution &#8212; a representative cannot simply leave samples without a request; representative must obtain the HCP&#x27;s signature at the point of delivery confirming receipt &#8212; Veeva iRep digital sample signatures with GPS geolocation and timestamp satisfy this requirement as a 21 CFR Part 11 electronic record; sample records (requests, receipts, distribution records) must be retained for 3 years and available for FDA inspection on request; periodic reconciliation of samples requested, samples received from manufacturer, and samples distributed to HCPs &#8212; any discrepancy must be investigated and documented. <strong>Prohibitions:</strong> No samples to anyone who is not a licensed prescriber or their authorised agent; no samples to a pharmacy for retail dispensing; no sample resale by recipients. <strong>Veeva relevance:</strong> <span class="crm-field-pill">Sample_vod__c</span>, <span class="crm-field-pill">Sample_Limit_vod__c</span>, <span class="crm-field-pill">Lot_vod__c</span>, and <span class="crm-field-pill">Sample_Receipt_vod__c</span> objects in iRep implement the Part 203 sampling audit trail end-to-end.</div>
        </div>
      </div>

      <p style="font-weight:700; color:#CC6600; margin:18px 0 10px 0; font-size:1.05em; border-bottom:2px solid #CC6600; padding-bottom:4px;">&#9670; Healthcare Fraud, Anti-Corruption &amp; Transparency</p>
      <div class="crm-obj-grid">
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#CC6600;">42 USC &#167;1320a-7b(b) &#8212; Anti-Kickback Statute (AKS)</div>
          <div class="crm-obj-api">Enforcement: OIG (Office of Inspector General), DOJ; criminal statute &#8212; conviction triggers mandatory exclusion from Medicare and Medicaid; no statute of limitations for criminal violations</div>
          <div class="crm-obj-desc"><strong>Core prohibition:</strong> Knowingly and wilfully offering, paying, soliciting, or receiving anything of value (&#x22;remuneration&#x22;) to induce or reward referrals of items or services covered by federal healthcare programmes (Medicare, Medicaid, TRICARE, VA). <strong>Critical &#x22;one purpose&#x22; test:</strong> The statute is violated if ANY one purpose of the arrangement is to induce referrals &#8212; it does not need to be the only or primary purpose. This makes innocent-sounding arrangements (speaker fees to high-prescribers, free consulting to key accounts) extremely legally vulnerable. <strong>&#x22;Remuneration&#x22; broadly defined:</strong> Cash payments, gifts, meals, entertainment, free or below-market consulting, excessive honoraria, inflated service contracts, stock options, charitable donations to a physician&#x27;s favoured cause, free samples used to generate billable prescriptions. <strong>Safe harbors (42 CFR Part 1001.952):</strong> Personal services agreements (written, minimum 1-year, FMV compensation for specifically described services); space and equipment rental (written, 1-year minimum, FMV); employment (bona fide employment at FMV); investment interests; group purchasing organisations. ALL conditions of a safe harbour must be satisfied &#8212; partial compliance provides no protection. <strong>Penalties:</strong> Criminal &#8212; up to 10 years imprisonment + up to $100,000 fine per violation; Civil Monetary Penalties &#8212; up to $100,000 per violation + 3&#215; remuneration amount; Mandatory exclusion from all federal healthcare programmes upon conviction &#8212; effectively a corporate death sentence for a company dependent on Medicare/Medicaid reimbursement.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#CC6600;">42 USC &#167;1320a-7h &#8212; Physician Payments Sunshine Act</div>
          <div class="crm-obj-api">Enacted: Affordable Care Act 2010; extended 2022 to include Advanced Practice Providers (NPs, PAs, CRNAs, CNMs, CNSs); administered by CMS; published annually in the Open Payments database at openpaymentsdata.cms.gov</div>
          <div class="crm-obj-desc"><strong>Reporting obligation:</strong> Applicable manufacturers and group purchasing organisations must report to CMS all payments or other transfers of value to covered recipients &#8212; &#8805;&#36;10 per individual item or &#8805;&#36;100 aggregate per year per recipient. <strong>Reportable categories:</strong> Consulting fees, compensation for non-consulting services (including promotional speaking and medical education), food and beverage, travel and lodging, education, entertainment, gifts, grants, honoraria, royalties and licences, research (classified separately as research is a more complex category with its own rules), ownership and investment interests, charitable contributions, current or prospective ownership/investment interest. <strong>Timeline:</strong> Reporting deadline March 31 for the prior calendar year (e.g., March 31, 2026 for 2025 payments); CMS publishes the Open Payments database June 30 each year; HCPs have 45 days to review and dispute their data before publication. <strong>Penalties:</strong> &#36;1,000&#8211;&#36;10,000 per payment for unknowing failures; &#36;10,000&#8211;&#36;100,000 per payment for knowing failures; &#36;150,000 maximum per company per year for unknowing; &#36;1 million maximum per company per year for knowing failures. <strong>Veeva relevance:</strong> Veeva Events Management captures every TOV across speaker programmes, advisory boards, meals, and HCP consulting engagements; the system generates the required CMS reporting data file, reconciles FMV thresholds, and creates the audit trail if any reported payment is disputed.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#CC6600;">31 USC &#167;3729 &#8212; False Claims Act (FCA)</div>
          <div class="crm-obj-api">Enforcement: DOJ Civil Division, US Attorneys offices, and &#x22;relators&#x22; (whistleblowers) filing qui tam lawsuits; largest single source of DOJ health care fraud recoveries &#8212; consistently &#36;2&#8211;&#36;4 billion annually across all industries</div>
          <div class="crm-obj-desc"><strong>Core prohibition:</strong> Knowingly submitting or causing the submission of false or fraudulent claims to the federal government for payment. <strong>&#x22;Knowingly&#x22; defined broadly:</strong> Actual knowledge, deliberate ignorance, or reckless disregard of the truth &#8212; no specific intent to defraud is required. <strong>Primary pharma FCA theories:</strong> (1) <em>Off-label promotion</em> &#8212; manufacturer promotes drug for unapproved use &#8594; physicians prescribe it off-label &#8594; Medicare/Medicaid reimburses &#8594; each reimbursement claim is a false claim because the prescribing decision was caused by illegal promotion; (2) <em>AKS-tainted claims</em> &#8212; under the Fraud Enforcement and Recovery Act (FERA 2009), any Medicare/Medicaid claim resulting from an AKS violation is automatically a false claim, regardless of whether the service was actually rendered; (3) <em>Best Price/AMP fraud</em> &#8212; under-reporting Average Manufacturer Price or Best Price to CMS causes government to overpay in the Medicaid Drug Rebate Programme. <strong>Qui tam (whistleblower) provisions:</strong> Private individuals (&#x22;relators&#x22;) may file a sealed complaint on behalf of the government; government investigates and may intervene; if successful, relator receives 15&#8211;25% of recovery when government intervenes, 25&#8211;30% if relator litigates alone. <strong>Penalties:</strong> Civil penalty of &#36;13,946&#8211;&#36;27,894 per false claim (2024 inflation-adjusted) plus treble damages (3&#215; the government&#x27;s loss). <strong>Landmark settlements:</strong> GlaxoSmithKline &#36;3B (2012, largest healthcare fraud settlement in US history at the time), Pfizer &#36;2.3B (2009), Abbott Laboratories &#36;1.5B (2012), all driven primarily by off-label promotion and/or AKS-tainted Medicare claims.</div>
        </div>
        <div class="crm-obj-card">
          <div class="crm-obj-name" style="color:#CC6600;">PhRMA Code on Interactions with Healthcare Professionals (2019)</div>
          <div class="crm-obj-api">Voluntary self-regulation by Pharmaceutical Research and Manufacturers of America &#8212; not a legal requirement, but non-compliance is used by OIG and DOJ as evidence of broader compliance programme failure and is incorporated by reference in Corporate Integrity Agreements</div>
          <div class="crm-obj-desc"><strong>Key provisions:</strong> <em>No gifts:</em> Absolutely no gifts of any monetary value to HCPs or their staff &#8212; the 2002 Code&#x27;s &#36;100 patient-benefit exception was eliminated entirely in the 2009 revision and remains absent. <em>Meals:</em> Only modest-value meals/refreshments provided in the context of a genuine, substantive educational or informational presentation; meals at restaurants without educational purpose are prohibited; entertainment (sporting events, golf, theatre) is prohibited entirely; no separate social events co-located with educational programmes. <em>CME funding:</em> Direct support for CME only through independent medical education grants to ACCME-accredited organisations; company cannot control speaker selection, content, or attendee criteria for funded CME. <em>Speaker programmes:</em> FMV-based honoraria documented in writing; programmes must feature genuine scientific exchange not available through other means; venues must be conducive to education not entertainment; repetitive engagement of the same speaker for the same programme requires documented scientific justification. <em>Consulting:</em> Written agreements specifying services; FMV compensation; services must actually be rendered and documented. <em>IIS/IIT grants:</em> Awarded through an independent scientific review process; no expectation of favourable results or publication support. <strong>Why it matters:</strong> DOJ and OIG treat PhRMA Code adherence as a marker of a functional compliance programme. Corporate Integrity Agreements (CIAs) entered into following DOJ settlements typically require PhRMA Code compliance by name. A company that has violated PhRMA Code provisions is considered to have a compromised compliance culture &#8212; prosecutors use this to argue for higher monetary penalties and longer CIA monitoring periods.</div>
        </div>
      </div>
    </dd>
"""

MODAL_CSS  = """

/* ════════════════════════════════════════════════════════════════════════════
   DIAGRAM ZOOM MODAL
   ════════════════════════════════════════════════════════════════════════════ */
.viz-modal-overlay {
  display: none;
  position: fixed; inset: 0; z-index: 9999;
  background: rgba(0,0,0,.92);
  flex-direction: column;
}
.viz-modal-overlay.open { display: flex; }

.viz-modal-bar {
  background: #111c2e; color: #c8d8f0;
  font-family: var(--ui-font); font-size: 12px; font-weight: 600;
  letter-spacing: .6px;
  padding: 10px 16px;
  display: flex; align-items: center; justify-content: space-between;
  border-bottom: 1px solid #2a3a5a; flex-shrink: 0; gap: 12px;
}
.viz-modal-bar-title {
  flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
  color: #7ec8c8;
}
.viz-modal-btns { display: flex; gap: 6px; align-items: center; flex-shrink: 0; }
.viz-modal-btns button {
  background: #1e2e4a; color: #c8d8f0;
  border: 1px solid #3a4a6a; border-radius: 5px;
  padding: 5px 11px; cursor: pointer; font-size: 13px; line-height: 1;
  transition: background .15s;
}
.viz-modal-btns button:hover { background: #2a4060; color: #fff; }
.viz-modal-pct { min-width: 50px; text-align: center; font-variant-numeric: tabular-nums; }
.viz-modal-hint {
  font-size: 10px; color: #4a6080; padding: 4px 12px 0;
  flex-basis: 100%; order: 10;
  /* shown only on first open */
}

.viz-modal-stage {
  flex: 1; overflow: hidden; position: relative; cursor: grab;
  background: #0a0e14;
}
.viz-modal-stage.dragging { cursor: grabbing; }

.viz-modal-content {
  position: absolute; top: 0; left: 0;
  transform-origin: 0 0;
  user-select: none; -webkit-user-select: none;
  transition: none;
}
.viz-modal-content svg {
  max-width: none !important; width: auto; height: auto; display: block;
}
.viz-modal-content img {
  max-width: none !important; display: block;
}

/* ── Expand hint badge on each diagram ── */
.vis-embed {
  position: relative;
}
.vis-expand-badge {
  position: absolute; top: 10px; right: 14px; z-index: 3;
  background: rgba(17,28,46,.88); color: #7ec8c8;
  font-family: var(--ui-font); font-size: 10px; font-weight: 700;
  letter-spacing: .8px; text-transform: uppercase;
  padding: 4px 10px; border-radius: 5px;
  border: 1px solid #2a3a5a;
  pointer-events: none;
  opacity: 0; transition: opacity .2s;
}
.vis-embed:hover .vis-expand-badge { opacity: 1; }
.vis-embed { cursor: zoom-in; }

"""

MODAL_HTML = """

<!-- ══════════════ DIAGRAM ZOOM MODAL ══════════════ -->
<div id="vizModal" class="viz-modal-overlay" role="dialog" aria-modal="true" aria-label="Diagram viewer">
  <div class="viz-modal-bar">
    <span class="viz-modal-bar-title" id="vizModalTitle"></span>
    <div class="viz-modal-btns">
      <button onclick="vizZoom(1.25)" title="Zoom in (+ key)">＋</button>
      <button id="vizPct" class="viz-modal-pct">100%</button>
      <button onclick="vizZoom(0.8)"  title="Zoom out (- key)">－</button>
      <button onclick="vizFit()"      title="Fit to window (0 key)">⊡ Fit</button>
      <button onclick="vizClose()"    title="Close (Esc)">✕ Close</button>
    </div>
  </div>
  <div class="viz-modal-stage" id="vizStage">
    <div class="viz-modal-content" id="vizContent"></div>
  </div>
</div>

"""

MODAL_JS   = """

// ── Diagram Zoom Modal ────────────────────────────────────────────────────
(function () {
  var modal   = document.getElementById('vizModal');
  var stage   = document.getElementById('vizStage');
  var content = document.getElementById('vizContent');
  var pctEl   = document.getElementById('vizPct');
  var titleEl = document.getElementById('vizModalTitle');

  var scale = 1, panX = 0, panY = 0;
  var dragging = false, startX, startY, startPX, startPY;
  var lastTouchDist = null, lastTouchMidX, lastTouchMidY;

  function applyT() {
    content.style.transform = 'translate(' + panX + 'px,' + panY + 'px) scale(' + scale + ')';
    pctEl.textContent = Math.round(scale * 100) + '%';
  }

  window.vizFit = function () {
    var sw = stage.clientWidth, sh = stage.clientHeight;
    // measure natural content size at scale=1
    content.style.transform = 'translate(0,0) scale(1)';
    var cw = content.offsetWidth, ch = content.offsetHeight;
    if (!cw || !ch) { scale = 1; panX = panY = 0; applyT(); return; }
    var fit = Math.min(sw / cw, sh / ch, 1);   // never scale up past 100% on fit
    scale = fit;
    panX = Math.max(0, (sw - cw * scale) / 2);
    panY = Math.max(0, (sh - ch * scale) / 2);
    applyT();
  };

  window.vizZoom = function (factor, cx, cy) {
    if (cx === undefined) { cx = stage.clientWidth / 2; cy = stage.clientHeight / 2; }
    panX = cx - (cx - panX) * factor;
    panY = cy - (cy - panY) * factor;
    scale = Math.min(10, Math.max(0.05, scale * factor));
    applyT();
  };

  window.vizOpen = function (fig) {
    var inner = fig.querySelector('.vis-inner');
    var label = fig.querySelector('.vis-label');
    content.innerHTML = inner ? inner.innerHTML : fig.innerHTML;
    // remove size constraints from embedded SVGs so they render at full resolution
    content.querySelectorAll('svg').forEach(function (s) {
      s.style.maxWidth = 'none';
      s.style.width = 'auto';
      // if viewBox exists but no explicit width, give it a large pixel width
      var vb = s.getAttribute('viewBox');
      if (vb) {
        var parts = vb.split(/[\s,]+/);
        if (parts.length === 4) {
          var naturalW = parseFloat(parts[2]);
          var naturalH = parseFloat(parts[3]);
          if (naturalW > 0) { s.setAttribute('width', naturalW); s.setAttribute('height', naturalH); }
        }
      }
    });
    content.querySelectorAll('img').forEach(function (img) {
      img.style.maxWidth = 'none';
    });
    titleEl.textContent = label ? label.textContent.trim() : '';
    scale = 1; panX = 0; panY = 0;
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    // fit after browser has laid out the cloned content
    requestAnimationFrame(function () { requestAnimationFrame(vizFit); });
  };

  window.vizClose = function () {
    modal.classList.remove('open');
    document.body.style.overflow = '';
    content.innerHTML = '';
  };

  // ── Mouse wheel zoom ──
  stage.addEventListener('wheel', function (e) {
    e.preventDefault();
    var rect = stage.getBoundingClientRect();
    var factor = e.deltaY < 0 ? 1.12 : 0.89;
    vizZoom(factor, e.clientX - rect.left, e.clientY - rect.top);
  }, { passive: false });

  // ── Mouse drag pan ──
  stage.addEventListener('mousedown', function (e) {
    if (e.button !== 0) return;
    dragging = true; stage.classList.add('dragging');
    startX = e.clientX; startY = e.clientY;
    startPX = panX; startPY = panY;
  });
  window.addEventListener('mousemove', function (e) {
    if (!dragging) return;
    panX = startPX + (e.clientX - startX);
    panY = startPY + (e.clientY - startY);
    applyT();
  });
  window.addEventListener('mouseup', function () {
    dragging = false; stage.classList.remove('dragging');
  });

  // ── Touch drag + pinch ──
  stage.addEventListener('touchstart', function (e) {
    if (e.touches.length === 1) {
      dragging = true;
      startX = e.touches[0].clientX; startY = e.touches[0].clientY;
      startPX = panX; startPY = panY;
      lastTouchDist = null;
    } else if (e.touches.length === 2) {
      dragging = false;
      lastTouchDist = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      lastTouchMidX = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      lastTouchMidY = (e.touches[0].clientY + e.touches[1].clientY) / 2;
    }
  }, { passive: true });
  stage.addEventListener('touchmove', function (e) {
    e.preventDefault();
    if (e.touches.length === 1 && dragging) {
      panX = startPX + (e.touches[0].clientX - startX);
      panY = startPY + (e.touches[0].clientY - startY);
      applyT();
    } else if (e.touches.length === 2 && lastTouchDist !== null) {
      var d = Math.hypot(
        e.touches[0].clientX - e.touches[1].clientX,
        e.touches[0].clientY - e.touches[1].clientY
      );
      var mx = (e.touches[0].clientX + e.touches[1].clientX) / 2;
      var my = (e.touches[0].clientY + e.touches[1].clientY) / 2;
      var rect = stage.getBoundingClientRect();
      vizZoom(d / lastTouchDist, mx - rect.left, my - rect.top);
      lastTouchDist = d;
    }
  }, { passive: false });
  stage.addEventListener('touchend', function () {
    dragging = false; lastTouchDist = null;
  }, { passive: true });

  // ── Keyboard shortcuts ──
  document.addEventListener('keydown', function (e) {
    if (!modal.classList.contains('open')) return;
    if (e.key === 'Escape')               { vizClose(); }
    else if (e.key === '+' || e.key === '=') { vizZoom(1.2); }
    else if (e.key === '-')               { vizZoom(0.83); }
    else if (e.key === '0')               { vizFit(); }
    else if (e.key === 'ArrowLeft')       { panX += 60; applyT(); }
    else if (e.key === 'ArrowRight')      { panX -= 60; applyT(); }
    else if (e.key === 'ArrowUp')         { panY += 60; applyT(); }
    else if (e.key === 'ArrowDown')       { panY -= 60; applyT(); }
  });

  // ── Close on backdrop click ──
  modal.addEventListener('click', function (e) {
    if (e.target === modal || e.target === stage) vizClose();
  });

  // ── Wire up all vis-embed figures ──
  document.querySelectorAll('.vis-embed').forEach(function (fig) {
    // add expand badge
    var badge = document.createElement('div');
    badge.className = 'vis-expand-badge';
    badge.textContent = '⊕ Click to expand';
    fig.appendChild(badge);

    fig.addEventListener('click', function (e) {
      if (e.target.closest('#vizModal')) return;
      vizOpen(fig);
    });
  });
})();

"""

VEEVA_USERMGMT = """
  <h2 id="veeva-user-mgmt">Veeva User Management &#8212; Access Control &amp; Permissions</h2>

  <p>Veeva CRM is built on the Salesforce platform, and its user management inherits the full depth of the Salesforce security model &#8212; with Veeva-specific overlays for life sciences compliance. Every person who accesses CRM data, submits a call report, drops a sample, or sends an Approved Email does so under a precisely configured permission stack. That stack determines not only what screens they see but what records they can read, what fields appear on those records, what they can create or delete, and which HCPs they can target. In a regulated pharmaceutical environment, permission misconfiguration is not a usability problem &#8212; it is a compliance risk. A commercial rep who can see an MSL&#x27;s scientific exchange notes, or an MSL who can initiate a promotional CLM session, creates a regulatory exposure that can surface in FDA inspections or DOJ investigations.</p>

  <p>The Salesforce/Veeva permission model is <em>additive and layered</em>: a user&#x27;s effective access is the union of everything granted by their Profile, plus everything added by their Permission Sets, constrained by Field-Level Security settings, and bounded by the data visibility rules of the Role Hierarchy and Sharing Rules. No single setting controls access in isolation &#8212; the system administrator must understand how all layers interact. Adding a Permission Set grants object access, but if Field-Level Security hides a key field at the profile level, that field remains hidden even with the Permission Set applied. This layered architecture is intentional: it allows fine-grained control without creating a separate profile for every possible combination of access needs.</p>

  <p>Veeva adds a second user management universe on top of CRM: the Vault platform (PromoMats and Vault Medical) runs its own user directory, its own role model, and its own security policy framework. A Vault user is not automatically a CRM user, and vice versa. Single Sign-On (SSO) can link the two directories for seamless login, but the permission structures are entirely separate. A Medical Director who approves documents in Vault PromoMats has no automatic CRM access &#8212; and a national sales director with full CRM visibility has no automatic ability to view or approve Vault documents. This separation is by design: Vault&#x27;s permission model is document-centric (who can do what to which document type in which lifecycle state), while CRM&#x27;s model is record-centric (who can do what to which Salesforce object).</p>

  <h3 id="vum-creation">User Creation &#8212; Step-by-Step Setup Flow</h3>

  <figure class="vis-embed" aria-label="Veeva CRM User Setup Flow">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Veeva CRM &#8212; User Creation &amp; Permission Setup Flow</div>
    <div class="vis-inner">
      <svg viewBox="0 0 960 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Veeva CRM user creation flow">
        <defs>
          <marker id="umA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#2A6099"/></marker>
          <marker id="umG" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#27AE60"/></marker>
        </defs>
        <rect width="960" height="420" fill="#0D1117" rx="10"/>
        <text x="480" y="26" text-anchor="middle" fill="#C8D8F0" font-size="13" font-weight="700" font-family="sans-serif">Veeva CRM &#8212; User Creation &amp; Permission Setup Flow</text>

        <!-- Row 1: Steps 1-4 -->
        <!-- Step 1: Salesforce Setup -->
        <rect x="20" y="50" width="130" height="88" rx="7" fill="#1A2A4A" stroke="#2A6099" stroke-width="1.5"/>
        <text x="85" y="72" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="700" font-family="sans-serif">1. Setup Portal</text>
        <text x="85" y="87" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Setup &#8594; Users &#8594; New User</text>
        <text x="85" y="100" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">System Admin role required</text>
        <text x="85" y="113" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Salesforce org: company.my.</text>
        <text x="85" y="126" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">salesforce.com/setup/users</text>
        <line x1="150" y1="94" x2="168" y2="94" stroke="#2A6099" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 2: User Record Fields -->
        <rect x="170" y="50" width="150" height="88" rx="7" fill="#1A2A4A" stroke="#2A6099" stroke-width="1.5"/>
        <text x="245" y="72" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="700" font-family="sans-serif">2. User Record</text>
        <text x="245" y="87" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">First/Last Name, Email</text>
        <text x="245" y="100" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Username (= Email, unique)</text>
        <text x="245" y="113" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Employee ID, Manager</text>
        <text x="245" y="126" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Locale, Timezone, Language</text>
        <line x1="320" y1="94" x2="338" y2="94" stroke="#2A6099" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 3: License -->
        <rect x="340" y="50" width="150" height="88" rx="7" fill="#1A2A4A" stroke="#2A6099" stroke-width="1.5"/>
        <text x="415" y="72" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="700" font-family="sans-serif">3. License Type</text>
        <text x="415" y="87" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Salesforce CRM (full)</text>
        <text x="415" y="100" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Salesforce Platform (lite)</text>
        <text x="415" y="113" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Determines feature access</text>
        <text x="415" y="126" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Drives per-seat cost</text>
        <line x1="490" y1="94" x2="508" y2="94" stroke="#2A6099" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 4: Profile -->
        <rect x="510" y="50" width="150" height="88" rx="7" fill="#1E3A5A" stroke="#3A70A0" stroke-width="1.5"/>
        <text x="585" y="72" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="700" font-family="sans-serif">4. Profile Assignment</text>
        <text x="585" y="87" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Base object permissions</text>
        <text x="585" y="100" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Page layouts, App access</text>
        <text x="585" y="113" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Field-Level Security base</text>
        <text x="585" y="126" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">One profile per user</text>
        <line x1="660" y1="94" x2="678" y2="94" stroke="#2A6099" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 5: Permission Sets -->
        <rect x="680" y="50" width="150" height="88" rx="7" fill="#1E3A5A" stroke="#3A70A0" stroke-width="1.5"/>
        <text x="755" y="72" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="700" font-family="sans-serif">5. Permission Sets</text>
        <text x="755" y="87" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Additive feature grants</text>
        <text x="755" y="100" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">CLM, Approved Email</text>
        <text x="755" y="113" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Sample Mgmt, Events</text>
        <text x="755" y="126" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Multiple sets per user</text>

        <!-- Downward arrow from Step 5 -->
        <line x1="755" y1="138" x2="755" y2="172" stroke="#2A6099" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Row 2: Steps 6-8 (right to left under steps 5-3) -->
        <!-- Step 6: Role Hierarchy -->
        <rect x="680" y="174" width="150" height="88" rx="7" fill="#1A3A2A" stroke="#2A8050" stroke-width="1.5"/>
        <text x="755" y="196" text-anchor="middle" fill="#80C8A0" font-size="10" font-weight="700" font-family="sans-serif">6. Role Assignment</text>
        <text x="755" y="211" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Role Hierarchy position</text>
        <text x="755" y="224" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Rep &#8594; DM &#8594; RBD &#8594; VP</text>
        <text x="755" y="237" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Controls record visibility</text>
        <text x="755" y="250" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Manager sees team data</text>
        <line x1="680" y1="218" x2="662" y2="218" stroke="#2A8050" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 7: Territory Sync -->
        <rect x="510" y="174" width="150" height="88" rx="7" fill="#1A3A2A" stroke="#2A8050" stroke-width="1.5"/>
        <text x="585" y="196" text-anchor="middle" fill="#80C8A0" font-size="10" font-weight="700" font-family="sans-serif">7. Territory Sync</text>
        <text x="585" y="211" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Veeva Align pushes</text>
        <text x="585" y="224" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">territory assignments</text>
        <text x="585" y="237" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">HCP targets linked to rep</text>
        <text x="585" y="250" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Call Plan auto-populated</text>
        <line x1="510" y1="218" x2="492" y2="218" stroke="#2A8050" stroke-width="1.5" marker-end="url(#umA)"/>

        <!-- Step 8: Active -->
        <rect x="340" y="174" width="150" height="88" rx="7" fill="#0A3A1A" stroke="#27AE60" stroke-width="2"/>
        <text x="415" y="196" text-anchor="middle" fill="#60E090" font-size="10" font-weight="700" font-family="sans-serif">8. User Active</text>
        <text x="415" y="211" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Active = true &#8594; login enabled</text>
        <text x="415" y="224" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Welcome email + temp pw</text>
        <text x="415" y="237" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">iRep app syncs on login</text>
        <text x="415" y="250" text-anchor="middle" fill="#8899AA" font-size="8.5" font-family="sans-serif">Deactivate (not delete)</text>

        <!-- Deactivation note -->
        <rect x="20" y="174" width="300" height="60" rx="6" fill="#2A1A0A" stroke="#806030" stroke-width="1" stroke-dasharray="4,3"/>
        <text x="170" y="193" text-anchor="middle" fill="#C09050" font-size="9.5" font-weight="700" font-family="sans-serif">&#9888; Deactivation vs Deletion</text>
        <text x="170" y="208" text-anchor="middle" fill="#9A7A50" font-size="8.5" font-family="sans-serif">Users must be DEACTIVATED, never deleted.</text>
        <text x="170" y="221" text-anchor="middle" fill="#9A7A50" font-size="8.5" font-family="sans-serif">Deleted users break audit trails (21 CFR Part 11).</text>

        <!-- SSO note -->
        <rect x="20" y="250" width="300" height="44" rx="6" fill="#1A1A3A" stroke="#5050A0" stroke-width="1"/>
        <text x="170" y="268" text-anchor="middle" fill="#9090C8" font-size="9" font-weight="700" font-family="sans-serif">SSO Integration (optional)</text>
        <text x="170" y="282" text-anchor="middle" fill="#7070A0" font-size="8.5" font-family="sans-serif">SAML 2.0 / Azure AD / Okta &#8594; Salesforce SSO</text>

        <!-- Key fields legend -->
        <rect x="20" y="310" width="920" height="94" rx="6" fill="#111820" stroke="#2A3A5A" stroke-width="1"/>
        <text x="30" y="328" fill="#7EC8C8" font-size="9.5" font-weight="700" font-family="sans-serif">Key User Record Fields:</text>
        <text x="30" y="346" fill="#8899AA" font-size="8.5" font-family="sans-serif">&#9656; Username: must be email format, globally unique across all Salesforce orgs, even if SSO is used (format: firstname.lastname@company.com.prod)</text>
        <text x="30" y="361" fill="#8899AA" font-size="8.5" font-family="sans-serif">&#9656; UserType: Standard (full CRM), PowerPartner (community), Guest &#8212; determines which License types and Profiles are available</text>
        <text x="30" y="376" fill="#8899AA" font-size="8.5" font-family="sans-serif">&#9656; IsActive: Boolean &#8212; set to false to deactivate; the user record, all owned records, and all audit entries are preserved permanently (Part 11 compliance)</text>
        <text x="30" y="391" fill="#8899AA" font-size="8.5" font-family="sans-serif">&#9656; FederationIdentifier: the SSO identifier (e.g., Azure AD Object ID) linking Salesforce user to corporate identity provider; required for SSO-enabled orgs</text>
        <text x="30" y="406" fill="#8899AA" font-size="8.5" font-family="sans-serif">&#9656; Territory2Id (Veeva Align): the primary territory assignment; drives which HCPs appear in the rep&#x27;s My Accounts list and Call Plan in iRep</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Veeva CRM user setup flow &#8212; 8 steps from Setup Portal through User Record, License, Profile, Permission Sets, Role Hierarchy, Territory Sync to Active; users must be deactivated (never deleted) to preserve 21 CFR Part 11 audit integrity</figcaption>
  </figure>

  <h3 id="vum-profiles">Profiles &#8212; The Base Permission Layer</h3>

  <p>A Profile is assigned one-per-user and controls the user&#x27;s baseline access: which objects they can see, what CRUD operations they can perform on each object, which fields appear on page layouts, which apps appear in the app launcher, and which tabs are visible. Profiles are the foundation of the permission stack &#8212; Permission Sets can only ADD to what a profile grants, never subtract. When designing a Profile, the principle of least privilege applies: grant only what the role requires, and use Permission Sets for any feature that only a subset of users with that profile need. Veeva ships standard managed profiles; companies customise by cloning these and adjusting as needed.</p>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">Veeva CRM Standard User Profile</div>
      <div class="crm-obj-api">Default field force profile &#183; ~90% of commercial reps</div>
      <div class="crm-obj-desc">The baseline profile for territory sales representatives. Grants Read/Create/Edit on <span class="crm-field-pill">Call_vod__c</span>, <span class="crm-field-pill">Account</span>, <span class="crm-field-pill">Contact</span>, <span class="crm-field-pill">Address_vod__c</span>. Read-only on <span class="crm-field-pill">Product_vod__c</span> and <span class="crm-field-pill">Key_Message_vod__c</span>. No access to <span class="crm-field-pill">Medical_Inquiry_vod__c</span>, <span class="crm-field-pill">Insight_vod__c</span>, or any Medical Affairs object &#8212; the firewall between commercial and medical is enforced at the profile level, not just by training or policy. Approved Email, CLM, and Sample Management are available but only activate when the corresponding Permission Sets are assigned. Page layouts show commercial fields only; MSL-specific fields (Discussion Topic, Scientific Exchange, Follow-Up Action) are absent entirely.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">MSL iRep Profile</div>
      <div class="crm-obj-api">Medical Affairs field &#183; Scientific exchange &#183; No commercial objects</div>
      <div class="crm-obj-desc">Configured for Medical Science Liaisons. Grants access to <span class="crm-field-pill">Medical_Inquiry_vod__c</span>, <span class="crm-field-pill">Insight_vod__c</span>, <span class="crm-field-pill">Follow_Up_Action_vod__c</span>, and the MSL-specific Call record type. <span class="crm-field-pill">Sample_vod__c</span> object is not visible &#8212; MSLs cannot initiate sample transactions. <span class="crm-field-pill">Products_Detailed_vod__c</span> commercial promotional detail fields are hidden. CLM is available but the content library points to Vault Medical scientific decks rather than PromoMats promotional Visual Aids &#8212; controlled by the Profile&#x27;s CLM content filter settings. The MSL&#x27;s call data is system-segregated from commercial call data; commercial managers cannot see MSL call reports even if they share the same manager role.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">Medical Information Profile</div>
      <div class="crm-obj-api">MI Center staff &#183; MIRF workflow &#183; SRL retrieval</div>
      <div class="crm-obj-desc">Designed for Medical Information specialists who handle inbound HCP inquiries. Full CRUD on <span class="crm-field-pill">Medical_Inquiry_vod__c</span> (MIRF records) including the AE flag field, unsolicited classification field, and SRL lookup. Read access to <span class="crm-field-pill">Account</span> and <span class="crm-field-pill">Contact</span> for HCP identity verification. No field force objects &#8212; no CLM, no Samples, no Call Reports from a territory perspective. The profile&#x27;s page layout shows the full MIRF workflow: inquiry classification, AE screening checkbox, SRL selection from Vault Medical, response logging, and case closure with outcome. Supervisors on this profile have View All on <span class="crm-field-pill">Medical_Inquiry_vod__c</span> to manage SLA compliance across the team.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">Veeva CRM System Administrator Profile</div>
      <div class="crm-obj-api">Full org access &#183; Configuration &amp; user management &#183; Strictly controlled headcount</div>
      <div class="crm-obj-desc">The Salesforce System Administrator profile grants Modify All Data and View All Data across every object &#8212; effectively bypassing all sharing rules, role hierarchy restrictions, and field-level security. In a validated Veeva environment, the number of System Admin users is explicitly documented in the System Validation documentation (IQ/OQ/PQ) and subject to change control. Every action taken by a System Admin user is logged in the Salesforce Setup Audit Trail with timestamp and user attribution &#8212; this trail cannot be modified or deleted. Best practice is to have fewer than 5 named System Admins, with a break-glass emergency access policy. Day-to-day admin tasks (user creation, permission set assignment, report building) are handled by a lesser-privileged custom admin profile that cannot modify system configuration.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">Sales Operations / Analytics Profile</div>
      <div class="crm-obj-api">Reporting &#183; Territory management &#183; Read-only field access</div>
      <div class="crm-obj-desc">For Sales Operations analysts, brand analytics teams, and SFDC admins who need broad data access for reporting but should not modify field records. Profile grants View All on Call_vod__c, Account, Contact, Sample_vod__c, and Events objects. No Create/Edit/Delete on field objects. Access to Salesforce Reports and Dashboards with full org-wide visibility (bypassing role hierarchy for reporting purposes). Typically combined with the Align_Territory_Manager Permission Set for teams managing territory alignment. Compliance note: View All access means this profile can see all HCP contact data, sample records, and call history &#8212; data governance policies must restrict access to this profile to named business need holders.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A6099;">Events Management Coordinator Profile</div>
      <div class="crm-obj-api">Speaker programs &#183; TOV tracking &#183; Sunshine Act data</div>
      <div class="crm-obj-desc">For field-based or home-office staff coordinating speaker programs, advisory boards, and HCP-facing events. Full CRUD on <span class="crm-field-pill">EM_Event_vod__c</span>, <span class="crm-field-pill">EM_Attendee_vod__c</span>, <span class="crm-field-pill">EM_Event_Speaker_vod__c</span>, <span class="crm-field-pill">TOV_vod__c</span>. Access to FMV validation workflow (checks HCP honorarium against pre-approved FMV rate cards stored in CRM). Cannot modify the FMV rate card records themselves &#8212; those are locked to Compliance team users. Every TOV entry is timestamped and attributed to the creating user; the audit trail feeds directly into the annual Open Payments (Sunshine Act) data export to CMS. Events coordinators cannot approve their own event requests &#8212; approval routing enforces a segregation of duties via Salesforce Approval Process.</div>
    </div>
  </div>

  <h3 id="vum-permsets">Permission Sets &#8212; Additive Feature Access</h3>

  <p>Permission Sets grant additional access on top of a user&#x27;s base profile. They are additive &#8212; they can never remove access that the profile already grants, only extend it. This makes them ideal for capabilities that only a subset of users with a given profile need: not every field rep uses CLM, not every commercial rep drops samples, not every MSL manages events. Rather than creating a separate profile for each combination, the base profile handles the common access and Permission Sets unlock the specific features. In Veeva CRM, most feature modules ship as pre-built managed Permission Sets (prefixed <em>vod</em> for Veeva on Demand) that the admin assigns; companies can also create custom Permission Sets for bespoke access requirements.</p>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">CLM_User_vod &#8212; Closed-Loop Marketing</div>
      <div class="crm-obj-api">Required for: any rep or MSL who presents content to HCPs via iRep tablets</div>
      <div class="crm-obj-desc">Grants Create/Read/Edit on <span class="crm-field-pill">CLM_Presentation_vod__c</span>, <span class="crm-field-pill">Clm_Presentation_Slide_vod__c</span>, <span class="crm-field-pill">Key_Message_vod__c</span>, and <span class="crm-field-pill">CLM_Slide_vod__c</span>. Enables the CLM tab in iRep, unlocks the CLM content library sync from Vault PromoMats (for commercial reps) or Vault Medical (for MSLs). Without this Permission Set, the rep&#x27;s iRep home screen shows no CLM launcher. Field-level permissions within this set control whether the rep can see dwell time analytics on their own slides or only the brand team&#x27;s aggregate dashboard. The Permission Set also grants read access to <span class="crm-field-pill">Products_Detailed_vod__c</span> reaction fields used to capture HCP sentiment at the slide level.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">Approved_Email_User_vod &#8212; Approved Email</div>
      <div class="crm-obj-api">Required for: reps sending HCP-facing email from iRep using MLR-approved templates</div>
      <div class="crm-obj-desc">Grants access to <span class="crm-field-pill">Approved_Document_vod__c</span> (the email template library synced from Vault PromoMats), <span class="crm-field-pill">Sent_Email_vod__c</span> (audit record of every Approved Email sent), and the Approved Email composer within iRep. Content is strictly limited to templates that have completed the MLR workflow in PromoMats and are in Active status &#8212; the Permission Set does not grant ability to compose free-text emails to HCPs. Every sent email is logged as a Sent_Email_vod__c record linked to the HCP Contact and the source template version. Unsubscribe handling is enforced automatically: if the HCP&#x27;s <span class="crm-field-pill">Email_Opt_Out_vod__c</span> is true, the Approved Email composer blocks sending to that HCP regardless of user action.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">Sample_Management_vod &#8212; PDMA Sampling</div>
      <div class="crm-obj-api">Required for: reps authorised to drop prescription drug samples (21 CFR Part 203)</div>
      <div class="crm-obj-desc">Grants Create/Edit on <span class="crm-field-pill">Sample_vod__c</span> (sample transaction records), <span class="crm-field-pill">Sample_Receipt_vod__c</span> (HCP signature capture), <span class="crm-field-pill">Lot_vod__c</span> (lot-level inventory tracking), and <span class="crm-field-pill">Sample_Limit_vod__c</span> (product-level distribution limits per HCP per period). Enables the Sample tab in iRep and the digital signature capture screen compliant with 21 CFR Part 203. When a sample transaction is submitted, the system validates: (a) the HCP has a valid DEA number in Network if the sample is a controlled substance Schedule III&#8211;V, (b) the HCP is not on the OIG exclusion list, (c) the rep has not exceeded the product&#x27;s per-HCP sample limit for the period. Any failed validation blocks submission and creates a compliance alert record.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">Events_User_vod &#8212; Events Management</div>
      <div class="crm-obj-api">Required for: HCP-facing event coordinators, MSLs attending advisory boards, speaker program managers</div>
      <div class="crm-obj-desc">Grants access to the Events Management module: <span class="crm-field-pill">EM_Event_vod__c</span> (event record with date, venue, budget), <span class="crm-field-pill">EM_Attendee_vod__c</span> (HCP attendance with TOV value), <span class="crm-field-pill">EM_Event_Speaker_vod__c</span> (speaker details with honorarium and FMV cap), <span class="crm-field-pill">TOV_vod__c</span> (itemised transfer of value record feeding Sunshine Act). The Permission Set enforces FMV validation on speaker honoraria: the field is compared against the pre-loaded FMV rate card for the HCP&#x27;s specialty; any honorarium exceeding the FMV cap triggers a mandatory approval workflow before the event can be marked complete. Meals at events are automatically capped at the per-head meal policy limit; entries above the cap are flagged for compliance review.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">Network_Data_Viewer_vod &#8212; HCP Master Data</div>
      <div class="crm-obj-api">Required for: analytics users and operations staff needing read-only access to Veeva Network master data</div>
      <div class="crm-obj-desc">Grants read-only access to Network-managed fields on <span class="crm-field-pill">Account</span> and <span class="crm-field-pill">Contact</span>: VID (Veeva ID), specialty, NPI, DEA number, OIG exclusion status, affiliation network, and address confidence score. Does not grant the ability to submit Data Change Requests (DCRs) &#8212; that requires a separate DCR_Submitter permission. Users with this set can view the full master data profile of an HCP for analytical purposes (targeting, segmentation, KOL tier scoring) without being able to alter the data. Particularly important for brand analytics teams who run call-pattern analysis against prescriber profiles &#8212; they need to join CRM call data with Network specialty and tier data but have no data stewardship role.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#4A90C0;">Align_Territory_Manager_vod &#8212; Territory Alignment</div>
      <div class="crm-obj-api">Required for: Sales Operations users managing territory boundaries and rep-HCP target lists via Veeva Align</div>
      <div class="crm-obj-desc">Grants access to <span class="crm-field-pill">Territory2</span> (Salesforce Enterprise Territory Management objects) and the Veeva Align CRM component. Users with this Permission Set can view and modify territory boundary definitions, reassign HCPs between territories, manage the Call Plan target list (which HCPs appear in each rep&#x27;s iRep My Accounts list), and trigger the Align sync that propagates territory changes to all affected rep tablets in the next scheduled sync cycle. Changes to territory assignments are logged with timestamp and user &#8212; key for IC (Incentive Compensation) disputes where a rep claims they were not assigned an HCP at the time of a contested call. Access is restricted to named Sales Ops headcount; no field rep should have this Permission Set.</div>
    </div>
  </div>

  <h3 id="vum-objectperms">Object-Level Permissions &#8212; CRUD + View/Modify All</h3>

  <p>Every object in Salesforce/Veeva CRM has six permission toggles that together define what a user can do with records of that type. These permissions are set at the Profile level and can be extended (but not restricted) by Permission Sets. Understanding exactly what each toggle does is critical for compliance: granting Delete on Call_vod__c to a field rep would allow them to remove call records from the audit trail &#8212; a 21 CFR Part 11 violation. Granting Modify All on Account would let a user overwrite Network-managed master data fields &#8212; breaking the MDM integrity that Veeva Network maintains.</p>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#60A870;">Create</div>
      <div class="crm-obj-api">Can instantiate new records of this object type</div>
      <div class="crm-obj-desc">Allows the user to create a new record. A field rep needs Create on Call_vod__c to submit a call report. An MSL needs Create on Insight_vod__c to log a scientific exchange note. Create permission does not automatically grant the ability to see other users&#x27; records &#8212; that is controlled by the Read permission and Sharing Rules. In Veeva CRM, Create on certain objects (Sample_vod__c, Sent_Email_vod__c) also triggers downstream validation logic &#8212; the business logic runs regardless of how the record was created.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#60A870;">Read</div>
      <div class="crm-obj-api">Can view records &#8212; subject to Sharing Rules and Role Hierarchy for which records are visible</div>
      <div class="crm-obj-desc">Without Read, the object and its records are completely invisible to the user &#8212; no tab, no related list, no search results. Read permission is the minimum required to see any record of that type. However, Read permission does NOT mean the user can see ALL records &#8212; only the records they own or that have been shared with them via Role Hierarchy or Sharing Rules. Read permission on Account with OWD set to Private means a rep can only see the HCP Accounts in their territory, even though they have Read on the object type. View All (below) overrides this scoping.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#60A870;">Edit</div>
      <div class="crm-obj-api">Can modify existing records they have Read access to</div>
      <div class="crm-obj-desc">Allows modifying existing records. Note: Edit on an object does not override Field-Level Security &#8212; a field set to read-only at the FLS level cannot be edited even if the user has Edit on the object. In Veeva CRM, Edit on Call_vod__c is typically granted only while the call is in Draft status; once submitted, the record is locked and Edit is effectively blocked by a validation rule even though the object-level permission remains. This is an important pattern: object-level CRUD is the outer gate; record-level and field-level controls provide finer-grained restrictions within that gate.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#C07030;">Delete</div>
      <div class="crm-obj-api">Can delete records &#8212; almost never granted to field users; compliance risk</div>
      <div class="crm-obj-desc">Grants the ability to delete records. In a 21 CFR Part 11 validated environment, Delete on any object that generates regulatory records (Call_vod__c, Sample_vod__c, Sent_Email_vod__c, Medical_Inquiry_vod__c) must never be granted to standard field users. Deleted records go to the Recycle Bin and can be restored within 15 days, but the deletion event itself is logged &#8212; and a deleted call report constitutes destruction of a regulated electronic record. In practice, Delete on Veeva objects is restricted to System Admins with documented change-control justification, or to data stewardship workflows that use a soft-delete pattern (setting a status field to Deleted rather than actually deleting the record).</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#C07030;">View All</div>
      <div class="crm-obj-api">Bypasses Sharing Rules and Role Hierarchy to see ALL records of this object type org-wide</div>
      <div class="crm-obj-desc">View All overrides the Organisation-Wide Default (OWD) sharing model for read access &#8212; a user with View All on Call_vod__c can see every call report in the organisation regardless of territory, manager hierarchy, or explicit sharing. This is appropriate for: compliance officers auditing call records across the entire field force, Medical Information supervisors monitoring all MIRF response SLAs, analytics users running national-level reports. View All should be restricted to named roles with documented business need and audited regularly. In a Veeva org, View All on Account combined with View All on Sample_vod__c would allow an analytics user to reconstruct the complete sampling history of every HCP in the US.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#C03030;">Modify All</div>
      <div class="crm-obj-api">Bypasses all sharing + allows edit/delete of ALL records &#8212; data stewardship and admin use only</div>
      <div class="crm-obj-desc">Modify All combines View All with the ability to edit and delete every record of that object, regardless of ownership or sharing settings. This is the most powerful object-level permission and effectively makes the user a data owner for that object across the entire organisation. In Veeva, Modify All on Network-managed objects (Account, Contact) must be granted with extreme care &#8212; a user with this permission can overwrite VID-linked master data fields that Veeva Network manages, breaking the MDM synchronisation. Modify All is appropriate for: data stewardship workflows (bulk address corrections after a Network refresh), migration scripts running as a named service account, and System Admins. It is never appropriate for field users or even most home-office roles.</div>
    </div>
  </div>

  <h3 id="vum-rolehierarchy">Role Hierarchy, OWD &amp; Sharing Rules &#8212; Data Visibility</h3>

  <p>Object-level permissions determine what a user can do with records they can see; the Role Hierarchy and Sharing architecture determines which records they can see. These are entirely separate concerns. A rep may have Read/Edit on Call_vod__c (object permission) but can only see their own territory&#x27;s call records (data visibility). Their District Manager has the same object permission but can see all call records belonging to reps in their team (role hierarchy roll-up). The three mechanisms that control data visibility are: Organisation-Wide Defaults (OWD) &#8212; the default access for all records of each object; Role Hierarchy &#8212; managers can see records owned by users below them; and Sharing Rules &#8212; criteria-based or ownership-based grants of access to additional records.</p>

  <p>In a standard Veeva CRM deployment, the typical OWD settings are: Account (Public Read Only &#8212; all users can see all HCP records, but only owners/territory reps can edit), Call_vod__c (Private &#8212; only the submitting rep and their managers via Role Hierarchy can see a call report), Sample_vod__c (Private), Medical_Inquiry_vod__c (Private &#8212; only Medical Information team via role + explicit sharing). The Role Hierarchy typically mirrors the sales organisation: Territory Rep &#8594; District Manager &#8594; Regional Business Director &#8594; Area VP &#8594; National Sales Director, with a parallel Medical Affairs hierarchy (MSL &#8594; Regional Medical Director &#8594; VP Medical Affairs) that is completely separate from the commercial hierarchy &#8212; the two hierarchies do not share roll-up visibility, enforcing the commercial/medical firewall at the data layer.</p>

  <h3 id="vum-permmodel">Permission Architecture &#8212; How All Layers Interact</h3>

  <figure class="vis-embed" aria-label="Veeva CRM Permission Architecture">
    <div class="vis-label"><span class="vis-icon">&#9670;</span> Veeva CRM &#8212; Full Permission &amp; Data Visibility Architecture</div>
    <div class="vis-inner">
      <svg viewBox="0 0 900 520" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Veeva CRM permission model architecture diagram">
        <defs>
          <marker id="pmA" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#4A90C0"/></marker>
          <marker id="pmB" markerWidth="7" markerHeight="5" refX="7" refY="2.5" orient="auto"><polygon points="0 0,7 2.5,0 5" fill="#60A870"/></marker>
        </defs>
        <rect width="900" height="520" fill="#0D1117" rx="10"/>
        <text x="450" y="28" text-anchor="middle" fill="#C8D8F0" font-size="13" font-weight="700" font-family="sans-serif">Veeva CRM &#8212; Permission &amp; Data Visibility Architecture</text>

        <!-- Layer 1: Profile -->
        <rect x="40" y="48" width="820" height="72" rx="8" fill="#1A2A4A" stroke="#3A70A0" stroke-width="2"/>
        <text x="60" y="74" fill="#7EC8C8" font-size="11" font-weight="700" font-family="sans-serif">LAYER 1 &#8212; Profile (Base Access)</text>
        <text x="60" y="92" fill="#8899AA" font-size="9" font-family="sans-serif">Object CRUD permissions &#183; Field-Level Security baseline &#183; App &amp; Tab visibility &#183; Page layouts &#183; Record Types &#183; Login hours &amp; IP ranges</text>
        <text x="60" y="107" fill="#8899AA" font-size="9" font-family="sans-serif">One profile per user &#183; Cannot grant more than the License type allows &#183; Least-privilege starting point &#183; Clone Veeva standard profiles; never modify managed originals</text>

        <!-- Additive arrow -->
        <text x="450" y="132" text-anchor="middle" fill="#4A90C0" font-size="9" font-family="sans-serif">&#43; Additive (can only extend, never restrict)</text>
        <line x1="450" y1="122" x2="450" y2="140" stroke="#4A90C0" stroke-width="1.5" marker-end="url(#pmA)"/>

        <!-- Layer 2: Permission Sets -->
        <rect x="40" y="142" width="820" height="72" rx="8" fill="#1A2A4A" stroke="#3A70A0" stroke-width="1.5" stroke-dasharray="6,3"/>
        <text x="60" y="168" fill="#7EC8C8" font-size="11" font-weight="700" font-family="sans-serif">LAYER 2 &#8212; Permission Sets (Additive Feature Grants)</text>
        <text x="60" y="186" fill="#8899AA" font-size="9" font-family="sans-serif">CLM_User &#183; Approved_Email &#183; Sample_Management &#183; Events_User &#183; Network_Viewer &#183; Align_Territory_Manager &#183; Custom org-specific sets</text>
        <text x="60" y="201" fill="#8899AA" font-size="9" font-family="sans-serif">Multiple sets per user &#183; Applied on top of Profile &#183; Cannot revoke profile permissions &#183; Permission Set Groups allow bundling multiple sets into a single assignment</text>

        <!-- FLS divider -->
        <text x="450" y="226" text-anchor="middle" fill="#4A90C0" font-size="9" font-family="sans-serif">&#43; Field-Level Security override (per field per profile/set)</text>
        <line x1="450" y1="216" x2="450" y2="234" stroke="#4A90C0" stroke-width="1.5" marker-end="url(#pmA)"/>

        <!-- Layer 3: FLS -->
        <rect x="40" y="236" width="820" height="60" rx="8" fill="#1A2040" stroke="#4060A0" stroke-width="1.5"/>
        <text x="60" y="260" fill="#9090D0" font-size="11" font-weight="700" font-family="sans-serif">LAYER 3 &#8212; Field-Level Security (FLS)</text>
        <text x="60" y="276" fill="#8899AA" font-size="9" font-family="sans-serif">Per-field: Hidden / Read-Only / Read-Write &#183; Set per Profile AND per Permission Set &#183; Most restrictive wins &#183; Hidden field = invisible even with Edit on object</text>
        <text x="60" y="289" fill="#8899AA" font-size="9" font-family="sans-serif">Critical for commercial/medical firewall: MSL insight fields are FLS-hidden on commercial profiles even though both share the Contact object &#183; FLS &#8800; Page Layout (FLS is enforced by API; page layout is UI only)</text>

        <!-- Sharing divider -->
        <text x="450" y="312" text-anchor="middle" fill="#60A870" font-size="9" font-family="sans-serif">+ Data Visibility (which records the user can see)</text>
        <line x1="450" y1="302" x2="450" y2="320" stroke="#60A870" stroke-width="1.5" marker-end="url(#pmB)"/>

        <!-- Layer 4: OWD + Role Hierarchy -->
        <rect x="40" y="322" width="400" height="80" rx="8" fill="#0A2A1A" stroke="#2A7050" stroke-width="1.5"/>
        <text x="60" y="346" fill="#60C890" font-size="10.5" font-weight="700" font-family="sans-serif">LAYER 4a &#8212; OWD + Role Hierarchy</text>
        <text x="60" y="362" fill="#8899AA" font-size="8.5" font-family="sans-serif">OWD: default access for every record (Private /</text>
        <text x="60" y="375" fill="#8899AA" font-size="8.5" font-family="sans-serif">Public Read-Only / Public R-W)</text>
        <text x="60" y="388" fill="#8899AA" font-size="8.5" font-family="sans-serif">Role Hierarchy: managers inherit visibility of</text>
        <text x="60" y="398" fill="#8899AA" font-size="8.5" font-family="sans-serif">records owned by users below them</text>

        <!-- Layer 4b: Sharing Rules -->
        <rect x="460" y="322" width="400" height="80" rx="8" fill="#0A2A1A" stroke="#2A7050" stroke-width="1.5"/>
        <text x="480" y="346" fill="#60C890" font-size="10.5" font-weight="700" font-family="sans-serif">LAYER 4b &#8212; Sharing Rules</text>
        <text x="480" y="362" fill="#8899AA" font-size="8.5" font-family="sans-serif">Owner-based: share all records owned by Role X</text>
        <text x="480" y="375" fill="#8899AA" font-size="8.5" font-family="sans-serif">with Role Y (e.g., MSL manager sees all MSL calls)</text>
        <text x="480" y="388" fill="#8899AA" font-size="8.5" font-family="sans-serif">Criteria-based: share records matching field</text>
        <text x="480" y="398" fill="#8899AA" font-size="8.5" font-family="sans-serif">conditions (e.g., all KOL-tier HCPs shared to MI)</text>

        <!-- Effective access -->
        <line x1="240" y1="402" x2="240" y2="430" stroke="#60A870" stroke-width="1.5" marker-end="url(#pmB)"/>
        <line x1="660" y1="402" x2="660" y2="430" stroke="#60A870" stroke-width="1.5" marker-end="url(#pmB)"/>
        <line x1="240" y1="430" x2="660" y2="430" stroke="#60A870" stroke-width="1.5"/>
        <line x1="450" y1="430" x2="450" y2="448" stroke="#60A870" stroke-width="1.5" marker-end="url(#pmB)"/>

        <rect x="120" y="450" width="660" height="54" rx="8" fill="#1A3A1A" stroke="#40A060" stroke-width="2"/>
        <text x="450" y="472" text-anchor="middle" fill="#80E0A0" font-size="12" font-weight="700" font-family="sans-serif">= Effective Access: What the User Can Do &amp; See</text>
        <text x="450" y="490" text-anchor="middle" fill="#8899AA" font-size="9" font-family="sans-serif">Profile &#43; Permission Sets = functional access &#183; FLS = field-level read/edit &#183; OWD &#43; Role Hierarchy &#43; Sharing Rules = record-level visibility</text>

        <!-- Right side: Role Hierarchy illustration -->
        <rect x="830" y="322" width="1" height="1" fill="none"/>
        <!-- small role hierarchy tree on right -->
        <text x="880" y="350" text-anchor="middle" fill="#4A6080" font-size="8.5" font-family="sans-serif">Role</text>
        <text x="880" y="362" text-anchor="middle" fill="#4A6080" font-size="8.5" font-family="sans-serif">Hierarchy</text>
        <text x="880" y="378" text-anchor="middle" fill="#5A7090" font-size="8" font-family="sans-serif">VP</text>
        <text x="880" y="392" text-anchor="middle" fill="#5A7090" font-size="8" font-family="sans-serif">RBD</text>
        <text x="880" y="406" text-anchor="middle" fill="#5A7090" font-size="8" font-family="sans-serif">DM</text>
        <text x="880" y="420" text-anchor="middle" fill="#5A7090" font-size="8" font-family="sans-serif">Rep</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Veeva CRM permission architecture &#8212; four layers from Profile (base CRUD and FLS) through Permission Sets (additive feature grants) through Field-Level Security through OWD/Role Hierarchy/Sharing Rules combine to produce each user&#x27;s effective access; no single layer controls access in isolation</figcaption>
  </figure>

  <h3 id="vum-vault-users">Vault User Management &#8212; PromoMats &amp; Vault Medical</h3>

  <p>Vault PromoMats and Vault Medical each maintain their own user directories, entirely separate from Veeva CRM. A person can be a Vault user without being a CRM user, and vice versa. Vault administrators manage users via the Vault Admin console at <em>company.veevavault.com/ui/#admin/users</em>. Vault uses a document-centric permission model built around <strong>Application Roles</strong>, <strong>Security Policies</strong>, and <strong>Document Lifecycle Role Assignments</strong> &#8212; the combination of which determines who can do what to which document in which review state. This model is more granular than the CRM model in one specific dimension: a user&#x27;s access can change depending on the document&#x27;s current lifecycle state. A Medical Writer who can edit a document in Draft state loses edit access the moment the document enters Medical Review &#8212; enforcing the integrity of the review process at the permission level.</p>

  <div class="crm-obj-grid">
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Vault Application Roles</div>
      <div class="crm-obj-api">Document-level role assignments &#183; Drive lifecycle action permissions</div>
      <div class="crm-obj-desc">Vault Application Roles define what a user can do with a document at each lifecycle state. Key roles in PromoMats: <strong>Owner</strong> (created the document; can edit in Draft, initiate workflow), <strong>Reviewer</strong> (MLR Medical, Legal, Regulatory &#8212; can annotate and vote in their assigned review step), <strong>Approver</strong> (can move documents from a review state to Approved; the final sign-off role), <strong>Viewer</strong> (read-only; can view documents in any state for reference), <strong>Document Creator</strong> (can initiate new documents from templates; cannot approve). A single Vault user can hold multiple Application Roles. Role assignment is per-vault &#8212; the same person may be an Approver in Vault PromoMats and a Viewer-only in Vault Medical.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Security Policies</div>
      <div class="crm-obj-api">Vault-level access matrix &#183; Combines role + document type + lifecycle state</div>
      <div class="crm-obj-desc">A Security Policy in Vault is the master access matrix: for each combination of Application Role and Document Type (SRL, Visual Aid, Scientific Deck, etc.) and Lifecycle State (Draft, Medical Review, Approved, Superseded), it specifies which actions are permitted: View, Edit, Download, Annotate, Start Workflow, Move to Next State, Delete. The Security Policy is assigned to each document type; all documents of that type use the same policy. Example: the PromoMats Visual Aid security policy might grant Document Creators Edit access in Draft state only, Reviewers Annotate-only in their respective review states, and Approvers the Move-to-Next-State action in the final approval step &#8212; while Viewers have read-only access in all states. Security Policy changes require Vault Admin access and are logged in the Vault audit trail.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Document Lifecycle Role Assignment</div>
      <div class="crm-obj-api">State-specific permissions &#183; MLR and MRB review integrity</div>
      <div class="crm-obj-desc">Within each lifecycle state, Vault allows specific Application Roles to be assigned at the document level &#8212; that is, a particular user is assigned the Reviewer role for a particular document&#x27;s Medical Review step. This is how the MLR workflow is personalised: the Medical Reviewer assigned to a specific Visual Aid is the person who receives the Workflow Task notification, and only that person (plus Approvers and Admins) can complete that task. If the assigned reviewer is unavailable, a Vault Admin must reassign the task &#8212; the reassignment is logged. This state-specific assignment means a user&#x27;s effective access to a document changes as it moves through lifecycle states: the Medical Writer loses edit access when the document enters Medical Review, and the Regulatory Reviewer gains approve access only in the Legal/Regulatory Review state, not before or after.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Vault User Types &amp; Licences</div>
      <div class="crm-obj-api">Full User &#183; Read-Only User &#183; External User &#183; Named User licensing</div>
      <div class="crm-obj-desc"><strong>Full User:</strong> Can create, edit, review, and approve documents based on their Application Role assignments. Standard licence for all MLR participants and Medical Affairs staff. <strong>Read-Only User:</strong> Can view and download documents in any Approved or Active state; cannot create, edit, annotate, or participate in workflows. Appropriate for senior leadership who need visibility into the content library without being workflow participants. Significantly lower licence cost. <strong>External User:</strong> Limited access for partners, agencies, or external reviewers participating in a specific workflow; typically scoped to a single document or project. <strong>Vault SSO:</strong> Vault supports SAML 2.0 SSO, allowing the same corporate identity provider used for Salesforce/CRM to authenticate Vault users &#8212; reducing password management overhead and enabling automated provisioning via SCIM when users join or leave the organisation.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">Vault Admin vs Vault Owner</div>
      <div class="crm-obj-api">System administration &#183; Validation boundary &#183; Change control</div>
      <div class="crm-obj-desc">The Vault System Administrator has access to all configuration settings: user management, Security Policy creation and modification, lifecycle state configuration, workflow template design, object field additions. In a validated Vault environment (21 CFR Part 11), all Vault Admin actions are logged in the Admin Audit Trail with timestamp, user, and action detail &#8212; this trail cannot be modified. Changes to Security Policies or lifecycle configurations that could affect document review integrity must go through formal change control (documented change request, risk assessment, UAT, and approval sign-off) before being deployed to production. A Vault Owner is the business owner of a specific document &#8212; they have Owner Application Role on their documents and can initiate workflows, but cannot modify system configuration. The separation between Vault Admin (system configuration) and Vault Owner (content ownership) mirrors the Salesforce System Admin vs business user distinction in CRM.</div>
    </div>
    <div class="crm-obj-card">
      <div class="crm-obj-name" style="color:#2A9A9A;">CRM &#8596; Vault User Provisioning</div>
      <div class="crm-obj-api">SSO linking &#183; Automated deprovisioning &#183; Identity governance</div>
      <div class="crm-obj-desc">When SSO is configured between CRM (Salesforce) and Vault, the two user directories remain separate but share the same identity provider. A user logging into CRM and then clicking a Vault link is automatically authenticated in Vault via the SSO token &#8212; no separate Vault password. However, the user must still be provisioned in Vault separately; SSO provides authentication but not authorisation. Most organisations implement an HRIS-driven provisioning workflow: when a new employee is onboarded, the HR system triggers user creation in both Salesforce and Vault with the appropriate profiles and Application Roles based on job function. When an employee is terminated, the offboarding workflow deactivates both accounts simultaneously &#8212; critical for preventing former MLR reviewers or ex-sales reps from retaining access to regulated content and customer data after separation.</div>
    </div>
  </div>
"""

FRONT_MATTER = """

<!-- ══════════════════════════════════════════════
     ABSTRACT
══════════════════════════════════════════════ -->
<section class="fm-page" id="abstract" role="region" aria-label="Abstract">
  <div class="fm-inner">
    <div class="fm-label">Abstract</div>
    <h2 class="fm-heading">A Practitioner's Complete Reference to Pharma Commercial &amp; Medical Affairs</h2>
    <div class="fm-rule"></div>
    <div class="fm-body">
      <p>This guide provides a comprehensive, story-driven reference covering the full spectrum of pharmaceutical commercial and medical affairs operations — from the earliest stages of laboratory discovery through post-launch lifecycle management. Written for practitioners, consultants, and cross-functional professionals operating at the intersection of science, strategy, and systems, it integrates operational process, regulatory framework, and technology platform into a single cohesive reference.</p>
      <p>The guide spans eleven chapters and one reference section, encompassing: the R&amp;D-to-market pipeline; commercial field operations and sales force effectiveness; medical affairs strategy, evidence generation, and MSL operations; the commercial–medical firewall; product launch management; organisational roles and team structures; US and international regulatory compliance (21 CFR, GxP, ICH, AKS, Sunshine Act, PDMA, PhRMA Code, False Claims Act); and the Veeva technology ecosystem (CRM, Vault PromoMats, Vault Medical, Network, Events Management, User Management).</p>
      <p>Throughout, abstract process is grounded in concrete Veeva object architecture, data-flow diagrams, and operational decision trees. Twenty-seven interactive SVG process maps — all zoomable — visualise key workflows. A 200+ term glossary provides precise definitions of commercial and medical affairs terminology.</p>
      <div class="fm-meta-grid">
        <div class="fm-meta-item"><span class="fm-meta-label">Scope</span><span class="fm-meta-val">US FDA frameworks; global references where noted</span></div>
        <div class="fm-meta-item"><span class="fm-meta-label">Chapters</span><span class="fm-meta-val">11 + Glossary</span></div>
        <div class="fm-meta-item"><span class="fm-meta-label">Diagrams</span><span class="fm-meta-val">27 interactive SVG process maps</span></div>
        <div class="fm-meta-item"><span class="fm-meta-label">Regulations</span><span class="fm-meta-val">21 CFR Parts 11/50/54/56/312/314/803, GxP, ICH E6/Q10, AKS, Sunshine Act, PDMA, FCA, PhRMA Code</span></div>
        <div class="fm-meta-item"><span class="fm-meta-label">Systems</span><span class="fm-meta-val">Veeva CRM, Vault PromoMats, Vault Medical, Network, Events Mgmt</span></div>
        <div class="fm-meta-item"><span class="fm-meta-label">Edition</span><span class="fm-meta-val">May 2026</span></div>
      </div>
      <p class="fm-keywords"><strong>Keywords:</strong> pharmaceutical commercial affairs · medical affairs · Veeva CRM · Vault PromoMats · FDA regulations · GxP compliance · 21 CFR Part 11 · Anti-Kickback Statute · Sunshine Act · product launch · HCP engagement · MSL operations · pharma operations · drug commercialisation</p>
    </div>
  </div>
</section>

<div class="ch-divider ch-both"></div>

<!-- ══════════════════════════════════════════════
     PREFACE
══════════════════════════════════════════════ -->
<section class="fm-page" id="preface" role="region" aria-label="Preface">
  <div class="fm-inner">
    <div class="fm-label">Preface</div>
    <h2 class="fm-heading">Why This Guide Was Written</h2>
    <div class="fm-rule"></div>
    <div class="fm-body fm-preface-body">
      <p>Pharmaceutical commercial and medical affairs are, in practice, far more technically complex than their descriptions suggest. A "sales rep" operates inside a validated Salesforce platform with seventeen compliance checkpoints before a single sample can be transferred. A "medical science liaison" manages scientific exchange under a documented scientific engagement plan, with every interaction recorded in a CRM and every response letter reviewed by regulatory. A "brand manager" navigates a content approval process — the MLR cycle — that can span four departments, two legal reviews, and a thirty-day regulatory hold before a single slide can be shown to a physician.</p>
      <p>None of this complexity is well-documented in any single place. Regulatory frameworks live in Federal Register notices. Veeva object architecture lives in administrator guides. MSL best-practice lives in MSLS position papers. Process maps live in PowerPoint decks that circulate inside individual companies and are never published externally.</p>
      <p>This guide is my attempt to synthesise everything: the regulatory foundations, the operational processes, the technology systems, and the organisational structures, into a single reference that a practitioner can actually use. Every section is written to answer the question a new hire asks on their first month, a consultant faces before their first engagement, and an experienced professional confronts when they move into a new function.</p>
      <p>The Veeva chapters in particular reflect hard-won knowledge. The object architecture, the permission model, the CLM mechanics, the Network-CRM integration — this is the kind of detail that takes months to learn on the job and rarely appears anywhere in writing. I have tried to document it precisely, with API names, field-level details, and the compliance logic that drives every design decision.</p>
      <p>This is a living document. Regulations change. Veeva releases new platform versions. PhRMA revises its Code. The edition date on the cover page reflects the state of all frameworks as of that month.</p>
      <p>If you are entering pharma for the first time, start with Chapter 1 and read sequentially — the guide is intentionally structured as a story, not a reference manual. If you are an experienced professional looking for a specific topic, the sidebar navigation and the interactive search will take you directly there.</p>
      <div class="fm-sig">
        <div class="fm-sig-name">Deepak Kumar</div>
        <div class="fm-sig-title">Pharma &amp; MedTech Consultant</div>
        <div class="fm-sig-date">May 2026</div>
      </div>
    </div>
  </div>
</section>

<div class="ch-divider ch-both"></div>

<!-- ══════════════════════════════════════════════
     TABLE OF CONTENTS PAGE
══════════════════════════════════════════════ -->
<section class="fm-page fm-toc-page" id="toc-page" role="region" aria-label="Table of Contents">
  <div class="fm-inner fm-toc-inner">
    <div class="fm-label">Contents</div>
    <h2 class="fm-heading">Table of Contents</h2>
    <div class="fm-rule"></div>

    <div class="fm-toc-grid">

      <a href="#intro" class="fm-toc-entry fm-toc-special">
        <span class="fm-toc-num">✦</span>
        <span class="fm-toc-title">Introduction</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Setting the scene — the pharma ecosystem, key stakeholders, and how commercial and medical affairs fit together</span>
      </a>

      <div class="fm-toc-part">Part I — Foundation</div>

      <a href="#ch1" class="fm-toc-entry">
        <span class="fm-toc-num">01</span>
        <span class="fm-toc-title">The Big Picture</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Drug lifecycle from discovery to patent expiry · Market structure · Competitive landscape · Value chain</span>
      </a>

      <a href="#ch2" class="fm-toc-entry">
        <span class="fm-toc-num">02</span>
        <span class="fm-toc-title">R&amp;D — Where It Begins</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Drug Discovery · Target ID → Lead Optimisation → Candidate Selection · Pre-Clinical GLP studies · IND application · Phase I SAD/MAD · Phase II PoC &amp; dose-finding · Phase III pivotal trials · NDA/BLA eCTD submission · FDA review, AdCom &amp; labelling · Expedited programmes (BTD/Fast Track/Priority/Accelerated) · REMS · When Commercial engagement starts · R&amp;D–Commercial interaction model</span>
      </a>

      <div class="fm-toc-part">Part II — Commercial Affairs</div>

      <a href="#ch3" class="fm-toc-entry">
        <span class="fm-toc-num">03</span>
        <span class="fm-toc-title">Commercial Affairs</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Brand planning · Market research · Sales force effectiveness · MLR content approval · HCP engagement · Market access · PDMA sample management · Competitive intelligence</span>
      </a>

      <div class="fm-toc-part">Part III — Medical Affairs</div>

      <a href="#ch4" class="fm-toc-entry">
        <span class="fm-toc-num">04</span>
        <span class="fm-toc-title">Medical Affairs</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Medical strategy · Evidence generation · MSL field operations · Medical information · Publications · Pharmacovigilance &amp; adverse event reporting</span>
      </a>

      <div class="fm-toc-part">Part IV — Integration</div>

      <a href="#ch5" class="fm-toc-entry">
        <span class="fm-toc-num">05</span>
        <span class="fm-toc-title">The Commercial–Medical Firewall</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Why the firewall exists · What is and isn't permitted · OPDP enforcement · Practical cross-functional governance</span>
      </a>

      <a href="#ch6" class="fm-toc-entry">
        <span class="fm-toc-num">06</span>
        <span class="fm-toc-title">The R&amp;D Bridge</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Phase III-to-launch transition · Medical-commercial co-creation · Health economics · Access strategy · KOL development</span>
      </a>

      <a href="#ch7" class="fm-toc-entry">
        <span class="fm-toc-num">07</span>
        <span class="fm-toc-title">The Launch!</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">36-month launch timeline · Pre-launch build · Day 1 readiness · Post-launch optimisation · Milestone tracking</span>
      </a>

      <div class="fm-toc-part">Part V — People &amp; Rules</div>

      <a href="#ch8" class="fm-toc-entry">
        <span class="fm-toc-num">08</span>
        <span class="fm-toc-title">The People</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Every role in commercial and medical affairs · Org structures · Career paths · Cross-functional accountability maps</span>
      </a>

      <a href="#ch9" class="fm-toc-entry">
        <span class="fm-toc-num">09</span>
        <span class="fm-toc-title">The Rules</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">21 CFR framework · GxP (GLP/GCP/GMP) · Anti-Kickback Statute · Sunshine Act · PDMA · False Claims Act · PhRMA Code · ICH guidelines · 21 CFR Part 11</span>
      </a>

      <a href="#ch10" class="fm-toc-entry">
        <span class="fm-toc-num">10</span>
        <span class="fm-toc-title">Putting It Together</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">How all functions align around a product · Annual operating cycle · Integrated planning · Cross-functional decision rights</span>
      </a>

      <div class="fm-toc-part">Part VI — Systems</div>

      <a href="#ch11" class="fm-toc-entry">
        <span class="fm-toc-num">11</span>
        <span class="fm-toc-title">Veeva Systems</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">Veeva CRM object architecture · Commercial &amp; MSL workflows · CLM loop · Vault PromoMats MLR · Vault Medical · Network MDM · Events Management · User Management &amp; permissions</span>
      </a>

      <div class="fm-toc-part">Reference</div>

      <a href="#glossary" class="fm-toc-entry fm-toc-special">
        <span class="fm-toc-num">A–Z</span>
        <span class="fm-toc-title">Glossary</span>
        <span class="fm-toc-dots"></span>
        <span class="fm-toc-desc">200+ definitions covering commercial affairs, medical affairs, regulatory, and Veeva platform terminology</span>
      </a>

    </div>
  </div>
</section>

<div class="ch-divider ch-both"></div>

"""

HTML = f'''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pharma Commercial &amp; Medical Affairs — The Complete Visual Guide · Deepak Kumar</title>

<!-- Google Fonts: elegant serif + clean sans -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ════════════════════════════════════════════════════════════════════════════
   DESIGN TOKENS  (3 themes: light / sepia / dark)
   ════════════════════════════════════════════════════════════════════════════ */
:root {{
  /* Brand palette */
  --navy:   #1B3A6B;
  --teal:   #0B5E5E;
  --purple: #4A2080;
  --green:  #1A5C34;
  --orange: #B85010;
  --gold:   #8B6914;
  --red:    #7A1515;

  /* Chapter accent colours */
  --comm:   #1B3A6B;
  --med:    #0B5E5E;
  --rd:     #4A2080;
  --launch: #B85010;
  --access: #1A5C34;
  --veeva-accent: #E05A00;

  /* Font scale */
  --base-size: 17px;
  --line-height: 1.95;
  --text-font:  'EB Garamond', 'Libre Baskerville', Georgia, serif;
  --ui-font:    'Inter', 'Segoe UI', system-ui, sans-serif;
  --mono-font:  'Fira Code', 'Cascadia Code', monospace;

  /* Layout */
  --toc-width:  300px;
  --content-max: 820px;
  --ch-padding-x: 96px;
  --ch-padding-y: 80px;

  /* Transitions */
  --ease: cubic-bezier(.4,0,.2,1);
}}

/* ── Light theme (default) ── */
[data-theme="light"] {{
  --bg:         #FAFAF7;
  --bg-alt:     #F5F3EE;
  --bg-toc:     #F0EDE5;
  --surface:    #FFFFFF;
  --ink:        #1A1A2A;
  --ink-2:      #374151;
  --ink-3:      #6B7280;
  --border:     #D4C9B0;
  --border-2:   #E5DDD0;
  --highlight:  #FFF9C4;
  --link:       var(--navy);
  --rule:       rgba(0,0,0,.08);
}}

/* ── Sepia theme ── */
[data-theme="sepia"] {{
  --bg:         #F4ECD8;
  --bg-alt:     #EEE4CC;
  --bg-toc:     #E8DDCA;
  --surface:    #FBF5E8;
  --ink:        #2C1F0E;
  --ink-2:      #4A3520;
  --ink-3:      #7A6045;
  --border:     #C8A87A;
  --border-2:   #D4BCA0;
  --highlight:  #FFE8A0;
  --link:       #6B3A10;
  --rule:       rgba(100,60,0,.12);
}}

/* ── Dark theme ── */
[data-theme="dark"] {{
  --bg:         #12141A;
  --bg-alt:     #1A1D26;
  --bg-toc:     #0E1016;
  --surface:    #1E2130;
  --ink:        #E2E8F0;
  --ink-2:      #CBD5E1;
  --ink-3:      #8B949E;
  --border:     #2D3748;
  --border-2:   #374151;
  --highlight:  #3D3A00;
  --link:       #7EB3E8;
  --rule:       rgba(255,255,255,.06);
  --navy:       #4A7ABF;
  --teal:       #2A9A9A;
}}

/* ════════════════════════════════════════════════════════════════════════════
   RESET & BASE
   ════════════════════════════════════════════════════════════════════════════ */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; font-size: var(--base-size); }}
body {{
  font-family: var(--text-font);
  background: var(--bg);
  color: var(--ink);
  line-height: var(--line-height);
  -webkit-font-smoothing: antialiased;
  transition: background .3s var(--ease), color .3s var(--ease);
}}
a {{ color: var(--link); text-decoration: none; }}
img, svg {{ max-width: 100%; }}


/* ── Veeva CRM expanded styles ── */
.crm-obj-grid {{
  display: grid; grid-template-columns: 1fr 1fr; gap: 18px;
  margin: 20px 0 36px;
}}
.crm-obj-card {{
  background: #161B22; border-radius: 6px;
  padding: 14px 16px;
}}
.crm-obj-card.comm {{
  border-left: 3px solid #4A7ABF;
  border-top: 1px solid #1B3A6B; border-right: 1px solid #1B3A6B; border-bottom: 1px solid #1B3A6B;
}}
.crm-obj-card.med {{
  border-left: 3px solid #2A9A9A;
  border-top: 1px solid #0B5E5E; border-right: 1px solid #0B5E5E; border-bottom: 1px solid #0B5E5E;
}}
.crm-obj-card.shared {{
  border-left: 3px solid #9060D0;
  border-top: 1px solid #4A2080; border-right: 1px solid #4A2080; border-bottom: 1px solid #4A2080;
}}
.crm-section-label {{
  font-family: var(--ui-font); font-size: 9px; font-weight: 700;
  letter-spacing: 2.5px; text-transform: uppercase;
  padding-bottom: 8px; margin-bottom: 16px; margin-top: 28px;
  border-bottom: 1px solid;
}}
.crm-section-label.comm {{ color: #4A7ABF; border-color: #1B3A6B; }}
.crm-section-label.med  {{ color: #2A9A9A; border-color: #0B5E5E; }}
.crm-obj-name {{ font-size: 12.5px; font-weight: 700; margin-bottom: 3px; }}
.crm-obj-name.comm   {{ color: #7EC8C8; }}
.crm-obj-name.med    {{ color: #2A9A9A; }}
.crm-obj-name.shared {{ color: #C0A0FF; }}
.crm-obj-api  {{ font-size: 9px; font-family: monospace; color: #3A6090; margin-bottom: 8px; letter-spacing: .3px; }}
.crm-obj-api.med {{ color: #1A5050; }}
.crm-obj-desc {{ font-size: 11.5px; color: #8B949E; line-height: 1.65; }}
.crm-obj-fields {{ margin-top: 8px; }}
.crm-field-pill {{
  display: inline-block; background: #0D1117; border: 1px solid #30363D;
  border-radius: 3px; padding: 2px 7px; font-size: 9.5px;
  color: #6B7280; margin: 2px 3px 2px 0; font-family: monospace;
}}
@media (max-width: 700px) {{ .crm-obj-grid {{ grid-template-columns: 1fr; }} }}
/* ════════════════════════════════════════════════════════════════════════════
   READING PROGRESS BAR
   ════════════════════════════════════════════════════════════════════════════ */
#progress-bar {{
  position: fixed; top: 0; left: 0; height: 3px; z-index: 9999;
  background: linear-gradient(90deg, var(--navy), var(--teal), var(--orange));
  width: 0%; transition: width .08s linear;
}}

/* ════════════════════════════════════════════════════════════════════════════
   READING CONTROLS BAR  (top-right strip)
   ════════════════════════════════════════════════════════════════════════════ */
#reader-controls {{
  position: fixed; top: 6px; right: 16px; z-index: 9990;
  display: flex; align-items: center; gap: 6px;
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 24px; padding: 5px 12px;
  box-shadow: 0 2px 12px rgba(0,0,0,.15);
  font-family: var(--ui-font); font-size: 11px;
}}
#reader-controls button {{
  border: none; background: none; cursor: pointer; padding: 4px 7px;
  border-radius: 12px; color: var(--ink-2); font-family: var(--ui-font);
  font-size: 12px; transition: background .15s;
}}
#reader-controls button:hover {{ background: var(--bg-alt); }}
#reader-controls .ctrl-sep {{
  width: 1px; height: 16px; background: var(--border); margin: 0 2px;
}}
.theme-btn {{ font-size: 14px !important; }}

/* ════════════════════════════════════════════════════════════════════════════
   FULL-SCREEN COVER
   ════════════════════════════════════════════════════════════════════════════ */
.cover {{
  min-height: 100vh;
  background: linear-gradient(150deg, #060E1F 0%, #0F2350 35%, #0B4040 70%, #1A0A30 100%);
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center; padding: 80px 48px;
  position: relative; overflow: hidden;
}}

/* Noise texture overlay */
.cover::before {{
  content: '';
  position: absolute; inset: 0;
  background-image:
    radial-gradient(ellipse 80% 50% at 50% -10%, rgba(27,58,107,.6) 0%, transparent 70%),
    url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='.04'/%3E%3C/svg%3E");
  pointer-events: none;
}}

/* Decorative ornament lines */
.cover-ornament {{
  width: 120px; height: 1px; background: rgba(255,255,255,.2);
  margin: 0 auto 36px; position: relative;
}}
.cover-ornament::before, .cover-ornament::after {{
  content: '◈';
  position: absolute; top: 50%; transform: translateY(-50%);
  color: rgba(255,255,255,.35); font-size: 10px;
}}
.cover-ornament::before {{ left: -20px; }}
.cover-ornament::after  {{ right: -20px; }}

.cover-badge {{
  background: rgba(255,255,255,.08);
  border: 1px solid rgba(255,255,255,.2);
  color: rgba(255,255,255,.7); font-family: var(--ui-font);
  font-size: 10px; letter-spacing: 4px; text-transform: uppercase;
  padding: 8px 28px; border-radius: 24px; margin-bottom: 48px;
  position: relative;
}}
.cover h1 {{
  font-family: 'EB Garamond', Georgia, serif;
  font-size: clamp(38px, 5vw, 64px);
  font-weight: 500; color: #FFFFFF;
  line-height: 1.1; max-width: 820px;
  margin-bottom: 20px; position: relative;
  letter-spacing: -.5px;
}}
.cover h1 em {{ color: #7EC8C8; font-style: normal; }}
.cover .subtitle {{
  font-size: clamp(14px, 1.5vw, 18px);
  color: rgba(255,255,255,.65);
  max-width: 620px; font-style: italic;
  margin-bottom: 16px; line-height: 1.8; position: relative;
  font-family: 'EB Garamond', Georgia, serif;
}}
.cover .author {{
  font-size: 15px; color: #7EC8C8;
  font-family: var(--ui-font); font-weight: 600;
  letter-spacing: 1px; margin-bottom: 56px; position: relative;
}}
.cover-pills {{
  display: flex; flex-wrap: wrap; gap: 10px;
  justify-content: center; margin-bottom: 64px; position: relative;
}}
.cover-pill {{
  background: rgba(255,255,255,.1);
  border: 1px solid rgba(255,255,255,.2);
  color: rgba(255,255,255,.85);
  font-family: var(--ui-font); font-size: 11px;
  padding: 5px 15px; border-radius: 14px; letter-spacing: .3px;
}}
.cover-meta {{
  color: rgba(255,255,255,.35); font-family: var(--ui-font);
  font-size: 11px; line-height: 2; position: relative;
}}
.cover-scroll {{
  position: absolute; bottom: 32px; left: 50%;
  transform: translateX(-50%);
  color: rgba(255,255,255,.35); font-family: var(--ui-font);
  font-size: 11px; letter-spacing: 2px; text-transform: uppercase;
  cursor: pointer; animation: bounce 2.5s ease infinite;
}}
@keyframes bounce {{
  0%,100% {{ transform: translateX(-50%) translateY(0); }}
  50%      {{ transform: translateX(-50%) translateY(8px); }}
}}

/* ════════════════════════════════════════════════════════════════════════════
   LAYOUT SHELL
   ════════════════════════════════════════════════════════════════════════════ */
.wrapper {{
  display: flex;
  max-width: 1560px;
  margin: 0 auto;
}}

/* ════════════════════════════════════════════════════════════════════════════
   SIDEBAR TABLE OF CONTENTS
   ════════════════════════════════════════════════════════════════════════════ */
.toc {{
  width: var(--toc-width);
  flex-shrink: 0;
  background: var(--bg-toc);
  border-right: 1px solid var(--border);
  position: sticky; top: 0; height: 100vh;
  overflow-y: auto; overflow-x: hidden;
  padding: 28px 18px 32px 22px;
  transition: background .3s var(--ease);
  scrollbar-width: thin;
  scrollbar-color: var(--border) transparent;
}}
.toc::-webkit-scrollbar {{ width: 4px; }}
.toc::-webkit-scrollbar-track {{ background: transparent; }}
.toc::-webkit-scrollbar-thumb {{ background: var(--border); border-radius: 2px; }}


/* ════════════════════════════════════════════════════════════════════════════
   GOOGLE SEARCH BAR + MODAL
   ════════════════════════════════════════════════════════════════════════════ */
.gsearch-wrap {{
  display: flex; align-items: center; gap: 4px;
}}
.gsearch-input {{
  width: 130px; padding: 4px 8px; border-radius: 14px;
  border: 1px solid var(--border); background: var(--bg-alt);
  color: var(--ink); font-family: var(--ui-font); font-size: 11px;
  outline: none; transition: width .2s, border-color .2s;
}}
.gsearch-input:focus {{ width: 180px; border-color: #7EC8C8; }}
.gsearch-btn {{
  border: 1px solid var(--border) !important; background: var(--bg-alt) !important;
  color: var(--ink-2) !important; border-radius: 10px !important;
  padding: 3px 9px !important; font-size: 11px !important; cursor: pointer;
  transition: background .15s !important;
}}
.gsearch-btn:hover {{ background: #7EC8C8 !important; color: #fff !important; border-color: #7EC8C8 !important; }}

/* Modal overlay */
.gsearch-modal-overlay {{
  display: none; position: fixed; inset: 0; z-index: 10000;
  background: rgba(0,0,0,.75);
  flex-direction: column;
  align-items: center; justify-content: center;
}}
.gsearch-modal-overlay.open {{ display: flex; }}

.gsearch-modal-bar {{
  width: 92%; max-width: 980px;
  background: #111c2e; border-radius: 10px 10px 0 0;
  border-bottom: 1px solid #2a3a5a;
  display: flex; align-items: center; gap: 10px;
  padding: 10px 16px; flex-shrink: 0;
  font-family: var(--ui-font);
}}
.gsearch-modal-title {{
  color: #7ec8c8; font-size: 13px; font-weight: 700; white-space: nowrap;
}}
.gsearch-modal-input {{
  flex: 1; padding: 6px 12px; border-radius: 20px;
  border: 1px solid #2a3a5a; background: #0d1828;
  color: #c8d8f0; font-size: 13px; font-family: var(--ui-font);
  outline: none;
}}
.gsearch-modal-input:focus {{ border-color: #7EC8C8; }}
.gsearch-modal-go {{
  background: #7EC8C8; color: #0d1828; border: none;
  padding: 6px 16px; border-radius: 16px; font-size: 13px;
  font-weight: 700; cursor: pointer; font-family: var(--ui-font);
  transition: background .15s;
}}
.gsearch-modal-go:hover {{ background: #a0e0e0; }}
.gsearch-modal-close {{
  background: none; border: 1px solid #3a4a6a; color: #c8d8f0;
  padding: 5px 12px; border-radius: 16px; font-size: 13px;
  cursor: pointer; font-family: var(--ui-font); transition: background .15s;
}}
.gsearch-modal-close:hover {{ background: #2a4060; color: #fff; }}

.gsearch-modal-panel {{
  width: 92%; max-width: 680px;
  background: #111c2e; border-radius: 14px;
  box-shadow: 0 20px 60px rgba(0,0,0,.7);
  overflow: hidden;
}}
.gsearch-engines {{
  display: flex; gap: 10px; flex-wrap: wrap;
  padding: 20px 20px 10px;
}}
.gse-btn {{
  display: flex; align-items: center; gap: 7px;
  padding: 10px 20px; border-radius: 10px; border: none;
  font-size: 14px; font-weight: 600; cursor: pointer;
  font-family: var(--ui-font); transition: transform .1s, box-shadow .15s;
}}
.gse-btn:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px rgba(0,0,0,.3); }}
.gse-google  {{ background: #fff; color: #3c4043; }}
.gse-bing    {{ background: #008373; color: #fff; }}
.gse-scholar {{ background: #4285f4; color: #fff; }}
.gse-pubmed  {{ background: #336699; color: #fff; }}
.gse-fda     {{ background: #cc0000; color: #fff; }}
.gsearch-note {{
  font-size: 11px; color: #4a6080; padding: 10px 20px 20px;
  font-family: var(--ui-font); line-height: 1.5;
}}
@media print {{
  .gsearch-modal-overlay, .gsearch-wrap {{ display: none !important; }}
}}

/* ════════════════════════════════════════════════════════════════════════════
   FRONT MATTER — Abstract, Preface, Table of Contents pages
   ════════════════════════════════════════════════════════════════════════════ */
.fm-page {{
  max-width: 860px; margin: 60px auto; padding: 0 32px 60px;
}}
.fm-inner {{
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 16px;
  padding: 48px 56px;
  box-shadow: 0 4px 32px rgba(0,0,0,.1);
}}
.fm-label {{
  font-family: var(--ui-font); font-size: 10px; font-weight: 800;
  letter-spacing: 3px; text-transform: uppercase;
  color: var(--accent); margin-bottom: 12px;
}}
.fm-heading {{
  font-family: var(--head-font); font-size: 2rem; font-weight: 700;
  color: var(--ink); margin: 0 0 20px; line-height: 1.2;
}}
.fm-rule {{
  width: 60px; height: 3px; background: var(--accent);
  border-radius: 2px; margin-bottom: 32px;
}}
.fm-body {{
  font-size: 1rem; line-height: 1.8; color: var(--ink-2);
}}
.fm-body p {{ margin: 0 0 18px; }}
.fm-body p:last-child {{ margin-bottom: 0; }}

/* Abstract meta grid */
.fm-meta-grid {{
  display: grid; grid-template-columns: 1fr 1fr;
  gap: 14px 24px; margin: 28px 0;
  padding: 24px; background: var(--bg-alt);
  border-radius: 10px; border: 1px solid var(--border);
}}
.fm-meta-item {{ display: flex; flex-direction: column; gap: 3px; }}
.fm-meta-label {{
  font-family: var(--ui-font); font-size: 9px; font-weight: 800;
  letter-spacing: 2px; text-transform: uppercase; color: var(--accent);
}}
.fm-meta-val {{ font-size: 13px; color: var(--ink); line-height: 1.4; }}
.fm-keywords {{
  font-size: 12px !important; color: var(--ink-3) !important;
  font-style: italic; padding: 16px; background: var(--bg-alt);
  border-radius: 8px; border-left: 3px solid var(--accent);
}}

/* Preface signature */
.fm-sig {{
  margin-top: 36px; padding-top: 24px;
  border-top: 1px solid var(--border);
}}
.fm-sig-name {{
  font-family: var(--head-font); font-size: 1.1rem; font-weight: 700;
  color: var(--ink);
}}
.fm-sig-title {{ font-size: 13px; color: var(--accent); margin-top: 2px; }}
.fm-sig-date  {{ font-size: 12px; color: var(--ink-3); margin-top: 4px; }}

/* TOC page */
.fm-toc-inner {{ padding: 48px 48px 40px; }}
.fm-toc-grid {{ display: flex; flex-direction: column; gap: 4px; margin-top: 8px; }}
.fm-toc-part {{
  font-family: var(--ui-font); font-size: 9px; font-weight: 800;
  letter-spacing: 3px; text-transform: uppercase;
  color: var(--ink-3); padding: 18px 0 6px;
  border-bottom: 1px solid var(--border); margin-bottom: 4px;
}}
.fm-toc-entry {{
  display: grid;
  grid-template-columns: 36px 1fr;
  grid-template-rows: auto auto;
  column-gap: 18px;
  padding: 12px 16px; border-radius: 10px;
  text-decoration: none; color: inherit;
  transition: background .15s;
  border: 1px solid transparent;
}}
.fm-toc-entry:hover {{
  background: var(--bg-alt);
  border-color: var(--border);
}}
.fm-toc-num {{
  grid-row: 1 / 3;
  font-family: var(--ui-font); font-size: 22px; font-weight: 900;
  color: var(--accent); line-height: 1;
  align-self: center; text-align: center;
}}
.fm-toc-title {{
  font-family: var(--head-font); font-size: 1rem; font-weight: 700;
  color: var(--ink); line-height: 1.2;
  grid-column: 2; grid-row: 1;
}}
.fm-toc-dots {{ display: none; }}
.fm-toc-desc {{
  font-size: 12px; color: var(--ink-3); line-height: 1.5;
  grid-column: 2; grid-row: 2; margin-top: 3px;
}}
.fm-toc-special .fm-toc-num {{
  font-size: 16px; color: var(--ink-2);
}}
@media print {{
  .fm-page {{ page-break-after: always; }}
  .fm-inner {{ box-shadow: none; border: 1px solid #ccc; }}
}}
@media (max-width: 640px) {{
  .fm-inner {{ padding: 28px 20px; }}
  .fm-meta-grid {{ grid-template-columns: 1fr; }}
}}
.toc-brand {{
  text-align: center;
  padding-bottom: 18px;
  border-bottom: 1px solid var(--border);
  margin-bottom: 18px;
}}
.toc-brand-avatar {{
  width: 46px; height: 46px; border-radius: 50%;
  object-fit: cover; object-position: center top;
  border: 2px solid #7EC8C8;
  display: block; margin: 0 auto 8px;
  flex-shrink: 0;
}}
.cover-avatar {{
  width: 88px; height: 88px; border-radius: 50%;
  object-fit: cover; object-position: center top;
  border: 3px solid #7EC8C8;
  display: block; margin: 0 auto 18px;
  box-shadow: 0 0 24px rgba(126,200,200,.35);
}}
.toc-brand .name {{
  font-family: var(--ui-font); font-size: 13px;
  font-weight: 700; color: var(--navy); letter-spacing: .2px;
}}
.toc-brand .sub {{
  font-family: var(--ui-font); font-size: 10px;
  color: var(--ink-3); margin-top: 3px;
}}

.toc-search {{
  width: 100%; padding: 8px 12px;
  font-size: 12px; font-family: var(--ui-font);
  background: var(--surface); border: 1px solid var(--border);
  border-radius: 8px; color: var(--ink); outline: none;
  margin-bottom: 20px; transition: border-color .2s;
}}
.toc-search:focus {{ border-color: var(--navy); box-shadow: 0 0 0 2px rgba(27,58,107,.12); }}

/* Section headers inside TOC */
.toc-section {{
  font-family: var(--ui-font); font-size: 9px; font-weight: 700;
  letter-spacing: 2.5px; text-transform: uppercase;
  color: var(--ink-3); margin: 18px 0 6px;
  padding-bottom: 5px; border-bottom: 1px solid var(--border-2);
}}
.toc a {{
  display: flex; align-items: center; gap: 8px;
  text-decoration: none; color: var(--ink-2);
  font-family: var(--ui-font); font-size: 12px;
  padding: 4px 8px; border-radius: 6px;
  transition: background .15s, color .15s, border-left-color .15s;
  border-left: 2px solid transparent; margin-bottom: 1px;
  line-height: 1.4;
}}
.toc a:hover {{
  background: rgba(27,58,107,.07);
  color: var(--navy);
  border-left-color: var(--navy);
}}
.toc a.ch {{
  font-weight: 600; font-size: 11.5px;
  color: var(--ink); margin-top: 6px;
}}
.toc a.sub {{
  padding-left: 20px; color: var(--ink-3);
  font-size: 11px;
}}
.toc a.active {{
  background: rgba(27,58,107,.1);
  color: var(--navy); border-left-color: var(--navy);
  font-weight: 600;
}}
/* Small dot indicator in TOC for active */
.toc a.active::before {{ content: '▸'; font-size: 9px; color: var(--navy); }}

/* ════════════════════════════════════════════════════════════════════════════
   MAIN CONTENT AREA
   ════════════════════════════════════════════════════════════════════════════ */
.content {{ flex: 1; min-width: 0; }}

/* ════════════════════════════════════════════════════════════════════════════
   CHAPTER — BOOK PAGE LAYOUT
   ════════════════════════════════════════════════════════════════════════════ */
.chapter {{
  padding: var(--ch-padding-y) var(--ch-padding-x);
  max-width: calc(var(--content-max) + var(--ch-padding-x) * 2);
  border-bottom: 1px solid var(--border);
  background: var(--bg);
  transition: background .3s var(--ease);
  position: relative;
}}
.chapter:nth-child(even) {{ background: var(--bg-alt); }}

/* Running chapter label at top of each chapter */
.ch-running {{
  font-family: var(--ui-font); font-size: 9px; letter-spacing: 3px;
  text-transform: uppercase; color: var(--ink-3);
  margin-bottom: 40px; display: flex; align-items: center; gap: 16px;
}}
.ch-running::after {{
  content: ''; flex: 1; height: 1px; background: var(--border-2);
}}

/* Decorative chapter number — large, faded, behind heading */
.ch-decorator {{
  display: flex; align-items: flex-start; gap: 28px; margin-bottom: 8px;
}}
.ch-big-num {{
  font-family: 'EB Garamond', Georgia, serif;
  font-size: 96px; line-height: .85; font-weight: 700;
  color: var(--border); flex-shrink: 0; user-select: none;
  margin-top: -8px; letter-spacing: -4px;
}}
.ch-heading-block {{ flex: 1; }}

.ch-label {{
  font-family: var(--ui-font); font-size: 10px;
  letter-spacing: 3px; text-transform: uppercase;
  color: var(--ink-3); margin-bottom: 10px;
  display: flex; align-items: center; gap: 10px;
}}
.ch-pill {{
  display: inline-block; padding: 3px 12px;
  border-radius: 12px; font-size: 9px; font-weight: 700;
  letter-spacing: 1.5px; text-transform: uppercase; color: white;
}}

/* Chapter main heading */
.chapter h1 {{
  font-family: 'EB Garamond', Georgia, serif;
  font-size: clamp(28px, 3vw, 42px);
  font-weight: 500; line-height: 1.15;
  color: var(--ink); margin-bottom: 12px;
  letter-spacing: -.3px;
}}

/* Chapter lead / epigraph */
.chapter .lead {{
  font-size: 19px; color: var(--ink-3);
  font-style: italic; margin-bottom: 52px;
  line-height: 1.8; max-width: 680px;
  border-left: 3px solid var(--border);
  padding-left: 24px; padding-top: 4px; padding-bottom: 4px;
  font-family: 'EB Garamond', Georgia, serif;
}}

/* Drop cap on first paragraph of each chapter */
.chapter > p:first-of-type::first-letter,
.chapter .drop-cap::first-letter {{
  float: left; font-family: 'EB Garamond', Georgia, serif;
  font-size: 4.2em; line-height: .82; font-weight: 700;
  color: var(--navy); margin: 4px 10px 0 0;
  padding: 0 4px 4px 0;
}}

/* Section headings */
.chapter h2 {{
  font-family: 'EB Garamond', Georgia, serif;
  font-size: clamp(20px, 2vw, 27px); font-weight: 600;
  margin: 64px 0 18px; color: var(--ink);
  padding-bottom: 10px;
  border-bottom: 2px solid var(--border);
  letter-spacing: -.2px;
}}
/* Ornament before h2 */
.chapter h2::before {{
  content: '§ '; color: var(--border); font-size: .85em;
  font-weight: 400;
}}
.chapter h3 {{
  font-family: 'EB Garamond', Georgia, serif;
  font-size: 21px; font-weight: 600;
  margin: 44px 0 14px; color: var(--navy);
}}
.chapter h4 {{
  font-family: var(--ui-font); font-size: 11px; font-weight: 700;
  margin: 28px 0 10px; color: var(--teal);
  text-transform: uppercase; letter-spacing: 1.5px;
}}
.chapter p {{
  margin-bottom: 20px; text-align: justify;
  hyphens: auto; -webkit-hyphens: auto;
}}
.chapter ul, .chapter ol {{
  margin: 14px 0 22px 26px;
}}
.chapter li {{ margin-bottom: 10px; }}
.chapter strong {{ color: var(--navy); }}

/* Ornamental section rule */
.ornament {{
  text-align: center; color: var(--border);
  margin: 48px 0; font-size: 18px; letter-spacing: 16px;
  user-select: none;
}}

/* ════════════════════════════════════════════════════════════════════════════
   CALLOUT BOXES  (redesigned with book-like feel)
   ════════════════════════════════════════════════════════════════════════════ */
.callout {{
  border-radius: 4px; padding: 24px 30px;
  margin: 36px 0; font-size: 15.5px;
  position: relative;
}}
.callout-title {{
  font-family: var(--ui-font); font-size: 10px; font-weight: 700;
  text-transform: uppercase; letter-spacing: 2px;
  margin-bottom: 12px; display: flex; align-items: center; gap: 8px;
}}
.callout::before {{
  content: ''; position: absolute;
  top: 0; left: 0; bottom: 0; width: 4px; border-radius: 4px 0 0 4px;
}}

.analogy   {{ background: #FFF9EE; border: 1px solid #E8D080; }}
.analogy::before {{ background: #C8A010; }}
.analogy .callout-title {{ color: #8B6914; }}

.keyterm   {{ background: #EEF4FF; border: 1px solid #C0D4F0; }}
.keyterm::before {{ background: var(--navy); }}
.keyterm .callout-title {{ color: var(--navy); }}

.warning   {{ background: #FFF0F0; border: 1px solid #F0C0C0; }}
.warning::before {{ background: #B01010; }}
.warning .callout-title {{ color: #B01010; }}

.insight   {{ background: #EDFAF5; border: 1px solid #A8DCC8; }}
.insight::before {{ background: var(--teal); }}
.insight .callout-title {{ color: var(--teal); }}

.launch-box {{ background: #FFF5EE; border: 1px solid #F0C0A0; }}
.launch-box::before {{ background: var(--orange); }}
.launch-box .callout-title {{ color: var(--orange); }}

/* Dark theme overrides for callout boxes */
[data-theme="dark"] .analogy    {{ background: #2A2000; border-color: #504000; }}
[data-theme="dark"] .keyterm    {{ background: #0A1830; border-color: #1A3060; }}
[data-theme="dark"] .warning    {{ background: #200808; border-color: #401010; }}
[data-theme="dark"] .insight    {{ background: #062018; border-color: #103020; }}
[data-theme="dark"] .launch-box {{ background: #1E0D00; border-color: #3A1A00; }}

/* ════════════════════════════════════════════════════════════════════════════
   FLOW STEPS
   ════════════════════════════════════════════════════════════════════════════ */
.flow {{
  display: flex; flex-wrap: wrap; gap: 0;
  margin: 28px 0; align-items: center;
}}
.flow-step {{
  background: var(--navy); color: white;
  padding: 10px 18px; border-radius: 6px;
  font-family: var(--ui-font); font-size: 12px;
  font-weight: 600; text-align: center;
}}
.flow-arrow {{ color: var(--ink-3); font-size: 18px; padding: 0 6px; }}
.flow.teal   .flow-step {{ background: var(--teal); }}
.flow.purple .flow-step {{ background: var(--purple); }}
.flow.orange .flow-step {{ background: var(--orange); }}
.flow.green  .flow-step {{ background: var(--green); }}

/* ════════════════════════════════════════════════════════════════════════════
   ROLE CARDS
   ════════════════════════════════════════════════════════════════════════════ */
.role-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 20px; margin: 28px 0;
}}
.role-card {{
  border: 1px solid var(--border); border-radius: 8px;
  padding: 22px; background: var(--surface);
  border-top: 3px solid var(--navy);
  transition: box-shadow .2s;
}}
.role-card:hover {{ box-shadow: 0 4px 20px rgba(0,0,0,.1); }}
.role-card.med    {{ border-top-color: var(--teal); }}
.role-card.rd     {{ border-top-color: var(--purple); }}
.role-card.access {{ border-top-color: var(--green); }}
.role-title  {{ font-family: var(--ui-font); font-weight: 700; font-size: 14px; color: var(--ink); margin-bottom: 6px; }}
.role-dept   {{ font-family: var(--ui-font); font-size: 9px; text-transform: uppercase; letter-spacing: 1.5px; color: var(--ink-3); margin-bottom: 12px; }}
.role-card p {{ font-size: 13px; color: var(--ink-2); margin: 0; text-align: left; }}

/* ════════════════════════════════════════════════════════════════════════════
   CHAPTER COLOUR DIVIDERS
   ════════════════════════════════════════════════════════════════════════════ */
.ch-divider {{ height: 6px; }}
.ch-comm   {{ background: linear-gradient(90deg, #1B3A6B, #4A7ABF); }}
.ch-med    {{ background: linear-gradient(90deg, #0B5E5E, #2A9A9A); }}
.ch-rd     {{ background: linear-gradient(90deg, #4A2080, #9060D0); }}
.ch-launch {{ background: linear-gradient(90deg, #B85010, #E87030); }}
.ch-both   {{ background: linear-gradient(90deg, #1B3A6B 0%, #0B5E5E 100%); }}
.ch-veeva  {{ background: linear-gradient(90deg, #7A3000, #E05A00); }}
.ch-gloss  {{ background: linear-gradient(90deg, #4A5568, #718096); }}

/* ════════════════════════════════════════════════════════════════════════════
   TIMELINE
   ════════════════════════════════════════════════════════════════════════════ */
.timeline {{ margin: 36px 0; }}
.tl-item {{
  display: flex; gap: 22px;
  margin-bottom: 28px; position: relative;
}}
.tl-marker {{
  flex-shrink: 0; width: 44px; height: 44px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--ui-font); font-weight: 700; font-size: 12px; color: white;
}}
.tl-line {{
  position: absolute; left: 22px; top: 44px;
  bottom: -28px; width: 2px; background: var(--border);
}}
.tl-body {{ flex: 1; padding-top: 10px; }}
.tl-body h4 {{
  font-size: 15px; margin: 0 0 6px;
  font-family: var(--ui-font); font-weight: 600;
}}
.tl-body p {{ font-size: 14px; color: var(--ink-2); margin: 0; text-align: left; }}

/* ════════════════════════════════════════════════════════════════════════════
   PHASE BANNER
   ════════════════════════════════════════════════════════════════════════════ */
.phase-banner {{
  border-radius: 8px; padding: 22px 28px;
  margin: 32px 0; display: flex; align-items: flex-start; gap: 20px;
}}
.phase-icon {{ font-size: 32px; flex-shrink: 0; line-height: 1; }}
.phase-body h3 {{ font-size: 18px; margin: 0 0 8px; }}
.phase-body p  {{ font-size: 14px; margin: 0; text-align: left; }}

/* ════════════════════════════════════════════════════════════════════════════
   BLOCK QUOTE  (book style)
   ════════════════════════════════════════════════════════════════════════════ */
blockquote {{
  margin: 36px 0; padding: 20px 28px;
  border-left: 3px solid var(--navy);
  background: var(--bg-alt);
  border-radius: 0 6px 6px 0;
  font-style: italic; font-size: 18px;
  font-family: 'EB Garamond', Georgia, serif;
  color: var(--ink-2); line-height: 1.8;
}}

/* ════════════════════════════════════════════════════════════════════════════
   VISUAL EMBED (SVG diagram containers)
   ════════════════════════════════════════════════════════════════════════════ */
.vis-embed {{
  margin: 44px 0; border-radius: 10px; overflow: hidden;
  border: 1px solid #2A3A5A;
  box-shadow: 0 6px 32px rgba(0,0,0,.22);
}}
.vis-label {{
  background: #1A2A4A; color: #D0D8E8;
  font-family: var(--ui-font); font-size: 10.5px; font-weight: 700;
  letter-spacing: 1px; padding: 11px 22px;
  text-transform: uppercase; display: flex; align-items: center; gap: 10px;
}}
.vis-icon {{ font-size: 12px; color: #7EC8C8; }}
.vis-inner {{
  background: #0D1117; overflow-x: auto; padding: 24px;
}}
.vis-cap {{
  background: #0D1117; color: #4A5568;
  font-family: var(--ui-font); font-size: 10px;
  text-align: center; padding: 8px; font-style: italic;
  border-top: 1px solid #1E2A3A;
}}
.vis-inner .sec {{
  padding: 0 !important; border: none !important; background: transparent !important;
}}
.vis-inner .sec-title {{ font-size: 16px !important; margin-bottom: 4px !important; }}
.vis-inner .dbox {{
  background: #161B22; border-radius: 8px;
  border: 1px solid #30363D; padding: 16px; overflow-x: auto;
}}
.vis-inner svg {{ max-width: 100%; height: auto; }}

/* ════════════════════════════════════════════════════════════════════════════
   TOOLTIP (term hover)
   ════════════════════════════════════════════════════════════════════════════ */
.tip {{
  border-bottom: 1px dashed var(--link); cursor: help;
  position: relative; color: var(--link); font-style: normal;
}}
.tip::after {{
  content: attr(data-tip);
  position: absolute; bottom: calc(100% + 8px); left: 50%;
  transform: translateX(-50%);
  background: #1A1A2E; color: #E2E8F0;
  font-family: var(--ui-font); font-size: 11px; line-height: 1.6;
  padding: 10px 14px; border-radius: 8px; width: 280px;
  z-index: 1000; pointer-events: none;
  opacity: 0; transition: opacity .2s;
  box-shadow: 0 6px 20px rgba(0,0,0,.35);
  white-space: normal; text-align: left;
}}
.tip:hover::after {{ opacity: 1; }}

/* ════════════════════════════════════════════════════════════════════════════
   SEARCH HIGHLIGHT
   ════════════════════════════════════════════════════════════════════════════ */
mark {{ background: var(--highlight); border-radius: 2px; color: inherit; }}

/* ════════════════════════════════════════════════════════════════════════════
   GLOSSARY
   ════════════════════════════════════════════════════════════════════════════ */
.gloss-search {{
  width: 100%; max-width: 500px;
  padding: 11px 18px; font-size: 14px;
  font-family: var(--ui-font);
  background: var(--surface); border: 2px solid var(--border);
  border-radius: 8px; color: var(--ink); outline: none;
  margin-bottom: 32px;
  transition: border-color .2s;
}}
.gloss-search:focus {{ border-color: var(--navy); }}
.glossary dt {{
  font-family: var(--ui-font); font-weight: 700;
  color: var(--navy); font-size: 14px;
  margin-top: 22px; padding-bottom: 4px;
  border-bottom: 1px dotted var(--border-2);
}}
.glossary dd {{
  margin-left: 0; margin-top: 6px;
  margin-bottom: 10px; font-size: 15px;
  color: var(--ink-2); line-height: 1.75;
}}

/* ════════════════════════════════════════════════════════════════════════════
   CHAPTER NAVIGATION FOOTER
   ════════════════════════════════════════════════════════════════════════════ */
.ch-nav-footer {{
  display: flex; align-items: center; justify-content: space-between;
  margin-top: 72px; padding-top: 28px;
  border-top: 1px solid var(--border);
  font-family: var(--ui-font);
}}
.ch-nav-link {{
  display: flex; align-items: center; gap: 8px;
  color: var(--ink-3); font-size: 12px; text-decoration: none;
  padding: 8px 14px; border-radius: 8px; border: 1px solid var(--border);
  transition: all .2s; max-width: 220px;
}}
.ch-nav-link:hover {{
  background: var(--bg-alt); color: var(--navy);
  border-color: var(--navy);
}}
.ch-nav-link.next {{ flex-direction: row; }}
.ch-nav-link.prev {{ flex-direction: row; }}
.ch-nav-arrow {{ font-size: 16px; color: var(--navy); flex-shrink: 0; }}
.ch-nav-text {{ white-space: nowrap; overflow: hidden; text-overflow: ellipsis; font-weight: 500; }}
.ch-nav-dot {{ color: var(--border); font-size: 16px; }}

/* ════════════════════════════════════════════════════════════════════════════
   VEEVA CHAPTER  (dark special treatment)
   ════════════════════════════════════════════════════════════════════════════ */
.chapter.veeva-ch {{
  background: #080C10; color: #E6EAF0;
}}
.chapter.veeva-ch h1,
.chapter.veeva-ch h2,
.chapter.veeva-ch h3 {{ color: #E6EAF0; }}
.chapter.veeva-ch h2::before {{ color: #2D3748; }}
.chapter.veeva-ch .lead {{ color: #8B949E; border-left-color: #30363D; }}
.chapter.veeva-ch p {{ color: #C9D1D9; }}
.chapter.veeva-ch .role-card {{
  background: #161B22; border-color: #30363D;
}}
.chapter.veeva-ch .role-title {{ color: #E6EAF0; }}
.chapter.veeva-ch .role-card p {{ color: #8B949E; }}
.chapter.veeva-ch h2 {{ border-bottom-color: #30363D; }}
.chapter.veeva-ch .ch-big-num {{ color: #1A2030; }}
.chapter.veeva-ch .ch-nav-footer {{ border-top-color: #2D3748; }}
.chapter.veeva-ch .ch-nav-link {{
  background: #161B22; border-color: #30363D; color: #8B949E;
}}
.chapter.veeva-ch .ch-nav-link:hover {{
  background: #1E2630; color: #E6EAF0;
}}
.gc        {{ background: #161B22; border: 1px solid #30363D; border-radius: 10px; overflow: hidden; }}
.gc-head   {{ padding: 10px 14px; font-size: 11px; font-weight: 700; color: #fff; }}
.gc-body   {{ padding: 12px 14px; font-size: 9px; color: #8B949E; line-height: 1.7; }}
.bv        {{ background: rgba(224,90,0,.25); color: #FFA657; border: 1px solid #E05A00; }}

/* ════════════════════════════════════════════════════════════════════════════
   BACK TO TOP BUTTON
   ════════════════════════════════════════════════════════════════════════════ */
#btt {{
  position: fixed; bottom: 32px; right: 32px;
  width: 46px; height: 46px;
  background: var(--navy); color: white;
  border: none; border-radius: 50%; cursor: pointer;
  font-size: 18px; display: none; align-items: center; justify-content: center;
  box-shadow: 0 4px 16px rgba(0,0,0,.3);
  transition: background .2s, transform .2s; z-index: 500;
}}
#btt:hover {{ background: var(--teal); transform: translateY(-2px); }}
#btt.visible {{ display: flex; }}

/* ════════════════════════════════════════════════════════════════════════════
   FOOTER
   ════════════════════════════════════════════════════════════════════════════ */
.book-footer {{
  padding: 56px 80px; background: #0D1117;
  color: rgba(255,255,255,.45);
  font-family: var(--ui-font); font-size: 12px; line-height: 2;
}}
.book-footer-inner {{
  max-width: 720px; margin: 0 auto; text-align: center;
}}
.book-footer-title {{
  font-size: 20px; font-weight: 700;
  color: rgba(255,255,255,.9); margin-bottom: 10px;
  font-family: 'EB Garamond', Georgia, serif; letter-spacing: -.3px;
}}
.book-footer-author {{ font-size: 14px; color: #7EC8C8; margin-bottom: 16px; }}
.book-footer-rule {{
  width: 60px; height: 1px; background: rgba(255,255,255,.15);
  margin: 20px auto;
}}

/* ════════════════════════════════════════════════════════════════════════════
   RESPONSIVE
   ════════════════════════════════════════════════════════════════════════════ */
@media (max-width: 1100px) {{
  :root {{ --ch-padding-x: 48px; --ch-padding-y: 60px; }}
}}
@media (max-width: 820px) {{
  .toc {{ display: none; }}
  :root {{ --ch-padding-x: 24px; --ch-padding-y: 40px; }}
  .cover h1 {{ font-size: 30px; }}
  #reader-controls {{ display: none; }}
}}

/* ════════════════════════════════════════════════════════════════════════════
   PRINT  (true book-style pagination)
   ════════════════════════════════════════════════════════════════════════════ */
@media print {{
  .toc, #btt, #progress-bar, #reader-controls,
  .ch-nav-footer, .cover-scroll {{ display: none !important; }}
  body {{ font-size: 11pt; line-height: 1.65; color: black; background: white; }}
  .cover {{
    min-height: auto; page-break-after: always;
    padding: 3in 1.5in; background: white !important;
  }}
  .cover h1, .cover .subtitle, .cover .author,
  .cover-badge, .cover-meta {{ color: black !important; }}
  .cover-pill {{ border: 1px solid black; color: black; background: white; }}
  .chapter {{ padding: 0.6in 1in; max-width: 100%; page-break-before: always; border: none; }}
  .chapter h1 {{ font-size: 22pt; }}
  .chapter h2 {{ font-size: 15pt; page-break-after: avoid; }}
  .chapter h3 {{ page-break-after: avoid; }}
  .chapter p  {{ orphans: 3; widows: 3; }}
  .vis-embed  {{ page-break-inside: avoid; border: 1px solid #CCC; }}
  .vis-label  {{ background: #EEE !important; color: black !important; }}
  .vis-inner  {{ background: white !important; }}
  .vis-cap    {{ background: white !important; }}
  .callout    {{ page-break-inside: avoid; }}
  blockquote  {{ border-left: 3px solid black; background: #F5F5F5; }}
  .book-footer {{ background: white; color: black; border-top: 2px solid black; }}
  /* Running headers via CSS counters */
  @page {{ margin: 0.9in 1in; }}
  @page :left  {{ @top-left   {{ content: "Pharma Commercial & Medical Affairs"; font-size: 8pt; }} }}
  @page :right {{ @top-right  {{ content: "Deepak Kumar — Pharma & MedTech Consultant"; font-size: 8pt; }} }}
  @page {{ @bottom-center {{ content: counter(page); font-size: 8pt; }} }}
}}
{MODAL_CSS}
</style>
</head>
<body>

<div id="progress-bar"></div>

<!-- READING CONTROLS -->
<div id="reader-controls" role="toolbar" aria-label="Reading controls">
  <button onclick="adjustFont(-1)" title="Decrease font size">A−</button>
  <button onclick="adjustFont(1)"  title="Increase font size">A+</button>
  <div class="ctrl-sep"></div>
  <button class="theme-btn" onclick="setTheme('light')"  title="Light theme">☀</button>
  <button class="theme-btn" onclick="setTheme('sepia')"  title="Sepia theme">📜</button>
  <button class="theme-btn" onclick="setTheme('dark')"   title="Dark theme">🌙</button>
  <div class="ctrl-sep"></div>
  <div class="gsearch-wrap">
    <input id="gsearchInput" class="gsearch-input" type="search"
           placeholder="🔍 Google…" aria-label="Google search"
           onkeydown="if(event.key==='Enter')openGSearch(this.value)" />
    <button class="gsearch-btn" onclick="openGSearch(document.getElementById('gsearchInput').value)" title="Search Google">Go</button>
  </div>
</div>

<!-- ══════════════ GOOGLE SEARCH MODAL ══════════════ -->
<div id="gsearchModal" class="gsearch-modal-overlay" role="dialog" aria-modal="true" aria-label="Google Search">
  <div class="gsearch-modal-panel">
    <div class="gsearch-modal-bar">
      <span class="gsearch-modal-title">🔍 Search</span>
      <input id="gsearchModalInput" class="gsearch-modal-input" type="search"
             placeholder="Type query and press Enter or click a search engine…"
             onkeydown="if(event.key==='Enter')launchSearch('google',this.value)" />
      <button class="gsearch-modal-close" onclick="closeGSearch()" title="Close (Esc)">✕</button>
    </div>
    <div class="gsearch-engines">
      <button class="gse-btn gse-google" onclick="launchSearch('google',document.getElementById('gsearchModalInput').value)">
        <svg width="18" height="18" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.5 0 6.6 1.2 9.1 3.2l6.8-6.8C35.8 2.5 30.3 0 24 0 14.6 0 6.6 5.6 2.5 13.8l7.9 6.1C12.3 13.3 17.7 9.5 24 9.5z"/><path fill="#4285F4" d="M46.5 24.5c0-1.6-.1-3.1-.4-4.5H24v8.5h12.7c-.6 3-2.3 5.5-4.8 7.2l7.5 5.8c4.4-4 7.1-10 7.1-17z"/><path fill="#FBBC05" d="M10.4 28.6A14.7 14.7 0 0 1 9.5 24c0-1.6.3-3.2.8-4.6l-7.9-6.1A23.9 23.9 0 0 0 0 24c0 3.9.9 7.5 2.5 10.8l7.9-6.2z"/><path fill="#34A853" d="M24 48c6.3 0 11.6-2.1 15.5-5.6l-7.5-5.8c-2.1 1.4-4.8 2.2-8 2.2-6.3 0-11.6-3.8-13.5-9.2l-7.9 6.1C6.6 42.4 14.6 48 24 48z"/></svg>
        Google
      </button>
      <button class="gse-btn gse-bing" onclick="launchSearch('bing',document.getElementById('gsearchModalInput').value)">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="#008373"><path d="M5 3l4 1.4v13.2l5.5-3.2-2.3-1.1 4.4-4.6 3.4 8.8L5 20.8z"/></svg>
        Bing
      </button>
      <button class="gse-btn gse-scholar" onclick="launchSearch('scholar',document.getElementById('gsearchModalInput').value)">
        📚 Scholar
      </button>
      <button class="gse-btn gse-pubmed" onclick="launchSearch('pubmed',document.getElementById('gsearchModalInput').value)">
        🧬 PubMed
      </button>
      <button class="gse-btn gse-fda" onclick="launchSearch('fda',document.getElementById('gsearchModalInput').value)">
        🏥 FDA.gov
      </button>
    </div>
    <div class="gsearch-note">
      Search opens in a floating popup window. If blocked, allow popups for this page in your browser.
    </div>
  </div>
</div>

<button id="btt" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Back to top">↑</button>

<!-- ══════════════════════════════════════════════
     COVER
══════════════════════════════════════════════ -->
<div class="cover" role="banner">
  <div class="cover-badge">The Complete Visual Reference · 2026</div>
  <div class="cover-ornament"></div>
  <h1>Pharma <em>Commercial</em> &amp; Medical Affairs</h1>
  <p class="subtitle">A complete, story-driven guide with visual process maps — from laboratory discovery to patient prescription — covering every function, every role, and every regulation.</p>
  <img src="data:image/jpeg;base64,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" class="cover-avatar" alt="Deepak Kumar" />
  <p class="author">✦ &nbsp; Deepak Kumar — Pharma &amp; MedTech Consultant &nbsp; ✦</p>
  <div class="cover-pills">
    <span class="cover-pill">Commercial Affairs</span>
    <span class="cover-pill">Medical Affairs</span>
    <span class="cover-pill">R&amp;D Pipeline</span>
    <span class="cover-pill">Product Launch</span>
    <span class="cover-pill">Veeva Systems</span>
    <span class="cover-pill">GxP &amp; Compliance</span>
    <span class="cover-pill">CAPA &amp; FDA</span>
    <span class="cover-pill">HCP Engagement</span>
    <span class="cover-pill">Process Diagrams</span>
    <span class="cover-pill">Roles &amp; Org Structure</span>
  </div>
  <div class="cover-meta">
    11 Chapters · Visual SVG Process Maps · Interactive Glossary · Hover Tooltips<br>
    FDA Regulatory Frameworks · ICH Guidelines · Veeva Platform Reference<br>
    <span style="opacity:.5;">May 2026 · All regulatory references reflect US FDA frameworks</span>
  </div>
  <div class="cover-scroll"
       onclick="document.getElementById('intro').scrollIntoView({{behavior:'smooth'}})">
    ▾ &nbsp; Begin Reading
  </div>
</div>

<!-- ══════════════════════════════════════════════
     MAIN LAYOUT
══════════════════════════════════════════════ -->
<div class="wrapper">

<!-- ── Sidebar TOC ── -->
<nav class="toc" id="toc" aria-label="Table of contents">
  <div class="toc-brand">
    <img src="data:image/jpeg;base64,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" class="toc-brand-avatar" alt="Deepak Kumar" />
    <div class="name">Deepak Kumar</div>
    <div class="sub">Pharma &amp; MedTech Consultant</div>
  </div>

  <input class="toc-search" id="tocSearch" type="search"
         placeholder="🔍  Search…" aria-label="Search content"
         oninput="searchContent(this.value)"/>

  <div class="toc-section">Front Matter</div>
  <a href="#abstract"  class="ch">Abstract</a>
  <a href="#preface"   class="ch">Preface</a>
  <a href="#toc-page"  class="ch">Table of Contents</a>

  <div class="toc-section">Contents</div>
  <a href="#intro" class="ch">✦ &nbsp; Introduction</a>

  <div class="toc-section">Part I — Foundation</div>
  <a href="#ch1" class="ch">Ch 1 · The Big Picture</a>
  <a href="#ch2" class="ch">Ch 2 · R&amp;D — Where It Begins</a>
  <a href="#ch2-discovery"      class="sub">Drug Discovery</a>
  <a href="#ch2-preclinical"    class="sub">Pre-Clinical</a>
  <a href="#ch2-ind"            class="sub">IND Application</a>
  <a href="#ch2-phase1"         class="sub">Phase I</a>
  <a href="#ch2-phase2"         class="sub">Phase II &amp; PoC</a>
  <a href="#ch2-phase3"         class="sub">Phase III</a>
  <a href="#ch2-nda"            class="sub">NDA/BLA Submission</a>
  <a href="#ch2-fda-review"     class="sub">FDA Review</a>
  <a href="#ch2-commercial-start" class="sub">Commercial Engagement</a>
  <a href="#ch2-rd-commercial"  class="sub">R&amp;D ↔ Commercial</a>

  <div class="toc-section">Part II — Commercial</div>
  <a href="#ch3" class="ch">Ch 3 · Commercial Affairs</a>
  <a href="#brand-planning"  class="sub">Brand Planning</a>
  <a href="#market-research" class="sub">Market Research</a>
  <a href="#sfe"             class="sub">Sales Force</a>
  <a href="#mlr"             class="sub">Content &amp; MLR</a>
  <a href="#hcp-eng"         class="sub">HCP Engagement</a>
  <a href="#market-access"   class="sub">Market Access</a>
  <a href="#samples"         class="sub">Sample Management</a>
  <a href="#ci"              class="sub">Competitive Intel</a>

  <div class="toc-section">Part III — Medical Affairs</div>
  <a href="#ch4"          class="ch">Ch 4 · Medical Affairs</a>
  <a href="#med-strategy" class="sub">Medical Strategy</a>
  <a href="#evidence"     class="sub">Evidence Generation</a>
  <a href="#msl"          class="sub">MSL Operations</a>
  <a href="#med-info"     class="sub">Medical Information</a>
  <a href="#publications" class="sub">Publications</a>
  <a href="#pv"           class="sub">Pharmacovigilance</a>

  <div class="toc-section">Part IV — Integration</div>
  <a href="#ch5" class="ch">Ch 5 · The Firewall</a>
  <a href="#ch6" class="ch">Ch 6 · R&amp;D Bridge</a>
  <a href="#ch7" class="ch">Ch 7 · The Launch!</a>
  <a href="#prelaunch"  class="sub">Pre-Launch Build</a>
  <a href="#launchday"  class="sub">Launch Day</a>
  <a href="#postlaunch" class="sub">Post-Launch</a>

  <div class="toc-section">Part V — People &amp; Rules</div>
  <a href="#ch8"    class="ch">Ch 8 · The People</a>
  <a href="#ch9"    class="ch">Ch 9 · The Rules</a>
  <a href="#ch10"   class="ch">Ch 10 · Putting It Together</a>

  <div class="toc-section">Part VI — Systems</div>
  <a href="#ch11"         class="ch">Ch 11 · Veeva Systems</a>
  <a href="#veeva-crm"    class="sub">Veeva CRM</a>
  <a href="#veeva-crm-arch"     class="sub" style="padding-left:28px;">↳ Object Architecture</a>
  <a href="#veeva-crm-commercial" class="sub" style="padding-left:28px;">↳ Commercial Workflow</a>
  <a href="#veeva-crm-msl"      class="sub" style="padding-left:28px;">↳ MSL Workflow</a>
  <a href="#veeva-crm-sample"   class="sub" style="padding-left:28px;">↳ Sample Management</a>
  <a href="#veeva-crm-clm"      class="sub" style="padding-left:28px;">↳ CLM Loop</a>
  <a href="#clm-crm-mechanics"  class="sub" style="padding-left:40px;">↳ CRM Mechanics</a>
  <a href="#clm-promomats"      class="sub" style="padding-left:40px;">↳ PromoMats ↔ CLM</a>
  <a href="#clm-medcomm"        class="sub" style="padding-left:40px;">↳ MedComm &amp; CLM</a>
  <a href="#veeva-crm-products"  class="sub" style="padding-left:28px;">↳ Product Management</a>
  <a href="#veeva-crm-mirf"      class="sub" style="padding-left:28px;">↳ MIRF &amp; Medical Info</a>
  <a href="#veeva-crm-ref"       class="sub" style="padding-left:28px;">↳ All Objects Reference</a>
  <a href="#veeva-vault"  class="sub">Vault PromoMats</a>
  <a href="#promomats-docs"            class="sub" style="padding-left:28px;">↳ Document Types</a>
  <a href="#promomats-workflow"        class="sub" style="padding-left:28px;">↳ MLR Workflow</a>
  <a href="#promomats-crm-integration" class="sub" style="padding-left:28px;">↳ CRM Integration</a>
  <a href="#veeva-med"    class="sub">Vault Medical</a>
  <a href="#vmed-doctypes"   class="sub" style="padding-left:28px;">↳ Document Types</a>
  <a href="#vmed-lifecycle"  class="sub" style="padding-left:28px;">↳ MRB Lifecycle</a>
  <a href="#vmed-objects"    class="sub" style="padding-left:28px;">↳ Vault Objects</a>
  <a href="#vmed-integration" class="sub" style="padding-left:28px;">↳ Integrations</a>
  <a href="#veeva-network" class="sub">Veeva Network</a>
  <a href="#network-entities"        class="sub" style="padding-left:28px;">↳ Data Entities</a>
  <a href="#network-stewardship"     class="sub" style="padding-left:28px;">↳ Data Stewardship</a>
  <a href="#network-crm-integration" class="sub" style="padding-left:28px;">↳ CRM Integration</a>
  <a href="#veeva-events" class="sub">Events Mgmt</a>
  <a href="#veeva-user-mgmt" class="sub">User Management</a>
  <a href="#vum-creation"      class="sub" style="padding-left:28px;">↳ User Creation Flow</a>
  <a href="#vum-profiles"      class="sub" style="padding-left:28px;">↳ Profiles</a>
  <a href="#vum-permsets"      class="sub" style="padding-left:28px;">↳ Permission Sets</a>
  <a href="#vum-objectperms"   class="sub" style="padding-left:28px;">↳ Object Permissions</a>
  <a href="#vum-rolehierarchy" class="sub" style="padding-left:28px;">↳ Role Hierarchy</a>
  <a href="#vum-permmodel"     class="sub" style="padding-left:28px;">↳ Permission Architecture</a>
  <a href="#vum-vault-users"   class="sub" style="padding-left:28px;">↳ Vault Users</a>

  <div class="toc-section">Reference</div>
  <a href="#glossary" class="ch">A–Z Glossary</a>
</nav>

<!-- ── Content ── -->
<main class="content" id="mainContent">

{FRONT_MATTER}
{ch_intro}
{nav_intro}

<div class="ch-divider ch-both"></div>
{ch1}
{nav_ch1}

<div class="ch-divider ch-rd"></div>
{ch2}
{nav_ch2}

<div class="ch-divider ch-comm"></div>
{ch3}
{nav_ch3}

<div class="ch-divider ch-med"></div>
{ch4}
{nav_ch4}

<div class="ch-divider ch-both"></div>
{ch5}
{nav_ch5}

<div class="ch-divider ch-rd"></div>
{ch6}
{nav_ch6}

<div class="ch-divider ch-launch"></div>
{ch7}
{nav_ch7}

<div class="ch-divider ch-both"></div>
{ch8}
{nav_ch8}

<div class="ch-divider" style="background:linear-gradient(90deg,#7A1515,#B03030);"></div>
{ch9}
{nav_ch9}

<div class="ch-divider ch-both"></div>
{ch10}
{nav_ch10}

<!-- ══════════════ CHAPTER 11: VEEVA SYSTEMS ══════════════ -->
<div class="ch-divider ch-veeva"></div>
<div class="chapter veeva-ch" id="ch11">
  <div class="ch-running">Chapter Eleven · Part VI — Systems</div>
  <div class="ch-decorator">
    <div class="ch-big-num">11</div>
    <div class="ch-heading-block">
      <div class="ch-label">
        <span class="ch-pill" style="background:#E05A00;">Ch 11</span>
        <span style="color:#E05A00;">Chapter Eleven</span>
      </div>
      <h1>Veeva Systems — The Technology Backbone</h1>
    </div>
  </div>
  <p class="lead">In modern pharmaceutical commercial and medical operations, Veeva is the operating system. It is the platform through which reps plan their calls, MLR teams approve materials, medical information specialists answer HCP questions, and compliance teams report transfers of value. Understanding Veeva is inseparable from understanding how pharma works.</p>

  <h2 id="veeva-crm">Veeva CRM — The Sales Rep's Cockpit</h2>

  <p>Veeva CRM is built on the Salesforce platform, extended with 20+ pharmaceutical-industry objects that simultaneously enforce PDMA sample compliance, MLR content controls, and Sunshine Act transfer-of-value tracking. It is the system of record for every touchpoint a commercial rep, MSL, or key account manager has with a healthcare professional — from the moment a cycle plan is built weeks before launch to the moment post-call analytics confirm whether the message landed.</p>

  <p>Two distinct user communities share the platform under strictly different permission profiles. <strong>Commercial teams</strong> — territory managers, regional directors, key account managers — use it to detail products, drop samples, send Approved Emails, and manage speaker events. <strong>Medical Affairs teams</strong> — MSLs, medical information specialists, medical science directors — use it for non-promotional scientific exchange, medical inquiry logging, KOL profiling, and congress engagement. Both communities share the same Account and Contact foundation but are separated by record types, validation rules, and page layouts that operationally enforce the commercial-medical firewall.</p>

  <!-- ═══════════════════════════════════
       OBJECT ARCHITECTURE
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-arch">The CRM Object Architecture</h3>

  <p>Veeva CRM organises its data into four functional layers. <strong>Foundation objects</strong> (Account, Contact, Territory, Veeva Network) form the master data layer — every activity ultimately rolls up to an Account record that is validated against Veeva Network's master HCP database. <strong>Planning objects</strong> (Cycle Plan, CLM Presentation, Medical Event) set strategic context before a rep or MSL steps into the field. <strong>Activity objects</strong> (Call Report, Approved Email, Medical Inquiry, MSL Call) capture every real-world interaction in real time. <strong>Sub-record objects</strong> — children of a Call — capture granular detail that feeds SFE analytics, PDMA reconciliation, and HCP engagement scoring.</p>

  <!-- Object Architecture Visual -->
  <figure class="vis-embed" aria-label="Veeva CRM Object Architecture">
    <div class="vis-label"><span class="vis-icon">◈</span> Veeva CRM — Complete Object Architecture &amp; Data Relationships</div>
    <div class="vis-inner" style="padding:24px 20px;">
      <svg viewBox="0 0 960 510" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:700px;display:block;">
        <defs>
          <marker id="arrd" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#30363D"/></marker>
          <marker id="arrb" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#1B3A6B"/></marker>
          <marker id="arrm" markerWidth="7" markerHeight="7" refX="5" refY="3.5" orient="auto"><path d="M0,1 L0,6 L6,3.5 z" fill="#0B5E5E"/></marker>
        </defs>
        <rect width="960" height="510" fill="#0D1117"/>
        <!-- Legend -->
        <rect x="20" y="12" width="10" height="10" rx="2" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <text x="34" y="21" fill="#8B949E" font-size="9.5">Foundation</text>
        <rect x="110" y="12" width="10" height="10" rx="2" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="124" y="21" fill="#8B949E" font-size="9.5">Commercial</text>
        <rect x="210" y="12" width="10" height="10" rx="2" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="224" y="21" fill="#8B949E" font-size="9.5">Medical Affairs</text>

        <!-- ── ROW 1: FOUNDATION ── -->
        <text x="8" y="68" fill="#4A5568" font-size="8" font-weight="700" letter-spacing="1.5">FOUNDATION</text>
        <!-- Account -->
        <rect x="8" y="75" width="210" height="72" rx="6" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <text x="113" y="96" text-anchor="middle" fill="#C0A0FF" font-size="12" font-weight="700">Account</text>
        <text x="113" y="111" text-anchor="middle" fill="#7060A0" font-size="8.5" font-family="monospace">Account (HCP / HCO)</text>
        <text x="113" y="126" text-anchor="middle" fill="#6B7280" font-size="9">NPI · Specialty · Target Status · Segment</text>
        <text x="113" y="139" text-anchor="middle" fill="#6B7280" font-size="9">Territory · Decile · Last Call Date</text>
        <!-- Contact -->
        <rect x="228" y="75" width="200" height="72" rx="6" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <text x="328" y="96" text-anchor="middle" fill="#C0A0FF" font-size="12" font-weight="700">Contact</text>
        <text x="328" y="111" text-anchor="middle" fill="#7060A0" font-size="8.5" font-family="monospace">Contact (Individual HCP)</text>
        <text x="328" y="126" text-anchor="middle" fill="#6B7280" font-size="9">License # · DEA · Address · Email</text>
        <text x="328" y="139" text-anchor="middle" fill="#6B7280" font-size="9">Consent Status · Opt-out Flags</text>
        <!-- Territory -->
        <rect x="438" y="75" width="200" height="72" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="538" y="96" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">Territory2</text>
        <text x="538" y="111" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">Territory2 (Salesforce)</text>
        <text x="538" y="126" text-anchor="middle" fill="#6B7280" font-size="9">Geo / Brick / Zip alignment</text>
        <text x="538" y="139" text-anchor="middle" fill="#6B7280" font-size="9">Rep assignment · Rollup rules</text>
        <!-- Veeva Network -->
        <rect x="648" y="75" width="300" height="72" rx="6" fill="#1A1010" stroke="#5A3000" stroke-width="1.5"/>
        <text x="798" y="96" text-anchor="middle" fill="#FFA657" font-size="12" font-weight="700">Veeva Network (MDM)</text>
        <text x="798" y="111" text-anchor="middle" fill="#7A4020" font-size="8.5" font-family="monospace">HCP / HCO Master Data</text>
        <text x="798" y="126" text-anchor="middle" fill="#6B7280" font-size="9">NPI validation · OIG exclusion check</text>
        <text x="798" y="139" text-anchor="middle" fill="#6B7280" font-size="9">Data Change Request (DCR) workflow</text>

        <!-- ── ROW 2: PLANNING ── -->
        <text x="8" y="172" fill="#4A5568" font-size="8" font-weight="700" letter-spacing="1.5">PLANNING</text>
        <!-- Cycle Plan -->
        <rect x="8" y="179" width="200" height="72" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="108" y="200" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">Cycle Plan</text>
        <text x="108" y="215" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">Cycle_Plan_vod__c</text>
        <text x="108" y="230" text-anchor="middle" fill="#6B7280" font-size="9">HCP target list · Call freq. goal</text>
        <text x="108" y="243" text-anchor="middle" fill="#6B7280" font-size="9">Segment priority · Window dates</text>
        <!-- CLM Presentation -->
        <rect x="218" y="179" width="210" height="72" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="323" y="200" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">CLM Presentation</text>
        <text x="323" y="215" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">Clm_Presentation_vod__c</text>
        <text x="323" y="230" text-anchor="middle" fill="#6B7280" font-size="9">iPad visual aid · Slide sequence</text>
        <text x="323" y="243" text-anchor="middle" fill="#6B7280" font-size="9">From Vault PromoMats (MLR-approved)</text>
        <!-- Call Objective (planning) -->
        <rect x="438" y="179" width="200" height="72" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="538" y="200" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">Call Objective</text>
        <text x="538" y="215" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">Call_Objective_vod__c</text>
        <text x="538" y="230" text-anchor="middle" fill="#6B7280" font-size="9">Pre-call goal · Next Best Action</text>
        <text x="538" y="243" text-anchor="middle" fill="#6B7280" font-size="9">AI-suggested from analytics</text>
        <!-- Medical Event -->
        <rect x="648" y="179" width="300" height="72" rx="6" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="798" y="200" text-anchor="middle" fill="#2A9A9A" font-size="12" font-weight="700">Medical Event</text>
        <text x="798" y="215" text-anchor="middle" fill="#1A5050" font-size="8.5" font-family="monospace">Medical_Event_vod__c</text>
        <text x="798" y="230" text-anchor="middle" fill="#6B7280" font-size="9">Congress · Advisory Board · Symposium</text>
        <text x="798" y="243" text-anchor="middle" fill="#6B7280" font-size="9">FMV caps · TOV pre-approval</text>

        <!-- ── ROW 3: ACTIVITY ── -->
        <text x="8" y="276" fill="#4A5568" font-size="8" font-weight="700" letter-spacing="1.5">FIELD ACTIVITY</text>
        <!-- Call Report -->
        <rect x="8" y="283" width="200" height="72" rx="6" fill="#0F1E35" stroke="#4A7ABF" stroke-width="2"/>
        <text x="108" y="304" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">Call Report</text>
        <text x="108" y="319" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">EM_Call_vod__c</text>
        <text x="108" y="334" text-anchor="middle" fill="#6B7280" font-size="9">Date · Channel · Duration · Status</text>
        <text x="108" y="347" text-anchor="middle" fill="#6B7280" font-size="9">Primary commercial activity record</text>
        <!-- Approved Email -->
        <rect x="218" y="283" width="210" height="72" rx="6" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="323" y="304" text-anchor="middle" fill="#7EC8C8" font-size="12" font-weight="700">Approved Email</text>
        <text x="323" y="319" text-anchor="middle" fill="#3A6090" font-size="8.5" font-family="monospace">Sent_Email_vod__c</text>
        <text x="323" y="334" text-anchor="middle" fill="#6B7280" font-size="9">MLR template · Open/Click rate</text>
        <text x="323" y="347" text-anchor="middle" fill="#6B7280" font-size="9">Consent-gated · Cadence-limited</text>
        <!-- Medical Inquiry -->
        <rect x="438" y="283" width="200" height="72" rx="6" fill="#071E1E" stroke="#2A9A9A" stroke-width="2"/>
        <text x="538" y="304" text-anchor="middle" fill="#2A9A9A" font-size="12" font-weight="700">Medical Inquiry</text>
        <text x="538" y="319" text-anchor="middle" fill="#1A5050" font-size="8.5" font-family="monospace">Medical_Inquiry_vod__c</text>
        <text x="538" y="334" text-anchor="middle" fill="#6B7280" font-size="9">On-label / Off-label / AE flag</text>
        <text x="538" y="347" text-anchor="middle" fill="#6B7280" font-size="9">Triggers SRL retrieval from Vault</text>
        <!-- MSL Call -->
        <rect x="648" y="283" width="300" height="72" rx="6" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="798" y="304" text-anchor="middle" fill="#2A9A9A" font-size="12" font-weight="700">MSL Call Report</text>
        <text x="798" y="319" text-anchor="middle" fill="#1A5050" font-size="8.5" font-family="monospace">Call_vod__c (Medical record type)</text>
        <text x="798" y="334" text-anchor="middle" fill="#6B7280" font-size="9">Non-promotional · No sample drop</text>
        <text x="798" y="347" text-anchor="middle" fill="#6B7280" font-size="9">Scientific topics · Insights captured</text>

        <!-- ── ROW 4: SUB-RECORDS ── -->
        <text x="8" y="380" fill="#4A5568" font-size="8" font-weight="700" letter-spacing="1.5">SUB-RECORDS (CHILDREN OF CALL)</text>
        <!-- Products Detailed -->
        <rect x="8" y="387" width="155" height="60" rx="5" fill="#0A1525" stroke="#1A2D45" stroke-width="1"/>
        <text x="85" y="406" text-anchor="middle" fill="#4A7ABF" font-size="10.5" font-weight="700">Products Detailed</text>
        <text x="85" y="420" text-anchor="middle" fill="#2A3A55" font-size="8" font-family="monospace">EM_Product_vod__c</text>
        <text x="85" y="435" text-anchor="middle" fill="#4A5568" font-size="9">Brand · Detail priority</text>
        <text x="85" y="447" text-anchor="middle" fill="#4A5568" font-size="9">1st / 2nd / 3rd detail slot</text>
        <!-- Key Messages -->
        <rect x="172" y="387" width="155" height="60" rx="5" fill="#0A1525" stroke="#1A2D45" stroke-width="1"/>
        <text x="249" y="406" text-anchor="middle" fill="#4A7ABF" font-size="10.5" font-weight="700">Key Messages</text>
        <text x="249" y="420" text-anchor="middle" fill="#2A3A55" font-size="8" font-family="monospace">Key_Message_vod__c</text>
        <text x="249" y="435" text-anchor="middle" fill="#4A5568" font-size="9">Message · Reaction score</text>
        <text x="249" y="447" text-anchor="middle" fill="#4A5568" font-size="9">+Like / Neutral / –Dislike</text>
        <!-- Sample Transaction -->
        <rect x="336" y="387" width="155" height="60" rx="5" fill="#0A1525" stroke="#1A2D45" stroke-width="1"/>
        <text x="413" y="406" text-anchor="middle" fill="#4A7ABF" font-size="10.5" font-weight="700">Sample Transaction</text>
        <text x="413" y="420" text-anchor="middle" fill="#2A3A55" font-size="8" font-family="monospace">Sample_Transaction_vod__c</text>
        <text x="413" y="435" text-anchor="middle" fill="#4A5568" font-size="9">Product · Lot · Qty</text>
        <text x="413" y="447" text-anchor="middle" fill="#4A5568" font-size="9">HCP signature · PDMA receipt</text>
        <!-- Sample Lot -->
        <rect x="500" y="387" width="140" height="60" rx="5" fill="#0A1525" stroke="#1A2D45" stroke-width="1"/>
        <text x="570" y="406" text-anchor="middle" fill="#4A7ABF" font-size="10.5" font-weight="700">Sample Lot</text>
        <text x="570" y="420" text-anchor="middle" fill="#2A3A55" font-size="8" font-family="monospace">Sample_Lot_vod__c</text>
        <text x="570" y="435" text-anchor="middle" fill="#4A5568" font-size="9">Lot # · Expiry date</text>
        <text x="570" y="447" text-anchor="middle" fill="#4A5568" font-size="9">Qty available / dispensed</text>
        <!-- Medical Insight -->
        <rect x="650" y="387" width="148" height="60" rx="5" fill="#051515" stroke="#0D2525" stroke-width="1"/>
        <text x="724" y="406" text-anchor="middle" fill="#2A7A7A" font-size="10.5" font-weight="700">Medical Insight</text>
        <text x="724" y="420" text-anchor="middle" fill="#0D3535" font-size="8" font-family="monospace">Insight_vod__c</text>
        <text x="724" y="435" text-anchor="middle" fill="#4A5568" font-size="9">Field observation → MA HQ</text>
        <text x="724" y="447" text-anchor="middle" fill="#4A5568" font-size="9">Competitive intel · Unmet need</text>
        <!-- Event Attendance -->
        <rect x="808" y="387" width="145" height="60" rx="5" fill="#051515" stroke="#0D2525" stroke-width="1"/>
        <text x="880" y="406" text-anchor="middle" fill="#2A7A7A" font-size="10.5" font-weight="700">Event Attendance</text>
        <text x="880" y="420" text-anchor="middle" fill="#0D3535" font-size="8" font-family="monospace">Med_Event_Attendance</text>
        <text x="880" y="435" text-anchor="middle" fill="#4A5568" font-size="9">HCP · Role · TOV amount</text>
        <text x="880" y="447" text-anchor="middle" fill="#4A5568" font-size="9">Sunshine Act reporting</text>

        <!-- ── CONNECTORS ── -->
        <!-- Account ↔ Contact -->
        <line x1="218" y1="111" x2="228" y2="111" stroke="#4A2080" stroke-width="1.5" marker-end="url(#arrd)"/>
        <!-- Account → Cycle Plan -->
        <line x1="108" y1="147" x2="108" y2="179" stroke="#1B3A6B" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrb)"/>
        <!-- Account → Call Report -->
        <line x1="80" y1="147" x2="80" y2="283" stroke="#1B3A6B" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrb)"/>
        <!-- Contact → Medical Inquiry -->
        <line x1="440" y1="147" x2="538" y2="283" stroke="#0B5E5E" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrm)"/>
        <!-- Contact → MSL Call -->
        <line x1="428" y1="111" x2="648" y2="319" stroke="#0B5E5E" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrm)"/>
        <!-- CLM → Call Report -->
        <line x1="323" y1="251" x2="200" y2="283" stroke="#1B3A6B" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrb)"/>
        <!-- Medical Event → MSL Call -->
        <line x1="798" y1="251" x2="798" y2="283" stroke="#0B5E5E" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrm)"/>
        <!-- Call Report → sub-records -->
        <line x1="85" y1="355" x2="85" y2="387" stroke="#1B3A6B" stroke-width="1" marker-end="url(#arrb)"/>
        <line x1="108" y1="355" x2="249" y2="387" stroke="#1B3A6B" stroke-width="1" marker-end="url(#arrb)"/>
        <line x1="130" y1="355" x2="380" y2="387" stroke="#1B3A6B" stroke-width="1" marker-end="url(#arrb)"/>
        <line x1="150" y1="355" x2="530" y2="387" stroke="#1B3A6B" stroke-width="1" marker-end="url(#arrb)"/>
        <!-- MSL → Insight / Attendance -->
        <line x1="750" y1="355" x2="724" y2="387" stroke="#0B5E5E" stroke-width="1" marker-end="url(#arrm)"/>
        <line x1="820" y1="355" x2="860" y2="387" stroke="#0B5E5E" stroke-width="1" marker-end="url(#arrm)"/>
      </svg>
    </div>
    <figcaption class="vis-cap">Veeva CRM Object Architecture — all 4 layers with parent-child relationships</figcaption>
  </figure>

  <!-- ═══════════════════════════════════
       COMMERCIAL AFFAIRS
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-commercial">Commercial Affairs — Objects &amp; Business Functions</h3>

  <p>For a territory manager, Veeva CRM governs the entire sales cycle from weekly territory planning through to post-call PDMA reconciliation. The system's permission set ensures reps can only see HCPs in their territory, only distribute MLR-approved promotional content, and only send Approved Emails within consent and cadence limits. Every action is timestamped and immutable — creating an FDA-auditable record of every commercial touchpoint.</p>

  <div class="crm-obj-grid">
    <div>
      <div class="crm-section-label comm">◈ Commercial Core Objects</div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Call Report (EM_Call_vod__c)</div>
        <div class="crm-obj-api">Primary activity record — created for every face-to-face, remote, or phone interaction</div>
        <div class="crm-obj-desc">Captures channel (F2F/virtual/phone), start time, duration, and outcome. Parent of all sub-records. Status moves from Draft → Submitted → Locked (cannot be edited after submission). Drives SFE metrics: call rate, reach, frequency.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Call_Date_vod__c</span>
          <span class="crm-field-pill">Channel_vod__c</span>
          <span class="crm-field-pill">Status_vod__c</span>
          <span class="crm-field-pill">Territory2__c</span>
          <span class="crm-field-pill">Next_Call_Objective_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Products Detailed (EM_Product_vod__c)</div>
        <div class="crm-obj-api">Child of Call Report — one record per brand discussed</div>
        <div class="crm-obj-desc">Records which product was detailed, at what priority (1st, 2nd, or 3rd detail), and which CLM presentation was used. The system enforces that only products on the approved detail list for the rep's territory can be selected.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Product_vod__c</span>
          <span class="crm-field-pill">Detail_Priority_vod__c</span>
          <span class="crm-field-pill">Presentation_vod__c</span>
          <span class="crm-field-pill">Discussion_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Key Messages (Key_Message_vod__c)</div>
        <div class="crm-obj-api">Child of Call Report — captures HCP reaction to each brand message</div>
        <div class="crm-obj-desc">The rep records how each key message was received: Strongly Agree / Agree / Neutral / Disagree. This reaction data feeds the CLM analytics loop — messages with consistently neutral or negative reactions trigger a content review cycle by brand teams.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Key_Message_vod__c</span>
          <span class="crm-field-pill">Reaction_vod__c</span>
          <span class="crm-field-pill">Product_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Approved Email (Sent_Email_vod__c)</div>
        <div class="crm-obj-api">Templated, MLR-reviewed emails — no free-text customisation permitted</div>
        <div class="crm-obj-desc">Reps select from a library of Vault PromoMats-approved email templates. The system gates sending on HCP consent (Multichannel Consent object) and enforces per-HCP send cadence limits. Open rate, click rate, and link engagement are tracked and reported to marketing analytics.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Email_Template_vod__c</span>
          <span class="crm-field-pill">Sent_Date_vod__c</span>
          <span class="crm-field-pill">Open_Flag_vod__c</span>
          <span class="crm-field-pill">Consent_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card comm" style="margin-bottom:12px;">
        <div class="crm-obj-name comm">Cycle Plan / Cycle Plan Account</div>
        <div class="crm-obj-api">Cycle_Plan_vod__c / Cycle_Plan_Account_vod__c</div>
        <div class="crm-obj-desc">The Cycle Plan defines the target HCP universe and call frequency goals for a promotional cycle (typically quarterly). Cycle Plan Account is the junction object — one record per HCP in the plan, holding the target call count, actual call count, and attainment %. Used to produce the rep's daily prioritised call list.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Target_Calls_vod__c</span>
          <span class="crm-field-pill">Actual_Calls_vod__c</span>
          <span class="crm-field-pill">Start_Date_vod__c</span>
          <span class="crm-field-pill">Segment_Priority_vod__c</span>
        </div>
      </div>
    </div>

    <div>
      <div class="crm-section-label med">◈ Medical Affairs Objects</div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Medical Inquiry (Medical_Inquiry_vod__c)</div>
        <div class="crm-obj-api">Any unsolicited question from an HCP about a product — commercial reps route these to Medical</div>
        <div class="crm-obj-desc">When an HCP raises a product question during a commercial call, the rep creates a Medical Inquiry record and immediately transfers it to the Medical Information team — they cannot answer it themselves. The record captures: inquiry type (on-label/off-label/adverse event), question text, product, and HCP. An adverse event flag automatically creates an AE workflow in PV systems.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Inquiry_Type_vod__c</span>
          <span class="crm-field-pill">Product_vod__c</span>
          <span class="crm-field-pill">Question_vod__c</span>
          <span class="crm-field-pill">AE_Flag_vod__c</span>
          <span class="crm-field-pill">Response_Letter_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">MSL Call Report (Call_vod__c — Medical RT)</div>
        <div class="crm-obj-api">Non-promotional scientific exchange — separate record type with different fields and validations</div>
        <div class="crm-obj-desc">Uses the same Call object as commercial reps but a different record type that disables all promotional fields (no Products Detailed, no Sample Drop, no CLM slides). MSL-specific fields include Scientific Discussion Topics (free-text), Insights Captured, and follow-up action items. The MSL's call is invisible to the commercial field force — maintaining the scientific independence firewall.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Scientific_Topics_vod__c</span>
          <span class="crm-field-pill">Insights_vod__c</span>
          <span class="crm-field-pill">KOL_Tier_vod__c</span>
          <span class="crm-field-pill">Follow_Up_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Medical Event / Event Attendance</div>
        <div class="crm-obj-api">Medical_Event_vod__c / Medical_Event_Attendance_vod__c</div>
        <div class="crm-obj-desc">Tracks all HCP engagement at congresses, advisory boards, speaker programs, and symposia. Each attendance record captures the HCP's NPI, role (attendee/speaker/moderator/chair), and every transfer of value (honorarium, travel, meals). These records flow into the annual Sunshine Act Open Payments submission with FMV validation enforced at entry.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Event_Type_vod__c</span>
          <span class="crm-field-pill">HCP_Role_vod__c</span>
          <span class="crm-field-pill">TOV_Amount_vod__c</span>
          <span class="crm-field-pill">FMV_Rate_vod__c</span>
          <span class="crm-field-pill">Sunshine_Flag_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card med" style="margin-bottom:12px;">
        <div class="crm-obj-name med">Medical Insight (Insight_vod__c)</div>
        <div class="crm-obj-api">Field intelligence submitted by MSLs upward to Medical Affairs leadership</div>
        <div class="crm-obj-desc">MSLs document scientific observations, competitive intelligence, treatment landscape shifts, and unmet medical needs gathered during HCP interactions. Insights are categorised, reviewed centrally, and feed the Medical Strategy and Evidence Generation planning process. This is the structured mechanism by which the field informs the strategy — not informal email chains.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Insight_Category_vod__c</span>
          <span class="crm-field-pill">Therapeutic_Area_vod__c</span>
          <span class="crm-field-pill">Priority_vod__c</span>
          <span class="crm-field-pill">Status_vod__c</span>
        </div>
      </div>

      <div class="crm-obj-card shared" style="margin-bottom:12px;border-left-color:#9060D0;border-color:#4A2080;">
        <div class="crm-obj-name shared">Multichannel Consent</div>
        <div class="crm-obj-api">Multichannel_Consent_vod__c — shared by commercial and medical</div>
        <div class="crm-obj-desc">Records each HCP's opt-in or opt-out status per communication channel (Approved Email, remote detailing, text message) and jurisdiction (GDPR, CCPA, country-specific). Both commercial Approved Email and Medical Information digital responses are gated by this object. A consent withdrawal automatically suppresses all digital communications within hours.</div>
        <div class="crm-obj-fields">
          <span class="crm-field-pill">Channel_vod__c</span>
          <span class="crm-field-pill">Consent_Type_vod__c</span>
          <span class="crm-field-pill">Opt_In_Date_vod__c</span>
          <span class="crm-field-pill">Jurisdiction_vod__c</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Commercial Workflow SVG -->
  <figure class="vis-embed" aria-label="Commercial Rep Daily Workflow">
    <div class="vis-label"><span class="vis-icon">◈</span> Commercial Field Rep — Daily CRM Workflow (Veeva CRM Objects at Each Stage)</div>
    <div class="vis-inner" style="padding:20px;">
      <svg viewBox="0 0 960 320" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:700px;display:block;">
        <rect width="960" height="320" fill="#0D1117"/>
        <!-- Phase columns -->
        <!-- PRE-CALL (x=0–240) -->
        <rect x="0" y="0" width="240" height="30" fill="#0F1E35"/>
        <text x="120" y="20" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700" letter-spacing="1">PRE-CALL</text>
        <!-- CALL EXECUTION (x=240–560) -->
        <rect x="240" y="0" width="320" height="30" fill="#0A1A2A"/>
        <text x="400" y="20" text-anchor="middle" fill="#4A9AEA" font-size="11" font-weight="700" letter-spacing="1">CALL EXECUTION</text>
        <!-- POST-CALL (x=560–760) -->
        <rect x="560" y="0" width="200" height="30" fill="#101A10"/>
        <text x="660" y="20" text-anchor="middle" fill="#4ACA6A" font-size="11" font-weight="700" letter-spacing="1">POST-CALL</text>
        <!-- ANALYTICS (x=760–960) -->
        <rect x="760" y="0" width="200" height="30" fill="#1A1030"/>
        <text x="860" y="20" text-anchor="middle" fill="#C0A0FF" font-size="11" font-weight="700" letter-spacing="1">ANALYTICS</text>
        <!-- Phase dividers -->
        <line x1="240" y1="0" x2="240" y2="320" stroke="#21262D" stroke-width="1.5"/>
        <line x1="560" y1="0" x2="560" y2="320" stroke="#21262D" stroke-width="1.5"/>
        <line x1="760" y1="0" x2="760" y2="320" stroke="#21262D" stroke-width="1.5"/>

        <!-- ROW 1: CRM Object Used (y=40–100) -->
        <rect x="0" y="30" width="240" height="20" fill="#0A1222"/>
        <text x="120" y="44" text-anchor="middle" fill="#4A5568" font-size="8.5" font-weight="600" letter-spacing="1">CRM OBJECT</text>
        <rect x="240" y="30" width="320" height="20" fill="#0A1222"/>
        <text x="400" y="44" text-anchor="middle" fill="#4A5568" font-size="8.5" font-weight="600" letter-spacing="1">CRM OBJECT</text>
        <rect x="560" y="30" width="200" height="20" fill="#0A1222"/>
        <text x="660" y="44" text-anchor="middle" fill="#4A5568" font-size="8.5" font-weight="600" letter-spacing="1">CRM OBJECT</text>
        <rect x="760" y="30" width="200" height="20" fill="#0A1222"/>
        <text x="860" y="44" text-anchor="middle" fill="#4A5568" font-size="8.5" font-weight="600" letter-spacing="1">CRM OBJECT</text>

        <!-- Object labels -->
        <rect x="10" y="55" width="220" height="52" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1"/>
        <text x="120" y="74" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">Cycle Plan Account</text>
        <text x="120" y="89" text-anchor="middle" fill="#6B7280" font-size="9">Prioritised HCP list · Target call</text>
        <text x="120" y="100" text-anchor="middle" fill="#6B7280" font-size="9">count · Last-call date visible</text>

        <rect x="250" y="55" width="145" height="52" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1"/>
        <text x="322" y="74" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">Call Report</text>
        <text x="322" y="89" text-anchor="middle" fill="#6B7280" font-size="9">New record created</text>
        <text x="322" y="100" text-anchor="middle" fill="#6B7280" font-size="9">Status = Draft</text>

        <rect x="405" y="55" width="145" height="52" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1"/>
        <text x="477" y="74" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">CLM Presentation</text>
        <text x="477" y="89" text-anchor="middle" fill="#6B7280" font-size="9">iPad visual aid launched</text>
        <text x="477" y="100" text-anchor="middle" fill="#6B7280" font-size="9">Slide timing tracked</text>

        <rect x="570" y="55" width="180" height="52" rx="5" fill="#0F1835" stroke="#1B3A6B" stroke-width="1"/>
        <text x="660" y="74" text-anchor="middle" fill="#7EC8C8" font-size="11" font-weight="700">Call Report → Submit</text>
        <text x="660" y="89" text-anchor="middle" fill="#6B7280" font-size="9">Status: Draft → Submitted</text>
        <text x="660" y="100" text-anchor="middle" fill="#6B7280" font-size="9">Locked · PDMA receipt sent</text>

        <rect x="770" y="55" width="180" height="52" rx="5" fill="#1A1030" stroke="#4A2080" stroke-width="1"/>
        <text x="860" y="74" text-anchor="middle" fill="#C0A0FF" font-size="11" font-weight="700">SFE Dashboard</text>
        <text x="860" y="89" text-anchor="middle" fill="#6B7280" font-size="9">Call rate · Reach · Freq.</text>
        <text x="860" y="100" text-anchor="middle" fill="#6B7280" font-size="9">Sample utilisation rate</text>

        <!-- ROW 2: Rep Action (y=115–175) -->
        <rect x="0" y="115" width="960" height="16" fill="#080C10"/>
        <text x="480" y="127" text-anchor="middle" fill="#4A5568" font-size="8" font-weight="600" letter-spacing="1">REP ACTION</text>

        <rect x="10" y="135" width="220" height="48" rx="5" fill="#0D0D0D" stroke="#21262D" stroke-width="1"/>
        <text x="120" y="153" text-anchor="middle" fill="#E6EAF0" font-size="10.5">Opens Veeva CRM → reviews</text>
        <text x="120" y="167" text-anchor="middle" fill="#E6EAF0" font-size="10.5">today's call list → sets route</text>
        <text x="120" y="178" text-anchor="middle" fill="#6B7280" font-size="9">Sets pre-call objective</text>

        <rect x="250" y="135" width="300" height="48" rx="5" fill="#0D0D0D" stroke="#21262D" stroke-width="1"/>
        <text x="400" y="153" text-anchor="middle" fill="#E6EAF0" font-size="10.5">Launches CLM → details product → captures</text>
        <text x="400" y="167" text-anchor="middle" fill="#E6EAF0" font-size="10.5">key message reaction → drops sample</text>
        <text x="400" y="178" text-anchor="middle" fill="#6B7280" font-size="9">Captures HCP e-signature for PDMA compliance</text>

        <rect x="570" y="135" width="180" height="48" rx="5" fill="#0D0D0D" stroke="#21262D" stroke-width="1"/>
        <text x="660" y="153" text-anchor="middle" fill="#E6EAF0" font-size="10.5">Completes call report →</text>
        <text x="660" y="167" text-anchor="middle" fill="#E6EAF0" font-size="10.5">adds next call objective</text>
        <text x="660" y="178" text-anchor="middle" fill="#6B7280" font-size="9">Submits → triggers AE check</text>

        <rect x="770" y="135" width="180" height="48" rx="5" fill="#0D0D0D" stroke="#21262D" stroke-width="1"/>
        <text x="860" y="153" text-anchor="middle" fill="#E6EAF0" font-size="10.5">Views personal dashboard</text>
        <text x="860" y="167" text-anchor="middle" fill="#E6EAF0" font-size="10.5">→ adjusts next cycle plan</text>
        <text x="860" y="178" text-anchor="middle" fill="#6B7280" font-size="9">Manager views team rollup</text>

        <!-- ROW 3: System Action (y=190–260) -->
        <rect x="0" y="190" width="960" height="16" fill="#080C10"/>
        <text x="480" y="202" text-anchor="middle" fill="#4A5568" font-size="8" font-weight="600" letter-spacing="1">SYSTEM AUTO-ACTION</text>

        <rect x="10" y="210" width="220" height="48" rx="5" fill="#070B10" stroke="#1A2A3A" stroke-width="1"/>
        <text x="120" y="228" text-anchor="middle" fill="#4A7ABF" font-size="10">Cycle Plan Account syncs</text>
        <text x="120" y="242" text-anchor="middle" fill="#4A7ABF" font-size="10">suggested call priority via AI</text>
        <text x="120" y="253" text-anchor="middle" fill="#4A5568" font-size="9">(Next Best Action engine)</text>

        <rect x="250" y="210" width="300" height="48" rx="5" fill="#070B10" stroke="#1A2A3A" stroke-width="1"/>
        <text x="400" y="228" text-anchor="middle" fill="#4A7ABF" font-size="10">CLM records slide ID, duration, swipe path</text>
        <text x="400" y="242" text-anchor="middle" fill="#4A7ABF" font-size="10">Sample lot qty decremented in real time</text>
        <text x="400" y="253" text-anchor="middle" fill="#4A5568" font-size="9">Off-label topic blocked by validation rule</text>

        <rect x="570" y="210" width="180" height="48" rx="5" fill="#070B10" stroke="#1A2A3A" stroke-width="1"/>
        <text x="660" y="228" text-anchor="middle" fill="#4A7ABF" font-size="10">PDMA receipt auto-generated</text>
        <text x="660" y="242" text-anchor="middle" fill="#4A7ABF" font-size="10">Adverse event flag → PV queue</text>
        <text x="660" y="253" text-anchor="middle" fill="#4A5568" font-size="9">Record locked, immutable</text>

        <rect x="770" y="210" width="180" height="48" rx="5" fill="#070B10" stroke="#1A2A3A" stroke-width="1"/>
        <text x="860" y="228" text-anchor="middle" fill="#4A7ABF" font-size="10">Data flows to Veeva Align,</text>
        <text x="860" y="242" text-anchor="middle" fill="#4A7ABF" font-size="10">IQVIA, Salesforce Analytics</text>
        <text x="860" y="253" text-anchor="middle" fill="#4A5568" font-size="9">QBR reporting auto-populated</text>

        <!-- Phase arrows at bottom -->
        <path d="M238,290 L244,285 L244,295 Z" fill="#21262D"/>
        <path d="M558,290 L564,285 L564,295 Z" fill="#21262D"/>
        <path d="M758,290 L764,285 L764,295 Z" fill="#21262D"/>
        <line x1="0" y1="290" x2="960" y2="290" stroke="#21262D" stroke-width="1"/>
        <text x="120" y="308" text-anchor="middle" fill="#4A5568" font-size="9">Morning planning (15 min)</text>
        <text x="400" y="308" text-anchor="middle" fill="#4A5568" font-size="9">During HCP visit (10–20 min per call)</text>
        <text x="660" y="308" text-anchor="middle" fill="#4A5568" font-size="9">Post-call (5 min)</text>
        <text x="860" y="308" text-anchor="middle" fill="#4A5568" font-size="9">Ongoing / weekly</text>
      </svg>
    </div>
    <figcaption class="vis-cap">Commercial Field Rep — CRM workflow from morning planning to post-call analytics</figcaption>
  </figure>

  <!-- ═══════════════════════════════════
       MSL / MEDICAL AFFAIRS WORKFLOW
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-msl">Medical Affairs (MSL) — Objects &amp; Workflow</h3>

  <p>The MSL uses the same Veeva CRM instance as the commercial team but operates under a completely different permission profile. The MSL's Call record type omits all commercial fields — there is no product detail priority, no CLM presentation, no sample drop. What the MSL sees instead is a scientific exchange workspace: free-text discussion topic fields, insight capture, medical inquiry logging, and KOL profile management. Critically, the MSL's call data is not visible to the commercial field force — the system enforces the firewall at the data layer, not just through policy.</p>

  <!-- MSL Workflow SVG -->
  <figure class="vis-embed" aria-label="MSL Scientific Exchange Workflow">
    <div class="vis-label"><span class="vis-icon">◈</span> MSL Scientific Exchange — CRM Workflow &amp; Objects</div>
    <div class="vis-inner" style="padding:20px;">
      <svg viewBox="0 0 960 280" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:700px;display:block;">
        <rect width="960" height="280" fill="#0D1117"/>
        <!-- Phase columns -->
        <rect x="0" y="0" width="240" height="30" fill="#071E1E"/>
        <text x="120" y="20" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700" letter-spacing="1">PRE-MEETING</text>
        <rect x="240" y="0" width="320" height="30" fill="#051515"/>
        <text x="400" y="20" text-anchor="middle" fill="#1A7A7A" font-size="11" font-weight="700" letter-spacing="1">SCIENTIFIC EXCHANGE</text>
        <rect x="560" y="0" width="200" height="30" fill="#071E1E"/>
        <text x="660" y="20" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700" letter-spacing="1">DOCUMENTATION</text>
        <rect x="760" y="0" width="200" height="30" fill="#0D1A10"/>
        <text x="860" y="20" text-anchor="middle" fill="#4ABA6A" font-size="11" font-weight="700" letter-spacing="1">FOLLOW-UP</text>
        <line x1="240" y1="0" x2="240" y2="280" stroke="#21262D" stroke-width="1.5"/>
        <line x1="560" y1="0" x2="560" y2="280" stroke="#21262D" stroke-width="1.5"/>
        <line x1="760" y1="0" x2="760" y2="280" stroke="#21262D" stroke-width="1.5"/>

        <!-- Row 1: Objects -->
        <rect x="0" y="30" width="960" height="16" fill="#080C10"/>
        <text x="480" y="42" text-anchor="middle" fill="#4A5568" font-size="8" font-weight="600" letter-spacing="1">CRM OBJECTS USED</text>

        <rect x="10" y="50" width="220" height="52" rx="5" fill="#071E1E" stroke="#0B5E5E" stroke-width="1"/>
        <text x="120" y="69" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Account + KOL Profile</text>
        <text x="120" y="84" text-anchor="middle" fill="#6B7280" font-size="9">Past scientific exchanges · Tier</text>
        <text x="120" y="95" text-anchor="middle" fill="#6B7280" font-size="9">Publications · Advisory board history</text>

        <rect x="250" y="50" width="145" height="52" rx="5" fill="#071E1E" stroke="#0B5E5E" stroke-width="1"/>
        <text x="322" y="69" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">MSL Call Report</text>
        <text x="322" y="84" text-anchor="middle" fill="#6B7280" font-size="9">Call_vod__c (Medical RT)</text>
        <text x="322" y="95" text-anchor="middle" fill="#6B7280" font-size="9">Non-promotional fields only</text>

        <rect x="405" y="50" width="145" height="52" rx="5" fill="#071E1E" stroke="#0B5E5E" stroke-width="1"/>
        <text x="477" y="69" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Medical Inquiry</text>
        <text x="477" y="84" text-anchor="middle" fill="#6B7280" font-size="9">If HCP raises question</text>
        <text x="477" y="95" text-anchor="middle" fill="#6B7280" font-size="9">Off-label → SRL triggered</text>

        <rect x="570" y="50" width="180" height="52" rx="5" fill="#071E1E" stroke="#0B5E5E" stroke-width="1"/>
        <text x="660" y="69" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Insight_vod__c</text>
        <text x="660" y="84" text-anchor="middle" fill="#6B7280" font-size="9">Scientific observation logged</text>
        <text x="660" y="95" text-anchor="middle" fill="#6B7280" font-size="9">Category · Priority · Area</text>

        <rect x="770" y="50" width="180" height="52" rx="5" fill="#071E1E" stroke="#0B5E5E" stroke-width="1"/>
        <text x="860" y="69" text-anchor="middle" fill="#2A9A9A" font-size="11" font-weight="700">Survey / Next Action</text>
        <text x="860" y="84" text-anchor="middle" fill="#6B7280" font-size="9">IIS form if applicable</text>
        <text x="860" y="95" text-anchor="middle" fill="#6B7280" font-size="9">Advisory board nomination</text>

        <!-- Row 2: MSL Action -->
        <rect x="0" y="110" width="960" height="16" fill="#080C10"/>
        <text x="480" y="122" text-anchor="middle" fill="#4A5568" font-size="8" font-weight="600" letter-spacing="1">MSL ACTION</text>

        <rect x="10" y="130" width="220" height="48" rx="5" fill="#060E0E" stroke="#0D2525" stroke-width="1"/>
        <text x="120" y="148" text-anchor="middle" fill="#C9D1D9" font-size="10">Reviews KOL account: prior calls,</text>
        <text x="120" y="162" text-anchor="middle" fill="#C9D1D9" font-size="10">publications, insights history</text>
        <text x="120" y="174" text-anchor="middle" fill="#6B7280" font-size="9">Pulls scientific deck from Vault Medical</text>

        <rect x="250" y="130" width="300" height="48" rx="5" fill="#060E0E" stroke="#0D2525" stroke-width="1"/>
        <text x="400" y="148" text-anchor="middle" fill="#C9D1D9" font-size="10">Opens MSL Call → on-label scientific discussion</text>
        <text x="400" y="162" text-anchor="middle" fill="#C9D1D9" font-size="10">→ if unsolicited off-label → opens Med Inquiry</text>
        <text x="400" y="174" text-anchor="middle" fill="#6B7280" font-size="9">Cannot show promotional CLM content — system blocked</text>

        <rect x="570" y="130" width="180" height="48" rx="5" fill="#060E0E" stroke="#0D2525" stroke-width="1"/>
        <text x="660" y="148" text-anchor="middle" fill="#C9D1D9" font-size="10">Submits MSL call report →</text>
        <text x="660" y="162" text-anchor="middle" fill="#C9D1D9" font-size="10">logs insight categories</text>
        <text x="660" y="174" text-anchor="middle" fill="#6B7280" font-size="9">Record invisible to commercial reps</text>

        <rect x="770" y="130" width="180" height="48" rx="5" fill="#060E0E" stroke="#0D2525" stroke-width="1"/>
        <text x="860" y="148" text-anchor="middle" fill="#C9D1D9" font-size="10">SRL sent via Vault Medical</text>
        <text x="860" y="162" text-anchor="middle" fill="#C9D1D9" font-size="10">if Med Inquiry was raised</text>
        <text x="860" y="174" text-anchor="middle" fill="#6B7280" font-size="9">Insights reviewed by MSL Director</text>

        <!-- Row 3: Compliance guardrails -->
        <rect x="0" y="186" width="960" height="16" fill="#080C10"/>
        <text x="480" y="198" text-anchor="middle" fill="#4A5568" font-size="8" font-weight="600" letter-spacing="1">COMPLIANCE GUARDRAILS (ENFORCED BY CRM)</text>
        <rect x="10" y="206" width="220" height="34" rx="4" fill="#0A0A06" stroke="#3A3010" stroke-width="1"/>
        <text x="120" y="221" text-anchor="middle" fill="#7A6A30" font-size="9">✓ No commercial call list access</text>
        <text x="120" y="234" text-anchor="middle" fill="#7A6A30" font-size="9">✓ No prescribing data visible</text>
        <rect x="250" y="206" width="300" height="34" rx="4" fill="#0A0A06" stroke="#3A3010" stroke-width="1"/>
        <text x="400" y="221" text-anchor="middle" fill="#7A6A30" font-size="9">✓ No sample drop field · ✓ No CLM promotional content</text>
        <text x="400" y="234" text-anchor="middle" fill="#7A6A30" font-size="9">✓ Off-label only on unsolicited inbound — validation enforced</text>
        <rect x="570" y="206" width="380" height="34" rx="4" fill="#0A0A06" stroke="#3A3010" stroke-width="1"/>
        <text x="760" y="221" text-anchor="middle" fill="#7A6A30" font-size="9">✓ MSL IC plan cannot be tied to Rx volume · ✓ Insight data not accessible to Sales</text>
        <text x="760" y="234" text-anchor="middle" fill="#7A6A30" font-size="9">✓ All records 21 CFR Part 11 compliant · timestamped · immutable</text>
      </svg>
    </div>
    <figcaption class="vis-cap">MSL scientific exchange workflow — objects, actions, and compliance guardrails</figcaption>
  </figure>

  <!-- ═══════════════════════════════════
       SAMPLE MANAGEMENT (PDMA)
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-sample">Sample Management — PDMA Compliance in Veeva CRM</h3>

  <p>The Prescription Drug Marketing Act (21 CFR Part 203) requires that every drug sample transferred from a company representative to a licensed healthcare professional be documented with a signed receipt, lot number, quantity, and an auditable chain of custody. Veeva CRM enforces every one of these requirements at the point of interaction — the rep cannot submit a call report that includes a sample drop without an HCP e-signature. Sample lots are tracked from receipt into the rep's inventory to final dispensing, with quarterly reconciliation built into the system workflow.</p>

  <figure class="vis-embed" aria-label="PDMA Sample Management Flow">
    <div class="vis-label"><span class="vis-icon">◈</span> PDMA Sample Management — End-to-End Flow in Veeva CRM</div>
    <div class="vis-inner" style="padding:24px 20px;">
      <svg viewBox="0 0 960 200" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:700px;display:block;">
        <rect width="960" height="200" fill="#0D1117"/>
        <!-- 8 steps horizontal -->
        <!-- Step definitions: x positions -->
        <!-- Step width ~108px, gap ~12px, 8 steps: 8*108 + 7*12 = 864 + 84 = hmm, let me use 9 steps at 95px each + 12px gap -->
        <!-- 9 steps: 9*95 + 8*12 = 855+96=951px, start at x=4 -->
        <defs>
          <linearGradient id="sampleGrad" x1="0" y1="0" x2="1" y2="0">
            <stop offset="0%" stop-color="#0F1E35"/>
            <stop offset="100%" stop-color="#0F2A20"/>
          </linearGradient>
        </defs>

        <!-- Step boxes + labels -->
        <!-- 1: Sample Lot Received -->
        <rect x="4" y="30" width="95" height="80" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="51" y="56" text-anchor="middle" fill="#4A7ABF" font-size="18">⊞</text>
        <text x="51" y="73" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Sample Lot</text>
        <text x="51" y="86" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Received</text>
        <text x="51" y="103" text-anchor="middle" fill="#4A5568" font-size="8">Lot # · Expiry</text>

        <!-- 2: Territory Assignment -->
        <rect x="111" y="30" width="95" height="80" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="158" y="56" text-anchor="middle" fill="#4A7ABF" font-size="18">◎</text>
        <text x="158" y="73" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Territory</text>
        <text x="158" y="86" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Allocation</text>
        <text x="158" y="103" text-anchor="middle" fill="#4A5568" font-size="8">Qty per rep</text>

        <!-- 3: Rep Inventory -->
        <rect x="218" y="30" width="95" height="80" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="265" y="56" text-anchor="middle" fill="#4A7ABF" font-size="18">≡</text>
        <text x="265" y="73" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Rep Inventory</text>
        <text x="265" y="86" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">In CRM</text>
        <text x="265" y="103" text-anchor="middle" fill="#4A5568" font-size="8">Live balance</text>

        <!-- 4: HCP Sample Request -->
        <rect x="325" y="30" width="95" height="80" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="372" y="56" text-anchor="middle" fill="#4A7ABF" font-size="18">✉</text>
        <text x="372" y="73" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">HCP Sample</text>
        <text x="372" y="86" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Request</text>
        <text x="372" y="103" text-anchor="middle" fill="#4A5568" font-size="8">Written/verbal</text>

        <!-- 5: E-Signature Capture -->
        <rect x="432" y="30" width="95" height="80" rx="5" fill="#1A1E10" stroke="#4A6A10" stroke-width="2"/>
        <text x="479" y="56" text-anchor="middle" fill="#8ABA30" font-size="18">✍</text>
        <text x="479" y="73" text-anchor="middle" fill="#AADA50" font-size="9.5" font-weight="700">HCP e-Sig</text>
        <text x="479" y="86" text-anchor="middle" fill="#AADA50" font-size="9.5" font-weight="700">Captured</text>
        <text x="479" y="103" text-anchor="middle" fill="#5A7A30" font-size="8">PDMA mandatory</text>

        <!-- 6: PDMA Receipt -->
        <rect x="539" y="30" width="95" height="80" rx="5" fill="#1A2010" stroke="#4A6010" stroke-width="1.5"/>
        <text x="586" y="56" text-anchor="middle" fill="#8ABA30" font-size="18">⊡</text>
        <text x="586" y="73" text-anchor="middle" fill="#AADA50" font-size="9.5" font-weight="700">PDMA Receipt</text>
        <text x="586" y="86" text-anchor="middle" fill="#AADA50" font-size="9.5" font-weight="700">Auto-generated</text>
        <text x="586" y="103" text-anchor="middle" fill="#5A7A30" font-size="8">Timestamped · Locked</text>

        <!-- 7: Inventory Decrement -->
        <rect x="646" y="30" width="95" height="80" rx="5" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="693" y="56" text-anchor="middle" fill="#4A7ABF" font-size="18">↓</text>
        <text x="693" y="73" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Lot Qty</text>
        <text x="693" y="86" text-anchor="middle" fill="#7EC8C8" font-size="9.5" font-weight="700">Decremented</text>
        <text x="693" y="103" text-anchor="middle" fill="#4A5568" font-size="8">Real-time balance</text>

        <!-- 8: Quarterly Reconciliation -->
        <rect x="753" y="30" width="95" height="80" rx="5" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <text x="800" y="56" text-anchor="middle" fill="#9060D0" font-size="18">⊕</text>
        <text x="800" y="73" text-anchor="middle" fill="#C0A0FF" font-size="9.5" font-weight="700">Quarterly</text>
        <text x="800" y="86" text-anchor="middle" fill="#C0A0FF" font-size="9.5" font-weight="700">Reconciliation</text>
        <text x="800" y="103" text-anchor="middle" fill="#6A5080" font-size="8">Discrepancy flag</text>

        <!-- 9: Audit Trail -->
        <rect x="860" y="30" width="95" height="80" rx="5" fill="#1A1010" stroke="#5A2000" stroke-width="1.5"/>
        <text x="907" y="56" text-anchor="middle" fill="#E05A00" font-size="18">⊙</text>
        <text x="907" y="73" text-anchor="middle" fill="#FFA657" font-size="9.5" font-weight="700">FDA Audit</text>
        <text x="907" y="86" text-anchor="middle" fill="#FFA657" font-size="9.5" font-weight="700">Trail (3 yr)</text>
        <text x="907" y="103" text-anchor="middle" fill="#7A4020" font-size="8">21 CFR 203</text>

        <!-- Connecting arrows -->
        <line x1="99" y1="70" x2="111" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="206" y1="70" x2="218" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="313" y1="70" x2="325" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="420" y1="70" x2="432" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="527" y1="70" x2="539" y2="70" stroke="#4A6A10" stroke-width="2" marker-end="url(#arrd)"/>
        <line x1="634" y1="70" x2="646" y2="70" stroke="#4A6A10" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="741" y1="70" x2="753" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="848" y1="70" x2="860" y2="70" stroke="#30363D" stroke-width="1.5" marker-end="url(#arrd)"/>

        <!-- Step numbers -->
        <circle cx="51" cy="30" r="9" fill="#1B3A6B"/>
        <text x="51" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">1</text>
        <circle cx="158" cy="30" r="9" fill="#1B3A6B"/>
        <text x="158" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">2</text>
        <circle cx="265" cy="30" r="9" fill="#1B3A6B"/>
        <text x="265" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">3</text>
        <circle cx="372" cy="30" r="9" fill="#1B3A6B"/>
        <text x="372" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">4</text>
        <circle cx="479" cy="30" r="9" fill="#4A6A10"/>
        <text x="479" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">5</text>
        <circle cx="586" cy="30" r="9" fill="#4A6010"/>
        <text x="586" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">6</text>
        <circle cx="693" cy="30" r="9" fill="#1B3A6B"/>
        <text x="693" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">7</text>
        <circle cx="800" cy="30" r="9" fill="#4A2080"/>
        <text x="800" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">8</text>
        <circle cx="907" cy="30" r="9" fill="#7A3000"/>
        <text x="907" y="34" text-anchor="middle" fill="white" font-size="9" font-weight="700">9</text>

        <!-- PDMA compliance band annotation -->
        <rect x="432" y="118" width="202" height="22" rx="4" fill="#1A2010" stroke="#4A6A10" stroke-width="1"/>
        <text x="533" y="133" text-anchor="middle" fill="#8ABA30" font-size="9">⚖ PDMA Compliance Window — 21 CFR Part 203</text>
        <line x1="479" y1="110" x2="479" y2="118" stroke="#4A6A10" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="586" y1="110" x2="586" y2="118" stroke="#4A6A10" stroke-width="1" stroke-dasharray="2,2"/>

        <!-- 3-year retention annotation -->
        <rect x="753" y="118" width="202" height="22" rx="4" fill="#1A1010" stroke="#5A2000" stroke-width="1"/>
        <text x="854" y="133" text-anchor="middle" fill="#FFA657" font-size="9">⊙ 3-Year Immutable Audit Trail Required</text>
        <line x1="800" y1="110" x2="800" y2="118" stroke="#5A2000" stroke-width="1" stroke-dasharray="2,2"/>
        <line x1="907" y1="110" x2="907" y2="118" stroke="#5A2000" stroke-width="1" stroke-dasharray="2,2"/>

        <text x="480" y="185" text-anchor="middle" fill="#4A5568" font-size="9" font-style="italic">Sample lots that expire before dispensing must be documented and destroyed with a witnessed destruction record — also captured in Veeva CRM</text>
      </svg>
    </div>
    <figcaption class="vis-cap">PDMA-compliant sample management — 9-step chain from lot receipt to FDA audit trail</figcaption>
  </figure>

  <!-- ═══════════════════════════════════
       CLM — CLOSED LOOP MARKETING
  ═══════════════════════════════════ -->
  <h3 id="veeva-crm-clm">Closed-Loop Marketing (CLM) — The Feedback Engine</h3>

  <p>CLM is the mechanism by which promotional messaging is continuously refined based on real-world HCP engagement. Content created by marketing is approved through Vault PromoMats, automatically pushed into the rep's CRM content library, presented via iPad during calls, and then — crucially — the engagement data flows back to analytics. Which slides were shown? In what order? For how long? Which key messages prompted a positive reaction? This feedback loop closes the gap between the messages brand teams intend to deliver and the messages HCPs actually receive and respond to.</p>

  <!-- CLM Loop SVG -->
  <figure class="vis-embed" aria-label="CLM Closed-Loop Marketing Cycle">
    <div class="vis-label"><span class="vis-icon">◈</span> Closed-Loop Marketing (CLM) — The Veeva Feedback Cycle</div>
    <div class="vis-inner" style="padding:28px 20px;">
      <svg viewBox="0 0 960 380" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;min-width:640px;display:block;">
        <rect width="960" height="380" fill="#0D1117"/>
        <!-- Center label -->
        <circle cx="480" cy="190" r="68" fill="#111820" stroke="#21262D" stroke-width="1.5"/>
        <text x="480" y="182" text-anchor="middle" fill="#4A5568" font-size="10" font-weight="700" letter-spacing="1">CLM</text>
        <text x="480" y="197" text-anchor="middle" fill="#4A5568" font-size="10" font-weight="700" letter-spacing="1">FEEDBACK</text>
        <text x="480" y="212" text-anchor="middle" fill="#4A5568" font-size="10" font-weight="700" letter-spacing="1">LOOP</text>

        <!-- 8 nodes around the circle at r=165 from center (480,190) -->
        <!-- Angles: 0=top, then clockwise every 45° -->
        <!-- Node dimensions: 130w x 65h -->

        <!-- Node 1: top (270° = 12 o'clock) cx=480, cy=190-165=25 → center at 480,25 -->
        <rect x="415" y="10" width="130" height="62" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="480" y="32" text-anchor="middle" fill="#4A9AEA" font-size="9.5" font-weight="700">① Brand Team</text>
        <text x="480" y="46" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="600">Creates Content</text>
        <text x="480" y="60" text-anchor="middle" fill="#4A5568" font-size="8.5">Visual aids · Emails · Leave-behinds</text>
        <circle cx="480" cy="10" r="9" fill="#1B3A6B"/>
        <text x="480" y="14" text-anchor="middle" fill="white" font-size="9" font-weight="700">1</text>

        <!-- Node 2: 45° (top-right) cx=480+165*sin45=480+117=597, cy=190-165*cos45=190-117=73 -->
        <rect x="620" y="42" width="130" height="62" rx="7" fill="#1A1030" stroke="#4A2080" stroke-width="1.5"/>
        <text x="685" y="64" text-anchor="middle" fill="#9060D0" font-size="9.5" font-weight="700">② MLR Review</text>
        <text x="685" y="78" text-anchor="middle" fill="#C0A0FF" font-size="10" font-weight="600">Vault PromoMats</text>
        <text x="685" y="92" text-anchor="middle" fill="#4A5568" font-size="8.5">Med · Legal · Reg simultaneous review</text>
        <circle cx="750" cy="42" r="9" fill="#4A2080"/>
        <text x="750" y="46" text-anchor="middle" fill="white" font-size="9" font-weight="700">2</text>

        <!-- Node 3: 90° (right) cx=480+165=645, cy=190 -->
        <rect x="800" y="160" width="148" height="62" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="874" y="182" text-anchor="middle" fill="#4A9AEA" font-size="9.5" font-weight="700">③ Auto-Publish</text>
        <text x="874" y="196" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="600">CRM Content Library</text>
        <text x="874" y="210" text-anchor="middle" fill="#4A5568" font-size="8.5">Expires auto-withdrawn · Versioned</text>
        <circle cx="948" cy="160" r="9" fill="#1B3A6B"/>
        <text x="948" y="164" text-anchor="middle" fill="white" font-size="9" font-weight="700">3</text>

        <!-- Node 4: 135° (bottom-right) cx=480+117=597, cy=190+117=307 -->
        <rect x="622" y="295" width="130" height="62" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="687" y="317" text-anchor="middle" fill="#4A9AEA" font-size="9.5" font-weight="700">④ Rep Presents</text>
        <text x="687" y="331" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="600">iPad CLM Session</text>
        <text x="687" y="345" text-anchor="middle" fill="#4A5568" font-size="8.5">Approved content only · Slide order free</text>
        <circle cx="752" cy="357" r="9" fill="#1B3A6B"/>
        <text x="752" y="361" text-anchor="middle" fill="white" font-size="9" font-weight="700">4</text>

        <!-- Node 5: 180° (bottom) cx=480, cy=190+165=355 -->
        <rect x="415" y="310" width="130" height="62" rx="7" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="480" y="332" text-anchor="middle" fill="#2A9A9A" font-size="9.5" font-weight="700">⑤ Engagement</text>
        <text x="480" y="346" text-anchor="middle" fill="#2A9A9A" font-size="10" font-weight="600">Data Captured</text>
        <text x="480" y="360" text-anchor="middle" fill="#4A5568" font-size="8.5">Slide ID · Time · Swipe · Reaction</text>
        <circle cx="480" cy="372" r="9" fill="#0B5E5E"/>
        <text x="480" y="376" text-anchor="middle" fill="white" font-size="9" font-weight="700">5</text>

        <!-- Node 6: 225° (bottom-left) cx=480-117=363, cy=190+117=307 -->
        <rect x="212" y="295" width="130" height="62" rx="7" fill="#071E1E" stroke="#0B5E5E" stroke-width="1.5"/>
        <text x="277" y="317" text-anchor="middle" fill="#2A9A9A" font-size="9.5" font-weight="700">⑥ Analytics</text>
        <text x="277" y="331" text-anchor="middle" fill="#2A9A9A" font-size="10" font-weight="600">SFE Dashboard</text>
        <text x="277" y="345" text-anchor="middle" fill="#4A5568" font-size="8.5">Message adoption · Slide heatmap</text>
        <circle cx="212" cy="357" r="9" fill="#0B5E5E"/>
        <text x="212" y="361" text-anchor="middle" fill="white" font-size="9" font-weight="700">6</text>

        <!-- Node 7: 270° (left) cx=480-165=315, cy=190 -->
        <rect x="14" y="160" width="148" height="62" rx="7" fill="#1A1010" stroke="#5A2000" stroke-width="1.5"/>
        <text x="88" y="182" text-anchor="middle" fill="#FFA657" font-size="9.5" font-weight="700">⑦ Insight Review</text>
        <text x="88" y="196" text-anchor="middle" fill="#FFA657" font-size="10" font-weight="600">Brand + Market Res.</text>
        <text x="88" y="210" text-anchor="middle" fill="#4A5568" font-size="8.5">Low-adoption msgs flagged for revision</text>
        <circle cx="14" cy="160" r="9" fill="#7A3000"/>
        <text x="14" y="164" text-anchor="middle" fill="white" font-size="9" font-weight="700">7</text>

        <!-- Node 8: 315° (top-left) cx=480-117=363, cy=190-117=73 -->
        <rect x="212" y="42" width="130" height="62" rx="7" fill="#0F1E35" stroke="#1B3A6B" stroke-width="1.5"/>
        <text x="277" y="64" text-anchor="middle" fill="#4A9AEA" font-size="9.5" font-weight="700">⑧ Content Update</text>
        <text x="277" y="78" text-anchor="middle" fill="#7EC8C8" font-size="10" font-weight="600">Re-submit to MLR</text>
        <text x="277" y="92" text-anchor="middle" fill="#4A5568" font-size="8.5">Revised slides → back to Vault → cycle</text>
        <circle cx="212" cy="42" r="9" fill="#1B3A6B"/>
        <text x="212" y="46" text-anchor="middle" fill="white" font-size="9" font-weight="700">8</text>

        <!-- Arc arrows connecting nodes (simplified straight lines at angle) -->
        <line x1="545" y1="40" x2="620" y2="62" stroke="#4A2080" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="750" y1="104" x2="800" y2="175" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="800" y1="207" x2="752" y2="295" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="687" y1="357" x2="545" y2="370" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#arrm)"/>
        <line x1="415" y1="370" x2="277" y2="357" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#arrm)"/>
        <line x1="212" y1="312" x2="162" y2="222" stroke="#0B5E5E" stroke-width="1.5" marker-end="url(#arrm)"/>
        <line x1="88" y1="160" x2="212" y2="104" stroke="#FFA657" stroke-width="1.5" marker-end="url(#arrd)"/>
        <line x1="342" y1="52" x2="415" y2="28" stroke="#1B3A6B" stroke-width="1.5" marker-end="url(#arrb)"/>
      </svg>
    </div>
    <figcaption class="vis-cap">CLM Closed-Loop Marketing — from content creation through HCP engagement back to optimised messaging</figcaption>
  </figure>

  {CLM_EXTRA_NEW}

  {CRM_EXTRA2}

  <div class="ornament">✦ &nbsp; ✦ &nbsp; ✦</div>

  {VAULT_EXTRA}

  {VAULT_MED_EXTRA}

  {NETWORK_EXTRA}

  <h2 id="veeva-events">Events Management — Sunshine Act Compliance</h2>
  <p>Every speaker program, advisory board, and medical symposium involving an HCP runs through Veeva Events Management. The system enforces Fair Market Value (FMV) caps on honoraria, tracks every meal, travel reimbursement, and consulting fee per HCP NPI, and generates the annual Open Payments (Sunshine Act) data file submitted to CMS each March. Anti-Kickback Statute guardrails — venue caps, meal caps, documentation of educational purpose — are built into the event request workflow.</p>

  {VEEVA_USERMGMT}

  <figure class="vis-embed" aria-label="Veeva Platform Ecosystem">
    <div class="vis-label"><span class="vis-icon">◈</span> Veeva Platform Ecosystem — Full System Map &amp; Data Flows</div>
    <div class="vis-inner">{sec_veeva}</div>
    <figcaption class="vis-cap">Veeva Platform Ecosystem — Full System Map &amp; Data Flows</figcaption>
  </figure>

  {nav_ch11}
</div>

<!-- ══════════════ GLOSSARY ══════════════ -->
<div class="ch-divider ch-gloss"></div>
<div class="chapter" id="glossary">
  <div class="ch-running">Reference Section · A–Z Glossary</div>
  <div class="ch-decorator">
    <div class="ch-big-num" style="color:var(--border-2);">A–Z</div>
    <div class="ch-heading-block">
      <div class="ch-label">
        <span class="ch-pill" style="background:#6B7280;">Reference</span>
      </div>
      <h1>Glossary of Key Terms</h1>
    </div>
  </div>
  <p class="lead">Every term defined — from regulatory frameworks to commercial operations. Use the search to filter instantly.</p>
  <input class="gloss-search" id="glossSearch" type="search"
         placeholder="Search terms (e.g. CAPA, GxP, PDMA, MLR)…"
         aria-label="Search glossary"
         oninput="filterGloss(this.value)"/>
  <dl class="glossary" id="glossDL">
    <dt id="g-ae">Adverse Event (AE / SAE)</dt>
    <dd>Any unintended medical occurrence in a patient using a drug. <strong>SAE (Serious AE)</strong>: results in death, life-threat, hospitalization, disability, or congenital anomaly. Any AE reported to the company must reach Pharmacovigilance within 24 hours; unexpected SAEs must reach the FDA within 15 days.</dd>
    <dt id="g-aks">Anti-Kickback Statute (AKS)</dt>
    <dd>42 USC §1320a-7b(b). Prohibits offering, paying, or receiving anything of value to induce referrals covered by federal healthcare programs. Speaker honoraria, consulting fees, and advisory board payments must reflect Fair Market Value for genuine services — not prescribing volume.</dd>
    <dt id="g-amcp">AMCP Dossier</dt>
    <dd>A comprehensive scientific and economic document (Academy of Managed Care Pharmacy format) submitted to health plans and hospital P&amp;T committees to support formulary listing. Includes clinical summaries, HEOR models, budget impact analysis, and outcomes-based contract proposals.</dd>
    <dt id="g-capa">CAPA — Corrective &amp; Preventive Action</dt>
    <dd>Quality system process (21 CFR Part 820) triggered when deviations, audit findings, or non-conformances occur. Corrective action eliminates the cause of an existing problem; preventive action prevents future recurrence. Process: Identify → Root Cause Analysis → Plan → Implement → Verify → Close. Tools: fishbone, 5-Whys, FMEA.</dd>
    <dt id="g-cfr11">21 CFR Part 11</dt>
    <dd>FDA regulation governing electronic records and electronic signatures. Requires audit trails (immutable, timestamped), access controls, and system validation. Applies to Veeva Vault, CRM, and any system used in regulated processes. ALCOA+ principle: records must be Attributable, Legible, Contemporaneous, Original, and Accurate.</dd>
    <dt id="g-cfr202">21 CFR Part 202 &amp; 203</dt>
    <dd><strong>Part 202 (Prescription Drug Advertising)</strong>: Requires "fair balance" of benefits and risks; all claims must be supported by substantial evidence (typically ≥2 controlled studies); brief summary of risks required in print ads. <strong>Part 203 (PDMA)</strong>: Governs sampling — signed HCP requests, receipt signatures, 3-year retention, lot tracking, no selling of samples.</dd>
    <dt id="g-gxp">GxP — Good Practice Guidelines</dt>
    <dd>Umbrella for FDA/ICH quality frameworks: <strong>GMP</strong> (manufacturing, 21 CFR 210/211), <strong>GCP</strong> (clinical trials, ICH E6), <strong>GLP</strong> (laboratory studies, 21 CFR 58), <strong>GDP</strong> (distribution/cold chain), <strong>GVP</strong> (pharmacovigilance), <strong>GAMP 5</strong> (computerized systems — Veeva = Category 4). All ensure quality, data integrity, and patient safety throughout the drug lifecycle.</dd>
    <dt id="g-heor">HEOR — Health Economics &amp; Outcomes Research</dt>
    <dd>Research generating evidence of a medicine's economic and real-world value. Key outputs: Cost-effectiveness analysis (cost per QALY), Budget Impact Model, AMCP Dossier, PROs (patient-reported outcomes). <strong>RWE/RWD</strong>: Real-World Evidence from claims data, EHR, registries — increasingly used post-approval for payer negotiations and label expansions.</dd>
    <dt id="g-hcp">HCP / HCO</dt>
    <dd><strong>HCP (Healthcare Professional)</strong>: Any licensed prescriber or recommender — physicians, NPs, PAs, pharmacists. Primary targets of commercial and medical engagement. <strong>HCO (Healthcare Organization)</strong>: Hospitals, clinics, group practices, IDNs. Managed through Key Account Management (KAM) teams.</dd>
    <dt id="g-ich">ICH Guidelines</dt>
    <dd>International Council for Harmonisation guidelines adopted by FDA, EMA, PMDA: <strong>E6(R2/R3)</strong> GCP; <strong>E9(R1)</strong> statistical principles/estimands; <strong>E2A–E2F</strong> pharmacovigilance; <strong>Q10</strong> pharmaceutical quality system; <strong>Q9</strong> quality risk management (FMEA); <strong>E8(R1)</strong> general clinical study considerations.</dd>
    <dt id="g-ind">IND / NDA / BLA / ANDA</dt>
    <dd><strong>IND</strong>: Allows human clinical trials to begin (30-day FDA review). <strong>NDA</strong> (21 CFR 314): Approval for new chemical entity. <strong>BLA</strong> (21 CFR 601): Approval for biologics. <strong>ANDA</strong>: Generic drugs — bioequivalence required, no new clinical trials. <strong>sNDA/sBLA</strong>: Supplemental filings for new indications or formulations. Standard review = 12 months; Priority Review = 6 months.</dd>
    <dt id="g-kol">KOL — Key Opinion Leader</dt>
    <dd>Influential HCP — typically academic physician, clinical trial PI, guideline author, or society president. <strong>Tier structure</strong>: National (Tier 1, MSL-managed) → Regional (Tier 2) → Local (Tier 3, sales-managed). KOL engagement includes advisory boards, speaker bureaus, IIRs, publication authorship. All interactions governed by FMV and AKS guardrails.</dd>
    <dt id="g-lbl">Label / Prescribing Information</dt>
    <dd>The FDA-approved document specifying a drug's approved indications, dosing, contraindications, warnings, and side effects. Every communication about the drug must stay within label boundaries. Off-label promotion is illegal and can trigger FCA, AKS, and criminal charges.</dd>
    <dt id="g-mdm">MDM — Master Data Management</dt>
    <dd>Processes maintaining a single clean HCP/HCO record across all systems. In pharma, powered by Veeva Network or IQVIA OneKey. Ensures CRM targeting, sample records, and Sunshine Act reporting all use the same, validated data for each prescriber.</dd>
    <dt id="g-mlr">MLR Review</dt>
    <dd>Medical-Legal-Regulatory review — three-committee approval required for all promotional and non-promotional materials before external use. Medical (accuracy, fair balance), Legal (IP, litigation, off-label risk), Regulatory (FDA Part 202 compliance, label alignment). Platform: Veeva Vault PromoMats.</dd>
    <dt id="g-msl">MSL — Medical Science Liaison</dt>
    <dd>Field-based medical affairs professionals (PhD/PharmD/MD) engaging KOLs with peer-level scientific exchange. Core activities: scientific exchange (on-label; off-label only if unsolicited), IIT support, insight capture, congress engagement. Must be organizationally independent from Sales — cannot be directed by commercial teams or compensated on sales metrics.</dd>
    <dt id="g-nda">NDA / PDUFA / Expedited Programs</dt>
    <dd><strong>PDUFA clock</strong> starts at 60-day filing acceptance: standard 12 months, Priority Review 6 months. <strong>Expedited programs</strong>: Fast Track (unmet need, rolling review), Breakthrough Therapy (intensive FDA guidance), Accelerated Approval (surrogate endpoint), Priority Review, Orphan Drug (7-year exclusivity + tax credits).</dd>
    <dt id="g-ols">Open Payments / Sunshine Act</dt>
    <dd>Physician Payments Sunshine Act (42 USC §1320a-7h). All transfers of value ≥$10 to physicians and teaching hospitals must be reported to CMS annually (filing deadline: March 31; published: June 30). Extended (2022) to include PAs, NPs, CNSs, CRNAs, CNMs. Publicly searchable at openpaymentsdata.cms.gov.</dd>
    <dt id="g-phrma">PhRMA Code</dt>
    <dd>Voluntary self-regulatory guidelines (revised 2019). No entertainment or recreational gifts; meals only at genuine educational meetings; no direct CME funding to HCPs; speaker programs must feature genuine scientific exchange; FMV for all engagements. Non-compliance risks OIG scrutiny.</dd>
    <dt id="g-rems">REMS — Risk Evaluation &amp; Mitigation Strategy</dt>
    <dd>FDA-mandated safety program (FDAAA 2007) for drugs with serious risks. Elements may include: Medication Guide, communication plan, ETASU (prescriber certification, pharmacy certification, patient enrollment/monitoring, required lab tests before dispensing). Medical Affairs manages REMS HCP communications.</dd>
    <dt id="g-rwe">RWE / RWD</dt>
    <dd><strong>Real-World Evidence/Data</strong>: Clinical evidence from claims data, EHRs, or patient registries — not randomized controlled trials. Shows how drugs perform in actual practice. Increasingly used by payers to support formulary decisions, by FDA for label expansions, and by Medical Affairs as an evidence generation strategy.</dd>
    <dt id="g-sfe">SFE — Sales Force Effectiveness</dt>
    <dd>Optimizing field force performance: <strong>Targeting</strong> (NRx decile, prescriber potential), <strong>Reach &amp; Frequency</strong> (% HCPs reached × calls/quarter), <strong>IC Design</strong> (quota-based incentive plans), <strong>Territory Alignment</strong>, <strong>Call Planning</strong>, <strong>SFA Compliance</strong> (CRM usage). Analytics from Veeva CRM + IQVIA Rx data.</dd>
    <dt id="g-srl">SRL — Standard Response Letter</dt>
    <dd>Pre-approved, MLR-reviewed document answering a frequently asked medical question. Medical Information retrieves from Vault Medical and sends with a cover note. Off-label SRLs only provided in response to unsolicited requests — never proactively distributed. All inquiries logged for AE check.</dd>
    <dt id="g-sunshine">Transfer of Value (TOV)</dt>
    <dd>Any monetary or non-monetary benefit from a pharma company to an HCP — meals, honoraria, travel, consulting fees, research grants, royalties. All TOVs tracked in Veeva Events Management and reported annually under the Sunshine Act. FMV enforcement and AKS compliance built into the system workflow.</dd>
    <dt id="g-veeva">Veeva Systems</dt>
    <dd>Cloud-based software platform purpose-built for life sciences: <strong>CRM</strong> (sales force automation, CLM, sampling, Approved Email), <strong>Vault PromoMats</strong> (MLR review), <strong>Vault Medical</strong> (med info/MSL content), <strong>Network</strong> (HCP/HCO MDM), <strong>Events Management</strong> (TOV/Sunshine Act). All 21 CFR Part 11 validated.</dd>
    {FDA_REGS_EXTRA}
  </dl>
  {nav_glossary}
</div>

<!-- ══════════════ FOOTER ══════════════ -->
<footer class="book-footer">
  <div class="book-footer-inner">
    <div class="book-footer-title">Pharma Commercial &amp; Medical Affairs — The Complete Visual Guide</div>
    <div class="book-footer-author">Deepak Kumar — Pharma &amp; MedTech Consultant</div>
    <div class="book-footer-rule"></div>
    <div>11 Chapters · SVG Process Diagrams · Interactive Glossary · Veeva Systems Reference</div>
    <div>FDA Regulatory Frameworks · GxP · CAPA · ICH Guidelines · PhRMA Code · Anti-Kickback · Sunshine Act</div>
    <div style="margin-top:12px;opacity:.4;">May 2026 · All regulatory references reflect US FDA frameworks as of May 2026</div>
  </div>
</footer>

{MODAL_HTML}
</main>
</div><!-- end .wrapper -->

<script>
{TOOLTIP_JS}

// ── Reading progress bar ──────────────────────────────────────────────────
const pb = document.getElementById('progress-bar');
window.addEventListener('scroll', function () {{
  const s = document.documentElement;
  const pct = s.scrollTop / (s.scrollHeight - s.clientHeight) * 100;
  pb.style.width = pct + '%';
  document.getElementById('btt').classList.toggle('visible', s.scrollTop > 500);
}}, {{ passive: true }});

// ── Scroll-spy TOC ────────────────────────────────────────────────────────
(function () {{
  const links = document.querySelectorAll('.toc a[href^="#"]');
  const secs  = Array.from(links).map(l => document.getElementById(l.getAttribute('href').slice(1)));
  function update() {{
    const y = window.scrollY + 160;
    let active = 0;
    secs.forEach((s, i) => {{ if (s && s.offsetTop <= y) active = i; }});
    links.forEach((l, i) => l.classList.toggle('active', i === active));
  }}
  window.addEventListener('scroll', update, {{ passive: true }});
  update();
}})();


// ── Google Search Modal ──────────────────────────────────────────────────
var _searchUrls = {{
  google:  function(q) {{ return 'https://www.google.com/search?q=' + encodeURIComponent(q); }},
  bing:    function(q) {{ return 'https://www.bing.com/search?q=' + encodeURIComponent(q); }},
  scholar: function(q) {{ return 'https://scholar.google.com/scholar?q=' + encodeURIComponent(q); }},
  pubmed:  function(q) {{ return 'https://pubmed.ncbi.nlm.nih.gov/?term=' + encodeURIComponent(q); }},
  fda:     function(q) {{ return 'https://www.fda.gov/search?s=' + encodeURIComponent(q); }}
}};

function openGSearch(q) {{
  q = (q || '').trim();
  if (!q) return;
  var modal = document.getElementById('gsearchModal');
  var input = document.getElementById('gsearchModalInput');
  input.value = q;
  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
  setTimeout(function() {{ input.select(); }}, 80);
}}

function launchSearch(engine, q) {{
  q = (q || document.getElementById('gsearchModalInput').value || '').trim();
  if (!q) return;
  var url = (_searchUrls[engine] || _searchUrls.google)(q);
  var popup = window.open(url, 'pharmaSearch',
    'width=1100,height=760,left=120,top=60,resizable=yes,scrollbars=yes,toolbar=yes,location=yes');
  if (!popup) {{
    // Popup blocked — open in new tab as fallback
    window.open(url, '_blank');
  }}
}}

function closeGSearch() {{
  document.getElementById('gsearchModal').classList.remove('open');
  document.body.style.overflow = '';
}}

document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape' && document.getElementById('gsearchModal').classList.contains('open')) {{
    closeGSearch();
  }}
}});
// ── Theme switcher ────────────────────────────────────────────────────────
function setTheme(t) {{
  document.documentElement.setAttribute('data-theme', t);
  try {{ localStorage.setItem('pharma-theme', t); }} catch(e) {{}}
}}
(function () {{
  try {{
    const saved = localStorage.getItem('pharma-theme');
    if (saved) document.documentElement.setAttribute('data-theme', saved);
  }} catch(e) {{}}
}})();

// ── Font size controls ────────────────────────────────────────────────────
let fontSize = 17;
function adjustFont(delta) {{
  fontSize = Math.min(24, Math.max(13, fontSize + delta));
  document.documentElement.style.setProperty('--base-size', fontSize + 'px');
  try {{ localStorage.setItem('pharma-fontsize', fontSize); }} catch(e) {{}}
}}
(function () {{
  try {{
    const saved = parseInt(localStorage.getItem('pharma-fontsize'));
    if (saved) {{ fontSize = saved; document.documentElement.style.setProperty('--base-size', saved + 'px'); }}
  }} catch(e) {{}}
}})();

// ── Content search ────────────────────────────────────────────────────────
let lastQuery = '';
function searchContent(q) {{
  q = q.trim();
  if (q === lastQuery) return;
  lastQuery = q;
  const content = document.getElementById('mainContent');
  content.querySelectorAll('mark').forEach(m => {{
    const p = m.parentNode;
    p.replaceChild(document.createTextNode(m.textContent), m);
    p.normalize();
  }});
  if (!q) return;
  const re = new RegExp(q.replace(/[.*+?^${{}}()|[\\]\\\\]/g, '\\\\$&'), 'gi');
  function walkText(node) {{
    if (node.nodeType === 3) {{
      if (re.test(node.nodeValue)) {{
        re.lastIndex = 0;
        const frag = document.createDocumentFragment();
        let last = 0, text = node.nodeValue;
        text.replace(re, function (match, offset) {{
          frag.appendChild(document.createTextNode(text.slice(last, offset)));
          const mark = document.createElement('mark');
          mark.textContent = match;
          frag.appendChild(mark);
          last = offset + match.length;
        }});
        frag.appendChild(document.createTextNode(text.slice(last)));
        node.parentNode.replaceChild(frag, node);
      }}
    }} else if (node.nodeType === 1 && !['SCRIPT','STYLE','INPUT','MARK','FIGURE'].includes(node.tagName)) {{
      Array.from(node.childNodes).forEach(walkText);
    }}
  }}
  walkText(content);
  const first = content.querySelector('mark');
  if (first) first.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
}}

// ── Glossary filter ─────────────────────────────────────────────────────────────────────────
function filterGloss(q) {{
  q = q.toLowerCase();
  const dl    = document.getElementById('glossDL');
  const items = dl.querySelectorAll('dt, dd');
  let show = true;
  items.forEach(el => {{
    if (el.tagName === 'DT') {{
      show = !q || el.textContent.toLowerCase().includes(q) ||
             (el.nextElementSibling && el.nextElementSibling.textContent.toLowerCase().includes(q));
    }}
    el.style.display = show ? '' : 'none';
  }});
}}
{MODAL_JS}
</script>
</body>
</html>'''

# ── Write output ─────────────────────────────────────────────────────────────────────────
open(OUT, 'w', encoding='utf-8').write(HTML)
print(f'Written: {OUT}')
print(f'Size   : {len(HTML):,} chars / {HTML.count(chr(10))+1:,} lines')
