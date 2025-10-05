// Secure7NetGuard Offline - Help Center

class HelpCenter {
    constructor() {
        this.helpGuides = [
            { id: 1, title: 'Como bloquear a tela', content: 'Para bloquear a tela, clique no botão de bloqueio.' },
            { id: 2, title: 'Como restaurar backups', content: 'Para restaurar backups, vá para a seção de configurações.' }
        ];
    }

    showHelpGuide(guideId) {
        const guide = this.helpGuides.find(guide => guide.id === guideId);
        if (guide) {
            console.log(`Título: ${guide.title}`);
            console.log(`Conteúdo: ${guide.content}`);
        } else {
            console.error('Guia de ajuda não encontrado.');
        }
    }
}

export default HelpCenter;