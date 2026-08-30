
(function () {
  var root = document.documentElement;

  /* A faixa de prototipo e sticky no topo. O cabecalho, tambem sticky, precisa
     parar logo abaixo dela: --proto-h carrega a altura medida. */
  function syncProtoHeight() {
    var b = document.querySelector('.proto-bar');
    root.style.setProperty('--proto-h', (b ? b.getBoundingClientRect().height : 0) + 'px');
  }
  syncProtoHeight();
  window.addEventListener('resize', syncProtoHeight);
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(syncProtoHeight).catch(function () {});
  }

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
  function bindOverture() {
    var skip = ov.querySelector('#btn-skip');
    if (skip) skip.addEventListener('click', closeOverture);
  }
  var abertaNaSessao = false;
  try { abertaNaSessao = !!sessionStorage.getItem('abertura'); } catch (e) {}
  if (ov && !motionOk) {
    /* Sem animacao a abertura seria uma tela escura e imovel: dispensa-se. */
    ov.hidden = true;
    showLgpd();
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
  var recorte = 'br';
  var tabs = document.querySelectorAll('.tab[data-scope]');
  var scopeLabel = document.getElementById('scope-label');
  for (var t = 0; t < tabs.length; t++) {
    tabs[t].addEventListener('click', function () {
      for (var j = 0; j < tabs.length; j++) tabs[j].setAttribute('aria-pressed', 'false');
      this.setAttribute('aria-pressed', 'true');
      recorte = this.dataset.scope === 'No Brasil' ? 'br' : 'mundo';
      if (scopeLabel) scopeLabel.textContent = recorte === 'br' ? 'no Brasil' : 'no mundo';
      pintaPainel();
      var g = document.getElementById('feed-grid');
      if (g) g.setAttribute('aria-label', 'Manchetes ' + (recorte === 'br' ? 'no Brasil' : 'no mundo'));
    });
  }

  /* ---- painel ao vivo ---- */
  var NOTICIAS = { br: [], mundo: [] };

  function el(tag, cls, txt) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (txt != null) n.textContent = txt;
    return n;
  }
  function quando(iso) {
    if (!iso) return '';
    var d = new Date(iso);
    if (isNaN(d)) return '';
    var min = Math.round((Date.now() - d.getTime()) / 60000);
    if (min < 1) return 'agora';
    if (min < 60) return 'há ' + min + ' min';
    if (min < 1440) return 'há ' + Math.round(min / 60) + ' h';
    return d.toLocaleDateString('pt-BR', { day: '2-digit', month: '2-digit' });
  }
  function externo(a, href) {
    a.href = href;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
  }
  /* O destino externo abre em nova aba. O aviso precisa chegar a quem usa leitor
     de tela sem poluir a tela: vai em texto oculto dentro do proprio link.
     aria-description foi descartado por falta de suporte nas tecnologias
     assistivas. */
  function avisoNovaAba() {
    return el('span', 'sr-only', ' (abre em nova aba, no site de origem)');
  }

  function pintaPainel() {
    var grade = document.getElementById('feed-grid');
    if (!grade) return;
    var itens = NOTICIAS[recorte] || [];
    grade.setAttribute('aria-busy', 'true');
    grade.textContent = '';
    if (!itens.length) {
      grade.appendChild(el('p', 'feed-empty',
        'Nenhuma manchete recente neste recorte. Alterne o recorte ou consulte as fontes abaixo.'));
      grade.setAttribute('aria-busy', 'false');
      return;
    }
    for (var i = 0; i < Math.min(itens.length, 6); i++) {
      var n = itens[i];
      var card = el('a', 'feed-card feed-card-live');
      externo(card, n.link);
      var meta = el('div', 'feed-meta');
      meta.appendChild(el('span', null, n.fonte || ''));
      meta.appendChild(el('span', null, quando(n.publicado_em)));
      card.appendChild(meta);
      card.appendChild(el('p', 'feed-title', n.titulo));
      if (n.via) card.appendChild(el('span', 'feed-via', 'via ' + n.via));
      card.appendChild(el('span', 'feed-cta', 'Ler na fonte →'));
      card.appendChild(avisoNovaAba());
      grade.appendChild(card);
    }
    grade.setAttribute('aria-busy', 'false');
  }

  function montaFita(fita, itens) {
    if (!fita || !itens.length) return false;
    var seq = [];
    while (seq.length < 14) seq = seq.concat(itens);
    var bloco = document.createDocumentFragment();
    for (var i = 0; i < seq.length; i++) {
      var n = seq[i];
      var a = el('a', 'tk-item');
      externo(a, n.link);
      a.appendChild(el('span', 'tk-src', n.fonte || ''));
      a.appendChild(el('span', 'tk-ttl', n.titulo));
      if (n.via) a.appendChild(el('span', 'tk-via', 'via ' + n.via));
      a.appendChild(avisoNovaAba());
      bloco.appendChild(a);
    }
    fita.appendChild(bloco.cloneNode(true));
    fita.appendChild(bloco);   /* segunda copia: fecha o laco em -50% */
    return true;
  }

  /* Cada faixa percorre metade da propria largura por ciclo. Com duracao fixa,
     a faixa mais longa corre mais rapido. Aqui a duracao deriva da largura
     medida, de modo que as duas faixas andem na mesma velocidade em px/s. */
  function ritmo(fita) {
    if (!fita) return 0;
    var px = parseFloat(getComputedStyle(document.documentElement)
      .getPropertyValue('--tk-speed')) || 58;
    var meia = fita.scrollWidth / 2;
    if (!meia) return 0;               /* oculto ou sem medida: mantem o CSS */
    var seg = meia / px;
    fita.style.animationDuration = seg.toFixed(1) + 's';
    return seg;
  }

  function ajustaRitmo() {
    ritmo(document.getElementById('tk-tape-br'));
    ritmo(document.getElementById('tk-tape-wo'));
  }

  function estado(rotulo, texto, carimbo) {
    var r = document.getElementById('estado-rotulo');
    var x = document.getElementById('estado-texto');
    var c = document.getElementById('estado-carimbo');
    if (r) r.textContent = rotulo;
    if (x) x.textContent = texto;
    if (c && carimbo) c.textContent = carimbo;
  }

  /* Nomeia as fontes que nao responderam. Sem esta lista o leitor nao tem como
     saber que a cobertura da coleta foi parcial. */
  function pintaFalhas(lista) {
    var alvo = document.getElementById('coleta-falhas');
    if (!alvo) return;
    alvo.textContent = '';
    if (!lista.length) { alvo.hidden = true; return; }
    var nomes = [];
    for (var i = 0; i < lista.length; i++) {
      nomes.push(String(lista[i]).split(':')[0].trim());
    }
    alvo.appendChild(el('span', 'label', lista.length === 1
      ? 'Fonte sem resposta nesta coleta'
      : 'Fontes sem resposta nesta coleta'));
    alvo.appendChild(el('span', 'coleta-nomes', nomes.join(' · ')));
    alvo.hidden = false;
  }

  function semPainel() {
    estado('Painel em implantação',
           'O serviço de agregação não respondeu. As fontes estão registradas e listadas abaixo, '
           + 'com endereço, e podem ser assinadas diretamente.',
           'Endereço definitivo do painel ainda não definido');
    pintaFalhas([]);
  }

  function recebe(d) {
        var itens = (d && d.itens) || [];
        if (!itens.length) throw new Error('vazio');
        for (var i = 0; i < itens.length; i++) {
          (NOTICIAS[itens[i].escopo] || NOTICIAS.mundo).push(itens[i]);
        }
        var g = new Date(d.gerado_em);
        var hora = isNaN(g) ? '' : g.toLocaleString('pt-BR',
          { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' });
        /* O agregador registra as fontes que nao responderam. Declarar apenas o
           total consultado esconderia a falha: a pagina informa o que respondeu. */
        var consultadas = d.fontes_consultadas || 21;
        var falhas = (d.fontes_com_falha || []).length;
        var responderam = consultadas - falhas;
        estado('Painel no ar',
               'Agregação automática de fontes públicas: ' + responderam + ' de ' + consultadas
               + ' responderam nesta coleta. ' + itens.length + ' manchetes: '
               + (d.no_brasil || 0) + ' no Brasil e ' + (d.no_mundo || 0)
               + ' no mundo. Cada item remete à publicação de origem.',
               hora ? 'Última coleta em ' + hora : '');
        pintaFalhas(d.fontes_com_falha || []);
        var rodape = document.getElementById('feed-rodape');
        if (rodape) rodape.textContent = 'Seis itens mais recentes do recorte selecionado';
        pintaPainel();
        var fita = document.getElementById('ticker');
        var a = montaFita(document.getElementById('tk-tape-br'), NOTICIAS.br);
        var b = montaFita(document.getElementById('tk-tape-wo'), NOTICIAS.mundo);
        if (fita && (a || b)) {
          if (!a) fita.querySelector('.tk-lane-br').hidden = true;
          if (!b) fita.querySelector('.tk-lane-wo').hidden = true;
          fita.hidden = false;
          ajustaRitmo();
          if (document.fonts && document.fonts.ready) {
            document.fonts.ready.then(ajustaRitmo).catch(function () {});
          }
          var reajuste = null;
          window.addEventListener('resize', function () {
            clearTimeout(reajuste);
            reajuste = setTimeout(ajustaRitmo, 250);
          });
          var carimbo = document.getElementById('tk-stamp');
          if (carimbo && hora) carimbo.textContent = itens.length + ' manchetes · ' + hora;
        }
  }

  if (window.__NOTICIAS__) {
    try { recebe(window.__NOTICIAS__); } catch (e) { semPainel(); }
  } else if (window.fetch) {
    fetch('data/noticias.json', { cache: 'no-store' })
      .then(function (r) { if (!r.ok) throw new Error('http'); return r.json(); })
      .then(recebe)
      .catch(function () { semPainel(); });
  } else {
    semPainel();
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
