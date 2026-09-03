/* Painel de apoio a preservacao de evidencias.
   ------------------------------------------------------------------
   REGRA DE PROJETO: nada sai do navegador.

   Este arquivo nao contem, e nao pode conter, nenhuma chamada de rede. Sem
   fetch, sem XMLHttpRequest, sem WebSocket, sem <form action>, sem sendBeacon.
   Tambem nao usa localStorage, sessionStorage nem IndexedDB para conteudo de
   incidente: aparelho compartilhado ou apreendido transforma persistencia em
   passivo, e nao em conveniencia.

   Do arquivo escolhido pela pessoa, le-se o conteudo apenas para calcular o
   resumo criptografico. O conteudo nao e guardado, nao e exibido e nao e
   transmitido. Fechar a pagina descarta tudo.

   Conferencia: `grep -nE "fetch|XMLHttpRequest|sendBeacon|WebSocket|localStorage|sessionStorage|indexedDB" js/preservar.js`
   deve nao retornar nada. */
(function () {
  var painel = document.getElementById('hash-painel');
  if (!painel) return;

  var entrada = document.getElementById('hash-arquivos');
  var lista = document.getElementById('hash-lista');
  var vazio = document.getElementById('hash-vazio');
  var limpar = document.getElementById('hash-limpar');
  var copiar = document.getElementById('hash-copiar');
  var estado = document.getElementById('hash-estado');
  var indisp = document.getElementById('hash-indisponivel');

  /* crypto.subtle so existe em contexto seguro. Em https funciona; ao abrir o
     arquivo direto do disco, nao. Sem ele o painel se retira e o guia de quatro
     etapas, que e a espinha da secao, continua valendo por si. */
  var cripto = window.crypto && window.crypto.subtle && window.isSecureContext;
  if (!cripto) {
    painel.hidden = true;
    if (indisp) indisp.hidden = false;
    return;
  }

  var registros = [];

  function hex(buf) {
    var b = new Uint8Array(buf), s = '';
    for (var i = 0; i < b.length; i++) s += ('0' + b[i].toString(16)).slice(-2);
    return s;
  }

  function tamanho(n) {
    if (n < 1024) return n + ' B';
    if (n < 1048576) return (n / 1024).toFixed(1).replace('.', ',') + ' KB';
    return (n / 1048576).toFixed(1).replace('.', ',') + ' MB';
  }

  function el(tag, cls, txt) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (txt != null) n.textContent = txt;
    return n;
  }

  function pinta() {
    lista.textContent = '';
    if (!registros.length) {
      vazio.hidden = false;
      limpar.disabled = true;
      copiar.disabled = true;
      return;
    }
    vazio.hidden = true;
    limpar.disabled = false;
    copiar.disabled = false;
    for (var i = 0; i < registros.length; i++) {
      var r = registros[i];
      var li = el('li', 'hash-item');
      var topo = el('div', 'hash-top');
      topo.appendChild(el('span', 'hash-nome', r.nome));
      topo.appendChild(el('span', 'hash-tam', tamanho(r.bytes)));
      li.appendChild(topo);
      li.appendChild(el('code', 'hash-valor', r.sha256));
      li.appendChild(el('p', 'hash-quando', 'Calculado em ' + r.quando));
      lista.appendChild(li);
    }
  }

  function texto() {
    var l = ['INVENTARIO DE INTEGRIDADE PROBATORIA',
             'Algoritmo: SHA-256',
             'Gerado em: ' + new Date().toLocaleString('pt-BR'),
             'Calculo local, no proprio navegador. Nenhum arquivo foi enviado.',
             ''];
    for (var i = 0; i < registros.length; i++) {
      var r = registros[i];
      l.push((i + 1) + '. ' + r.nome);
      l.push('   tamanho: ' + tamanho(r.bytes));
      l.push('   SHA-256: ' + r.sha256);
      l.push('');
    }
    l.push('Conferencia posterior: recalcular o resumo do mesmo arquivo deve');
    l.push('devolver exatamente o mesmo valor. Divergencia indica alteracao.');
    return l.join('\n');
  }

  function digere(arquivo) {
    return arquivo.arrayBuffer()
      .then(function (buf) { return window.crypto.subtle.digest('SHA-256', buf); })
      .then(function (dig) {
        /* buf e dig saem de escopo aqui: o conteudo nao e retido. */
        registros.push({
          nome: arquivo.name,
          bytes: arquivo.size,
          sha256: hex(dig),
          quando: new Date().toLocaleString('pt-BR')
        });
      });
  }

  entrada.addEventListener('change', function () {
    var arquivos = Array.prototype.slice.call(entrada.files || []);
    if (!arquivos.length) return;
    estado.textContent = 'Calculando ' + arquivos.length
      + (arquivos.length > 1 ? ' resumos...' : ' resumo...');
    var fila = Promise.resolve();
    arquivos.forEach(function (a) {
      fila = fila.then(function () { return digere(a); }).catch(function () {
        registros.push({ nome: a.name, bytes: a.size,
                         sha256: 'nao foi possivel calcular',
                         quando: new Date().toLocaleString('pt-BR') });
      });
    });
    fila.then(function () {
      estado.textContent = registros.length
        + (registros.length > 1 ? ' arquivos no inventario' : ' arquivo no inventario');
      pinta();
      entrada.value = '';
    });
  });

  limpar.addEventListener('click', function () {
    registros = [];
    estado.textContent = '';
    pinta();
  });

  copiar.addEventListener('click', function () {
    var t = texto();
    var area = document.createElement('textarea');
    area.value = t;
    area.setAttribute('readonly', 'readonly');
    area.style.position = 'fixed';
    area.style.left = '-9999px';
    document.body.appendChild(area);
    area.select();
    var ok = false;
    try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
    document.body.removeChild(area);
    estado.textContent = ok
      ? 'Inventario copiado para a area de transferencia'
      : 'Nao foi possivel copiar. Selecione os valores na lista acima.';
  });

  pinta();
})();
