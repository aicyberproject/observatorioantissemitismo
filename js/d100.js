/* Verificador de numero do Disque 100 e conferidor do kit "Reproduza o achado".
   Experimentos da pagina agenda-futura.html. Os dados vem embutidos na propria
   pagina (script application/json). Nao ha rede, armazenamento no navegador,
   cookie nem envio: o que se digita fica na tela e some ao fechar. */
(function (raiz) {
  'use strict';

  /* Aceita 2472, 2.472 e 2 472. Devolve inteiro, ou null se nao for inteiro. */
  function leInteiro(txt) {
    var t = String(txt == null ? '' : txt).trim();
    if (!t) return null;
    if (/^\d{1,3}([. ]\d{3})+$/.test(t) || /^\d{1,3}(,\d{3})+$/.test(t)) t = t.replace(/[., ]/g, '');
    if (!/^\d+$/.test(t)) return null;
    var n = parseInt(t, 10);
    return isFinite(n) ? n : null;
  }

  /* Aceita 3,61 e 3.61. Devolve numero, ou null. */
  function leDecimal(txt) {
    var t = String(txt == null ? '' : txt).trim().replace('%', '').replace(',', '.');
    if (!/^\d+(\.\d+)?$/.test(t)) return null;
    return parseFloat(t);
  }

  function procura(numeros, txt) {
    var n = leInteiro(txt);
    if (n === null) return { erro: 'Digite um número inteiro, como 2472 ou 2.472.' };
    var achados = [];
    for (var i = 0; i < numeros.length; i++) if (numeros[i].valor === n) achados.push(numeros[i]);
    return { numero: n, achados: achados };
  }

  function confere(item, txt) {
    var v = item.tipo === 'percentual' ? leDecimal(txt) : leInteiro(txt);
    if (v === null) return { estado: 'invalido' };
    var ok = item.tipo === 'percentual' ? Math.abs(v - item.esperado) < 0.005 : v === item.esperado;
    return { estado: ok ? 'confere' : 'diverge', informado: v };
  }

  function formata(n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '.'); }

  var api = { leInteiro: leInteiro, leDecimal: leDecimal, procura: procura, confere: confere, formata: formata };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  raiz.D100 = api;

  /* ---- interface ---- */
  function el(tag, texto, classe, estilo) {
    var e = document.createElement(tag);
    if (texto != null) e.textContent = texto;
    if (classe) e.className = classe;
    if (estilo) e.style.cssText = estilo;
    return e;
  }

  function limpa(no) { while (no.firstChild) no.removeChild(no.firstChild); }

  function liga() {
    var bruto = document.getElementById('dados-d100');
    if (!bruto) return;
    var dados;
    try { dados = JSON.parse(bruto.textContent); } catch (e) { return; }

    /* verificador */
    var campo = document.getElementById('d100-num');
    var botao = document.getElementById('d100-verificar');
    var saida = document.getElementById('d100-saida');
    if (campo && botao && saida) {
      var verifica = function () {
        limpa(saida);
        var r = procura(dados.numeros, campo.value);
        if (r.erro) { saida.appendChild(el('p', r.erro, 'body', 'margin:10px 0 0;font-weight:600')); return; }
        if (!r.achados.length) {
          var c0 = el('div', null, 'frm-aviso');
          c0.setAttribute('role', 'status');
          c0.appendChild(el('p', 'O número ' + formata(r.numero) + ' não consta da página do Disque 100.', 'body', 'margin:0;font-weight:600'));
          c0.appendChild(el('p', 'O verificador só reconhece os números reproduzidos lá. Isso não diz que o número esteja errado: diz que ele não foi conferido aqui. Confira a divulgação de origem e a unidade que ela declara.', 'body', 'margin:10px 0 0'));
          saida.appendChild(c0);
          return;
        }
        var caixa = el('div', null, 'frm-aviso');
        caixa.setAttribute('role', 'status');
        if (r.achados.length > 1) {
          caixa.appendChild(el('p', 'O número ' + formata(r.numero) + ' aparece em ' + r.achados.length + ' entradas, com sentidos diferentes. Não é a mesma medida.', 'body', 'margin:0;font-weight:600'));
        }
        for (var i = 0; i < r.achados.length; i++) {
          var a = r.achados[i];
          var bloco = el('div', null, null, 'margin-top:12px');
          bloco.appendChild(el('p', formata(a.valor) + ': ' + a.o_que + '.', 'body', 'margin:0;font-weight:600'));
          bloco.appendChild(el('p', 'Unidade declarada: ' + a.unidade + '. Janela: ' + a.janela + '.', 'body', 'margin:6px 0 0'));
          bloco.appendChild(el('p', 'Origem: ' + a.origem + '.', 'body', 'margin:6px 0 0'));
          bloco.appendChild(el('p', 'Não compare com: ' + a.nao_comparar, 'body', 'margin:6px 0 0'));
          caixa.appendChild(bloco);
        }
        saida.appendChild(caixa);
      };
      botao.addEventListener('click', verifica);
      campo.addEventListener('keydown', function (ev) { if (ev.key === 'Enter') verifica(); });
    }

    /* conferidor */
    var area = document.getElementById('d100-conferidor');
    var conferir = document.getElementById('d100-conferir');
    var resumo = document.getElementById('d100-resumo');
    if (area && conferir && resumo) {
      var tab = document.createElement('table');
      tab.className = 'tab-kpi';
      var cap = el('caption', 'Totais esperados e resultado da conferência', 'sr-only');
      tab.appendChild(cap);
      var cab = document.createElement('thead'), trc = document.createElement('tr');
      ['Conferência', 'Anexo E', 'Seu resultado', 'Situação'].forEach(function (t) {
        var th = el('th', t); th.setAttribute('scope', 'col'); trc.appendChild(th);
      });
      cab.appendChild(trc); tab.appendChild(cab);
      var corpo = document.createElement('tbody');
      var linhas = [];
      dados.conferencias.forEach(function (it) {
        var tr = document.createElement('tr');
        var th = el('th', it.descricao); th.setAttribute('scope', 'row'); tr.appendChild(th);
        tr.appendChild(el('td', it.item));
        var td = document.createElement('td');
        var inp = document.createElement('input');
        inp.type = 'text'; inp.inputMode = 'decimal'; inp.autocomplete = 'off';
        inp.setAttribute('aria-label', 'Seu resultado para: ' + it.descricao);
        inp.style.width = '9em';
        td.appendChild(inp); tr.appendChild(td);
        var st = el('td', '');
        tr.appendChild(st);
        corpo.appendChild(tr);
        linhas.push({ it: it, inp: inp, st: st });
      });
      tab.appendChild(corpo);
      var rol = el('div', null, 'tab-rolagem'); rol.appendChild(tab); area.appendChild(rol);

      conferir.addEventListener('click', function () {
        var ok = 0, div = 0, vazias = 0, inval = 0;
        linhas.forEach(function (l) {
          if (!l.inp.value.trim()) { l.st.textContent = ''; vazias++; return; }
          var r = confere(l.it, l.inp.value);
          if (r.estado === 'confere') { l.st.textContent = 'Confere'; ok++; }
          else if (r.estado === 'diverge') {
            var esp = l.it.tipo === 'percentual' ? String(l.it.esperado).replace('.', ',') + '%' : formata(l.it.esperado);
            l.st.textContent = 'Diverge. Esperado: ' + esp; div++;
          } else { l.st.textContent = 'Valor inválido'; inval++; }
        });
        limpa(resumo);
        var caixa = el('div', null, 'frm-aviso'); caixa.setAttribute('role', 'status');
        var feitas = ok + div + inval;
        if (!feitas) { caixa.appendChild(el('p', 'Digite ao menos um resultado.', 'body', 'margin:0;font-weight:600')); }
        else {
          caixa.appendChild(el('p', ok + ' de ' + feitas + ' conferem' + (div ? '; ' + div + (div === 1 ? ' diverge' : ' divergem') : '') + (inval ? '; ' + inval + ' inválidos' : '') + '.', 'body', 'margin:0;font-weight:600'));
          if (div) caixa.appendChild(el('p', 'A divergência não refuta o achado por si só. Confira a versão dos arquivos, o filtro e a unidade (denúncia distinta ou linha). Se persistir, o Eixo quer saber: veja a página de contato.', 'body', 'margin:10px 0 0'));
        }
        resumo.appendChild(caixa);
      });
    }
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', liga);
    else liga();
  }
})(typeof window !== 'undefined' ? window : globalThis);
