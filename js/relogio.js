/* Relogio de preservacao: experimento da pagina agenda-futura.html.
   Faz so conta de data no navegador. Nao envia, nao grava e nao lembra nada:
   sem rede, sem armazenamento no navegador, sem cookie.
   Regra de calculo: nota tecnica do Eixo 3 de 04/10/2026, secoes 4, 10.3 e 12. */
(function (raiz) {
  'use strict';

  var MARGEM_DIAS = 30;
  var ROTULO = 'Data estimada, de caráter informativo, a conferir com advogado ou Defensoria Pública. ' +
    'O provedor deve ter excluído o registro depois do prazo, salvo guarda prorrogada por requisição ou ordem judicial. ' +
    'Experimento em revisão jurídica, sem valor de orientação.';

  function ultimoDia(ano, mes) { return new Date(Date.UTC(ano, mes, 0)).getUTCDate(); }

  /* Soma de meses de data a data. Se o dia nao existir no mes de destino,
     termo no ultimo dia do mes (Lei 9.784/1999, art. 66, par. 3). */
  function somaMeses(d, meses) {
    var t = d.m - 1 + meses;
    var ano = d.a + Math.floor(t / 12);
    var mes = ((t % 12) + 12) % 12 + 1;
    return { a: ano, m: mes, d: Math.min(d.d, ultimoDia(ano, mes)) };
  }

  function analisa(iso) {
    var r = /^(\d{4})-(\d{2})-(\d{2})$/.exec(iso || '');
    if (!r) return null;
    var o = { a: +r[1], m: +r[2], d: +r[3] };
    if (o.a < 1990 || o.m < 1 || o.m > 12 || o.d < 1 || o.d > ultimoDia(o.a, o.m)) return null;
    return o;
  }

  function dias(a, b) {
    return Math.round((Date.UTC(b.a, b.m - 1, b.d) - Date.UTC(a.a, a.m - 1, a.d)) / 86400000);
  }

  function fmt(o) {
    function z(n) { return (n < 10 ? '0' : '') + n; }
    return z(o.d) + '/' + z(o.m) + '/' + o.a;
  }

  /* d: data informada (AAAA-MM-DD). h: hoje (AAAA-MM-DD). */
  function calcula(d, h) {
    var D = analisa(d), H = analisa(h);
    if (!D) return { erro: 'Informe uma data válida.' };
    if (!H) return { erro: 'Não foi possível ler a data de hoje.' };
    if (dias(H, D) > 0) return { erro: 'A data informada está no futuro.' };
    var A = somaMeses(D, 6), C = somaMeses(D, 12);
    var fa = dias(H, A), fc = dias(H, C);
    var estado, linhas = [], destaque = false;
    if (fc < 0) {
      estado = 'passou_tudo';
      linhas.push('Os dois prazos provavelmente já correram. Os registros devem ter sido excluídos, salvo guarda prorrogada.');
      linhas.push('Denuncie mesmo assim: o conteúdo e outras provas podem existir.');
    } else if (fa < 0) {
      estado = 'passou_acesso';
      linhas.push('O prazo dos registros de acesso a aplicações provavelmente já correu. O registro deve ter sido excluído, salvo guarda prorrogada.');
      linhas.push('O prazo dos registros de conexão ainda corre: faltam ' + fc + ' dia' + (fc === 1 ? '' : 's') + '.');
      if (fc < MARGEM_DIAS) { destaque = true; linhas.push('Denuncie hoje.'); }
    } else {
      estado = 'dentro';
      linhas.push('Faltam ' + fa + ' dia' + (fa === 1 ? '' : 's') + ' para o fim do prazo dos registros de acesso a aplicações.');
      if (fa < MARGEM_DIAS) { destaque = true; linhas.push('Denuncie hoje.'); }
    }
    return { estado: estado, acesso: fmt(A), conexao: fmt(C), diasAcesso: fa, diasConexao: fc,
             linhas: linhas, destaque: destaque, rotulo: ROTULO };
  }

  var api = { calcula: calcula, somaMeses: somaMeses, fmt: fmt, analisa: analisa };
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  raiz.Relogio = api;

  /* ---- interface ---- */
  function hojeLocal() {
    var n = new Date();
    function z(x) { return (x < 10 ? '0' : '') + x; }
    return n.getFullYear() + '-' + z(n.getMonth() + 1) + '-' + z(n.getDate());
  }

  function liga() {
    var campo = document.getElementById('rel-data');
    var botao = document.getElementById('rel-calcular');
    var saida = document.getElementById('rel-saida');
    if (!campo || !botao || !saida) return;
    campo.max = hojeLocal();

    function p(texto, forte) {
      var e = document.createElement('p');
      e.className = 'body';
      e.style.margin = '10px 0 0';
      if (forte) e.style.fontWeight = '600';
      e.textContent = texto;
      return e;
    }

    function mostra() {
      while (saida.firstChild) saida.removeChild(saida.firstChild);
      var r = calcula(campo.value, hojeLocal());
      if (r.erro) { saida.appendChild(p(r.erro, true)); return; }
      var caixa = document.createElement('div');
      caixa.className = 'frm-aviso';
      caixa.setAttribute('role', 'status');
      if (r.destaque) caixa.style.borderLeftWidth = '8px';
      caixa.appendChild(p('Registros de acesso a aplicações (6 meses): até cerca de ' + r.acesso + '.', true));
      caixa.appendChild(p('Registros de conexão (1 ano): até cerca de ' + r.conexao + '.', true));
      for (var i = 0; i < r.linhas.length; i++) caixa.appendChild(p(r.linhas[i], r.destaque));
      var rot = p(r.rotulo, false);
      rot.className = 'fonte';
      caixa.appendChild(rot);
      saida.appendChild(caixa);
    }

    botao.addEventListener('click', mostra);
  }

  if (typeof document !== 'undefined') {
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', liga);
    else liga();
  }
})(typeof window !== 'undefined' ? window : globalThis);
