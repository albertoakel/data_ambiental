<script>
// Dados das colormaps
var colormapData = {{COLORMAP_DATA}};

// Mapeamento de nomes completos para nomes limpos
var nameMapping = {{NAME_MAPPING}};

// Função para encontrar camada ativa
function findActiveLayer() {
    var layerControl = document.querySelector('.leaflet-control-layers');
    if (!layerControl) return null;

    var checkboxes = layerControl.querySelectorAll('input[type="checkbox"]');

    for (var i = 0; i < checkboxes.length; i++) {
        var cb = checkboxes[i];
        if (cb.checked) {
            var label = cb.parentElement;
            var text = label.textContent || label.innerText;
            text = text.trim();

            // Procurar por qualquer nome conhecido
            for (var fullName in nameMapping) {
                if (text === fullName || text.includes(fullName) || fullName.includes(text)) {
                    return nameMapping[fullName];
                }
            }

            // Tentativa alternativa: remover emojis e comparar
            var cleanText = text.replace(/[^\w\s]/g, '').trim();
            for (var fullName in nameMapping) {
                var cleanFullName = fullName.replace(/[^\w\s]/g, '').trim();
                if (cleanText === cleanFullName ||
                    cleanText.includes(cleanFullName) ||
                    cleanFullName.includes(cleanText)) {
                    return nameMapping[fullName];
                }
            }
        }
    }
    return null;
}

// Função para atualizar colormap
function updateColormap() {
    var container = document.getElementById('single-colormap');
    if (!container) return;

    var activeKey = findActiveLayer();

    if (activeKey && colormapData[activeKey]) {
        container.innerHTML = colormapData[activeKey];
        container.style.display = 'block';
    } else {
        // Verificar se há alguma camada temática ativa
        var hasThematicLayer = false;
        var layerControl = document.querySelector('.leaflet-control-layers');
        if (layerControl) {
            var checkboxes = layerControl.querySelectorAll('input[type="checkbox"]');
            for (var i = 0; i < checkboxes.length; i++) {
                if (checkboxes[i].checked) {
                    var label = checkboxes[i].parentElement;
                    var text = label.textContent || label.innerText;
                    text = text.trim();

                    // Verificar se é uma camada temática (não é Bairro ou outras)
                    if (text !== 'Bairro' && !text.includes('Informações')) {
                        hasThematicLayer = true;
                        break;
                    }
                }
            }
        }

        if (!hasThematicLayer) {
            container.style.display = 'none';
        }
    }
}

// Inicializar
document.addEventListener('DOMContentLoaded', function() {
    // Estado inicial
    setTimeout(updateColormap, 800);

    // MutationObserver para detectar mudanças
    var observer = new MutationObserver(function(mutations) {
        updateColormap();
    });

    setTimeout(function() {
        var layerControl = document.querySelector('.leaflet-control-layers');
        if (layerControl) {
            observer.observe(layerControl, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['class', 'checked']
            });
        }

        // Event listeners diretos
        document.addEventListener('click', function(e) {
            if (e.target.type === 'checkbox' ||
                e.target.closest('.leaflet-control-layers')) {
                setTimeout(updateColormap, 150);
            }
        });

        // Atualizar periodicamente (fallback)
        setInterval(updateColormap, 2000);
    }, 1200);
});
</script>