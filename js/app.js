
(function () {
  var root = document.documentElement;
  function syncLgpdHeight() {
    var l = document.getElementById('lgpd');
    var h = (l && !l.hidden) ? l.getBoundingClientRect().height : 0;
    root.style.setProperty('--lgpd-h', h + 'px');
  }

  /* ---- abertura ---- */
  var ov = document.getElementById('overture');
  var timer = null;
  var motionOk = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  function showLgpd() {
    var l = document.getElementById('lgpd');
    var seen = false;
    try { seen = !!sessionStorage.getItem('lgpd-ok'); } catch (e) {}
    if (l && !seen) { l.hidden = false; syncLgpdHeight(); }
  }
  function closeOverture() {
    if (!ov || ov.hidden) return;
    clearTimeout(timer);
    try { sessionStorage.setItem('abertura', '1'); } catch (e) {}
    ov.classList.add('is-leaving');
    setTimeout(function () {
      ov.hidden = true;
      ov.classList.remove('is-leaving');
      showLgpd();
    }, motionOk ? 700 : 0);
  }
  function playOverture() {
    if (!ov) return;
    var clone = ov.cloneNode(true);
    ov.parentNode.replaceChild(clone, ov);
    ov = clone;
    ov.hidden = false;
    ov.classList.remove('is-leaving');
    bindOverture();
    timer = setTimeout(closeOverture, 6600);
  }
  function bindOverture() {
    var skip = ov.querySelector('#btn-skip');
    var sound = ov.querySelector('#btn-sound');
    if (skip) skip.addEventListener('click', closeOverture);
    if (sound) sound.addEventListener('click', function () {
      var on = sound.getAttribute('aria-pressed') === 'true';
      sound.setAttribute('aria-pressed', String(!on));
      sound.querySelector('#sound-label').textContent = !on ? 'Som ativado' : 'Ativar som';
    });
  }
  var abertaNaSessao = false;
  try { abertaNaSessao = !!sessionStorage.getItem('abertura'); } catch (e) {}
  if (ov && !motionOk) {
    /* Sem animacao a abertura seria uma tela escura e imovel: dispensa-se. */
    ov.hidden = true;
    showLgpd();
    var rp = document.getElementById('sw-replay');
    if (rp) rp.hidden = true;
  } else if (ov && abertaNaSessao) {
    ov.hidden = true;
    showLgpd();
  } else if (ov) {
    bindOverture();
    timer = setTimeout(closeOverture, 6600);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeOverture(); });
  } else {
    /* paginas internas nao tem abertura: o aviso de LGPD entra direto */
    showLgpd();
  }

  /* ---- abas de recorte ---- */
  var tabs = document.querySelectorAll('.tab[data-scope]');
  var scopeLabel = document.getElementById('scope-label');
  for (var t = 0; t < tabs.length; t++) {
    tabs[t].addEventListener('click', function () {
      for (var j = 0; j < tabs.length; j++) tabs[j].setAttribute('aria-selected', 'false');
      this.setAttribute('aria-selected', 'true');
      if (scopeLabel) scopeLabel.textContent = this.dataset.scope === 'No Brasil' ? 'no Brasil' : 'no mundo';
    });
  }

  /* ---- filtros da linha do tempo ---- */
  var chips = document.querySelectorAll('.chip[data-filter]');
  var items = document.querySelectorAll('.tl-item');
  for (var c = 0; c < chips.length; c++) {
    chips[c].addEventListener('click', function () {
      var f = this.dataset.filter;
      for (var j = 0; j < chips.length; j++) chips[j].setAttribute('aria-pressed', 'false');
      this.setAttribute('aria-pressed', 'true');
      for (var i = 0; i < items.length; i++) {
        items[i].hidden = !(f === 'Todos' || items[i].dataset.kind === f);
      }
    });
  }

  /* ---- LGPD ---- */
  var ok = document.getElementById('lgpd-ok');
  if (ok) ok.addEventListener('click', function () {
    document.getElementById('lgpd').hidden = true;
    root.style.setProperty('--lgpd-h', '0px');
    try { sessionStorage.setItem('lgpd-ok', '1'); } catch (e) {}
  });
  window.addEventListener('resize', syncLgpdHeight);
})();
