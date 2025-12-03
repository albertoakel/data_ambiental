<script>
// Dados das colormaps (serão injetados pelo Python)
var colormapData = {{COLORMAP_DATA}};

// Função para atualizar lista de legendas
function updateLegendList() {
    var legendList = document.getElementById('legend-list');
    if (!legendList) return;

    legendList.innerHTML = '';

    // Ordenar features por nome
    var features = Object.keys(colormapData).sort();

    features.forEach(function(featureName) {
        var div = document.createElement('div');
        div.style.cssText = 'padding: 3px 0; border-bottom: 1px solid #eee; cursor: pointer;';
        div.innerHTML = featureName;

        div.onclick = function() {
            // Encontrar e ativar esta camada
            var layerControl = document.querySelector('.leaflet-control-layers');
            if (layerControl) {
                var checkboxes = layerControl.querySelectorAll('input[type="checkbox"]');

                for (var i = 0; i < checkboxes.length; i++) {
                    var cb = checkboxes[i];
                    var label = cb.parentElement;
                    var text = label.textContent || label.innerText;
                    text = text.trim();

                    if (text.includes(featureName) || featureName.includes(text.replace(/[^\w\s]/g, '').trim())) {
                        // Desmarcar todas as outras camadas temáticas
                        for (var j = 0; j < checkboxes.length; j++) {
                            if (i !== j) {
                                var otherText = checkboxes[j].parentElement.textContent || checkboxes[j].parentElement.innerText;
                                otherText = otherText.trim();

                                if (otherText !== 'Bairro' && !otherText.includes('Informações')) {
                                    checkboxes[j].checked = false;
                                    checkboxes[j].dispatchEvent(new Event('change'));
                                }
                            }
                        }

                        // Marcar esta camada
                        cb.checked = true;
                        cb.dispatchEvent(new Event('change'));
                        break;
                    }
                }
            }
        };

        legendList.appendChild(div);
    });
}

// Inicializar lista de legendas
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(updateLegendList, 1500);
    setInterval(updateLegendList, 3000);
});
</script>