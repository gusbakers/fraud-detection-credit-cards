<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Credit Card Fraud Detection System</title>
<link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0e1a;
    --bg2: #0f1629;
    --bg3: #141d35;
    --accent: #00d4ff;
    --accent2: #7c3aed;
    --accent3: #10b981;
    --warn: #f59e0b;
    --text: #e2e8f0;
    --muted: #64748b;
    --border: rgba(255,255,255,0.07);
    --card: rgba(255,255,255,0.04);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'DM Sans', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* HERO */
  .hero {
    position: relative;
    padding: 72px 48px 56px;
    border-bottom: 1px solid var(--border);
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: 
      radial-gradient(ellipse 60% 50% at 80% 20%, rgba(0,212,255,0.08) 0%, transparent 60%),
      radial-gradient(ellipse 40% 60% at 10% 80%, rgba(124,58,237,0.07) 0%, transparent 60%);
    pointer-events: none;
  }

  .hero-tag {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.25);
    color: var(--accent);
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 0.12em;
    padding: 6px 14px;
    border-radius: 4px;
    margin-bottom: 24px;
  }

  .hero-tag::before { content: '▶'; font-size: 9px; }

  h1 {
    font-size: clamp(28px, 5vw, 48px);
    font-weight: 700;
    line-height: 1.15;
    letter-spacing: -0.02em;
    margin-bottom: 16px;
  }

  h1 span {
    background: linear-gradient(135deg, var(--accent) 0%, var(--accent2) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .hero-sub {
    color: var(--muted);
    font-size: 16px;
    font-weight: 400;
    max-width: 600px;
    line-height: 1.6;
    margin-bottom: 32px;
  }

  /* BADGES */
  .badges {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 0;
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
    font-family: 'Space Mono', monospace;
    letter-spacing: 0.02em;
    border: 1px solid transparent;
  }

  .badge img { width: 14px; height: 14px; object-fit: contain; }
  .badge-python   { background: rgba(55,118,171,0.15); border-color: rgba(55,118,171,0.4); color: #60a5fa; }
  .badge-snowflake{ background: rgba(41,181,232,0.12); border-color: rgba(41,181,232,0.35); color: #29b5e8; }
  .badge-databricks{ background: rgba(255,61,0,0.1); border-color: rgba(255,61,0,0.3); color: #ff6b35; }
  .badge-mlflow   { background: rgba(1,148,226,0.12); border-color: rgba(1,148,226,0.35); color: #0194e2; }
  .badge-streamlit{ background: rgba(255,75,75,0.12); border-color: rgba(255,75,75,0.3); color: #ff4b4b; }
  .badge-mit      { background: rgba(16,185,129,0.1); border-color: rgba(16,185,129,0.3); color: #10b981; }

  /* MAIN CONTENT */
  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 48px 80px;
  }

  .section {
    margin-top: 56px;
  }

  .section-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 0.2em;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: var(--border);
    max-width: 120px;
  }

  h2 {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
    letter-spacing: -0.01em;
  }

  /* METRICS */
  .metrics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
  }

  .metric-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 16px;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s;
  }

  .metric-card:hover {
    transform: translateY(-2px);
    border-color: rgba(0,212,255,0.2);
  }

  .metric-card.warn {
    border-color: rgba(245,158,11,0.3);
    background: rgba(245,158,11,0.05);
  }

  .metric-value {
    font-family: 'Space Mono', monospace;
    font-size: 24px;
    font-weight: 700;
    color: var(--accent3);
    margin-bottom: 6px;
  }

  .metric-card.warn .metric-value { color: var(--warn); }

  .metric-label {
    font-size: 11px;
    color: var(--muted);
    font-weight: 500;
    letter-spacing: 0.05em;
  }

  .warn-badge {
    position: absolute;
    top: 8px;
    right: 8px;
    font-size: 14px;
  }

  .warn-note {
    background: rgba(245,158,11,0.08);
    border: 1px solid rgba(245,158,11,0.25);
    border-left: 3px solid var(--warn);
    border-radius: 8px;
    padding: 16px 18px;
    font-size: 13px;
    line-height: 1.6;
    color: #fcd34d;
  }

  .warn-note strong { color: var(--warn); }

  /* TECH STACK */
  .stack-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
  }

  .stack-item {
    display: flex;
    align-items: center;
    gap: 14px;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    transition: border-color 0.2s, transform 0.2s;
  }

  .stack-item:hover {
    border-color: rgba(0,212,255,0.2);
    transform: translateX(3px);
  }

  .stack-icon {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    flex-shrink: 0;
  }

  .stack-info { min-width: 0; }
  .stack-name { font-size: 13px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .stack-role { font-size: 11px; color: var(--muted); margin-top: 2px; }

  /* ARCHITECTURE */
  .arch-flow {
    display: flex;
    flex-direction: column;
    gap: 0;
    position: relative;
  }

  .arch-step {
    display: flex;
    align-items: stretch;
    gap: 0;
  }

  .arch-line {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 40px;
    flex-shrink: 0;
  }

  .arch-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--accent);
    border: 2px solid var(--bg);
    box-shadow: 0 0 10px rgba(0,212,255,0.5);
    flex-shrink: 0;
    margin-top: 18px;
  }

  .arch-connector {
    width: 2px;
    flex: 1;
    background: linear-gradient(to bottom, var(--accent), var(--accent2));
    opacity: 0.3;
    min-height: 20px;
  }

  .arch-content {
    flex: 1;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 8px;
    margin-left: 8px;
  }

  .arch-title {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    font-weight: 700;
    color: var(--accent);
    margin-bottom: 4px;
  }

  .arch-desc {
    font-size: 12px;
    color: var(--muted);
    line-height: 1.5;
  }

  /* DATASET */
  .dataset-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 20px;
  }

  .stat-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .stat-label { font-size: 12px; color: var(--muted); font-weight: 500; }
  .stat-value {
    font-family: 'Space Mono', monospace;
    font-size: 18px;
    font-weight: 700;
    color: var(--accent);
  }

  /* DECISIONS */
  .decisions-list { display: flex; flex-direction: column; gap: 10px; }

  .decision-item {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 14px;
    align-items: start;
    transition: border-color 0.2s;
  }

  .decision-item:hover { border-color: rgba(124,58,237,0.3); }

  .decision-icon {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: rgba(124,58,237,0.15);
    border: 1px solid rgba(124,58,237,0.3);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    flex-shrink: 0;
  }

  .decision-q {
    font-size: 13px;
    font-weight: 600;
    color: var(--text);
    margin-bottom: 5px;
  }

  .decision-a { font-size: 12px; color: var(--muted); line-height: 1.5; }

  /* AUTHOR */
  .author-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px 32px;
    display: flex;
    align-items: center;
    gap: 24px;
    position: relative;
    overflow: hidden;
  }

  .author-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse 60% 80% at 90% 50%, rgba(0,212,255,0.05) 0%, transparent 60%);
    pointer-events: none;
  }

  .author-avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    flex-shrink: 0;
  }

  .author-name { font-size: 20px; font-weight: 700; margin-bottom: 4px; }
  .author-handle { font-family: 'Space Mono', monospace; font-size: 12px; color: var(--accent); margin-bottom: 10px; }
  .author-tags { display: flex; flex-wrap: wrap; gap: 6px; }

  .author-tag {
    background: rgba(255,255,255,0.06);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 3px 10px;
    font-size: 11px;
    color: var(--muted);
    font-weight: 500;
  }

  .live-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, var(--accent), #0099cc);
    color: #000;
    font-weight: 700;
    font-size: 13px;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    letter-spacing: 0.03em;
    transition: opacity 0.2s, transform 0.2s;
  }

  .live-btn:hover { opacity: 0.9; transform: translateY(-1px); }
  .live-pulse {
    width: 8px; height: 8px; border-radius: 50%;
    background: #000;
    box-shadow: 0 0 0 0 rgba(0,0,0,0.4);
    animation: pulse 1.5s infinite;
  }

  @keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0,0,0,0.5); }
    70% { box-shadow: 0 0 0 6px rgba(0,0,0,0); }
    100% { box-shadow: 0 0 0 0 rgba(0,0,0,0); }
  }

  /* STRUCTURE */
  .file-tree {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 24px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    line-height: 2;
    color: var(--muted);
  }

  .file-tree .folder { color: var(--accent); font-weight: 700; }
  .file-tree .comment { color: #334155; }

  /* SETUP */
  .code-block {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px 20px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: var(--accent3);
    margin: 8px 0 16px;
    line-height: 1.7;
  }

  .step-num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 24px; height: 24px;
    border-radius: 50%;
    background: rgba(0,212,255,0.1);
    border: 1px solid rgba(0,212,255,0.3);
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--accent);
    font-weight: 700;
    margin-right: 10px;
    flex-shrink: 0;
  }

  .step-title {
    font-size: 14px;
    font-weight: 600;
    display: flex;
    align-items: center;
    margin-bottom: 4px;
  }

  p { font-size: 14px; color: var(--muted); line-height: 1.7; }

  hr { display: none; }

  @media (max-width: 600px) {
    .hero, .container { padding-left: 20px; padding-right: 20px; }
    .dataset-grid { grid-template-columns: 1fr; }
    .author-card { flex-direction: column; text-align: center; }
    .author-tags { justify-content: center; }
  }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-tag">PORTFOLIO PROJECT · ML ENGINEERING</div>
  <h1>🔍 Credit Card<br><span>Fraud Detection</span> System</h1>
  <p class="hero-sub">End-to-end machine learning pipeline for detecting fraudulent credit card transactions — built with industry-standard tools across the full data lifecycle.</p>
  <div class="badges">
    <span class="badge badge-python">🐍 Python 3.10</span>
    <span class="badge badge-snowflake">❄️ Snowflake</span>
    <span class="badge badge-databricks">🔶 Databricks</span>
    <span class="badge badge-mlflow">📊 MLflow</span>
    <span class="badge badge-streamlit">🎈 Streamlit</span>
    <span class="badge badge-mit">✅ MIT License</span>
  </div>
</div>

<div class="container">

  <!-- WHY -->
  <div class="section">
    <div class="section-label">01 · MOTIVATION</div>
    <h2>Why I Built This</h2>
    <p>Fraud costs financial institutions billions every year. I wanted to build something that goes beyond a basic notebook — a real pipeline that handles data ingestion, transformation, model training, interpretability and monitoring, the same way it would be done in a production environment.</p>
    <br>
    <p>This project covers the full stack: SQL data warehousing in Snowflake, ML experimentation in Databricks, experiment tracking with MLflow, and a live dashboard anyone can open right now.</p>
  </div>

  <!-- RESULTS -->
  <div class="section">
    <div class="section-label">02 · RESULTS</div>
    <h2>Model Performance</h2>
    <div class="metrics-grid">
      <div class="metric-card warn">
        <div class="warn-badge">⚠️</div>
        <div class="metric-value">1.0000</div>
        <div class="metric-label">AUC-ROC</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">0.9988</div>
        <div class="metric-label">F1 Score</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">0.9990</div>
        <div class="metric-label">Precision</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">0.9987</div>
        <div class="metric-label">Recall</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">0.9997</div>
        <div class="metric-label">Accuracy</div>
      </div>
    </div>
    <div class="warn-note">
      <strong>⚠️ Note on AUC-ROC score:</strong> A perfect 1.0 score on the test set was flagged for investigation. SHAP analysis identified that feature importance was heavily concentrated in a small subset of features, suggesting potential data leakage from the synthetic data generation process. This is documented as a known limitation and a learning outcome — recognizing and communicating model anomalies is part of responsible ML practice. A revised version with strict temporal feature splits is planned for v2.
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section">
    <div class="section-label">03 · TECH STACK</div>
    <h2>Tools & Technologies</h2>
    <div class="stack-grid">
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(41,181,232,0.12);">❄️</div>
        <div class="stack-info">
          <div class="stack-name">Snowflake</div>
          <div class="stack-role">Data Warehouse · Medallion Architecture</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(255,100,50,0.12);">🔶</div>
        <div class="stack-info">
          <div class="stack-name">Databricks</div>
          <div class="stack-role">ML Platform · Community Edition</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(1,148,226,0.12);">📊</div>
        <div class="stack-info">
          <div class="stack-name">MLflow</div>
          <div class="stack-role">Experiment Tracking · Model Registry</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(255,75,75,0.12);">🎈</div>
        <div class="stack-info">
          <div class="stack-name">Streamlit</div>
          <div class="stack-role">Live Dashboard · Public Deploy</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(55,118,171,0.12);">🐍</div>
        <div class="stack-info">
          <div class="stack-name">Python 3.10</div>
          <div class="stack-role">XGBoost · LightGBM · scikit-learn</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(255,150,0,0.12);">🔍</div>
        <div class="stack-info">
          <div class="stack-name">SHAP</div>
          <div class="stack-role">Model Interpretability · Explainability</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(30,200,80,0.12);">⚙️</div>
        <div class="stack-info">
          <div class="stack-name">GitHub Actions</div>
          <div class="stack-role">CI/CD · Automated Testing</div>
        </div>
      </div>
      <div class="stack-item">
        <div class="stack-icon" style="background:rgba(100,100,255,0.12);">🐳</div>
        <div class="stack-info">
          <div class="stack-name">Docker</div>
          <div class="stack-role">Containerization · Reproducibility</div>
        </div>
      </div>
    </div>
  </div>

  <!-- ARCHITECTURE -->
  <div class="section">
    <div class="section-label">04 · ARCHITECTURE</div>
    <h2>Pipeline Overview</h2>
    <div class="arch-flow">
      <div class="arch-step">
        <div class="arch-line"><div class="arch-dot"></div><div class="arch-connector"></div></div>
        <div class="arch-content">
          <div class="arch-title">SYNTHETIC DATASET</div>
          <div class="arch-desc">100,000 transactions · 14 interpretable business features · 15% fraud rate</div>
        </div>
      </div>
      <div class="arch-step">
        <div class="arch-line"><div class="arch-dot" style="background:var(--accent2); box-shadow:0 0 10px rgba(124,58,237,0.5)"></div><div class="arch-connector"></div></div>
        <div class="arch-content">
          <div class="arch-title" style="color:var(--accent2)">SNOWFLAKE DATA WAREHOUSE</div>
          <div class="arch-desc">RAW → STAGING → ANALYTICS → ML_RESULTS · Medallion Architecture</div>
        </div>
      </div>
      <div class="arch-step">
        <div class="arch-line"><div class="arch-dot" style="background:#ff6b35; box-shadow:0 0 10px rgba(255,107,53,0.5)"></div><div class="arch-connector"></div></div>
        <div class="arch-content">
          <div class="arch-title" style="color:#ff6b35">DATABRICKS COMMUNITY EDITION</div>
          <div class="arch-desc">EDA (8 visualizations) · Feature Engineering (SMOTE-Tomek + RobustScaler) · 4 models trained</div>
        </div>
      </div>
      <div class="arch-step">
        <div class="arch-line"><div class="arch-dot" style="background:#0194e2; box-shadow:0 0 10px rgba(1,148,226,0.5)"></div><div class="arch-connector"></div></div>
        <div class="arch-content">
          <div class="arch-title" style="color:#0194e2">MLFLOW EXPERIMENT TRACKING</div>
          <div class="arch-desc">Parameters · Metrics · Models registered in Model Registry</div>
        </div>
      </div>
      <div class="arch-step">
        <div class="arch-line"><div class="arch-dot" style="background:var(--accent3); box-shadow:0 0 10px rgba(16,185,129,0.5)"></div><div class="arch-connector" style="opacity:0"></div></div>
        <div class="arch-content">
          <div class="arch-title" style="color:var(--accent3)">STREAMLIT LIVE DASHBOARD</div>
          <div class="arch-desc">Public deploy · SHAP interpretability · Confusion matrix · Metrics overview</div>
        </div>
      </div>
    </div>
  </div>

  <!-- DATASET -->
  <div class="section">
    <div class="section-label">05 · DATASET</div>
    <h2>Data Overview</h2>
    <div class="dataset-grid">
      <div class="stat-card"><span class="stat-label">Total Transactions</span><span class="stat-value">100K</span></div>
      <div class="stat-card"><span class="stat-label">Fraud Cases</span><span class="stat-value" style="color:var(--warn)">15K</span></div>
      <div class="stat-card"><span class="stat-label">Legitimate Cases</span><span class="stat-value" style="color:var(--accent3)">85K</span></div>
      <div class="stat-card"><span class="stat-label">Features</span><span class="stat-value">14</span></div>
    </div>
    <p>Built a synthetic dataset with realistic fraud patterns instead of an anonymized public dataset. Features include transaction amount, hour of day, merchant category, distance from home, failed attempts, account age, and online vs. in-person — all variables that map directly to real fraud detection logic.</p>
  </div>

  <!-- KEY DECISIONS -->
  <div class="section">
    <div class="section-label">06 · DESIGN DECISIONS</div>
    <h2>Key Technical Choices</h2>
    <div class="decisions-list">
      <div class="decision-item">
        <div class="decision-icon">📏</div>
        <div>
          <div class="decision-q">Why RobustScaler instead of StandardScaler?</div>
          <div class="decision-a">Fraudulent transactions are outliers by definition. RobustScaler uses median and IQR instead of mean and standard deviation, making it significantly more resistant to extreme values.</div>
        </div>
      </div>
      <div class="decision-item">
        <div class="decision-icon">⚖️</div>
        <div>
          <div class="decision-q">Why SMOTE-Tomek instead of simple oversampling?</div>
          <div class="decision-a">SMOTE generates synthetic minority class samples while Tomek Links removes ambiguous boundary samples from the majority class. The combination produces a cleaner decision boundary and better generalization.</div>
        </div>
      </div>
      <div class="decision-item">
        <div class="decision-icon">🎯</div>
        <div>
          <div class="decision-q">Why Average Precision as primary metric?</div>
          <div class="decision-a">With imbalanced datasets, accuracy is misleading. A model predicting everything as legitimate would score 85% accuracy. Average Precision measures what actually matters: performance on the minority fraud class.</div>
        </div>
      </div>
      <div class="decision-item">
        <div class="decision-icon">🔍</div>
        <div>
          <div class="decision-q">Why SHAP for interpretability?</div>
          <div class="decision-a">Financial institutions are increasingly required to explain AI-driven decisions. SHAP provides instance-level explanations showing exactly which features pushed a prediction toward fraud or legitimate — making the model auditable.</div>
        </div>
      </div>
      <div class="decision-item">
        <div class="decision-icon">🏛️</div>
        <div>
          <div class="decision-q">Why a Medallion Architecture in Snowflake?</div>
          <div class="decision-a">Separating RAW, STAGING, ANALYTICS and ML_RESULTS layers mirrors how data teams structure production pipelines. It makes transformations reproducible, auditable and easy to extend.</div>
        </div>
      </div>
    </div>
  </div>

  <!-- PROJECT STRUCTURE -->
  <div class="section">
    <div class="section-label">07 · STRUCTURE</div>
    <h2>Project Structure</h2>
    <div class="file-tree">
      <span class="folder">fraud-detection-credit-cards/</span><br>
      ├── <span class="folder">notebooks/</span><br>
      │   ├── <span class="folder">01_eda/</span>                 <span class="comment">← data loading + 8 EDA visualizations</span><br>
      │   ├── <span class="folder">02_feature_engineering/</span> <span class="comment">← SMOTE-Tomek, RobustScaler, MI selection</span><br>
      │   ├── <span class="folder">03_modeling/</span>            <span class="comment">← 4 models + MLflow tracking</span><br>
      │   └── <span class="folder">04_evaluation/</span>          <span class="comment">← SHAP interpretability</span><br>
      ├── <span class="folder">src/</span><br>
      │   └── <span class="folder">sql/</span>                    <span class="comment">← Snowflake DDL scripts (run in order)</span><br>
      ├── <span class="folder">dashboards/</span><br>
      │   └── app.py                  <span class="comment">← Streamlit dashboard</span><br>
      ├── <span class="folder">tests/</span>                      <span class="comment">← unit tests</span><br>
      ├── <span class="folder">.github/workflows/</span>          <span class="comment">← CI/CD pipeline</span><br>
      ├── requirements.txt<br>
      └── .env.example
    </div>
  </div>

  <!-- LIVE DASHBOARD -->
  <div class="section">
    <div class="section-label">08 · LIVE DEMO</div>
    <h2>Dashboard</h2>
    <p style="margin-bottom:16px;">The full pipeline is deployed and accessible — no setup required.</p>
    <a href="https://3bp7tg2fe3kqp.streamlit.app" class="live-btn" target="_blank">
      <div class="live-pulse"></div>
      Open Live Dashboard →
    </a>
  </div>

  <!-- SETUP -->
  <div class="section">
    <div class="section-label">09 · SETUP</div>
    <h2>Run Locally</h2>

    <div class="step-title"><span class="step-num">1</span> Clone the repository</div>
    <div class="code-block">git clone https://github.com/gusbakers/fraud-detection-credit-cards.git<br>cd fraud-detection-credit-cards</div>

    <div class="step-title"><span class="step-num">2</span> Install dependencies</div>
    <div class="code-block">pip install -r requirements.txt</div>

    <div class="step-title"><span class="step-num">3</span> Configure credentials</div>
    <div class="code-block">cp .env.example .env<br><span style="color:var(--muted)"># Fill in your Snowflake credentials</span></div>

    <div class="step-title"><span class="step-num">4</span> Run notebooks in order</div>
    <div class="code-block">notebooks/01_eda/<br>notebooks/02_feature_engineering/<br>notebooks/03_modeling/<br>notebooks/04_evaluation/</div>
  </div>

  <!-- AUTHOR -->
  <div class="section">
    <div class="section-label">10 · AUTHOR</div>
    <div class="author-card">
      <div class="author-avatar">👤</div>
      <div>
        <div class="author-name">Gustavo Feliz</div>
        <div class="author-handle">@gusbakers · github.com/gusbakers</div>
        <div class="author-tags">
          <span class="author-tag">Master's in Machine Learning · Cornell Tech</span>
          <span class="author-tag">Data Engineer</span>
          <span class="author-tag">ML Engineer</span>
          <span class="author-tag">AI Engineer</span>
        </div>
      </div>
    </div>
    <br>
    <p style="font-size:13px; font-style:italic;">Built end-to-end as a portfolio project demonstrating the full data and ML lifecycle — from raw data ingestion to a live deployed dashboard.</p>
  </div>

</div>
</body>
</html>
