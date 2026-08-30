/* Leitura por ponteiro nos graficos.
   O valor nunca depende do ponteiro: cada figura tem tabela equivalente em
   <details> e os rotulos diretos ficam no proprio desenho. Este arquivo apenas
   acrescenta a leitura rapida ao passar o mouse ou ao focar pelo teclado. */
(function () {
  var alvos = document.querySelectorAll('.viz .hit[data-t]');
  if (!alvos.length) return;

  var tip = document.createElement('div');
  tip.className = 'viz-tip';
  tip.setAttribute('role', 'status');
  var rotulo = document.createElement('b');
  var valor = document.createElement('span');
  tip.appendChild(rotulo);
  tip.appendChild(valor);
  document.body.appendChild(tip);

  function posiciona(x, y) {
    var c = tip.getBoundingClientRect();
    var esq = Math.min(Math.max(8, x + 14), window.innerWidth - c.width - 8);
    var topo = y - c.height - 12;
    if (topo < 8) topo = y + 18;
    tip.style.left = esq + 'px';
    tip.style.top = topo + 'px';
  }
  function mostra(el, x, y) {
    rotulo.textContent = el.getAttribute('data-t') || '';
    valor.textContent = el.getAttribute('data-v') || '';
    tip.setAttribute('data-on', '1');
    posiciona(x, y);
  }
  function esconde() { tip.setAttribute('data-on', '0'); }

  for (var i = 0; i < alvos.length; i++) {
    (function (el) {
      el.addEventListener('mouseenter', function (e) { mostra(el, e.clientX, e.clientY); });
      el.addEventListener('mousemove', function (e) { posiciona(e.clientX, e.clientY); });
      el.addEventListener('mouseleave', esconde);
      /* Sem tabindex: 73 marcas viram 73 paradas de tabulacao entre o topo e o
         rodape. Quem navega por teclado le os mesmos valores na tabela que
         acompanha cada figura, e cada marca tem <title> para leitor de tela. */
    })(alvos[i]);
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') esconde(); });
  window.addEventListener('scroll', esconde, { passive: true });
})();
