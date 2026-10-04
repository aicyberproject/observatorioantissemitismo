/* Modelo demonstrativo de formulario: nao envia nem guarda nada.
   Impede qualquer submissao, inclusive por tecla Enter. Nao faz chamada de
   rede e nao usa armazenamento do navegador. */
(function () {
  var f = document.getElementById('modelo');
  if (!f) return;
  f.addEventListener('submit', function (e) { e.preventDefault(); });
})();
