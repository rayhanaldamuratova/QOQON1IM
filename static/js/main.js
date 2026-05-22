document.addEventListener('DOMContentLoaded', () => {

  /* ---- Mobile menu ---- */
  const hamburger  = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileClose= document.getElementById('mobile-close');
  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => mobileMenu.classList.add('open'));
    mobileClose?.addEventListener('click', () => mobileMenu.classList.remove('open'));
    mobileMenu.querySelectorAll('a').forEach(a =>
      a.addEventListener('click', () => mobileMenu.classList.remove('open'))
    );
  }

  /* ---- Active nav link ---- */
  const path = window.location.pathname;
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(a => {
    if (a.getAttribute('href') === path) a.classList.add('active');
  });

  /* ---- Navbar scroll effect (home page transparent header only) ---- */
  const navbar = document.querySelector('.header-transparent .navbar');
  if (navbar) {
    const onScroll = () => {
      navbar.classList.toggle('scrolled', window.scrollY > 80);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---- Scroll reveal ---- */
  const revealObs = new IntersectionObserver((entries) => {
    entries.forEach((entry, i) => {
      if (entry.isIntersecting) {
        setTimeout(() => entry.target.classList.add('visible'), i * 80);
        revealObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

  /* ---- Counter animation ---- */
  function animateCount(el, target, suffix) {
    let start = null;
    const dur = 1800;
    const step = (ts) => {
      if (!start) start = ts;
      const p = Math.min((ts - start) / dur, 1);
      const ease = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.floor(ease * target) + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }
  const statsObs = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.hero-stat-value').forEach(el => {
          const val = el.dataset.value, sfx = el.dataset.suffix || '';
          if (val) animateCount(el, parseInt(val), sfx);
        });
        statsObs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.3 });
  const statsBar = document.querySelector('.hero-stats-bar');
  if (statsBar) statsObs.observe(statsBar);

  /* ---- Card tilt ---- */
  document.querySelectorAll('.card, .staff-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const r = card.getBoundingClientRect();
      const x = ((e.clientX - r.left) / r.width  - 0.5) * 7;
      const y = ((e.clientY - r.top)  / r.height - 0.5) * 7;
      card.style.transform = `translateY(-4px) rotateX(${-y}deg) rotateY(${x}deg)`;
      card.style.transition = 'transform 0.08s ease';
    });
    card.addEventListener('mouseleave', () => {
      card.style.transform = '';
      card.style.transition = 'all 0.28s cubic-bezier(0.4,0,0.2,1)';
    });
  });

  /* ---- Gallery lightbox ---- */
  document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      if (!img) return;
      const ov = document.createElement('div');
      ov.style.cssText = 'position:fixed;inset:0;background:rgba(0,0,0,0.93);z-index:9999;display:flex;align-items:center;justify-content:center;cursor:zoom-out;';
      ov.innerHTML = `
        <img src="${img.src}" style="max-width:90vw;max-height:90vh;border-radius:10px;object-fit:contain;box-shadow:0 24px 80px rgba(0,0,0,0.6);">
        <button id="lb-close" style="position:absolute;top:20px;right:24px;background:rgba(255,255,255,0.1);border:none;color:#fff;font-size:1.4rem;width:44px;height:44px;border-radius:50%;cursor:pointer;display:flex;align-items:center;justify-content:center;"><i class="fa-solid fa-xmark"></i></button>
      `;
      const close = () => ov.remove();
      ov.addEventListener('click', e => { if (e.target === ov) close(); });
      ov.querySelector('#lb-close').addEventListener('click', close);
      document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); }, { once: true });
      document.body.appendChild(ov);
    });
  });

  /* ---- Auto-dismiss alerts ---- */
  document.querySelectorAll('.alert').forEach(el => {
    setTimeout(() => {
      el.style.transition = 'opacity 0.4s,transform 0.4s';
      el.style.opacity = '0'; el.style.transform = 'translateY(-8px)';
      setTimeout(() => el.remove(), 400);
    }, 4000);
  });

});
