---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<span class='anchor' id='about-me'></span>

<div class='side-mascot-rail side-mascot-rail--right' id='side-mascot-layer-right' aria-hidden='true'></div>

<div class='featured-grid'>
  <div class='featured-card'>
    <div class='featured-card-image'>
      <img src='images/works/phd-simulator-cover.jpg' alt='PhD Simulator cover'>
    </div>
    <div class='featured-card-body'>
      <p class='featured-card-title'>&#127918; &#30740;&#31350;&#29983;&#27169;&#25311;&#22120;&#23567;&#28216;&#25103;</p>
      <div class='featured-actions'>
        <a class='featured-button featured-button--primary' href='https://kw66.github.io/PhD_Simulator/' target='_blank' rel='noopener noreferrer'>&#9654;&#65039; Play v1.0</a>
        <a class='featured-button' href='https://github.com/kw66/PhD_Simulator' target='_blank' rel='noopener noreferrer'>&#128230; Project</a>
        <a class='featured-button' href='https://kw-game-graduate-simulator-v2.vercel.app/' target='_blank' rel='noopener noreferrer'>&#129497; View v2.0</a>
      </div>
    </div>
  </div>

  <div class='featured-card'>
    <div class='featured-card-image'>
      <img src='images/works/atreid-featured.png' alt='Anytime Person Re-Identification overview'>
    </div>
    <div class='featured-card-body'>
      <p class='featured-card-title'>&#128340; &#20840;&#26102;&#27573;&#34892;&#20154;&#37325;&#35782;&#21035;</p>
      <div class='featured-actions'>
        <a class='featured-button featured-button--primary' href='https://arxiv.org/pdf/2509.16635' target='_blank' rel='noopener noreferrer'>&#128196; Paper</a>
        <a class='featured-button' href='https://github.com/kw66/AT-ReID' target='_blank' rel='noopener noreferrer'>&#128450;&#65039; Dataset</a>
        <a class='featured-button' href='https://github.com/kw66/AT-ReID/tree/main/AT-ReID' target='_blank' rel='noopener noreferrer'>&#128187; Code</a>
      </div>
    </div>
  </div>
</div>

<div class='paper-list-item'>
  <p class='work-title'>MFEN: Multi-Frequency Expert Network for Visible-Infrared Person Re-ID</p>
  <p class='work-authors'><strong>Xulin Li</strong>, Yan Lu, Bin Liu, Qinhong Yang, Qi Chu, Tao Gong, Nenghai Yu</p>
  <div class='work-meta-row'>
    <p class='work-meta'>&#127970; Venue: CVPR 2026 &#10024; Highlight</p>
    <span class='paper-link-button paper-link-button--disabled' aria-disabled='true'>&#128196; Paper</span>
  </div>
  <div class='paper-tags'>
    <span class='paper-tag'>Mixture of Experts</span>
    <span class='paper-tag'>Frequency-Domain</span>
  </div>
</div>

<div class='paper-list-item'>
  <p class='work-title'>Towards Anytime Retrieval: A Benchmark for Anytime Person Re-Identification</p>
  <p class='work-authors'><strong>Xulin Li</strong>, Yan Lu, Bin Liu, Jiaze Li, Qinhong Yang, Tao Gong, Qi Chu, Mang Ye, Nenghai Yu</p>
  <div class='work-meta-row'>
    <p class='work-meta'>&#127970; Venue: IJCAI 2025 &#128293; Oral</p>
    <a class='paper-link-button' href='https://arxiv.org/pdf/2509.16635' target='_blank' rel='noopener noreferrer'>&#128196; Paper</a>
  </div>
  <div class='paper-tags'>
    <span class='paper-tag'>Mixture of Experts</span>
    <span class='paper-tag'>Multi-Task Learning</span>
  </div>
</div>

<div class='paper-list-item'>
  <p class='work-title'>Counterfactual Intervention Feature Transfer for Visible-Infrared Person Re-identification</p>
  <p class='work-authors'><strong>Xulin Li</strong>, Yan Lu, Bin Liu, Yating Liu, Guojun Yin, Qi Chu, Jingyang Huang, Feng Zhu, Rui Zhao, Nenghai Yu</p>
  <div class='work-meta-row'>
    <p class='work-meta'>&#127970; Venue: ECCV 2022</p>
    <a class='paper-link-button' href='https://arxiv.org/abs/2208.00967' target='_blank' rel='noopener noreferrer'>&#128196; Paper</a>
  </div>
  <div class='paper-tags'>
    <span class='paper-tag'>Causal Inference</span>
    <span class='paper-tag'>Counterfactual</span>
    <span class='paper-tag'>Heterogeneous Graph</span>
  </div>
</div>

<div class='paper-list-item'>
  <p class='work-title'>Cloth-aware Center Cluster Loss for Cloth-Changing Person Re-identification</p>
  <p class='work-authors'><strong>Xulin Li</strong>, Bin Liu, Yan Lu, Qi Chu, Nenghai Yu</p>
  <div class='work-meta-row'>
    <p class='work-meta'>&#127970; Venue: PRCV 2022</p>
    <a class='paper-link-button' href='https://link.springer.com/chapter/10.1007/978-3-031-18907-4_41' target='_blank' rel='noopener noreferrer'>&#128196; Paper</a>
  </div>
  <div class='paper-tags'>
    <span class='paper-tag'>Metric Learning</span>
  </div>
</div>

<script>
  (function () {
    const mascotBase = "{{ '/images/mascots/' | relative_url }}";
    const mascotSources = Array.from({ length: 45 }, (_, index) => {
      const name = `mascot-${String(index + 1).padStart(2, '0')}.png`;
      return `${mascotBase}${name}`;
    }).filter((src) => !src.endsWith('mascot-43.png'));
    const leftLayerId = 'side-mascot-layer-left';
    const rightLayerId = 'side-mascot-layer-right';
    const config = {
      minWidth: 1280,
      size: 84,
      gap: 42,
      speed: 34,
      leftInset: 2,
      rightInset: 14
    };
    let rafId = null;
    let resizeTimer = null;
    let state = null;

    function randomFrom(items) {
      return items[Math.floor(Math.random() * items.length)];
    }

    function computeOpacity(y, height) {
      const fade = config.size * 0.9;
      const top = y;
      const bottom = y + config.size;
      const enter = Math.max(0, Math.min(1, bottom / fade));
      const exit = Math.max(0, Math.min(1, (height - top) / fade));
      return Math.min(enter, exit);
    }

    function paintMascot(item) {
      item.el.style.transform = `translate3d(0, ${Math.round(item.y)}px, 0)`;
      item.el.style.opacity = `${computeOpacity(item.y, item.laneHeight)}`;
    }

    function respawnMascot(item) {
      item.el.src = randomFrom(mascotSources);
    }

    function buildLane(side, height, layer) {
      const items = [];
      const spacing = config.size + config.gap;
      const positions = [];
      if (side === 'left') {
        for (let y = -(config.size + config.gap); y < height + spacing; y += spacing) {
          positions.push(y);
        }
      } else {
        for (let y = height + config.gap; y > -(spacing + config.size); y -= spacing) {
          positions.push(y);
        }
      }

      positions.forEach((y) => {
        const el = document.createElement('img');
        el.className = `side-mascot side-mascot--${side}`;
        el.alt = '';
        el.decoding = 'async';
        el.loading = 'eager';
        el.src = randomFrom(mascotSources);
        layer.appendChild(el);
        const item = { el, side, y, laneHeight: height };
        items.push(item);
      });

      return items;
    }

    function recycleLane(lane) {
      const { side, items, height } = lane;
      const spacing = state.spacing;
      const beyond = config.gap;
      items.forEach((item) => {
        if (side === 'left' && item.y >= height + beyond) {
          const minY = Math.min(...items.map((entry) => entry.y));
          item.y = minY - spacing;
          respawnMascot(item);
        }
        if (side === 'right' && item.y <= -(config.size + beyond)) {
          const maxY = Math.max(...items.map((entry) => entry.y));
          item.y = maxY + spacing;
          respawnMascot(item);
        }
      });
    }

    function step(now) {
      if (!state) return;
      const dt = Math.min((now - state.lastTime) / 1000, 0.05);
      state.lastTime = now;

      state.left.items.forEach((item) => {
        item.y += state.speed * dt;
      });
      state.right.items.forEach((item) => {
        item.y -= state.speed * dt;
      });

      recycleLane(state.left);
      recycleLane(state.right);
      state.left.items.forEach((item) => paintMascot(item));
      state.right.items.forEach((item) => paintMascot(item));

      rafId = window.requestAnimationFrame(step);
    }

    function renderSideMascots() {
      const leftLayer = document.getElementById(leftLayerId);
      const rightLayer = document.getElementById(rightLayerId);
      if (!leftLayer || !rightLayer) return;

      leftLayer.innerHTML = '';
      rightLayer.innerHTML = '';
      if (rafId) {
        window.cancelAnimationFrame(rafId);
        rafId = null;
      }
      state = null;

      if (window.innerWidth < config.minWidth) return;

      const leftHeight = Math.max(leftLayer.parentElement.offsetHeight, 760);
      const rightHeight = Math.max(rightLayer.parentElement.offsetHeight, 960);

      state = {
        speed: config.speed,
        spacing: config.size + config.gap,
        lastTime: performance.now(),
        left: {
          side: 'left',
          height: leftHeight,
          items: buildLane('left', leftHeight, leftLayer)
        },
        right: {
          side: 'right',
          height: rightHeight,
          items: buildLane('right', rightHeight, rightLayer)
        }
      };

      state.left.items.forEach((item) => {
        item.el.style.width = `${config.size}px`;
        item.el.style.left = `${config.leftInset}px`;
        paintMascot(item);
      });
      state.right.items.forEach((item) => {
        item.el.style.width = `${config.size}px`;
        item.el.style.right = `${config.rightInset}px`;
        paintMascot(item);
      });

      rafId = window.requestAnimationFrame(step);
    }

    window.addEventListener('load', renderSideMascots);
    window.addEventListener('resize', () => {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(renderSideMascots, 180);
    });
    window.addEventListener('beforeunload', () => {
      if (rafId) {
        window.cancelAnimationFrame(rafId);
      }
    });
  })();
</script>
