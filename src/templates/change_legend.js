<script>
// Aguardar carregamento
window.addEventListener('load', function() {
    // Esperar o Leaflet inicializar
    setTimeout(function() {
        // NOME da camada que será EXCLUÍDA da regra exclusiva
        // Exemplo: "Nomes Bairros" - pode ter várias ativas junto com outras
        const EXCLUDED_LAYER_NAME = "Nomes Bairros";
        
        // Obter todos os checkboxes de camadas
        const layerCheckboxes = () => {
            return document.querySelectorAll('.leaflet-control-layers-list input[type="checkbox"]');
        };
        
        // Verificar se uma camada deve ser excluída da regra
        function isExcludedLayer(checkbox) {
            const label = checkbox.nextElementSibling;
            if (label && label.tagName === 'SPAN') {
                const layerName = label.textContent.trim();
                return layerName === EXCLUDED_LAYER_NAME;
            }
            return false;
        }
        
        // Obter apenas camadas NÃO excluídas
        function getNonExcludedCheckboxes() {
            return Array.from(layerCheckboxes()).filter(cb => !isExcludedLayer(cb));
        }
        
        // Configurar evento para cada checkbox
        const setupExclusiveLayers = () => {
            const checkboxes = layerCheckboxes();
            
            checkboxes.forEach(checkbox => {
                // Remover eventos anteriores para evitar duplicação
                checkbox.removeEventListener('change', handleLayerChange);
                checkbox.addEventListener('change', handleLayerChange);
            });
        };
        
        // Handler para mudança de camada
        function handleLayerChange(event) {
            const clickedCheckbox = event.target;
            const isExcluded = isExcludedLayer(clickedCheckbox);
            
            if (clickedCheckbox.checked && !isExcluded) {
                // Se ativou uma camada NÃO excluída, desativa outras não-excluídas
                const nonExcludedCheckboxes = getNonExcludedCheckboxes();
                
                nonExcludedCheckboxes.forEach(cb => {
                    if (cb !== clickedCheckbox && cb.checked) {
                        cb.checked = false;
                        // Trigger change event no Leaflet
                        cb.dispatchEvent(new Event('change', { bubbles: true }));
                    }
                });
            }
            // Se a camada for excluída, não faz nada especial - pode ser ativada com outras
        }
        
        // Executar inicialização
        setupExclusiveLayers();
        
        // Reaplicar quando o controle de camadas for expandido/contraído
        const observer = new MutationObserver(setupExclusiveLayers);
        const layerControl = document.querySelector('.leaflet-control-layers');
        if (layerControl) {
            observer.observe(layerControl, { childList: true, subtree: true });
        }
        
        console.log('✅ Modo camada única ativado');
        console.log(`ℹ️ Camada excluída da regra: "${EXCLUDED_LAYER_NAME}"`);
    }, 2000);
});
</script>
